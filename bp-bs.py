import barnaba as bb
import MDAnalysis
import os
import shutil
import numpy as np

#import mdtraj as md


# annotate
pwd = ''
os.mkdir(pwd + 'frames')
#pdb = pwd + '28.pdb'
#topology=pwd + 'res_2-23.pdb'
#tt = md.load(topology,pwd + 'res_2-23.dcd')
U=MDAnalysis.Universe(pwd+'../all_renamed.pdb', pwd+'nucleic.dcd')
rna = U.select_atoms('all')

stride = 1

for ts in U.trajectory[::stride]:
    with MDAnalysis.Writer(pwd + 'frames/frame_' + str(ts.frame) + ".pdb", rna.n_atoms) as W:
        W.write(rna)

total_bp = []
total_bs = []
Rgyr = []
e2e = []
new = []
for ts in U.trajectory[::stride]:
    print(ts)
    nterm = rna.select_atoms('resid 2 and name P')[0]
    cterm = rna.select_atoms('resid 26 and name P')[0]
    Rgyr.append((rna.radius_of_gyration()/10))
    e2e.append((np.linalg.norm(cterm.position - nterm.position)/10))
    print(ts.frame)
    #with MDAnalysis.Writer(pwd + "pdb.pdb", rna.n_atoms) as W:
     #   W.write(rna)
      #  print(len(rna.select_atoms('resid 22')))
    stackings, pairings, res = bb.annotate(pwd + 'frames/frame_' + str(ts.frame) + ".pdb")
        # list base pairings
    print("BASE-PAIRS", len(pairings[0][0]))
    for p in range(len(pairings[0][0])):
        res1 = res[pairings[0][0][p][0]]
        res2 = res[pairings[0][0][p][1]]
        interaction =  pairings[0][1][p]
        print("%10s %10s %4s" % (res1,res2,interaction))

        # list base-stackings
    print("STACKING",len(stackings[0][0]))
    for p in range(len(stackings[0][0])):
        res1 = res[stackings[0][0][p][0]]
        res2 = res[stackings[0][0][p][1]]
        interaction =  stackings[0][1][p]
        print("%10s %10s %4s" % (res1,res2,interaction))
    total_bp.append((len(pairings[0][0])))
    total_bs.append((len(stackings[0][0])))
    new_line =str(ts.frame) + '\t' + str(np.linalg.norm(cterm.position - nterm.position)/10) + '\t' + str(rna.radius_of_gyration()/10) + '\t' + str(len(pairings[0][0])) + '\t' + str(len(stackings[0][0])) + '\n'
    new.append(new_line)
#stackings, pairings, res = bb.annotate(tt)

#shutil.rmtree(pwd + 'frames')


#np.savetxt(pwd +'bp.dat', np.array(total_bp), delimiter='\t')
#np.savetxt(pwd +'bs.dat', np.array(total_bs), delimiter='\t')
file = open(pwd+"ts_X_Rg_bp_bs.dat",'w')
for i in range (len(new)):
    file.write(new[i])
file.close()
