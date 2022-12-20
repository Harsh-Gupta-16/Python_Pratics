A=[]
B=[]
C=[]
a=int(input("count of values you are going to insert "))
for i in range(0,a):
    B=int(input())
    A.append(B)
if a < 4:
    print('Invalid input')
else:
    # n=a-1;
    # while n>=0:
    #     max=A[n]*A[n-1]*A[n-2]*A[n-3]
    #     C.append(max)
    #     n=n-1
    # C.sort(reverse=True)
    # print(C[0])
    A.sort(reverse=True)
    sub=A[a-1]*A[a-2]*A[a-3]*A[a-4]
    add=A[0]*A[1]*A[2]*A[3]
    if (sub > add) : print(sub)
    else: print(add)