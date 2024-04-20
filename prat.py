'''print("hello"+" "+"WORLD")
a=21
b=30
c=b
b=a
a=c
print(a)
print(b)
var='12'
print(int(var[0])+int(var[1]))
x='malayalam'
n=len(x)
w=''
i=0
for x[i] in x[n-1]:
    w=w+x[i]
    i<=n
print(w)
if(x==w):
    print('yes')
else:
    print('no')'''
'''def palindrome(word):
    word=word.lower()
    start=0
    end=len(word)-1
    while start<end:
        if word[start]!=word[end]:
            start+=1
            end-=1
            print('false')
        return True

word=input('enter a word to check:')
if palindrome(word):
    print('yes')
else:
    print('no')'''


l=[]
n=int(input("enter the no ofelements:"))
for i in range(n):
    x=int(input())
    l.append(x)
k=l[0]
for i in range(n-1):
    if l[i]>=k:
        k=l[i]
    print(k)
