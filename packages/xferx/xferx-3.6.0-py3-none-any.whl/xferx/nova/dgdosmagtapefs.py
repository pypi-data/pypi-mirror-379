# Copyright (C) 2014 Andrea Bonomi <andrea.bonomi@gmail.com>

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to
# deal in the Software without restriction, including without limitation the
# rights to use, copy, modify, merge, publish, distribute, sublicense, and/or
# sell copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

import errno
import math
import os
import struct
import sys
import typing as t
from datetime import date

from ..abstract import AbstractDirectoryEntry, AbstractFile, AbstractFilesystem
from ..commons import ASCII, IMAGE, READ_FILE_FULL, filename_match
from ..device.abstract import AbstractDevice
from ..device.tape import Tape

__all__ = [
    "DGDOSMagTapeFile",
    "DGDOSMagTapeDirectoryEntry",
    "DGDOSMagTapeFilesystem",
]


# RDOS System Reference - Pag 35
# https://bitsavers.trailing-edge.com/pdf/dg/software/rdos/093-400027-00_RDOS_SystemReference_Oct83.pdf

DATA_WORDS = 255  # data words per block
DATA_BLOCK_SIZE = DATA_WORDS * 2  # data block size in bytes
FILE_NUMBER_WORDS = 2  # extra words per block
FILE_NUMBER_SIZE = FILE_NUMBER_WORDS * 2  # file number size in bytes
TAPE_BLOCK_WORDS = DATA_WORDS + FILE_NUMBER_WORDS  # tape block size in words
TAPE_BLOCK_SIZE = TAPE_BLOCK_WORDS * 2  # tape block size in bytes
DUMP_NAME_BLOCK_ID = 0o377


def get_file_number(buffer: bytes) -> int:
    """
    Get the file number from the tape block
    """
    if len(buffer) != TAPE_BLOCK_SIZE:
        raise OSError(errno.EIO, f"Invalid block size {len(buffer)}")
    file_number1, file_number2 = struct.unpack(">HH", buffer[-FILE_NUMBER_SIZE:])
    if file_number1 != file_number2:
        raise OSError(errno.EIO, f"Invalid file number: {file_number1} != {file_number2}")
    return file_number1  # type: ignore


class DGDOSMagTapeFile(AbstractFile):
    entry: "DGDOSMagTapeDirectoryEntry"
    closed: bool
    size: int  # size in bytes

    def __init__(self, entry: "DGDOSMagTapeDirectoryEntry", file_mode: t.Optional[str] = None):
        self.entry = entry
        self.closed = False
        self.file_mode = file_mode or IMAGE
        self.size = entry.get_size()
        self._content: t.Optional[bytes] = None

    @property
    def content(self) -> bytes:
        if self._content is None:
            self.entry.fs.dev.tape_seek(self.entry.tape_pos)
            data = bytearray()
            while True:
                buffer = self.entry.fs.dev.tape_read_forward()
                if not buffer:
                    break
                if len(buffer) != TAPE_BLOCK_SIZE:
                    raise OSError(errno.EIO, os.strerror(errno.EIO))
                data.extend(buffer[:-FILE_NUMBER_SIZE])  # remove the last 2 words of eack block
            self._content = bytes(data)
        return self._content

    def read_block(
        self,
        block_number: int,
        number_of_blocks: int = 1,
    ) -> bytes:
        """
        Read block(s) of data from the file
        """
        if number_of_blocks == READ_FILE_FULL:
            number_of_blocks = self.entry.length
        if (
            self.closed
            or block_number < 0
            or number_of_blocks < 0
            or block_number + number_of_blocks > self.entry.length
        ):
            raise OSError(errno.EIO, os.strerror(errno.EIO))
        data = self.content[block_number * DATA_BLOCK_SIZE : (block_number + number_of_blocks) * DATA_BLOCK_SIZE]
        # Convert to ASCII if needed
        if self.file_mode == ASCII:
            return bytes([0x0A if x == 0x0D else x for x in data])
        else:
            return data

    def write_block(
        self,
        buffer: t.Union[bytes, bytearray],
        block_number: int,
        number_of_blocks: int = 1,
    ) -> None:
        """
        Write block(s) of data to the file
        """
        raise OSError(errno.EROFS, os.strerror(errno.EROFS))

    def get_size(self) -> int:
        """
        Get file size in bytes
        """
        return self.size

    def get_block_size(self) -> int:
        """
        Get file block size in bytes
        """
        return DATA_BLOCK_SIZE

    def close(self) -> None:
        """
        Close the file
        """
        self.closed = True

    def __str__(self) -> str:
        return self.entry.fullname


