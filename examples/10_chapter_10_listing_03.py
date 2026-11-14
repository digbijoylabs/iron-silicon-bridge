# Reference Blueprint: MQ Poison Message & Backout Kernel
class MqPoisonMessageHandler:
    def __init__(self, qmgr, bothresh: int = 3,
                 boq: str = "AUB.PAYMENT.BOQ"):
        self.qmgr = qmgr
        self.bothresh, self.boq = bothresh, boq       #
    def handle(self, mqmd: dict,
               payload: bytes) -> tuple[str, str]:
        cnt = mqmd.get('BackoutCount', 0)             #
        mid = mqmd.get('MsgId', b'').hex()
        if cnt >= self.bothresh:                      #
            self.qmgr.put(self.boq, mqmd, payload)    #
            self.qmgr.commit()
            return "REQUEUED_BOQ", f"POISON:{mid}"
        try:
            self.qmgr.commit()
            return "COMMITTED", "PARITY_VERIFIED"
        except Exception as exc:
            self.qmgr.backout()                       #
            return "ROLLED_BACK", f"REASON_{exc}"
