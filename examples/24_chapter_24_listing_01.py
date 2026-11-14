# Reference Blueprint: SMF Real-Time Anomaly Scoring Kernel
class SmfAnomalyDetector:
    def __init__(self, alert_sink=None, threshold: float = 0.85):
        self.sink = alert_sink
        self.threshold = threshold                    #
    def score_record(self, r_type: int,
                     feats: dict) -> tuple[bool, float]:
        if r_type != 110:                             #
            return False, 0.0
        cpu = feats.get('cpu_ms', 0.0)
        susp = feats.get('susp_ms', 0.0)
        ratio = susp / max(cpu, 0.001)                #
        score = min(1.0, ratio / 10.0)
        if score >= self.threshold:                   #
            self.emit_alert(feats, score)
            return True, score
        return False, score

    def emit_alert(self, feats: dict, score: float) -> dict:
        evt = {"tran_id": feats.get('tran_id'), "score": score}
        if self.sink:
            self.sink.publish("OPERATOR_ALERT", evt)  #
        return evt
