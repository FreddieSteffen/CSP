#Import statements
import turtle as trtl
import random as rand

trtl.addshape("diamond",((0,-6), (6,3), (5,5), (4,6), (-4,6), (-5,5), (-6,3)))
turtle_shape = ["diamond"]
turtle_colors = ["red", "blue", "green", "yellow", "black", "purple", "cyan", "pink", "orange", "grey", "light sky blue"]

font_setup = ("Arial", 20, "normal")
timer = 5
counter_interval = 1000   #1000 represents 1 second
timer_up = False

xLow = -250
xHigh = 250
yLow = -200
yHigh = 200

#Game configuration
global score
score = 0
global turtleSize 
turtleSize = 10

def update_score():
  global score
  score = score + 1
  score_writer.clear()
  score_writer.write(score, font=font_setup)

def countdown():
  global timer, timer_up
  counter.clear()
  if timer <= 0:
    counter.write("Time's Up", font=font_setup)
    timer_up = True
    t.hideturtle()
  else:
    counter.write("Timer: " + str(timer), font=font_setup)
    timer = timer - 1
    counter.getscreen().ontimer(countdown, counter_interval) 

#Initialize turtle
t = trtl.Turtle(shape="diamond") #Called it t to save time
t.color(turtle_colors[0])
t.pencolor("black")
t.pensize(5)
t.shapesize(turtleSize)

start = trtl.Turtle()
start.hideturtle()

score_writer = trtl.Turtle()
score_writer.hideturtle()
score_writer.penup()
score_writer.goto(0,180)
score_writer.pendown()

counter =  trtl.Turtle()
counter.hideturtle()
counter.penup()
counter.goto(-20,150)
counter.pendown()

#Game functions
def spot_clicked(x, y):
  change_position()
  update_score()
  smaller_shape()
  new_colors()

def change_position():
  new_xpos = rand.randint(xLow,xHigh)
  new_ypos = rand.randint(yLow,yHigh)
  t.penup()
  t.goto(new_xpos, new_ypos)
  t.pendown()

def smaller_shape(): #Making the game harder by lowering the shapes size
  global turtleSize
  turtleSize = turtleSize - 1
  t.shapesize(turtleSize) #Sets shape size to be 1 smaller

def new_colors():
  t.stamp()
  turtle_colors.pop(0)
  t.color(turtle_colors[0])

#Events
wn = trtl.Screen()
wn.setup(width=500, height=400)
wn.cv._rootwindow.resizable(False, False)

countdown()
t.onclick(spot_clicked)

wn.mainloop()
