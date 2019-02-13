######
# you need to be in some allowed computing group to do so !
# possibilities:
# - 48 cores and 500GB RAM machines
# - 24 cores and 1TB RAM machines


# user inputs
jobTitle = 'prism_10mmside_50B30F_halfH'              # no extension !
simulation_file_dir = '/eos/user/e/esenes/'     # terminate with /
simulation_file = 'prism_10mmside_50B30F_halfH.cst'                   # with extension !
num_threads = 48                           # ALLOWED 48 CORES or 24
suite_type = '-t'
solver_type = '-tw'
jobFlavour = 'tomorrow'

# options
needMpi = False # just for BIG number of cells (>billion)


#------------------
# user settings
eos_home_location = 'root://eoshome-e.cern.ch'
user_afs_home = '/afs/cern.ch/user/e/esenes/'
accounting_group = 'group_u_BE.u_bigmem'

# options handling
assert num_threads==48 or num_threads==24
## MPI
MPI = ''
if needMpi:
    MPI = ' --withmpi '

# write the script that will run on the cluster
f = open(jobTitle+'.sh','w')
f.write('#!/bin/bash\n')
f.write('export EOS_MGM_URL='+eos_home_location+'\n')
f.write('\n#copy input file from EOS to local condor jobdir\n')
f.write('eos cp '+simulation_file_dir+simulation_file+' ./'+simulation_file+'\n')
f.write('\n#Run CST !\n')
f.write('hostname -f> machinefile\n')
f.write('/afs/cern.ch/project/parc/cst2018/cst_design_environment '+suite_type+' '+solver_type+' ./'+simulation_file+' --numthreads '+str(num_threads)+MPI+'--machinefile machinefile'+'\n')
f.write('\n#Compress and copy back to EOS\n')
f.write('tar -cvf '+jobTitle+'.tar ./'+simulation_file[:-4]+' ./'+simulation_file+'\n')
f.write('eos cp ./'+jobTitle+'.tar '+simulation_file_dir+jobTitle+'.tar\n')
f.write('\nexit 0\n')
f.close()

# write the condor submission file
f = open(jobTitle+'.sub','w')
f.write('executable\t\t= '+jobTitle+'.sh\n')
f.write('RequestCpus\t\t= '+str(num_threads)+'\n')
f.write('+BigMemJob\t\t= True\n')
f.write('+WCKey\t\t= CST\n')
f.write('+AccountingGroup\t\t= \"'+accounting_group+'\"\n')
if num_threads == 48: # only for 48 cores machines
    f.write('+Requirements = OpSysAndVer =?= \"CentOS7\" \n')
f.write('+JobFlavour\t\t= \"'+jobFlavour+'\"\n')
f.write('environment\t\t= CST_INSTALLPATH=\"/afs/cern.ch/project/parc/cst2018\"; CST_WAIT_FOR_LICENSE=on; CST_LICENSE_SERVER=\"1705@lxlicen01\",\"1705@lxlicen02\",\"1705@lxlicen03\"; HOME=\"'+user_afs_home+'\"\n')
file_ending = '''transfer_output_files   = \"\"
output          = cst.$(ClusterId).$(ProcId).out
error           = cst.$(ClusterId).$(ProcId).err
log             = cst.$(ClusterId).$(ProcId).log
queue\n
'''
f.write(file_ending)
f.close()



# toDO -->
# 4) interactive UI for the terminal ???
