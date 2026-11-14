# Reference Blueprint: Provenance Assertion Kernel
class ProvenanceAssertionEngine:
    def __init__(self, key: bytes, max_drift_seconds: int = 60):
        self.key, self.max_drift = key, max_drift_seconds #
    def verify_retrieval(self, meta: dict,
                         cur_lsn: int) -> tuple[bool, str]:
        src = meta.get('source_id')
        lsn = meta.get('source_lsn')
        age = meta.get('age_seconds', 9999)           #
        if not (isinstance(src, str) and isinstance(lsn, int)):
            return False, "Malformed provenance metadata"
        if age > self.max_drift:
            return False, f"Chunk stale: age {age}s"  #
        if lsn > cur_lsn:
            return False, f"Drift: LSN {lsn}"         #
        raw = f"{src}:{lsn}:{cur_lsn}".encode()
        sig = hmac.new(self.key, raw, 'sha256').hexdigest()[:16]
        return True, f"VERIFIED:{src}:LSN_{lsn}:{sig}" #
