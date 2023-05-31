"""
inference.py

DLAV, Groupe 64, Project 27: Multi-task

This scripts allows to evaluate a model on the 3 datasets: AnimalPose, ApolloCar3D, Coco

"""

import subprocess

#checkpoint to modify

command = "python -m openpifpaf.eval --write-predictions --dataset=animal --animal-upsample=2 --animal-no-eval-annotation-filter\
      --batch-size 1 --loader-workers 1 --checkpoint=multi_from_45.epoch052 --decoder=cifcaf:0 --seed-threshold 0.01 --force-complete-pose"
args = command.split()
subprocess.run(args, check=True)

command = "python -m openpifpaf.eval --write-predictions --dataset=apollo --apollo-upsample=2 --apollo-bmin=2 --batch-size 1\
      --loader-workers 1 --checkpoint=multi_from_45.epoch052 --decoder=cifcaf:0 --seed-threshold 0.01 --force-complete-pose"
args = command.split()
subprocess.run(args, check=True)

command = "python -m openpifpaf.eval --write-predictions --dataset=cocokp --cocokp-orientation-invariant=0.1--cocokp-upsample=2\
      --batch-size 1 --loader-workers 1 --checkpoint=multi_from_45.epoch052 --decoder=cifcaf:0 --seed-threshold 0.01 --force-complete-pose"
args = command.split()
subprocess.run(args, check=True)