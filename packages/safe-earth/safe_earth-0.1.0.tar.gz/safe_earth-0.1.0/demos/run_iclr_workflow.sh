#!/bin/bash

#SBATCH --time=12:00:00
#SBATCH --mem=120G

# Specify a job name:
#SBATCH -J generate_iclr_metrics_indemosdirectory
#SBATCH -o %x-%j.out



# Set up the environment by loading modules
module load cuda cudnn
module --ignore_cache load "conda"

# Run a script
conda init bash
conda activate faireenvconda
python demos/iclr_workflow.py
