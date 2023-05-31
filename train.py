"""
train.py

DLAV, Groupe 64, Project 27: Multi-task

This scripts allows to launch a training on the three datasets using DWA

"""

import subprocess

#Command to modify
command = "openpifpaf.train --dataset=cocokp-animal-apollo --basenet=shufflenetv2k30\
      --apollo-square-edge=513 --lr=0.0002 --momentum=0.9  --b-scale=5.0 --epochs=500\
          --lr-decay 160 260 --lr-decay-epochs=10  --weight-decay=1e-5 --val-interval 1\
              --loader-workers 1 --apollo-upsample 2 --apollo-bmin=2 --batch-size=10 --clip-grad-value=10.0\
                  --animal-square-edge=513 --animal-extended-scale --animal-orientation-invariant=0.1\
                      --animal-upsample=2 --animal-bmin=2 --cocokp-square-edge=513 --cocokp-extended-scale\
                          --cocokp-orientation-invariant=0.1 --cocokp-upsample=2"

#split the command into arguments
args = command.split()

#Run the command
subprocess.run(args, check=True)