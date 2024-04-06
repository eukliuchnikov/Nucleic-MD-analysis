import MDAnalysis as mda
from MDAnalysis.analysis import distances

import numpy as np
import matplotlib.pyplot as plt
#matplotlib inline

#import mdtraj as md

cutoff = 7.5

# annotate
pwd = ''
u=mda.Universe(pwd+'0.pdb', pwd+'nucleic.dcd')

#print('PMO has {} residues and PEP has {} residues'.format(n_PMO, n_PEP))

with open("contacts75.dat", "w") as h:
    for ts in u.trajectory:
        PMO = u.select_atoms('name C5 and resid 2-26')
        PEP = u.select_atoms('name CZ and resid 27-33')

        PMO_com = PMO.center_of_mass(compound='residues')
        PEP_com = PEP.center_of_mass(compound='residues')

        n_PMO = len(PMO_com)
        n_PEP = len(PEP_com)

        res_dist = distances.distance_array(PMO.positions, PEP.positions, box=u.dimensions)
        #print(res_dist)
        for row in res_dist:
            contacts = 0
            for col in row:
                #print(col)
                if (float(col) < cutoff):
                    contacts = contacts + 1
            h.write(str(contacts) + "\t")
        h.write("\n") 




   
