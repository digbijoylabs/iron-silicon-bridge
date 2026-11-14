-- The Outbox Table Definition
CREATE TABLE outbox_events (
    event_id UUID PRIMARY KEY,
    aggregate_type VARCHAR(255) NOT NULL,
    aggregate_id VARCHAR(255) NOT NULL,
    event_type VARCHAR(255) NOT NULL,
    payload JSONB NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    processed BOOLEAN DEFAULT FALSE
);

/* Example: Defining a DB2 Table with a Field Procedure */
CREATE TABLE PRODDB.CUSTOMER_DATA
  ( CUST_ID      CHAR(10) NOT NULL,
    SSN          CHAR(9)  FIELDPROC FPEC001, /* Exit intercept */
    FIRST_NAME   VARCHAR(50),
    LAST_NAME    VARCHAR(50),
    CREDIT_SCORE INTEGER
  ) IN PRODDB.TSPACE01;
