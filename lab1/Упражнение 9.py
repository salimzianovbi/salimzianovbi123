import  turtle
turtle.shape('turtle')
turtle.speed(10)

n=12
import numpy as np

R=30
for i in range(3, n+1):
    turtle.left(90+(180-(i - 2) * 180 / i)/2)

    for c in range(i):
        d = (i - 2) * 180 / i



        turtle.forward(2*R*np.sin(180/i*np.pi/180))
        turtle.left(180 - (i - 2) * 180 / i)


    turtle.right(180 - ((i - 2) * 180 / i)/2)





    turtle.penup()
    turtle.forward(50)
    turtle.pendown()
    R+=50






