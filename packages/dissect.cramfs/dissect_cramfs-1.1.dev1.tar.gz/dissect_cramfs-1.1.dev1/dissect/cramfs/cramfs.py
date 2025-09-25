from __future__ import annotations

import stat
import zlib
from functools import cached_property, lru_cache
from typing import TYPE_CHECKING, BinaryIO

from dissect.util.stream import AlignedStream, RangeStream

from dissect.cramfs.c_cramfs import c_cramfs
from dissect.cramfs.exception import (
    FileNotFoundError,
    NotADirectoryError,
    NotAFileError,
    NotASymlinkError,
)

if TYPE_CHECKING:
    from collections.abc import Iterator


class CramFS:
    """CramFS filesystem implementation.

    Args:
        fh: A file-like object of the volume containing the filesystem.
    """

    def __init__(self, fh: BinaryIO):
        fh.seek(0)
        self.fh = fh
        self.sb = c_cramfs.cramfs_super_block(fh)

        if self.sb.magic != c_cramfs.CRAMFS_MAGIC:
            raise ValueError("Invalid CramFS filesystem")

        self.root = self.inode((self.sb.root.offset << 2) - 12)

        self._read_block = lru_cache(1024)(self._read_block)

    def inode(self, offset: int) -> INode:
        return INode(self, offset)

    def get(self, path: str | int, node: INode | None = None) -> INode:
        """Return an inode for the given path or offset.

        Args:
            path: The path or offset of the inode.
            node: An optional inode object to relatively resolve the path from.
        """
        if isinstance(path, int):
            return self.inode(path)

        node = node or self.root
        for p in path.split("/"):
            if not p:  # Ignore empty path components due to leading or trailing or forward slashes
                continue

            for entry in node.iterdir():
                if entry.name == p:
                    node = entry
                    break
            else:
                raise FileNotFoundError(f"File not found: {path}")

        return node

    def _read_block(self, offset: int, size: int) -> bytes:
        """Read a block of data from the filesystem.

        Args:
            offset: The offset of the block.
            size: The size of the block to read.
        """
        if size == 0:
            # Sparse block aka hole
            return b"\x00" * c_cramfs.CRAMFS_BLOCK_SIZE

        uncompressed = offset & c_cramfs.CRAMFS_FLAG_UNCOMPRESSED_BLOCK
        direct = offset & c_cramfs.CRAMFS_FLAG_DIRECT_POINTER

        if direct:
            raise NotImplementedError("Direct pointers are not supported yet")

        offset &= ~(c_cramfs.CRAMFS_FLAG_UNCOMPRESSED_BLOCK | c_cramfs.CRAMFS_FLAG_DIRECT_POINTER)

        self.fh.seek(offset)
        return self.fh.read(size) if uncompressed else zlib.decompress(self.fh.read(size))


