import csv
import operator
import itertools

with open('numbers.csv',newline ='') as file:
    reader = csv.reader(file, quoting=csv.QUOTE_NONNUMERIC)
    list=[]
    for row in reader:
        for i in row:
            list.append(int(i))
flag =0
count =0
n = len(list)
list2 = []
index = []
for i in range(n):
    list2.append(list[i])
    list2.sort()

if (all(i < j for i, j in zip(list, list[1:]))):
   print("Given numbers are non-decreasing")
   flag = 1
else:
   for i in range(n):
        if list[i] != list2[i]:
            count = count +1
            index.append(list[i])
if count ==2:
    a = index[0]
    b = index[1]
    print ("given list can be made non decreasing by switching {} and {}".format(a,b))
if count != 2 and flag !=1:
    print ("Given list cannot be made non-decreasing by a single switch")
