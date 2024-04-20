l=[]
n=int(input("enter the no ofelements:"))
for i in range(n):
    x=int(input())
    l.append(x)
k=l[0]
for i in range(n-1):
    if l[i]>=k:
        k=l[i]
    return k