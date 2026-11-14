EXEC CICS GET CONTAINER('AIPAYLOAD')
                 CHANNEL('AICHANNEL')
                 INTO(WS-INPUT-BUFFER)
                 RESP(WS-RESP)
       END-EXEC.
