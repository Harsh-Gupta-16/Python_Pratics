# Consider the below series:
# 1, 2, 1, 3, 2, 5, 3, 7, 5, 11, 8, 13, 13, 17, ...
# This series is a mixture of 2 series - all the odd terms in this series form a Fibonacci series and all the even terms are the prime numbers in ascending order.
# Write a program to find the Nth term in this series.
# The value N is a Positive integer that should be read from STDIN. The Nth term that is calculated by the program should be written to STDOUT. Other than the value of Nth term, no other characters/strings or message should be written to STDOUT.
# For example, when N = 14, the 14th term in the series is 17. So only the value 17 should be printed to STDOUT.
first=0
second=1
temp=0
counter=1
N=int(input('Enter the Value: '))
if(N%2==1):
    N=(N//2)+1
    while counter<N:
        temp=first+second
        first=second
        second=temp
        counter +=1 
    print(temp)
else:
    N=N//2
    if(N > 1):
        for i in range(2,N):
            if (N%i==0):
                break
            else:
                print(N)
                break