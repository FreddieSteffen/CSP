#Freddie Steffen
import turtle as trtl
import random as rand

myPen = trtl.Turtle()
#Screen Setup
trtl.Screen().bgcolor("#3fa652")
myPen.shape("arrow")
myPen.pensize(5)
myPen.speed(10)
myPen.color("white")
myPen.write("Turtle Race!", align='center',  font=("Times New Roman", 20, "normal"))

#Complete the code here

#Lists
line_positions_X = [-160,-160,180,180,0]
line_positions_Y = [150,0,150,0,0]
turtle_colors = ["white", "blue", "pink", "green", "red"]
turtle_shapes = ["arrow", "turtle", "circle", "square"]
turtles = []

#Variables
global posX
global posY
posX = int(line_positions_X[0])
posY = int(line_positions_Y[0])
global TurtlePosY
TurtlePosY = 140
turtlePosition = 0
global turtleNumber
turtleNumber = 0
global winner
winner = None

#Definitions
def draw_lines():
  myPen.penup()
  for i in range(2):
    posX = int(line_positions_X[0])
    posY = int(line_positions_Y[0])
    myPen.goto(posX,posY)
    posX = line_positions_X.pop(0)
    posY = line_positions_Y.pop(0)
    myPen.pendown()
    myPen.hideturtle()

def celebration():
  myPen.clear()
  myPen.penup()
  myPen.goto(0,0)
  myPen.pendown()
  for turtle in turtles:
    turtle.hideturtle()
  myPen.write(f"Turtle #{winner} Wins!", align="center", font=("Times New Roman", 100, "normal"))

#Make Start and Finish Line
myPen.onclick(draw_lines)
for i in range(2):
  draw_lines()

#Moving turtles to start line
for s in turtle_shapes:
  turtle = trtl.Turtle(shape=s)
  turtles.append(turtle)
  turtleNumber = turtleNumber + 1
  new_color = turtle_colors.pop()
  turtle.color(new_color)
  turtle.penup()
  turtle.goto(-180, TurtlePosY)
  turtle.setheading(0)
  TurtlePosY = TurtlePosY - 30

#Making turtles move a random amount accros the screen
while True:
  for turtleNumber, turtle in enumerate(turtles, start=1):
    turtle.forward(rand.randint(1,8))
    turtlePosition = turtle.xcor()
    if turtlePosition >= 180:
      winner = turtleNumber
      break
  
  if winner is not None:
    break

celebration()

#Ending parts to keep whats on screen there
wn = trtl.Screen()
wn.mainloop()