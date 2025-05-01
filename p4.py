# Section 1 - Helper functions
import turtle, time, random
def set_background(image_filename):
    screen = turtle.Screen()
    try:
        screen.bgpic(f"/workspaces/Computational-Thinking-8/Backgrounds/{image_filename}.png")
    except:
        screen.bgpic(f"/workspaces/Computational-Thinking-8/Backgrounds/{image_filename}.gif")
def create_sprite(image_filename, x=0, y=0):
    image_file = f"/workspaces/Computational-Thinking-8/Images/{image_filename}.gif"
    screen = turtle.Screen()
    screen.register_shape(image_file)
    sprite = turtle.Turtle()
    sprite.shape(image_file)
    sprite.penup()
    sprite.goto(x,y)
    return sprite


# Section 2 - Variables
# TODO - add starting values for all the variables
x1 = (-200)
y1 = (-100)
x2 = (-200)
y2 = (0)
x3 = (-200)
y3 = (75)
x4 = (-200)
y4 = (150)


# Section 3 - Setup
# TODO - use your own background, and set your four turtles to images of your choice
set_background("barn")
t1 = create_sprite("bench",x1,y1)
t2 = create_sprite("basketball",x2,y2)
t3 = create_sprite("baseball",x3,y3)
t4 = create_sprite("bike",x4,y4)






# Section 4 - Racing
# TODO - set how much each variable changes by and increase the number of repeats to at least 30
# TODO - explain here which sprites are faster or slower
# bike will always win because it has the highest lowest posible speed which will make it always win because it is higher then all the others
for i in range(390):
    x1 += random.randint (0,100)
    x2 += random.randint (0,75)
    x3 += random.randint (45,85)
    x4 += random.randint (100,200)
    t1.goto(x1, y1)
    t2.goto(x2, y2)
    t3.goto(x3, y3)
    t4.goto(x4, y4)
    time.sleep(0.1)


# Section 5 - Winner
# TODO - complete the elif for player 2 winning
# TODO - write another elif for player 3 and player 4
if x1 >= x2 and x1 >= x3 and x1 >= x4:
    print("player 1 wins!")
elif x2 >= x1 and x2 >= x3 and x2 >= x4:
    print("player 2 wins!")
elif x3 >= x1 and x3 >= x2 and x3 >= x4:
    print("player 3 wins!")
else:
    print("player 4 wins!")

turtle.exitonclick()
