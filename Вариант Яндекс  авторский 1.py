'''
from turtle import *
left(90)
k=20
fd(9*k)
rt(90)
for i in range(0,2):


    fd(3*k)
    rt(90)
    fd(3*k)
    rt(270)
for i in range(0,2):
    fd(3*k)
    rt(90)
fd(9*k)
up()
for x in range(0,10):
    for y in range(0,10):
        goto(x*k,y*k)
        dot(3)
           
from itertools import *
a=0
for x in product('декнся', repeat=6):
    s=''.join(x)
    a+=1
    if s=='яндекс':
        print(s)
        print(a)
        break
        
s = open('9.csv').readlines()
b=[x.split(',') for x in s]
a=[]
for x in range(len(b)):
    c=[]
    for y in range(3):
        c.append(int(b[x][y]))
    a.append(c)
c=0
for x in range(len(a)):
    if len(set(a[x]))==len(a[x]):
        if sum(a[x])%3==0:
            c+=1
print(c)

a='7'*200
while '7777' in a or '33333' in a:
    if '7777' in a:
        a=a.replace('7777','33',1)
    if '33333' in a:
        a=a.replace('33333','777',1)
print(a.count('3'))

s = open('17 (2).txt').readlines()
a=[int(x) for x in s]
b=[int(x) for x in s]
b.sort(reverse=True)
for i in b:
    if i<1000:
        c=i
        break
v=0
n=0
for i in range(len(a)-1):
    if (len(str(a[i]))==3 and len(str(a[i+1]))!=3) or (len(str(a[i]))!=3 and len(str(a[i+1]))==3):
        if a[i]+a[i+1]>=c:
            v+=1
            n=max(n,a[i]+a[i+1])
print(v,n)

for n in range(1,100):
    a=bin(n)[2:]
    if a.count('1')%2==0:
        a='11'+a
    else:
        a=a+'00'
    r=int(a,2)
    if r>116:
        print(n)
        break

x = 3*15**1140+2*15**1025+15**923-3*15**86+2*15**74+3
b=[]
while x>0:
    b.append(x%15)
    x=x//15
b.sort(reverse=True)
c=0
for i in range(len(b)):
    a=0
    while b[i]==b[i+a] and a+i+1<len(b):
        a+=1
        c=max(c,a)
print(c)

def f(n):
    if n==1: return 1
    if n>1 and n%3: return f(n-1)+f(n-3)
    else: return f(n-2)+3*n
print(f(65))

def f(n):
    if n<2: return 0
    if n==2: return 1
    else:return f(n-2)+f(n//2)
print(f(31))

s=open('24.txt').readline()
s=s.split('AB')
print(len(max(s,key=len))+2)

s=open('26.txt').readlines()
t=int(s[0])
n=s[1]
s=[int(x) for x in s]
s.pop(0)
s.pop(0)
s.sort()
c=0
x=0
v=0
z=0
for i in range(len(s)):
    c+=int(s[i])
    z+=sum(s[0:i])
    x+=1
    if c<t:
        v=int(s[i])
    if c==t:
        print(x,z)
        break
    if c>t:
        print(x-1,z)
        break

s=open('27B.txt').readlines()
s.pop(0)
s=[int(x) for x in s]
a=s
a.sort(reverse=True)
for i in range(len(s)):
    c=s[i]
    for x in range(len(a)):
        c*=a[x]
        if c%21==0:
            print(c)
            z=1
            break
        else:
            c//=a[x]
    if z==1:
        break
 '''
x = 3*15**1140+2*15**1025+15**923-3*15**86+2*15**74+3
b=[]
while x>0:
    b.append(x%15)
    x=x//15
b.sort(reverse=True)
c=1
z=0
for i in range(len(b)-1):
    if b[i]==b[i+1]:
        c+=1
    else:
        c+=1
        z=max(z,c)
        c=0
print(z)
print(b.count(14))
print(b)






                
