# Reference Blueprint: SYSADATA Compiler Geometry Extractor
import struct

def parse_adata_record(raw_bytes: bytes) -> dict:
    """Extract compiler byte geometry from SYSADATA records."""
    hdr = raw_bytes[:4]
    rec_type, rec_len = struct.unpack(">HH", hdr)     #
    if rec_type != 0x0042:  # Symbol Table Record
        return {}

    # Extract big-endian absolute offset and field length
    geom = raw_bytes[12:20]
    offset, length = struct.unpack(">II", geom)       #
    ebcdic_name = raw_bytes[20:50].split(b'\x00')[0]
    field_name = ebcdic_name.decode('cp037').strip()  #
    return {
        "field": field_name,
        "offset": offset,
        "length": length,
        "is_valid": True  #
    }
