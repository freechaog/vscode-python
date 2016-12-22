




str1 = input("input a num:")
l1 = str1.strip().split()
l2 = list(set(l1))

dict1={}
for i in l2:
    dict1[i] = l1.count(i)
print(dict1)
