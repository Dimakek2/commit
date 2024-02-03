from ipaddress import*
#12922
'''

for x in ip_network('136.36.240.16/255.255.255.248'):
    if '101' not in bin(int(x))[2:].zfill(32):
        print(x)
'''
#12245
'''
b=0
for x in ip_network('192.168.32.48/255.255.255.240'):
    a = bin(int(x))[2:]
    if a.count('1')%2==0:
        b+=1
        print(b)
'''
#5
'''
def per(x):
    nn=''
    while x:
        nn += str(x%3)
        x//=3
    return nn[::-1]
b=[]
for i in range(10,100):
    a = per(i)
    if i%4==0:
        a = a+a[-3:]        
    if i%4!=0:
        a= a+per(i%4*4)
    r = int(a,3)
    if r<127:
        b.append(r)

print(max(b),b)
'''
#6
'''
from turtle import *
for i in range(0,15*3):
    fd(150)
    rt(24)
'''
#8
'''
from itertools import*
b=[]
for x in product('014689acefg',repeat =6):
    s=''.join(x)
    if len(set(s))==len(s) and s[0] in 'acef468':
        b.append(s)
print(len(b))
'''
#9
s = open('9_10121.csv').readlines()
a = [i.split(',') for i in s]
b=[]
for i in range(len(a)):
    c=[]
    for j in range(0,6):
        c.append(int(a[i][j]))
    b.append(c)
a=0
for i in range(len(b)):
    if len(set(b[i]))!=len(b[i]):
        s =sum(b[i])
        p = 0
        l = 0
        for j in range(0,len(b[i])):
            
            if b[i].count(b[i][j])>1:
                p += b[i][j]
                l += 1
        if s//6>p//l:
            a+=i+1
print(a)










#23
'''
def f(n,stop):
    if n==81: return 0
    if n==stop: return 1
    if n>stop: return 0
    if n<stop:
        return f(n+3,stop)+f(2*n-1,stop)+f(n+int(str(n)[0]),stop)
print(f(42,73)*f(73,89))
'''
