#Import statements
import turtle as trtl
import random as rand
import leaderboard as lb

trtl.addshape("diamond",((0,-6), (6,3), (5,5), (4,6), (-4,6), (-5,5), (-6,3)))
turtle_shape = ["diamond"]
turtle_colors = ["red", "blue", "green", "yellow", "black", "purple", "cyan", "pink", "orange", "grey", "light sky blue"]

font_setup = ("Arial", 20, "normal")
timer = 30
counter_interval = 1000   #1000 represents 1 second
timer_up = False

xLow = -250
xHigh = 250
yLow = -200
yHigh = 200

#Game configuration
leaderboard_file_name = "a122_leaderboard.txt"
leader_names_list = []
leader_scores_list = []
max_chars = 7
player_name = trtl.textinput("Name", "Enter your name, with max char "+str(max_chars))
player_name = player_name[:max_chars]

while "," in player_name or len(player_name)==0 or "1" in player_name or "2" in player_name or "3" in player_name or "4" in player_name or "5" in player_name or "6" in player_name or "7" in player_name or "8" in player_name or "9" in player_name:
  player_name = trtl.textinput("Name", "Please do not use a comma, nothing, or number Enter your name")

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
    t.penup()
    t.hideturtle()
    counter.write("Time's Up", font=font_setup)
    timer_up = True
    manage_leaderboard()
  else:
    counter.write("Timer: " + str(timer), font=font_setup)
    timer = timer - 1
    counter.getscreen().ontimer(countdown, counter_interval) 

#Initialize turtle
t = trtl.Turtle(shape="diamond") #Called it t to save time
t.color(turtle_colors[0])
t.setheading(90)
t.pencolor("black")
t.pensize(5)
t.shapesize(turtleSize)

start = trtl.Turtle()
start.hideturtle()

score_writer = trtl.Turtle()
score_writer.hideturtle()
score_writer.penup()
score_writer.goto(-180,180)
score_writer.pendown()

counter =  trtl.Turtle()
counter.hideturtle()
counter.penup()
counter.goto(20,180)
counter.pendown()

spot = trtl.Turtle()
spot.hideturtle()

#Game functions
def spot_clicked(x, y):
  change_position()
  update_score()
  smaller_shape()
  '''new_colors()'''

def change_position():
  new_xpos = rand.randint(xLow,xHigh)
  new_ypos = rand.randint(yLow,yHigh)
  t.hideturtle()
  t.penup()
  t.goto(new_xpos, new_ypos)
  t.pendown()
  t.showturtle()

def smaller_shape(): #Making the game harder by lowering the shapes size
  global turtleSize
  if turtleSize > 1:
    turtleSize = turtleSize - 1
  else:
    turtleSize = 10
  t.shapesize(turtleSize) #Sets shape size to be 1 smaller

def new_colors():
  '''t.stamp()'''
  turtle_colors.pop(0)
  t.color(turtle_colors[0])

def manage_leaderboard():
  global score
  global spot
  #Get the names and scores from the leaderboard file
  leader_names_list = lb.get_names(leaderboard_file_name)
  leader_scores_list = lb.get_scores(leaderboard_file_name)
  #Show the leaderboard with or without the current player
  if (len(leader_scores_list) < 5 or score >= leader_scores_list[4]):
    lb.update_leaderboard(leaderboard_file_name, leader_names_list, leader_scores_list, player_name, score)
    lb.draw_leaderboard(True, leader_names_list, leader_scores_list, spot, score)
  else:
    lb.draw_leaderboard(False, leader_names_list, leader_scores_list, spot, score)

#Events
wn = trtl.Screen()
wn.setup(width=500, height=400)
wn.cv._rootwindow.resizable(False, False)

countdown()
t.onclick(spot_clicked)

wn.mainloop()
