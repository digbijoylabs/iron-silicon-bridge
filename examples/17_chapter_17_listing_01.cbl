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
