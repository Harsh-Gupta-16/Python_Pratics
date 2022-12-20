import os

# Python Program to Calculate Profit or Loss
def prof_loss(): 
    actual_cost = int(input())
    sale_amount = int(input())
    if sale_amount > actual_cost:
        print(f'Total Profit = {float(sale_amount-actual_cost)}' )
    elif sale_amount < actual_cost:
        print(f'Total Loss = {float(actual_cost-sale_amount)}')
    else:
        print("No Profit No Loss!!!")

    
    
    

from math import degrees,radians
def deg_rad():
    lst=[]
    lst1=[]
    for ele in range(0,5):
        ele=int(input())
        lst.append(round(degrees(ele),2))
        lst1.append(round(radians(ele),2))
    print(lst)
    print(lst1)
def strings():
    txt = input()
    print(txt.swapcase())
    print(txt.title())
    print(txt.isalnum())
    print(txt.zfill(50))
prof_loss()
deg_rad()
strings()