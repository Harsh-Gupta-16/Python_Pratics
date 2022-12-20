n=int(input("enter the number you want to chek is prime or not"))
i=1
while(i<n):
    if(i%n==0):
        i=i+1
        print("not a prime number")
    else:
        print("prime number")
