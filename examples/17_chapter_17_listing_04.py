# Reference Blueprint: CICS Container Marshalling Kernel
class CicsContainerMarshaller:
    def __init__(self, codepage: str = "cp500"):
        self.codepage = codepage                      #
    def pack_comp3(self, val: int, length: int) -> bytes:
        max_d = length * 2 - 1
        if abs(val) >= 10 ** max_d:                   #
            raise ValueError(f"Exceeds size {length}B")
        sign = 0x0D if val < 0 else 0x0C
        raw = f"{abs(val):0{max_d}d}{sign:X}"
        return bytes.fromhex(raw)                     #
    def build_channel_payload(self, fields: dict) -> dict:
        c = {}
        for name, (val, c_type, sz) in fields.items():
            if c_type == 'CHAR':
                if len(str(val)) > sz:
                    raise ValueError(f"Exceeds {sz}") #
                enc = str(val).ljust(sz).encode(self.codepage)
                c[name] = enc
            elif c_type == 'BIT':
                c[name] = self.pack_comp3(val, sz)    #
        return c
