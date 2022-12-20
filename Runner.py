R=[]
while True:
    km=input()
    if km=='q' : break
    elif float(km)>=42.195 or float(km)<=0.0 : pass
    else: R.append(float(km))
R.sort(reverse=True)
if len(R)>3 :
    for i in range(0,3):
        print(R[i])
else :
    print(R)

