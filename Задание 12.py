import turtle
turtle.shape('turtle')


turtle.left(90)

turtle.speed(50)



for d in range (1000):

    for i in range(180):
        turtle.forward(1)
        turtle.right(1)

    for i in range(180):
        turtle.forward(0.3)
        turtle.right(1)
