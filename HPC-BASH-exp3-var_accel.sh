#! /bin/bash
#Runtime Testing
sbatch HPC-SBATCH-var_accel-apx.sh
sbatch HPC-SBATCH-var_accel-exact.sh
sbatch HPC-SBATCH-var_accel-kavr_24-p05.sh
sbatch HPC-SBATCH-var_accel-kavr_24-p06.sh
sbatch HPC-SBATCH-var_accel-kavr_24-p07.sh
sbatch HPC-SBATCH-var_accel-kavr_24-p08.sh
sbatch HPC-SBATCH-var_accel-kavr_24-p09.sh
sbatch HPC-SBATCH-var_accel-kavr_24-p10.sh
sbatch HPC-SBATCH-var_accel-kavr_24-p11.sh
sbatch HPC-SBATCH-var_accel-kavr_24-p12.sh
#Memory Tracing
sbatch HPC-SBATCH-var_accel-apx-mem.sh
sbatch HPC-SBATCH-var_accel-exact-mem.sh
sbatch HPC-SBATCH-var_accel-kavr_24-p05-mem.sh
sbatch HPC-SBATCH-var_accel-kavr_24-p06-mem.sh
sbatch HPC-SBATCH-var_accel-kavr_24-p07-mem.sh
sbatch HPC-SBATCH-var_accel-kavr_24-p08-mem.sh
sbatch HPC-SBATCH-var_accel-kavr_24-p09-mem.sh
sbatch HPC-SBATCH-var_accel-kavr_24-p10-mem.sh
sbatch HPC-SBATCH-var_accel-kavr_24-p11-mem.sh
sbatch HPC-SBATCH-var_accel-kavr_24-p12-mem.sh