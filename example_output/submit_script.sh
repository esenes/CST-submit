#!/bin/bash
export EOS_MGM_URL=root://eoshome-e.cern.ch

#copy input file from EOS to local condor jobdir
eos cp /eos/user/e/esenes/simulation_file.cst ./simulation_file.cst

#run CST
/afs/cern.ch/project/parc/cst2018/cst_design_environment -t -tw ./simulation_file.cst --numthreads 32

#compress and copy back to EOS
tar -cvf sim_results.tar ./simulation_file
eos cp ./sim_results.tar /eos/user/e/esenes/sim_results.tar

exit 0
