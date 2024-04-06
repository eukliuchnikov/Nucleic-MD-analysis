import os
import MDAnalysis
import time

#os.system("rm -r results/")
#os.system("rm -r dcds/")

pwd = ''
os.system("mkdir dcds")
U=MDAnalysis.Universe(pwd+'0.pdb', pwd+'nucleic.dcd')
rna = U.select_atoms('all')
for ts in U.trajectory[::1]:
    with MDAnalysis.Writer(pwd + 'dcds/frame' + str(ts.frame) + ".dcd", rna.n_atoms) as W:
        W.write(rna)


pwd = 'dcds/'
li=os.listdir(pwd)
for elem in li:
    name = elem.rsplit('.',1)[0]
    cm =  "~/Tools/amber20/bin/MMPBSA.py -O -i mmpbsa.in -cp rna.prmtop -y " + pwd + str(elem) + " -o FINAL_RESULTS_MMPBSA_" + str(name) + ".dat"
    #cmd = "echo '" + "~/Tools/amber20/bin/MMPBSA.py -O -i ../mmpbsa.in -cp ../rna.prmtop -y " + str(elem) + " -o FINAL_RESULTS_MMPBSA_" + str(name) + ".dat"'
  
    print(cm)
    os.system(cm)
    time.sleep(1)


os.system("mkdir results")
os.system("mv FINAL* results/")

li=os.listdir('results')
print(li)
enthalpies = []
for elem in li:
    name = elem.rsplit('.',1)[0].split('_')[3]
    with open('results/' + elem, 'r') as file:
        lines = file.readlines()
        file.close()
        for line in lines:
            if 'TOTAL' in line:
                new_line = name + '\t' + line.split()[1] + '\n'
                #if (float(line.split()[1]) < -1300.0):
                enthalpies.append(new_line)
                    	
pwd = ''
energy_file = open(pwd + "H.dat",'w')
for i in range (len(enthalpies)):
    energy_file.write(enthalpies[i])
energy_file.close()	


