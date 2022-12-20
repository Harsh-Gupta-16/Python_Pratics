from vpython import *
canvas(background=color.blue)
donut=ring(radius=0.45,Thickness=0.25,color=vector(400,100,1))
chocolate=ring(radius=0.50,Thickness=0.25,color=vector(0.4,0.2,1))
ran=0
while True:
    rate(10)
    donut.pos = vector(3*cos(ran),sin(ran),1)
    chocolate.pos = vector(3*cos(ran),sin(ran),1)
    ran = ran+0.03