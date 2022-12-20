A = []
print("Enter count of values you are given to insert:")
N = int(input())
print(f'Enter {N} numbers:')
for i in range(0,N):
        V = int(input())
        A.append(V)
if N < 4 or N > 100000:
    print("Invalid Input")
else:
    A.sort()
    sub = A[0]*A[1]*A[2]*A[3]
    add = A[N-1]*A[N-2]*A[N-3]*A[N-4]
    if sub > add: print(float(sub))
    else: print(float(add))