class INode:
    def __init__(self, fs: CramFS, offset: int):
        self.fs = fs
        self.offset = offset

    def __repr__(self) -> str:
        return f"<INode {self.name!r} ({self.offset})>"

    @cached_property
    def inode(self) -> c_cramfs.cramfs_inode:
        """Return the inode header."""
        self.fs.fh.seek(self.offset)
        return c_cramfs.cramfs_inode(self.fs.fh)

    @property
    def mode(self) -> int:
        """Return the file mode."""
        return self.inode.mode

    @property
    def uid(self) -> int:
        """Return the user ID."""
        return self.inode.uid

    @property
    def major(self) -> int:
        """Return the major device ID for block and character devices."""
        if not self.is_device():
            raise NotAFileError(f"{self!r} is not character- or block device")
        return (self.inode.size >> 8) & 0xFF

    @property
    def minor(self) -> int:
        """Return the minor device ID for block and character devices."""
        if not self.is_device():
            raise NotAFileError(f"{self!r} is not character- or block device")
        return self.inode.size & 0xFF

    @property
    def size(self) -> int:
        """Return the file size."""
        if self.is_device():
            return 0
        return self.inode.size

    @property
    def gid(self) -> int:
        """Return the group ID."""
        return self.inode.gid

    @property
    def data_offset(self) -> int:
        """Offset to the start of the data block or ``INode``.

        - For files: this is the offset to the first data block.
        - For directories: this is the offset to the first ``INode``.
        - For symlinks: this is the offset the data block holding the target name.
        """
        return self.inode.offset << 2

    @property
    def name(self) -> str:
        """Return the name of this inode."""
        return self.inode.name.decode().strip("\x00")

    @cached_property
    def link(self) -> str:
        """Return the symlink target."""
        if not self.is_symlink():
            raise NotASymlinkError(f"{self!r} is not a symlink")
        return self.open().read().decode().strip("\x00")

    @cached_property
    def blocks(self) -> list[tuple[int, int]]:
        """Return a list containing pairs of starting offsets and byte lengths for each block of this inode."""
        result = []

        self.fs.fh.seek(self.data_offset)
        num_blocks = ((self.size + c_cramfs.CRAMFS_BLOCK_SIZE) - 1) // c_cramfs.CRAMFS_BLOCK_SIZE
        prev = self.data_offset + num_blocks * 4
        for offset in c_cramfs.uint32[num_blocks](self.fs.fh):
            result.append((prev, offset - prev))
            prev = offset

        return result

    def is_dir(self) -> bool:
        """Return whether this inode is a directory."""
        return stat.S_ISDIR(self.mode)

    def is_file(self) -> bool:
        """Return whether this inode is a file."""
        return stat.S_ISREG(self.mode)

    def is_symlink(self) -> bool:
        """Return whether this inode is a symlink."""
        return stat.S_ISLNK(self.mode)

    def is_block_device(self) -> bool:
        """Return whether this inode is a block device."""
        return stat.S_ISBLK(self.mode)

    def is_character_device(self) -> bool:
        """Return whether this inode is a character device."""
        return stat.S_ISCHR(self.mode)

    def is_device(self) -> bool:
        """Return whether this inode is a device file."""
        return self.is_block_device() or self.is_character_device()

    def is_fifo(self) -> bool:
        """Return whether this inode is a FIFO (named pipe)."""
        return stat.S_ISFIFO(self.mode)

    def is_socket(self) -> bool:
        """Return whether this inode is a socket."""
        return stat.S_ISSOCK(self.mode)

    def is_ipc(self) -> bool:
        """Return whether this inode is an IPC object (FIFO or socket)."""
        return self.is_fifo() or self.is_socket()

    def listdir(self) -> dict[str, INode]:
        """Return a directory listing."""
        return {inode.name: inode for inode in self.iterdir()}

    dirlist = listdir

    def iterdir(self) -> Iterator[INode]:
        """Iterate directory contents."""
        if not self.is_dir():
            raise NotADirectoryError(f"{self!r} is not a directory")

        self.fs.fh.seek(self.data_offset)
        while (offset := self.fs.fh.tell()) != self.data_offset + self.size:
            yield self.fs.inode(offset)

    def open(self) -> BlockStream | RangeStream:
        """Return a file-like object for reading."""
        if self.is_dir():
            return RangeStream(self.fs.fh, self.data_offset, self.size)
        return BlockStream(self)


class BlockStream(AlignedStream):
    def __init__(self, inode: INode):
        super().__init__(inode.size, c_cramfs.CRAMFS_BLOCK_SIZE)
        self.inode = inode
        self.blocks = self.inode.blocks
        self.num_blocks = len(self.blocks)

    def _read(self, offset: int, length: int) -> bytes:
        result = []
        block_idx = offset // c_cramfs.CRAMFS_BLOCK_SIZE

        while length > 0 and block_idx < self.num_blocks:
            start, read_len = self.blocks[block_idx]
            result.append(self.inode.fs._read_block(start, read_len))

            length -= c_cramfs.CRAMFS_BLOCK_SIZE
            block_idx += 1

        return b"".join(result)
