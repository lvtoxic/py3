from random import randint

# a=[randint(0,20) for _ in range(30)]
# print (a)

umber=[11, 0, 16, 5, 19, 13, 12, 4, 13, 14, 10, 1, 15, 14, 15, 0, 5, 4, 9, 4, 14, 12, 8, 12, 18, 17, 5, 5, 2, 3]
d=dict.fromkeys(umber,0)

for i in umber:
    d[i]+=1
print (sorted(((v,k) for k,v in d.items()),reverse=True)[::3])


import heapq
print (heapq.nlargest(3,((v,k)for k,v in d.items())))

from collections import Counter

print (Counter(umber))

print (Counter(umber).most_common(3))



