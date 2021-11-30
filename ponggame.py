#import required library
import turtle
#creating a screen
w = turtle.Screen()
w.title("pong game")
w.setup(width = 1000, height = 600)
w.bgcolor("lightblue")

#left paddle
lp = turtle.Turtle()
lp.speed(0)
lp.shape("square")
lp.color("black")
lp.shapesize(stretch_wid=6,stretch_len=2)
lp.penup()
lp.goto(-400,0)

#right paddle
rp = turtle.Turtle()
rp.speed(0)
rp.shape("square")
rp.color("black")
rp.shapesize(stretch_wid=6,stretch_len=2)
rp.penup()
rp.goto(400,0)

#creating ball
b = turtle.Turtle()
b.speed(20)
b.shape("circle")
b.color("yellow")
b.penup()
b.goto(0,0)
b.dx = 5
b.dy = -5

#intilizing the score
left_player = 0
right_player = 0

#display the score
sketch = turtle.Turtle()
sketch.speed(0)
sketch.color("red")
sketch.penup()
sketch.hideturtle()
sketch.goto(0,260)
sketch.write("Left_Player : 0  Right_Player : 0", align = "center", font = ("Courier", 24, "normal"))

#functions to move paddle vertically
def rpup():
    y= rp.ycor()
    y = y +20
    rp.sety(y)
def rpdown():
    y = rp.ycor()
    y = y-20
    rp.sety(y)
def lpup():
    y = lp.ycor()
    y = y+20
    lp.sety(y)
def lpdown():
    y = lp.ycor()
    y = y-20
    lp.sety(y)
#keyboardbindings
w.listen()
w.onkeypress(rpup,"Up")
w.onkeypress(rpdown,"Down")
w.onkeypress(lpup,"w")
w.onkeypress(lpdown,"s")


while True:
    w.update()

    b.setx(b.xcor()+b.dx)
    b.sety(b.ycor()+b.dy)

    #checking borders
    if b.ycor()>280:
        b.sety(280)
        b.dy = b.dy* -1
    if b.ycor()<-280:
        b.sety(-280)
        b.dy = b.dy*-1
    if b.xcor()>500:
        b.goto(0,0)
        b.dy = b.dy*-1
        left_player += 1
        sketch.clear()
        sketch.write("Left_Player : {} Right_Player : {}".format(left_player, right_player), align = "center", font =("Courier", 24, "normal"))
    if b.xcor()<-500:
        b.goto(0,0)
        b.dy = b.dy*-1
        right_player += 1
        sketch.clear()
        sketch.write("Left_Player : {} Right_Player : {}".format(left_player, right_player), align = "center", font =("Courier", 24, "normal"))
        #checking for paddle and ball collision
    if (b.xcor()>360 and b.xcor()<370) and (b.ycor()<rp.ycor()+40 and b.ycor()> rp.ycor() - 40):
        b.setx(360) 
        b.dx = b.dx*-1
    if (b.xcor()<-360 and b.xcor()>-370) and (b.ycor()<lp.ycor()+40 and b.ycor()>lp.ycor()-40):
        b.setx(-360)
        b.dx = b.dx*-1
        



