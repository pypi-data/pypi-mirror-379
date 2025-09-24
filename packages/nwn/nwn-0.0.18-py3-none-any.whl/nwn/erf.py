"""Read and write ERF (Encapsulated Resource Format) archives."""

import struct
from typing import NamedTuple, BinaryIO
from enum import Enum
from datetime import date, timedelta

from ._shared import (
    get_nwn_encoding,
    GenderedLanguage,
    restype_to_extension,
    extension_to_restype,
    FileMagic,
)


class Reader:
    """
    Class to read and access an ERF archive (MOD, HAK, ERF, ...)

    Example:
        >>> with open("Prelude.mod", "rb") as file:
        ...    erf = Reader(file)
        ...    print(erf.filenames)
        ...    gff_data = erf.read_file("item.uti")
        ...    ...

    Args:
        file: The file object to read from.
    """

    class Version(Enum):
        V_1_0 = "V1.0"
        # E_1_0 = "E1.0"

    class _Header(NamedTuple):
        file_type: FileMagic
        file_version: "Reader.Version"
        locstr_count: int
        locstr_sz: int
        entry_count: int
        offset_to_locstr: int
        offset_to_keylist: int
        offset_to_reslist: int
        build_year: int
        build_day: int
        description_strref: int

    class Entry(NamedTuple):
        resref: str
        restype: int
        offset: int
        disk_size: int
        uncompressed_size: int

        @property
        def filename(self):
            return f"{self.resref.lower()}.{restype_to_extension(self.restype)}"

    def _seek(self, relative_to_start):
        self._file.seek(self._root_offset + relative_to_start)

    def __init__(self, file, max_entries=65535, max_locstr=100):
        self._file = file
        self._root_offset = self._file.tell()

        ft = self._file.read(4)
        fv = self.Version(self._file.read(4).decode("ASCII"))
        va = struct.unpack("IIIIIIIII", self._file.read(36))
        self._header = self._Header(FileMagic(ft), fv, *va)

        if self._header.entry_count > max_entries:
            raise ValueError("Too many resources")

        if self._header.locstr_count > max_locstr:
            raise ValueError("Too many localized strings")

        self._seek(self._header.offset_to_locstr)
        loc_str = {}
        for _ in range(self._header.locstr_count):
            lid = GenderedLanguage.from_id(struct.unpack("I", self._file.read(4))[0])
            sz = struct.unpack("I", self._file.read(4))[0]
            st = self._file.read(sz).decode(get_nwn_encoding())
            loc_str[lid] = st

        self._seek(self._header.offset_to_reslist)
        resources = []
        for _ in range(self._header.entry_count):
            offset = struct.unpack("I", self._file.read(4))[0]
            disk_size = struct.unpack("I", self._file.read(4))[0]
            uncompressed = disk_size
            resources.append((offset, disk_size, uncompressed))

        self._seek(self._header.offset_to_keylist)
        keys = []
        for _ in range(self._header.entry_count):
            resref = self._file.read(16).split(b"\x00")[0].decode("ASCII")
            _ = struct.unpack("I", self._file.read(4))[0]  # res_id unused
            res_type = struct.unpack("H", self._file.read(2))[0]
            _ = self._file.read(2)  # unused
            keys.append((resref, res_type))

        self._localized_strings = loc_str

        self._files = {
            f"{resref.lower()}.{restype_to_extension(restype)}": self.Entry(
                resref, restype, o, d, u
            )
            for (resref, restype), (o, d, u) in zip(keys, resources)
        }

    @property
    def file_type(self) -> FileMagic:
        """The file type of the ERF archive."""
        return self._header.file_type

    @property
    def build_date(self) -> date:
        """The build date of the ERF archive."""
        return date(1900 + self._header.build_year, 1, 1) + timedelta(
            days=self._header.build_day
        )

    @property
    def localized_strings(self) -> dict[GenderedLanguage, str]:
        """The localized strings in the ERF archive."""
        return self._localized_strings

    @property
    def description_strref(self) -> int:
        """The STRREF set in the ERF header. 0 if not set."""
        return self._header.description_strref

    @property
    def filenames(self) -> list[str]:
        """
        Returns the filenames in the ERF archive.

        Returns:
            A list of filenames present in the ERF archive.
        """
        return list(self._files.keys())

    @property
    def filemap(self) -> dict[str, Entry]:
        """
        Returns the mapping of files.

        This method returns the internal dictionary that maps file names to their
        corresponding file data.

        Returns:
            A dict mapping file names to their corresponding Entry objects.
        """
        return self._files

    def read_file(self, filename: str) -> bytes:
        """
        Retrieve the contents of a file from the archive.

        Args:
            filename: The name of the file to retrieve.

        Returns:
            The contents of the file as a byte string.

        Raises:
            KeyError: If the file is not found in the archive.
            ValueError: If the filename is of a unknown restype.
        """
        resource = self._files[filename.lower()]
        self._seek(resource.offset)
        return self._file.read(resource.disk_size)


