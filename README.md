# CST-submit
CST submission examples for HTCondor cluster at CERN

Launch flags (see /afs/cern.ch/project/parc/cst2018/cst_design_environment --help):

```
--m   START CST MICROWAVE STUDIO
--t   START CST PARTICLE STUDIO
```

Solver options flags:
```
--p   Start the PARAMETER SWEEP using the last solver used
--o   Start the OPTIMISER using the last solver used
--f   Start the FREQUENCY solver
--r   Start the TRANSIENT solver
--e   Start the EIGENMODE solver
--tp  Start the PARTICLE TRACKING solver. (only in --t)
--tw  Start the WAKEFIELD solver. (only in --t)
--pic Start the Particle In Cell (PIC) solver. (only in --t)
```


Based on these examples: https://cern.service-now.com/service-portal/article.do?n=KB0005870
