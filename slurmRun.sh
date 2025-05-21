#!/bin/bash

# Set max time to your time estimation for your program be as precise as possible
# for optimal cluster utilization
#SBATCH --time=02:00:00

#
# There are a lot of ways to specify hardware ressources we recommend this one
#

# Set ntasks to 1 except when you are trying to run 2 tasks that are exactly the same
# although in some cases like simulations with random events this may be desirable
#SBATCH --ntasks=1  # number of processor cores (i.e. tasks)

# Now set your cpu and memory requirements and onve again be as precise as possible
# keep in mind if your pregram exceeds the requested memory it will be terminated prematurely
# the configuration below will result in a job allocation of 2 cores and 40 MB of RAM
#SBATCH --cpus-per-task=1
#SBATCH --mem-per-cpu=30G
#SBATCH --array=1-13167


# If you so choose Slurm will notify you when certain events happen for your job
# for a full list of possible options look furhter down
#SBATCH --mail-type END

# Feel free to give your job a good name to better identify it later
# the same name expansions as for the ourput and error path apply here as well
# see below for additional information
#SBATCH --job-name="GMDNEMDNMAP1"

# Always try to use absolute paths for your output and error files
# IF you only specify an output file all error messages will automaticly be redirected in there
# You can utilize name expansion to make sure each job has a uniq output file if the file already exists 
# Slurm will delete all the content that was there before before writing to this file so beware.
#SBATCH --output=~/MAP/test.out
#SBATCH --error=~/MAP/test.err
#SBATCH --partition=short

#
# Prepare your environment
#

# causes jobs to fail if one command fails - makes failed jobs easier to find with tools like sacct
set -e

# load modules
module load python/3.7.12
cd ~/FP/GMDNtoEMDN-main/
source ../.venv/bin/activate
export PATH="$HOME/.rustup/toolchains/stable-x86_64-unknown-linux-gnu/bin:$PATH"

# Set variables you need
export OMP_NUM_THREADS=$SLURM_CPUS_PER_TASK

declare -i tasknumb=$(($SLURM_ARRAY_TASK_ID))
srun python3 Main.py $(($tasknumb*3)) 1
#srun python3 Main.py $(($tasknumb*3)) 2 #ADD these if u want to run more than the first classifier
#srun python3 Main.py $(($tasknumb*3)) 3
#srun python3 Main.py $(($tasknumb*3)) 4
#srun python3 Main.py $(($tasknumb*3)) 5

# exit gracefully
exit 0
