* Reference Blueprint: CICS Container Retrieval Kernel
       IDENTIFICATION DIVISION.
       PROGRAM-ID. GETACCT.
       DATA DIVISION.
       WORKING-STORAGE SECTION.
       01 WS-RESP              PIC S9(8) COMP.
       01 WS-BUFFER-LEN        PIC S9(8) COMP VALUE 4096.
       01 WS-ACCOUNT-BUFFER    PIC X(4096).
       PROCEDURE DIVISION.
           EXEC CICS GET CONTAINER('ACCOUNT-IN')
                     CHANNEL('AUB-API-CHAN')
                     INTO(WS-ACCOUNT-BUFFER)
                     FLENGTH(WS-BUFFER-LEN)
                     RESP(WS-RESP)
           END-EXEC.
           GOBACK.

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
