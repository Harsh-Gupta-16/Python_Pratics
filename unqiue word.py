R=[]
ch=0
u=0
abc=input('Enter the String Input ')
for i in abc:
    if i not in R:
        R.append(i)
        u+=1
    ch+=1
print('Unique Word ',u)
print('Character ',ch)