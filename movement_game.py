# Section 1 - Helper functions (DON'T CHANGE!!)
import turtle, math, time, random
def set_background(image_filename):
	screen = turtle.Screen()
	try:
		screen.bgpic(f"/workspaces/Computational-Thinking-8/Backgrounds/{image_filename}.png")
	except:
		screen.bgpic(f"/workspaces/Computational-Thinking-8/Backgrounds/{image_filename}.gif")

def set_image(sprite, image_filename):
    image_file = f"./Images/{image_filename}.gif"
    screen = turtle.Screen()
    screen.register_shape(image_file)
    sprite.shape(image_file)

def create_sprite(image_filename, x=0, y=0):
    sprite = turtle.Turtle()
    set_image(sprite, image_filename)
    sprite.penup()
    sprite.goto(x,y)
    window.update()
    return sprite

def get_distance(s1, s2):
	dx = s1.xcor() - s2.xcor()
	dy = s1.ycor() - s2.ycor()
	return math.sqrt(dx*dx + dy*dy)

def draw_rectangle( color="black",x=0,y=0, width=100, height=100,):
	sprite = turtle.Turtle()
	sprite.speed(0)
	sprite.pencolor(color)
	sprite.color(color)
	sprite.penup()
	sprite.goto(x - (width*0.5), y + (height*0.5))
	sprite.pendown()
	sprite.begin_fill()
	for i in range(2):
		sprite.forward(width)
		sprite.right(90)
		sprite.forward(height)
		sprite.right(90)
	sprite.end_fill()
	sprite.hideturtle()


window = turtle.Screen()
window.tracer(0)


# Section 2: Setup
spongebob = create_sprite("Screenshot 2025-11-05 10.16.25 AM", 0, -200)
patrick = create_sprite("Screenshot 2025-11-05 10.31.19 AM", 0, 200)
set_background("Screenshot 2025-11-05 10.20.05 AM (1)")
if random.randint(1, 2) == 1:
    it ="spongebob"
else:
    it = "patrick"
text = create_sprite("alien",-200,200)
text.color("black")
text.write(f"{it} is it!",font = ("Times New Roman", 40, "normal"))
text.hideturtle()

# Section 3: Controls
def move_up():
    spongebob.setheading(90)
    spongebob.forward(10)
        
def move_down():
    spongebob.setheading(270)
    spongebob.forward(10)
    
def move_left():
    spongebob.setheading(180)
    spongebob.forward(10)
    
def move_right():    
    spongebob.setheading(0)
    spongebob.forward(10)

window.onkeypress(move_up, "w")
window.onkeypress(move_down, "s")
window.onkeypress(move_left, "a")
window.onkeypress(move_right, "d")

def move_up():
    patrick.setheading(90)
    patrick.forward(10)
        
def move_down():
    patrick.setheading(270)
    patrick.forward(10)
    
def move_left():
    patrick.setheading(180)
    patrick.forward(10)
    
def move_right():    
    patrick.setheading(0)
    patrick.forward(10)

window.onkeypress(move_up, "Up")
window.onkeypress(move_down, "Down")
window.onkeypress(move_left, "Left")
window.onkeypress(move_right, "Right")

# Section 4: Game Loop
window.listen()
timer = 0
while True:
	time.sleep(0.1)
	timer += 0.1 
	 
    
	if spongebob.ycor() >= 300:
		spongebob.goto(spongebob.xcor(), -290)
	if spongebob.ycor() <= -300:
		spongebob.goto(spongebob.xcor(), 290)
	if spongebob.xcor() >= 370:
		spongebob.goto(-360, spongebob.ycor())
	if spongebob.xcor() <= -370:
		spongebob.goto(360, spongebob.ycor())

	if patrick.ycor() >= 300:
		patrick.goto(patrick.xcor(), -290)
	if patrick.ycor() <= -300:
		patrick.goto(patrick.xcor(), 290)
	if patrick.xcor() >= 370:
		patrick.goto(-360, patrick.ycor())
	if patrick.xcor() <= -370:
		patrick.goto(360, patrick.ycor())






	window.update()

	if get_distance(spongebob, patrick) < 35:
		break
	

if it == "spongebob":
	print(f"Game Over, Spongebob won and took {timer} seconds!")
else:
	print(f"Game Over, Patrick won and took {timer} seconds!")