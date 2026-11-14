# Reference Blueprint: Perpetual Bridge Governance Kernel
class PerpetualBridgePolicy:
    READS = {'CICS_READ', 'SMF_QUERY', 'DB2_RO'}
    MUTS = {'CICS_WRITE', 'DB2_UPDATE', 'JCL_SUBMIT'}
    def __init__(self, creds: dict[str, bytes], sink):
        self.creds, self.sink = creds, sink           #
        self.seen: set[str] = set()
    def _ok(self, s: str, m: str, sig: str) -> bool:
        k = self.creds.get(s)
        return bool(k and hmac.compare_digest(
            hmac.new(k, m.encode(), 'sha256').hexdigest(), sig))
    def evaluate(self, act: str, pay: dict) -> tuple[bool, str]:
        if act not in self.READS | self.MUTS:         #
            return False, "Unknown action rejected"
        if act in self.READS:  # Upstream RACF/SAF context verified
            return True, "Read authorized by policy"
        ts, n = pay.get('ts', 0), pay.get('nonce', '')
        if abs(time.time() - ts) > 300 or n in self.seen:
            return False, "Expired or replayed"       #
        b_h = hashlib.sha256(pay.get('body', b'')).hexdigest()
        rsc = pay.get('rsc', '')
        canon = f"{act}:{rsc}:{b_h}:{ts}:{n}"         #
        v = {s for s, g in pay.get('signatures', {}).items()
             if self._ok(s, canon, g)}
        if len(v) < 2: return False, "Dual custody required"
        self.seen.add(n)
        self.sink.write("ACT", v=1,                   #
                        data={"act": act, "by": list(v)})
        return True, "Request verified"
