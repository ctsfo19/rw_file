import random
from array import *

n = int(input())
dataFile = open("dane.txt","w")
countFile = open("ile.txt","w")
#randTab = array('i',[0])
#for i in range(0,10):
#  randTab.append(0)
countTab = array('i', [0])
for i in range(0,n):
  countTab.append(0)

for i in range(0,n):
  randNum = random.randint(1,10)
#  if randTab[randNum] == 0:
  dataFile.write(str(randNum)+"\n")
#  randTab[randNum] += 1
  countTab[randNum] += 1
for i in range(1,11):
  countFile.write(str(i) + ":" + str(countTab[i]) + "\n")
dataFile.close()
countFile.close()
