# Reference Blueprint: Modernization Factory Gate Orchestrator
class ModernizationFactoryOrchestrator:
    GATES = ['UNDERSTAND', 'BOUNDS', 'SYNTH', 'SEC', 'PARITY']
    def __init__(self, key: bytes, authorized_leads: set):
        self.key, self.authorized = key, authorized_leads #
        self.nonces: set[str] = set()

    def evaluate_candidate(self, mod_id: str, art_dig: str,
                           evi_dig: str, env: str,
                           results: dict) -> tuple[bool, str]:
        for g in self.GATES:                          #
            score = results.get(g, 0.0)
            if not (math.isfinite(score) and score >= 1.0):
                return False, f"Failed gate {g}"      #
        lead = results.get('human_signoff', {})
        s_id, exp = lead.get('signer_id'), lead.get('exp', 0)
        n, sig = lead.get('nonce', ''), lead.get('sig', '')
        if time.time() > exp or n in self.nonces:
            return False, "Signature expired or replayed"
        msg = f"{mod_id}:{art_dig}:{evi_dig}:{env}:{exp}:{n}:{s_id}"
        mac = hmac.new(self.key, msg.encode(), 'sha256').hexdigest()
        if (s_id not in self.authorized or
                not hmac.compare_digest(sig, mac)):
            return False, "Invalid lead signature"    #
        self.nonces.add(n)
        raw = f"PROMOTE:{mod_id}:{art_dig}:{evi_dig}:{env}".encode()
        tok = hmac.new(self.key, raw, 'sha256').hexdigest()
        return True, f"APPROVED:{mod_id}:{env}:{tok[:16]}" #