class DGDOSMagTapeDirectoryEntry(AbstractDirectoryEntry):
    """
    MagTape Directory Entry
    """

    fs: "DGDOSMagTapeFilesystem"
    file_number: int  # File number
    length: int  # Length in blocks
    tape_pos: int = 0  # Tape position
    is_dump: bool = False  # Dump/raw format

    def __init__(self, fs: "DGDOSMagTapeFilesystem"):
        self.fs = fs

    @classmethod
    def read(
        cls,
        fs: "DGDOSMagTapeFilesystem",
        buffer: bytes,
        tape_pos: int,
        size: int,
    ) -> "DGDOSMagTapeDirectoryEntry":
        self = DGDOSMagTapeDirectoryEntry(fs)
        self.file_number = buffer[-1]
        self.tape_pos = tape_pos
        self.length = (len(buffer) + size) // TAPE_BLOCK_SIZE
        self.is_dump = (buffer[0] == DUMP_NAME_BLOCK_ID) if buffer else False
        return self

    @property
    def is_empty(self) -> bool:
        return False

    @property
    def fullname(self) -> str:
        return f"{self.file_number}"

    @property
    def basename(self) -> str:
        return f"{self.file_number}"

    def get_length(self, fork: t.Optional[str] = None) -> int:
        """
        Get the length in blocks
        """
        return self.length

    def get_size(self, fork: t.Optional[str] = None) -> int:
        """
        Get file size in bytes
        """
        return self.length * DATA_BLOCK_SIZE

    def get_block_size(self) -> int:
        """
        Get file block size in bytes
        """
        return DATA_BLOCK_SIZE

    @property
    def creation_date(self) -> t.Optional[date]:
        return None

    @property
    def file_type(self) -> t.Optional[str]:
        """File type"""
        return 'dump' if self.is_dump else 'raw'

    def delete(self) -> bool:
        """
        Delete the directory entry
        """
        raise OSError(errno.EROFS, os.strerror(errno.EROFS))

    def write(self) -> bool:
        """
        Write the directory entry
        """
        raise OSError(errno.EROFS, os.strerror(errno.EROFS))

    def open(self, file_mode: t.Optional[str] = None, fork: t.Optional[str] = None) -> DGDOSMagTapeFile:
        """
        Open a file
        """
        return DGDOSMagTapeFile(self, file_mode)

    def __str__(self) -> str:
        return f"{self.file_number:>3} {self.file_type:<4} {self.tape_pos:>10} {self.get_size():>12}"

    def __repr__(self) -> str:
        return str(self)


