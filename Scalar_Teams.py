def solve(str,n):
    countz=0
    count1=0
    cnt=0
    for i in range(n):
        if str[i]=='0':
            countz+=1
        else:
            count1+=1
        if countz == count1:
            cnt+=1
    
    if cnt == 0:
        return -1
    else:
        return cnt

A='00011011'
n=len(A)
print(solve(A,n))