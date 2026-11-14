01  WS-MORTGAGE-CALC.
           05  WS-PRINCIPAL-AMT       PIC S9(9)V99   COMP-3.
           05  WS-INTEREST-RATE       PIC S9(3)V9(5) COMP-3.
           05  WS-ACCRUED-INT         PIC S9(7)V99   COMP-3.
           
       CALCULATE-INTEREST.
           COMPUTE WS-ACCRUED-INT = 
              WS-PRINCIPAL-AMT * (WS-INTEREST-RATE / 1200)
           ON SIZE ERROR
              GO TO ERROR-HANDLER-400.
