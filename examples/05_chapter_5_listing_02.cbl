01  DB2-CUSTOMER-ROW.
           05  CUST-ID               PIC X(10).
           05  CUST-NAME             PIC X(50).
           05  CUST-BALANCE          PIC S9(7)V99 COMP-3.
       
       01  DB2-INDICATOR-VARS.
           05  CUST-NAME-IND         PIC S9(4) COMP.
           05  CUST-BAL-IND          PIC S9(4) COMP.
