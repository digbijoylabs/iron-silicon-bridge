/* Example: Defining a DB2 Table with a Field Procedure */
CREATE TABLE PRODDB.CUSTOMER_DATA
  ( CUST_ID      CHAR(10) NOT NULL,
    SSN          CHAR(9)  FIELDPROC FPEC001, /* Exit intercept */
    FIRST_NAME   VARCHAR(50),
    LAST_NAME    VARCHAR(50),
    CREDIT_SCORE INTEGER
  ) IN PRODDB.TSPACE01;
