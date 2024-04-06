from prody import *
from matplotlib.pylab import *
ion()

prot = parsePDB("rna_100ns.pdb")

calphas = prot.select('all')

def gammaDependent(dist2, i, j):
     """Return a force constant based on the given square distance."""
     ress = calphas.getResindices()
     print (ress[i], ress[j])
     print (i, j)
     if i <= 150:
         return 100
     elif i <= 166:
         return 1
     elif i <= 171:
         return 100
     elif i <= 389:
         return 1
     elif i <= 535:
         return 100
     elif i <= 551:
         return 1
     elif i <= 556:
         return 100    
     else:
         return 1

anm = ANM('hAGO2 ANM analysis')
anm.buildHessian(calphas, cutoff = 15, gamma = 1)
anm.calcModes()
writeNMD('AD-69259_100ns.nmd', anm[:10], calphas)
