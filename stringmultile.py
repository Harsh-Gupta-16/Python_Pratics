a=int(input('Enter the Number: '))
multi=1
while a>0:
    n=a%10
    multi=multi*n
    a=a//10
print(multi)
