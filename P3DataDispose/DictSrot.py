from random import randint

# print ({k: randint(60,100) for k in 'abcdefghj'})


d={'a': 74, 'b': 93, 'c': 80, 'd': 93, 'e': 82, 'f': 66, 'g': 77, 'h': 97, 'j': 94}
# l=[(v,k) for k,v in d.items()]
# print (sorted(l,reverse=True))


print (sorted(d.items(),key=lambda items:items[1],reverse=True))

for i,(k,v)in enumerate(d,1):
    print (i,k,v)