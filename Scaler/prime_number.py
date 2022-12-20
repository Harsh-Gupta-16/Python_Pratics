number=int(input("Enter the number for check prime or not "))
i=2
count = 0
while(i<=number//2):
    if(number%i==0):
        count = count + 1
        break
    i=i+1

if (count==0 and number!=1):
    print('{} is a prime number'.format(number) )
else:
    print(f'{number} is not a prime number')    
