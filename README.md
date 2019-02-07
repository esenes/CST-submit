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
Possible job flavours:
```
espresso     = 20 minutes
microcentury = 1 hour
longlunch    = 2 hours
workday      = 8 hours
tomorrow     = 1 day
testmatch    = 3 days
nextweek     = 1 week
```

or otherwise change `+JobFlavour = "the flavour you picked"` to `+MaxRuntime = Number of seconds`. The second approach allows to plan longer jobs than a week.

In the normal jobs one gets 2 GB of RAM and 20 GB of disk space per requested core. So for 16 cores, 32 gigs of RAM and 320 of disk space.

In big memory jobs one can access 2 kinds of machines: 48 cores and 500GB of RAM -or- 24 cores and 1TB of RAM.





Based on these examples: https://cern.service-now.com/service-portal/article.do?n=KB0005870 and 
http://batchdocs.web.cern.ch/batchdocs/local/submit.html 
