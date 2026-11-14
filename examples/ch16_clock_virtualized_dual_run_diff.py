# Reference Blueprint: Dual-Run Parity Comparator
class RecordParityComparator:
    def __init__(self, req: set[str], fin: set[str]):
        low = lambda s: {f.lower() for f in s}
        self.req, self.fin = low(req), low(fin)       #
        self.mask = {'x_trace_id', 'x_span_id'}
    def clean(self, d: dict) -> dict:
        out = {}
        for k, v in d.items():
            if (lk := k.lower()) not in self.mask:
                if lk in out: raise ValueError(k)     #
                out[lk] = v
        return out
    def compare(self, z: dict, cl: dict) -> tuple[bool, str]:
        z, cl = self.clean(z), self.clean(cl)
        if not self.req.issubset(z) or set(z) != set(cl): #
            return False, "SCHEMA_KEY_MISMATCH"
        for k, zv in z.items():
            if k in self.fin:
                d1, d2 = Decimal(str(zv)), Decimal(str(cl[k]))
                if not (d1.is_finite() and d1 == d2):
                    return False, f"FINANCIAL_DRIFT:{k}" #
            elif (type(zv), zv) != (type(cl[k]), cl[k]):
                return False, f"VALUE_DRIFT:{k}"      #
        return True, "RECORD_MATCH"
