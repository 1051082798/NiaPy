# encoding=utf8
# This is temporary fix to import module from parent folder
# It will be removed when package is published on PyPI
import sys
sys.path.append('../')
# End of fix

from NiaPy.algorithms.other import TabuSearch
from NiaPy.task import StoppingTask
from NiaPy.benchmarks import Sphere

# we will run Sine Cosine Algorithm algorithm for 5 independent runs
for i in range(5):
    task = StoppingTask(D=10, nFES=10000, benchmark=Sphere())
    algo = TabuSearch(NP=30, a=7, Rmin=0.1, Rmax=3)
    best = algo.run(task=task)
    print(best)

# vim: tabstop=3 noexpandtab shiftwidth=3 softtabstop=3
