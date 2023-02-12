import random


n = int(input())
list1 = [random.randint(1,5)  for i in range(n)]    
print(list1)
max = max(list1)
min = min(list1)
for i in range(len(list1)):
    if list1[i] == max:
        list1[i]= min
print(list1)        