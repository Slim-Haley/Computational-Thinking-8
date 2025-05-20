# Section 1 - Helper functions (DON'T CHANGE!!)
import turtle, math, time, random
def set_background(image_filename):
	screen = turtle.Screen()
	try:
		screen.bgpic(f"/workspaces/Computational-Thinking-8/Backgrounds/{image_filename}.png")
	except:
		screen.bgpic(f"/workspaces/Computational-Thinking-8/Backgrounds/{image_filename}.gif")
def set_image(sprite, image_filename):
	image_file = f"/workspaces/Computational-Thinking-8/Images/{image_filename}.gif"
	screen = turtle.Screen()
	screen.register_shape(image_file)
	sprite.shape(image_file)
def create_sprite(image_filename, x=0, y=0):
	sprite = turtle.Turtle()
	set_image(sprite, image_filename)
	sprite.penup()
	sprite.goto(x,y)
	return sprite
def get_distance(s1, s2):
	dx = s1.xcor() - s2.xcor()
	dy = s1.ycor() - s2.ycor()
	return math.sqrt(dx*dx + dy*dy)
window = turtle.Screen()
window.tracer(0)

# Section 2: Setup
# TODO - create your player character
s1 = create_sprite("baseball",0,0)
s2 = create_sprite("cat2",300,10)
s3 = create_sprite("can",-300,10)
s4 = create_sprite("bike",-300,10)
s5 = create_sprite("character1",300,10)
s6 = create_sprite("basketball",-300,10)
s7 = create_sprite("bat",300,10)

# TODO - set your background
set_background("summer")
# TODO - set the starting value for your variable
get_distance(s1,s2)

# Section 3: Controls
# TODO - define your controls
def move_up():
	s1.setheading(90)
	s1.forward(10)
   	 
def move_down():
	s1.setheading(270)
	s1.forward(10)
    
def move_left():
	s1.setheading(180)
	s1.forward(10)
    
def move_right():    
	s1.setheading(0)
	s1.forward(10)



# TODO - pick keys for each control
window.onkeypress(move_up, "w")
window.onkeypress(move_down, "s")

window.onkeypress (move_left, "a")
window.onkeypress (move_right, "d")


# Section 4: Game Loop
window.listen()
timer = 0
s4.hideturtle()
s5.hideturtle()
s6.hideturtle()
s7.hideturtle()




while True:
	time.sleep(0.1)
	timer += 1  
	 
    
 	# # TODO - code for automatic actions

	
	
	if get_distance(s1,s2) < 50:
		set_background("cornfield")
		s4.showturtle()
		s5.showturtle()

	if get_distance(s1,s2) < 50:
		set_background("cornfield")
		s3.hideturtle()
		s2.hideturtle()
		s2.goto(1000,1000)
		s3.goto(1000,1000)

	if get_distance(s1,s3) < 50:
		set_background("flowers")
		s3.hideturtle()
		s2.hideturtle()
		s2.goto(1000,1000)
		s1.goto(0,0)
		


	if get_distance(s1,s3) < 50:
		set_background("flowers")
		s6.showturtle()
		s7.showturtle()
		s6.goto(-300,10)
		s7.goto(300,10)
		s3.goto(1000,1000)

	if get_distance(s1,s7) < 50:
		s1.goto(0,0)
		s1.write("1 room away",font = ("Arial", 30, "normal"))
		set_background("fall")
		s6.hideturtle()
		s7.hideturtle()
		

	if get_distance(s1,s4) < 50:
		set_background("underwater")
		s1.write("you win",font = ("Arial", 75, "normal"))
		s6.hideturtle()
		s7.hideturtle()
		s4.goto(1000,1000)
		s5.goto(123456789,123456789)


	


	if get_distance(s1,s3) < 50:
		set_background("flowers")

	#s1.clear()
	#s1.write(f"{rooms_away}")
	window.update()

	#if :get_distance(s1,s7):
	#break
	

print("you win")
