import struct
from typing import BinaryIO

from nwn._shared import get_nwn_encoding, GenderedLanguage, FileMagic
from nwn.gff._types import (
    Dword,
    CExoString,
    ResRef,
    CExoLocString,
    Struct,
    List,
    Double,
    Int64,
    Dword64,
    VOID,
    SIMPLE_TYPES,
)
from nwn.gff._impl import FieldKind, Header, FieldEntry, StructEntry


def read(file: BinaryIO) -> tuple[Struct, FileMagic]:
    """
    Read a GFF data from a binary stream.

    Example:
        >>> with open("file.gff", "rb") as f:
        ...     root, file_type = gff.read(f)
        ...     print(root)

    Args:
        file: The binary stream to read from.

    Returns:
        A tuple containing the root struct and the file type.
    """

    root_offset = file.tell()
    labels = []
    fields = []
    structs = []
    list_indices = []
    field_indices = []
    resolved_structs = {}
    struct_parents = {}

    header = Header(
        file.read(4).decode("ascii"),
        file.read(4).decode("ascii"),
        *struct.unpack("<12i", file.read(48)),
    )
    if header.file_version != "V3.2":
        raise ValueError(f"Unsupported GFF version: {header.file_version}")

    file.seek(root_offset + header.label_offset)
    for _ in range(header.label_count):
        labels.append(file.read(16).split(b"\x00")[0].decode("ascii"))

    file.seek(root_offset + header.field_offset)
    for _ in range(header.field_count):
        data = struct.unpack("<III", file.read(12))
        fields.append(FieldEntry(FieldKind(data[0]), data[1], data[2]))

    file.seek(root_offset + header.field_indices_offset)
    for _ in range(header.field_indices_size // 4):
        field_indices.append(struct.unpack("<I", file.read(4))[0])

    file.seek(root_offset + header.list_indices_offset)
    for _ in range(header.list_indices_size // 4):
        list_indices.append(struct.unpack("<I", file.read(4))[0])

    file.seek(root_offset + header.struct_offset)
    for _ in range(header.struct_count):
        data = struct.unpack("<III", file.read(12))
        structs.append(StructEntry(data[0], data[1], data[2]))

    def _read_field_value(field):
        if field.type in SIMPLE_TYPES:
            cls = SIMPLE_TYPES[field.type]
            us = cls.SIMPLE_DATA_FORMAT
            data = struct.pack("<I", field.data_or_offset)[: struct.calcsize(us)]
            up = struct.unpack("<" + us, data)
            return cls(up[0])

        file.seek(root_offset + header.field_data_offset + field.data_or_offset)

        if field.type == FieldKind.DOUBLE:
            return Double(struct.unpack("<d", file.read(8))[0])

        if field.type == FieldKind.DWORD64:
            return Dword64(struct.unpack("<Q", file.read(8))[0])

        if field.type == FieldKind.INT64:
            return Int64(struct.unpack("<q", file.read(8))[0])

        if field.type == FieldKind.CEXOSTRING:
            sz = struct.unpack("<I", file.read(4))[0]
            if sz > 0xFFFF:
                raise ValueError("String too long")
            return CExoString(file.read(sz).decode(get_nwn_encoding()))

        if field.type == FieldKind.RESREF:
            sz = struct.unpack("<b", file.read(1))[0]
            if sz > 16:
                raise ValueError("Resref too long")
            return ResRef(file.read(sz).decode(get_nwn_encoding()))

        if field.type == FieldKind.CEXOLOCSTRING:
            _ = struct.unpack("<I", file.read(4))[0]
            strref = Dword(struct.unpack("<I", file.read(4))[0])
            count = struct.unpack("<I", file.read(4))[0]
            entries = {}
            for _ in range(count):
                fid = GenderedLanguage.from_id(struct.unpack("<I", file.read(4))[0])
                sz = struct.unpack("<I", file.read(4))[0]
                entries[fid] = file.read(sz).decode(get_nwn_encoding())
            return CExoLocString(strref, entries)

        if field.type == FieldKind.VOID:
            sz = struct.unpack("<I", file.read(4))[0]
            return VOID(file.read(sz))

        if field.type == FieldKind.LIST:
            offset = field.data_or_offset // 4
            size = list_indices[offset]
            start = offset + 1
            end = start + size

            return List([_read_struct(field, lid) for lid in list_indices[start:end]])

        if field.type == FieldKind.STRUCT:
            return _read_struct(field, field.data_or_offset)

        raise NotImplementedError(f"Field {field} not implemented")

    def _read_struct(parent, struct_idx) -> Struct:
        if struct_idx in resolved_structs:
            if struct_parents[struct_idx] != parent:
                raise ValueError("Struct already resolved with different parent")
            return resolved_structs[struct_idx]

        struct_entry = structs[struct_idx]

        if struct_entry.field_count == 1:
            field_array_indices = [struct_entry.data_or_offset]
        else:
            start = struct_entry.data_or_offset // 4
            end = start + struct_entry.field_count
            if end < start:
                raise ValueError("Field index array out of bounds")

            field_array_indices = field_indices[start:end]

        resolved_structs[struct_idx] = Struct(
            struct_entry.id,
            **{
                labels[fld.label_index]: _read_field_value(fld)
                for fld in map(lambda x: fields[x], field_array_indices)
            },
        )

        struct_parents[struct_idx] = parent
        return resolved_structs[struct_idx]

    root = _read_struct(None, 0)
    return root, FileMagic(header.file_type)
