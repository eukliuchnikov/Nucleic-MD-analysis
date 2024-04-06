import barnaba as bb
import MDAnalysis
import os
import shutil
import numpy as np

#import mdtraj as md


# annotate
pwd = ''
U=MDAnalysis.Universe(pwd+'0.pdb', pwd+'nucleic.dcd')
rna = U.select_atoms('resid 27')

total_bp = []
total_bs = []
Rgyr = []
e2e = []

for ts in U.trajectory:
    Rgyr.append((rna.radius_of_gyration()/10))
    print(ts.frame)

file = open(pwd+"Rg.dat",'w')
for i in range (len(Rgyr)):

    file.write(str(Rgyr[i]) + '\n')
file.close()
