/* Example: REXX script checking return code and trapping msgs */
"ALLOC DDNAME(SYSIN) DSN('AUB.PROD.PARMLIB(DB2CONF)') SHR"
IF RC ^= 0 THEN DO
   SAY 'Allocation failed. Terminating automation.'
   EXIT 8
END
