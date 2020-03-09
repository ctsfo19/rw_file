from array import *
import random

genF = open("1000_liczb.txt","w")
sortF = open("sort.txt","w")

nums = [0]*1000
sort = [0]*1000000

for i in range(0,1000):
    a = random.randint(0,1000000)
    nums[i] = a
    sort[a] += 1
    genF.write(str(a) + "\n")
for i in range(0, 1000000):
    while sort[i] != 0:
        sortF.write(str(i)+"\n")
        sort[i] -=1
genF.close()
sortF.close()