class Writer:
    """
    A class to write ERF files.

    Example:
        >>> with open("Prelude.mod", "wb") as file:
        ...    with Writer(file, file_type="MOD ") as e:
        ...        e.add_localized_string(Language.ENGLISH, "Prelude")
        ...        with open("item.uti", "rb") as item:
        ...            e.add_file("item.uti", item)
    """

    class Entry(NamedTuple):
        resref: str
        restype: int
        offset: int
        size: int

    def __init__(
        self,
        file: BinaryIO,
        file_type: FileMagic = FileMagic(b"ERF "),
        build_date=date.today(),
    ):
        self._file = file
        self._entries = []
        self._locstr = {}

        self._file_type = FileMagic(file_type)
        self._build_year = build_date.year - 1900
        self._build_day = build_date.timetuple().tm_yday - 1

    def __enter__(self):
        self._file.write(self._file_type)
        self._file.write(Reader.Version.V_1_0.value.encode("ASCII"))
        self._file.write(b"\x00" * 36)
        self._file.write(b"\x00" * 116)  # reserved bytes as per spec
        assert self._file.tell() == 160
        return self

    def add_localized_string(self, gendered_lang: GenderedLanguage, text):
        self._locstr[gendered_lang] = text

    def add_file_data(self, filename: str, data: bytes):
        """
        Adds a file to the ERF archive.

        Args:
            filename: The name of the file to add, including its extension.
            data: The binary data of the file to add.
        """
        offset = self._file.tell()
        size = len(data)
        # ensure we have a restype
        base, ext = filename.split(".")
        if len(base) > 16:
            raise ValueError("Resource name too long")
        rt = extension_to_restype(ext)
        self._entries.append(Writer.Entry(base, rt, offset, size))
        self._file.write(data)
        assert self._file.tell() == offset + size

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is not None:
            return False

        locstr_offset = self._file.tell()
        for gendered_lang, text in self._locstr.items():
            encoded_text = text.encode(get_nwn_encoding())
            self._file.write(struct.pack("I", gendered_lang.to_id()))
            self._file.write(struct.pack("I", len(encoded_text)))
            self._file.write(encoded_text)
        locstr_size = self._file.tell() - locstr_offset

        keylist_offset = self._file.tell()
        for resref, restype, offset, size in self._entries:
            res_ref = resref.ljust(16, "\x00").encode("ASCII")
            res_id = 0  # res_id unused
            self._file.write(res_ref)
            self._file.write(struct.pack("I", res_id))
            self._file.write(struct.pack("H", restype))
            self._file.write(b"\x00\x00")  # Unused

        reslist_offset = self._file.tell()
        for _, _, offset, size in self._entries:
            self._file.write(struct.pack("i", offset))
            self._file.write(struct.pack("i", size))

        eof_offset = self._file.tell()

        self._file.seek(8)
        self._file.write(
            struct.pack(
                "IIIIIIIII",
                len(self._locstr),
                locstr_size,
                len(self._entries),
                locstr_offset,
                keylist_offset,
                reslist_offset,
                self._build_year,
                self._build_day,
                0,  # description_strref
            )
        )
        self._file.seek(eof_offset)
        return False
