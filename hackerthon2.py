import os

def stringops():
    a=input()
    print(a[3:5])
    print(a[-6:-3])
    print(len(a))
    print(a.replace(" ",""))
    print(a.replace(a[5],"p"))
    print(a.lower())

def stringopss():
    a=input()
    print(a.count(a[4]))
    print(a.encode())
    print(a.isalnum())
    print(a.find('l',2,5))
    print(a.find('W'))
    
    
    
    
    
def listup():
    lst = []
    for ele in range(0,5):
        ele=int(input())
        lst.append(ele)
    print([lst[i] for i in range(len(lst)) if i%2!=0])
    print([lst[i] for i in range(len(lst)) if i%2!=1])
    tup=tuple(lst)
    print(len(tup))
    tup=list(tup)
    tup[1]=5
    print(tuple(tup))

    
    
    

stringops()
stringopss()
listup()