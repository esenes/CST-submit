#!/bin/bash
export EOS_MGM_URL=root://eoshome-e.cern.ch

#copy input file from EOS to local condor jobdir
eos cp /eos/user/e/esenes/mySim.cst ./mySim.cst

#Run CST !
/afs/cern.ch/project/parc/cst2018/cst_design_environment -t -tw ./mySim.cst --numthreads 24

#Compress and copy back to EOS
tar -cvf my_script.tar ./mySim
eos cp ./my_script.tar /eos/user/e/esenes/my_script.tar

exit 0
