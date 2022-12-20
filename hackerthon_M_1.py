import os

def sets():
    k1=int(input())
    k1=set(range(1,(k1+1)))          
    print(k1)
    k2=[]
    n=int(input())
    for i in range(1,(n+1)):
        if i%5==0: k2.append(i)
    k2=set(k2)
    print(k2)
    k1.add(15)
    print(k1)
    for i in range(950,975): k2.add(i)
    print(k2)
    k1.discard(1000)
    print(k1)
    print(k1.union(k2))
    print(k1.intersection(k2))
    print(k1.difference(k2))
    print(k2.difference(k1))
    print(k1.symmetric_difference(k2))

def dictionary():
    d = {}
    for i in range(0,3):
        k,v=input().split()
        d[k]=v
    print(d)
    for key in d.keys(): print(key)
    for key in d.values(): print(key)
    d["D"]="8"
    d["E"]="15"
    print(d)
    d.popitem()
    print(d)
def loopsconds():
    s =input()
    count=0
    for i in s:
        if i not in "AEIOUaeiou":count+=1
    print(count)            
    q =[]
    for i in range(0,5):
        q.append(int(input()))
    average=sum(q)/len(q)
    if int(average) >=90:print('Great')
    elif int(average) in range(60,90):print('Above Average')
    elif int(average) in range(40,60):print('Average')
    else: print('Fail')
    string = input().split()
    print (" ".join(reversed(string)))
sets()
dictionary()
loopsconds()

