# turtle joins
import turtle

# back round color
turtle.Screen().bgcolor("blue")



t = turtle.Turtle()
# move to starting spot
t.goto(0, - 0)
t.color("red")

t.speed(0)

colors = ["red","yellow","orange"]
for i in range(10000):
    t.color( colors[ i % 3] )
    t.forward(1 + i)
    t.left(500)
   
turtle.exitonclick()