#!/bin/bash
# Job name
#SBATCH --job-name v_m-k-p06
# Submit to the primary QoS
#SBATCH -q primary
# Request one node
#SBATCH -N 1
# Total number of cores, in this example it will 1 node with 1 core each. 
#SBATCH -n 1
# Request memory
#SBATCH --mem=128G
# Mail when the job begins, ends, fails, requeues 
#SBATCH --mail-type=ALL
# Where to send email alerts
#SBATCH --mail-user=Wqs7sYxJKDby2QLPysfq@proton.me
# Create an output file that will be output_<jobid>.out 
#SBATCH -o output_%j.out
# Create an error file that will be error_<jobid>.out
#SBATCH -e errors_%j.err
# Set maximum time limit 
#SBATCH -t 1-0:0:0
# Set pref to MDT cluster
#SBATCH -w mdt[1-83]

python3 var_m-kavr_24-p06.py