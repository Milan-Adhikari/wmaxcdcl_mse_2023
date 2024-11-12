#!/bin/bash -l
# module load gurobi/702                 # not necessary if loaded in ~/.profile
# module load python/3.7-anaconda
BEGIN=$(date '+%s%2N' )
echo $SLURM_JOB_ID                         # print info about job id
cat /proc/cpuinfo                      # print details about CPUs
cat /proc/meminfo                      # print details about memory
free -h                                # print short info about memory
lsb_release -a                         # print info about OS version
cd  ${SLURM_SUBMIT_DIR}
python3 main.py
END=$(date '+%s%2N' )
DURATION=`expr $END - $BEGIN`
RESULT=$(awk "BEGIN {printf \"%.2f\",${DURATION}/100}")
echo The HPC node was busy for $RESULT seconds