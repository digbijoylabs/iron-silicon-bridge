/* Reference Blueprint: REXX Swarm Dependency Scanner */
PARSE ARG dsn member                                    /* <1> */
IF dsn = '' | member = '' THEN EXIT 8

"ALLOC F(SYSLIB) DA('"dsn"') SHR REUSE"      /* <2> */
CALL OUTTRAP 'amb.'
ADDRESS TSO "AMBLIST LISTOBJ DDN=SYSLIB M="member /* <3> */
CALL OUTTRAP 'OFF'

has_cobol = 0; has_hlasm = 0
DO i = 1 TO amb.0
   IF POS('IGZ', amb.i) > 0 THEN has_cobol = 1 /* <4> */
   IF POS('DFH', amb.i) > 0 THEN has_hlasm = 1
END

/* Emit structured JSON descriptor for AI Swarm ingestion */
out = '{"mod":"'member'", "cbl":'has_cobol', "cics":'has_hlasm'}'
SAY out                                           /* <5> */
"FREE F(SYSLIB)"
EXIT 0
