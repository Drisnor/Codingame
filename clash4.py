#t=[i for i in input().split()]
t=["I", "hate", "My", "love"]
l=len(t)
m=l//2
if l%2==0:
    print(t[m-1]+t[m])
else:
    print(t[m])

"""
a=input().split()
l=len(a)
i=int(l/2)
if l%2==0:
    print(a[i-1],end='')
print(a[i])
"""
