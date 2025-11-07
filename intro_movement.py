# Section 1 - Helper functions (DON'T CHANGE!!)
import turtle, time, random
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

window = turtle.Screen()
window.tracer(0)

# Section 2: Setup
set_background("castle")
s1 = create_sprite("character1",0,-200)

# Section 3: define movement controls
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

window.onkeypress(move_up, "w")
window.onkeypress(move_down, "s")
window.onkeypress(move_left, "a")
window.onkeypress(move_right, "d")

# Section 4: define other controls
# hide and show controls
def hide():
    s1.hideturtle()
def show():
    s1.showturtle()

window.onkeypress(hide, "h")
window.onkeyrelease(show, "h")

def draw():
    s1.pendown()

window.onkeypress(draw, "c")

def sdraw():
    #sdraw = stop draw
    s1.penup()

window.onkeypress(sdraw, "v")

def erase():
    s1.clear()

window.onkeypress(erase, "e")

def redp():
    s1.color("red")

window.onkeypress(redp, "r")

def greenp():
    s1.color("green")

window.onkeypress(greenp, "t")

def reset():
    s1.goto(0, 0)

window.onkeypress(reset, "f")

def thicker():
    s1.pensize(5)

window.onkeypress(thicker, "p")

def thinner():
    s1.pensize(1)

window.onkeypress(thinner, "o")

# Section 5: game loop
window.listen()
while True:
    time.sleep(0.001)
    window.update()