class DGDOSMagTapeFilesystem(AbstractFilesystem):
    """
    Data General DOS/RDOS MagTape Filesystem

    Tapes use a fixed block size of 257, 16-bit words.
    The first 255 words of each block contain user data,
    while the last two words contain the file number.

    Word
        +-------------------------------------+
     0  |                                     |
        /                Data                 / 510 bytes
    254 |                                     |
        +-------------------------------------+
    255 |             File number             | 2 bytes
        +-------------------------------------+
    256 |             File number             | 2 bytes
        +-------------------------------------+

    RDOS System Reference - Pag 35
    https://bitsavers.trailing-edge.com/pdf/dg/software/rdos/093-400027-00_RDOS_SystemReference_Oct83.pdf
    """

    fs_name = "dgdosmt"
    fs_description = "Data General DOS/RDOS Magtape"
    fs_platforms = ["nova"]
    fs_entry_metadata = [
        "is_dump",
    ]

    dev: Tape

    def __init__(self, file_or_device: t.Union["AbstractFile", "AbstractDevice"]):
        if isinstance(file_or_device, AbstractFile):
            self.dev = Tape(file_or_device)
        elif isinstance(file_or_device, Tape):
            self.dev = file_or_device
        else:
            raise OSError(errno.EIO, f"Invalid device type for {self.fs_description} filesystem")

    @classmethod
    def mount(
        cls,
        file_or_dev: t.Union["AbstractFile", "AbstractDevice"],
        strict: t.Union[bool, str] = True,
        **kwargs: t.Union[bool, str],
    ) -> "DGDOSMagTapeFilesystem":
        self = cls(file_or_dev)
        if strict:
            # Check if the file is a valid tape
            self.dev.tape_rewind()
            try:
                while True:
                    # First file block
                    buffer = self.dev.tape_read_forward()
                    if not buffer:
                        break
                    file_number = get_file_number(buffer)
                    # Other file blocks
                    try:
                        while True:
                            buffer = self.dev.tape_read_forward()
                            if not buffer:
                                break
                            tmp = get_file_number(buffer)
                            if tmp != file_number:
                                raise OSError(errno.EIO, f"Invalid file number: {tmp} != {file_number}")
                    except EOFError:
                        pass
            except EOFError:
                pass
        return self

    def read_dir_entries(self) -> t.Iterator["DGDOSMagTapeDirectoryEntry"]:
        """
        Read the directory entries from the tape
        """
        self.dev.tape_rewind()
        try:
            while True:
                tape_pos = self.dev.tape_pos
                header, size = self.dev.tape_read_header()
                if not header:
                    break
                yield DGDOSMagTapeDirectoryEntry.read(self, header, tape_pos, size)
        except EOFError:
            pass

    def filter_entries_list(
        self,
        pattern: t.Optional[str],
        include_all: bool = False,
        expand: bool = True,
        wildcard: bool = True,
    ) -> t.Iterator["DGDOSMagTapeDirectoryEntry"]:
        for entry in self.read_dir_entries():
            if filename_match(entry.basename, pattern, wildcard):
                yield entry

    @property
    def entries_list(self) -> t.Iterator["DGDOSMagTapeDirectoryEntry"]:
        for entry in self.read_dir_entries():
            if not entry.is_empty:
                yield entry

    def get_file_entry(self, fullname: str) -> DGDOSMagTapeDirectoryEntry:
        try:
            return next(self.filter_entries_list(fullname, wildcard=False))
        except StopIteration:
            raise FileNotFoundError(errno.ENOENT, os.strerror(errno.ENOENT), fullname)

    def dir(self, volume_id: str, pattern: t.Optional[str], options: t.Dict[str, bool]) -> None:
        pattern = pattern.upper() if pattern else None
        if not options.get("brief"):
            sys.stdout.write("Num Type         Size\n")
            sys.stdout.write("--- ----         ----\n")
        for x in self.filter_entries_list(pattern):
            if options.get("brief"):
                sys.stdout.write(f"{x.fullname:>3}\n")
            else:
                sys.stdout.write(f"{x.fullname:>3} {x.file_type:<4} {x.get_size():>12}\n")

    def examine(self, arg: t.Optional[str], options: t.Dict[str, t.Union[bool, str]]) -> None:
        if arg:
            self.dump(arg)
        else:
            sys.stdout.write("Num Type   Tape pos         Size\n")
            sys.stdout.write("--- ----   --------         ----\n")
            for entry in self.read_dir_entries():
                sys.stdout.write(f"{entry}\n")

    def get_size(self) -> int:
        """
        Get filesystem size in bytes
        """
        return self.dev.get_size()

    @classmethod
    def initialize(
        cls, file_or_dev: t.Union["AbstractFile", "AbstractDevice"], **kwargs: t.Union[bool, str]
    ) -> "DGDOSMagTapeFilesystem":
        """
        Initialize the filesystem
        """
        self = cls(file_or_dev)
        self.dev.tape_rewind()
        # Logical end of tape (2 tape marks)
        self.dev.tape_write_mark()
        self.dev.tape_write_mark()
        self.dev.tape_truncate()
        return self

    def close(self) -> None:
        self.dev.close()

    def chdir(self, fullname: str) -> bool:
        return False

    def get_pwd(self) -> str:
        return ""
