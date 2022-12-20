# for i in range(1900,2050):
#     if(((i%4==0) and (i % 100!=0)) or (i%400==0)):
#         print(i,end=' ')

i=int(input('Enter the number'))
if(((i%4==0) and (i % 100!=0)) or (i%400==0)):
    print('This is leap year')
else:
    print('not a leap yeaar')