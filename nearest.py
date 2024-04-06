import math

aauu = 0
auua = 0
uaau = 0
cagu = 0
cuga = 0
gacu = 0
guca = 0
cggc = 0
gccg = 0
ggcc = 0
overH = 0
init = 3.4
symm = 0.4

with open("156.dat", "r") as f:
    flines = f.readlines()

if (flines[1][2] == "A"):
    overH = overH -0.6
if (flines[1][2] == "C"):
    overH = overH -1.2
if (flines[1][2] == "G"):
    overH = overH -0.6
if (flines[1][2] == "U"):
    overH = overH -0.1

if (flines[0][20] == "A"):
    overH = overH -0.6
if (flines[0][20] == "C"):
    overH = overH -1.2
if (flines[0][20] == "G"):
    overH = overH -0.6
if (flines[0][20] == "U"):
    overH = overH -0.1

for i in range(2,20):
    if ((flines[0][i] == "A" and flines[0][i + 1] == "A" and flines[1][i] == "U" and flines[1][i+1] == "U") or (flines[0][i] == "U" and flines[0][i + 1] == "U" and flines[1][i] == "A" and flines[1][i+1] == "A")):
        aauu += 1
    if ((flines[0][i] == "A" and flines[0][i + 1] == "U" and flines[1][i] == "U" and flines[1][i+1] == "A")):
        auua += 1
    if ((flines[0][i] == "U" and flines[0][i + 1] == "A" and flines[1][i] == "A" and flines[1][i+1] == "U")):
        uaau += 1
    if ((flines[0][i] == "C" and flines[0][i + 1] == "A" and flines[1][i] == "G" and flines[1][i+1] == "U") or (flines[0][i] == "U" and flines[0][i + 1] == "G" and flines[1][i] == "A" and flines[1][i+1] == "C")):
        cagu += 1
    if ((flines[0][i] == "C" and flines[0][i + 1] == "U" and flines[1][i] == "G" and flines[1][i+1] == "A") or (flines[0][i] == "A" and flines[0][i + 1] == "G" and flines[1][i] == "U" and flines[1][i+1] == "C")):
        cuga += 1
    if ((flines[0][i] == "G" and flines[0][i + 1] == "A" and flines[1][i] == "C" and flines[1][i+1] == "U") or (flines[0][i] == "U" and flines[0][i + 1] == "C" and flines[1][i] == "A" and flines[1][i+1] == "G")):
        gacu += 1
    if ((flines[0][i] == "G" and flines[0][i + 1] == "U" and flines[1][i] == "C" and flines[1][i+1] == "A") or (flines[0][i] == "A" and flines[0][i + 1] == "C" and flines[1][i] == "U" and flines[1][i+1] == "G")):
        guca += 1
    if ((flines[0][i] == "C" and flines[0][i + 1] == "G" and flines[1][i] == "G" and flines[1][i+1] == "C")):
        cggc += 1
    if ((flines[0][i] == "G" and flines[0][i + 1] == "C" and flines[1][i] == "C" and flines[1][i+1] == "G")):
        gccg += 1
    if ((flines[0][i] == "G" and flines[0][i + 1] == "G" and flines[1][i] == "C" and flines[1][i+1] == "C") or (flines[0][i] == "C" and flines[0][i + 1] == "C" and flines[1][i] == "G" and flines[1][i+1] == "G")):
        ggcc += 1
print("aauu, auua, uaau, cagu, cuga, gacu, guca, cggc, gccg, ggcc")
print(aauu, auua, uaau, cagu, cuga, gacu, guca, cggc, gccg, ggcc)
G = aauu*(-0.9) + auua*(-0.9) + uaau*(-1.1) + cagu*(-1.8) + cuga*(-1.7) + gacu*(-2.3) + guca*(-2.1) + cggc*(-2.0) + gccg*(-3.4) + ggcc*(-2.9) + overH + init + symm

H = aauu*(-6.6) + auua*(-5.7) + uaau*(-8.1) + cagu*(-10.5) + cuga*(-7.6) + gacu*(-13.3) + guca*(-10.2) + cggc*(-8.0) + gccg*(-14.2) + ggcc*(-12.2)

TS = H-G
print(G, H, TS)
