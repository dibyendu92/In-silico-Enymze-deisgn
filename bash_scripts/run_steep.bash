#!/bin/bash
#SBATCH --job-name="evb_run"
#SBATCH --output="evb_run.%j.%N.out"
#SBATCH --partition=shared
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --mem=2G
#SBATCH --export=ALL
#SBATCH -t 47:59:59


# . Modules and paths
module purge
#module load  gaussian

export scratch=/scratch/${USER}/${SLURM_JOB_ID}
export SCRDIR=${scratch}


#===================================================
# . Molaris
export EVB_LIB=${HOME}/lib/evb_kemp.lib
export PARM_LIB=${HOME}/lib/parm_kemp.lib
export AMINO_LIB=${HOME}/lib/amino98_kemp.lib
#export PDB_CONECT=${HOME}/lib/pdb_dictionary
export SOLVENT_OPT=${HOME}/lib/solvent.opt
export LD_LIBRARY_PATH=${HOME}/local/lib/molaris:${LD_LIBRARY_PATH}
export OUT_DIR=.
#===================================================
f='steep_run.inp'
o=`basename $f .inp`.out
#if [ ! -e "${o}" ] ; then
# . Copy files to scratch space
cp  $f     ${scratch}/
cp  *pdb   ${scratch}/
#cp  *dat   ${scratch}/

#        script=call_gauss.py
#        if [ -e "$script" ] ; then
#            cp $script ${scratch}/
#        fi
        
        # . Prepare restart file
#        resfile=`awk '/rest_in/ { print $2; }' $f`
#        if [ "$resfile" ] ; then
#            cp $resfile ${scratch}/
#            sed -i "/rest_in/ s/evb_equil_...\///" ${scratch}/$f
#        fi
        
# . Run simulation
cd ${scratch}/
molaris_hpc9.15_new  $f  >  `basename $f .inp`.out
cd -
        
# . Copy results
o=`basename $f .inp`
if [ ! -e "${o}" ] ; then mkdir ${o} ; fi
rsync -a  ${scratch}/${o}/  ./${o}/
cp    ${scratch}/${o}.out  .

# . The following files may not exist if this is not a QM/MM run
 #       cat   ${scratch}/qm.xyz   >> qm.xyz    2> /dev/null
 #       cp    ${scratch}/job*.inp  .           2> /dev/null
 #       cp    ${scratch}/job*.log  .           2> /dev/null
 #       cp    ${scratch}/mol.in*   .           2> /dev/null
 #       cp    ${scratch}/d.o*      .           2> /dev/null
        
# . Clean scratch space
rm -r ${scratch}/*
        
# . Check for a failed Molaris job
        # grep -q "NORMAL TERMINATION" `basename $f .inp`.out ; if ! [ $? -eq 0 ] ; then break ; fi
