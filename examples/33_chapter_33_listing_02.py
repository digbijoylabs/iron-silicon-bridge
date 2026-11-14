# Reference Blueprint: Closed-Loop Agentic Refactoring Engine
class AgenticRefactorEngine:
    def __init__(self, spec_agent, code_agent, verifier):
        self.spec = spec_agent                         #
        self.code, self.vfy = code_agent, verifier

    def refactor_slice(self, pdg: dict, traces: list) -> tuple:
        spec = self.spec.extract_invariants(pdg)       #
        suite = self.vfy.synthesize_suite(spec, traces)#
        for attempt in range(5):
            cand = self.code.synthesize(spec, attempt)
            ok, err = self.vfy.assert_parity(cand, suite)
            if ok:
                return cand, True                      #
            self.code.reflect_and_patch(cand, err)     #
        return "", False
