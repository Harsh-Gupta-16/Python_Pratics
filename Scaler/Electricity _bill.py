consume = int(input("Enter the consumption unit: "))
if consume>=1 and consume <=100:
    print('Total bill is zero')
if consume > 100 and consume <= 200:
    sum=(100)*5
    print(f'The total bill has to pay is {sum}')
if consume > 200 and consume <= 300:
    sum=(100)*5 + (consume-200)*10
    print(f'The total bill has to pay is {sum}')
if consume>300:
    sum=(100)*5 + (100)*10 + (consume-300)*12
    print(f'The total bill has to pay is {sum}')