EXEC CICS WEB READ
            HTTPHEADER('traceparent')
            VALUE(WS-TRACEPARENT)
            NAMELENGTH(11)
            VALUELENGTH(55)
       END-EXEC.
