01 WS-TRANSACTION-DATA.
          05 WS-TX-TYPE            PIC X(01).
          05 WS-PAYLOAD            PIC X(32).
          05 WS-CARD-INFO REDEFINES WS-PAYLOAD.
             10 WS-CARD-NUM        PIC X(16).
             10 WS-CARD-EXP        PIC X(04).
             10 WS-CARD-CVV        PIC 9(03).
             10 FILLER             PIC X(09).
          05 WS-ACH-INFO REDEFINES WS-PAYLOAD.
             10 WS-ROUTING-NUM     PIC 9(09).
             10 WS-ACCOUNT-NUM     PIC X(17).
             10 FILLER             PIC X(06).
