import turtle
turtle.speed(25)

def star(t,size):
   for i in range(5):
    t.forward(size)
    t.right(144)


def starSpiral():
    size=1
    for i in range(60):
        star(turtle,size)
        size=size + 5
#       turtle.forward(10)
        turtle.right(5)


starSpiral()
turtle.penup()
turtle.forward(280)
turtle.pendown()

starSpiral()
turtle.penup()
turtle.backward(200)
turtle.pendown()

starSpiral()
turtle.forward(100)

turtle.exitonclick()
