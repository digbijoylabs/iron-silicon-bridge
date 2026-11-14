//AIAUTOB  JOB (ACCT),'AI BATCH EXEC',
//             CLASS=A,MSGCLASS=X,MSGLEVEL=(1,1)
//*-------------------------------------------------------
//* This JCL submits a batch job triggered by an AI swarm.
//* The swarm must monitor the JES spool for completion.
//*-------------------------------------------------------
//STEP01   EXEC PGM=COBPROG1
//STEPLIB  DD DSN=PROD.LOADLIB,DISP=SHR
//INPUT    DD DSN=PROD.DATA.IN(0),DISP=SHR
//OUTPUT   DD DSN=PROD.DATA.OUT(+1),
//            DISP=(NEW,CATLG,DELETE),
//            SPACE=(CYL,(50,10),RLSE),
//            DCB=(RECFM=FB,LRECL=80,BLKSIZE=800)
//SYSOUT   DD SYSOUT=*
//SYSDBOUT DD SYSOUT=*
