file_decomp = open("/home/farkhad/RNA/seq_from_ALNYLAM/AD-69156/md/2/MMPBSA/FINAL_DECOMP_MMPBSA.dat","r")
decomp = file_decomp.readlines()
receptor = []
receptor_std = []
ligand = []
ligand_std = []
for i in range (8,27):
    en = decomp[i].split(",")[17]
    std = decomp[i].split(",")[18]
    receptor.append(en)
    receptor_std.append(std)

for i in range (47,28,-1):
    en = decomp[i].split(",")[17]
    std = decomp[i].split(",")[18]
    ligand.append(en)
    ligand_std.append(std)

rec_file = open("/home/farkhad/RNA/seq_from_ALNYLAM/AD-69156/md/2/MMPBSA/receptor.dat",'w')
#lig_file = open("ligand.dat",'w')
for i in range (len(receptor)):
    #print(str(receptor[i]))
    rec_file.write(str(receptor[i])+'\t'+str(receptor_std[i])+'\n')

rec_file.close()
lig_file = open("/home/farkhad/RNA/seq_from_ALNYLAM/AD-69156/md/2/MMPBSA/ligand.dat",'w')
for j in range (len(ligand)):
    #print(str(ligand[j]))
    lig_file.write(str(ligand[j])+'\t'+str(ligand_std[j])+'\n')
lig_file.close()




