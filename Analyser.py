import re
import numpy as np

txtPath = "English-w2v-skip-10-11.txt"
readnumber = 27972 #Number until the reader reads entries out of the file. Set in place to prevent decoding errors.
processnumber = 100 #Number of entries compared with each other. To prevent performance problems.

def verteilung(wlist, vlist):
    wvertlist = [] # wörterverteilungsliste
    vvertlist = [] # vectorverteilungsliste
    for x in range(len(wlist)):
        for y in range(len(wlist)):
            wvertlist.append(wlist[x] + " + " + wlist[y])
            vvertlist.append(np.linalg.norm(vlist[x]-vlist[y]))
    resultlist = [wvertlist, vvertlist]
    return resultlist

wordlist = []
vectorlist = []
with open(txtPath, "r", encoding="latin-1") as f:
    filelines = f.read().splitlines(True)
    for line in filelines[2:readnumber]:
        words = line.split()
        if words:
            wordlist.append(words[0])
            vectorlist.append(np.array([float(i) for i in words[1:]]))
vert = verteilung(wordlist[0:processnumber], vectorlist[0:processnumber])
for x in range(len(vert[0])):
    print(vert[0][x] + ": " + str(vert[1][x]))