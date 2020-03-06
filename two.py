import random
from array import *

n = int(input("Give even number of unique random numbers to be generated:"))
maxVal = int(input("Give maximum value of numbers to be generated:"))

dataFile = open("dane.txt","w")
pairFile = open("pary.txt","w")

pairTab = array('i',[0])

randTab = array('i',[])
for i in range(0,maxVal):
  randTab.append(0)

for j in range(1,n+1):
  randNum = random.randint(0,maxVal)
  if randTab[randNum] == 0:
    dataFile.write(str(randNum)+"\n")
    pairTab.append(randNum)
    randTab[randNum] += 1
  else:
    j -= 2

for k in range(1,n+1):
  randTab[k] = 0

for l in range(0, int(n/2)):
  rPair = random.randint(int(n/2), n)
  if randTab[rPair] == 0:
    pairFile.write(str(pairTab[l]) + " - " + str(pairTab[rPair]) + "\n")
    randTab[rPair] += 1
  else:
    l -= 2


dataFile.close()
pairFile.close()
