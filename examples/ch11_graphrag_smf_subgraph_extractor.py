# Reference Blueprint: GraphRAG Subgraph Context Extractor
class SubgraphContextExtractor:
    def __init__(self, max_tokens: int = 4000):
        self.max_tokens = max_tokens                  #
    def extract_bounded_context(self, client,
                                target: str) -> dict:
        q = ("MATCH (p:Prog {name: $n})"
             "-[r:CALLS|READS|WRITES*1..2]-(d)"
             " RETURN r, d LIMIT 100")
        data = client.run(q, n=target).data()         #
        ctx = {"root": target, "deps": [], "tokens": 0} #
        for rec in data:
            r = rec['r']
            r_list = r if isinstance(r, list) else [r]
            rel_str = "->".join(
                getattr(x, 'type', 'CALLS') for x in r_list
            )
            d_name = rec['d'].get('name', 'UNKNOWN')
            dep = f"{rel_str}:{d_name}"
            cost = max(1, len(dep) // 4) # Illustrative estimate
            if ctx["tokens"] + cost > self.max_tokens: #
                break
            ctx["deps"].append(dep)
            ctx["tokens"] += cost
        return ctx                                    #
