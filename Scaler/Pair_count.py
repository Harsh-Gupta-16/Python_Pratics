ls = [1,2,3,4]
b=7
count=0
for i in range(0,len(ls)-1):
    for j in range(i+1,len(ls)):
        if ls[i]+ls[j]==b:
            count+=1
print(count)