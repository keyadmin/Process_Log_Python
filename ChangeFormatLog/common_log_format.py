import os
#import sys
import fileinput # libr read stdin 
f2 = open("common.log","w+")
# for lps in sys.stdin: #can use this function instead
for lps in fileinput.input():
    arr = lps.split('"')
    arr.pop(6)
    arr.pop(5)
    arr.pop(4)
    arr.pop(3)
    joins=''.join(arr)
    print(joins)
    f2.write(joins) #create and write common.log
    f2.write("\n")
