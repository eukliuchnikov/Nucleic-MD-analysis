import MDAnalysis as mda
from MDAnalysis.analysis import distances

import numpy as np
import matplotlib.pyplot as plt
#matplotlib inline

#import mdtraj as md

# annotate
pwd = ''
u=mda.Universe(pwd+'0.pdb', pwd+'new+old.dcd')

#print('PMO has {} residues and PEP has {} residues'.format(n_PMO, n_PEP))

with open("distance.dat", "w") as h:
    for ts in u.trajectory:
        PMO = u.select_atoms('resid 2-26')
        PEP = u.select_atoms('resid 27-33')

        PMO_com = PMO.center_of_mass(compound='residues')
        PEP_com = PEP.center_of_mass(compound='residues')

        n_PMO = len(PMO_com)
        n_PEP = len(PEP_com)

        res_dist = distances.distance_array(PMO_com, PEP_com, box=u.dimensions)

        for row in res_dist:
            h.write(str(row.min()) + "\t")
        h.write("\n") 




   
