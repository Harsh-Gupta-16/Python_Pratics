import math
n1=int(input("enter first number"))
n2=int(input("enter second number"))
i=1
while(i<=n1 and i<=n2):
    if((n1%i==0) and (n2%i==0)):
        gcd=i
    i=i+1
print("gcd of twno numbers",gcd)
print('GCD of two nunbers',math.gcd(n1,n2))