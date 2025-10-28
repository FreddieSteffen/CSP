#1.2.5 Shall We Play a Game Summitive
#Blackjack/Slots Game
import turtle as trtl
import random as rand
'''import leaderboard as lb'''
import tkinter as tk

t = trtl.Turtle() #Named this to save some time

#Lists
SuitsList = ["Hearts", "Diamonds", "Spades", "Clubs"]
NumList = [1,2,3,4,5,6,7,8,9,10,11,12,13]

TempNumList = NumList
TempSuitsList = SuitsList

#Variables
CardValue = rand.choice(NumList)
CardSuit = rand.choice(SuitsList)
CardName = ""

PlayerScore = 0
DealerScore = 0
penpos = -130

max_chars = 8
font_setup = ("Arial", 20, "normal")

#Functions
def FaceCardValue():
  global CardValue
  global CardSuit
  global CardName
  if CardValue == 13:
    CardValue = 10
    CardName = "King"
  if CardValue == 12:
    CardValue = 10
    CardName = "Queen"
  if CardValue == 11:
    CardValue = 10
    CardName = "Jack"
  if CardValue == 1:
    CardValue = 11
    CardName = "Ace"
  else:
     CardName = str(CardValue)
  print(CardName, "of", CardSuit)

def writerMove():
  t.speed(0)
  t.hideturtle()
  t.penup()
  t.setheading(90)
  t.back(20)
  t.pendown()

def ChipsTotal():
   chipsT = trtl.Turtle()
   chipsT.hideturtle()
   chipsT.penup()
   chipsT.speed(0)
   chipsT.goto(0,160)
   chipsT.write("Chips:", Chips, font=("Arial", 14, "bold"))

def PlayGame():
  '''BetValue()'''
  CardValue = rand.randint(1,13)
  FaceCardValue()
  MainGameCreate()

def BetValue():
  global bet
  global Chips
  bet = trtl.textinput("Bet", "How much do you want to bet")
  if bet.isnumeric():
    if int(bet) <= Chips:
      PlayGame()
  else:
    bet = trtl.textinput("Bet", "Please enter only numbers")

def ReplayGame():
  pen.clear()
  t.clear()
  pen.fillcolor("grey")
  pen.penup()
  pen.goto(-200,200)
  pen.pendown()
  pen.begin_fill()
  for i in range(2):
    pen.forward(80)
    pen.left(90)
    pen.forward(40)
    pen.left(90)
  pen.end_fill()
  pen.write("Continue", align="center", font=("Arial", 14, "bold"))

  pen.begin_fill()
  pen.penup()
  pen.goto(200,200)
  pen.pendown()
  for i in range(2):
    pen.forward(80)
    pen.left(90)
    pen.forward(40)
    pen.left(90)
  pen.end_fill()
  pen.write("Cash Out", align="center", font=("Arial", 14, "bold"))

def MainGameCreate():
   global PlayerScore
   global DealerScore
   t.penup()
   t.goto(-200,200)
   t.write("Dealer", font=("Arial", 14, "bold"))

   t.goto(160,200)
   t.write(str(player_name), font=("Arial", 14, "bold"))

   t.goto(-200,-160)
   t.write("Dealer Score:", DealerScore, font=("Arial", 14, "bold"))

   t.goto(160,-160)
   t.write(f"{player_name} Score: {PlayerScore}", font=("Arial", 14, "bold"))

   for i in range(3): #TRYING TO MAKE THIS WORK
    global penpos
    pen.fillcolor("grey")
    pen.penup()
    pen.goto(-130,-200)
    pen.pendown()
    pen.begin_fill()
    for i in range(2):
      pen.forward(80)
      pen.left(90)
      pen.forward(40)
      pen.left(90)
    pen.end_fill()
    pen.write("Continue", align="center", font=("Arial", 14, "bold"))
    penpos = penpos - 80


#Game Portion

#Start Screen
#Get the users name
player_name = trtl.textinput("Name", "Enter your name, with max char "+str(max_chars))
player_name = player_name[:max_chars]

while "," in player_name or len(player_name)==0 or "1" in player_name or "2" in player_name or "3" in player_name or "4" in player_name or "5" in player_name or "6" in player_name or "7" in player_name or "8" in player_name or "9" in player_name:
  player_name = trtl.textinput("Name", "Please do not use a comma, nothing, or number Enter your name")

#Ask if they want rules
screen = trtl.Screen()

#Create a turtle for text and buttons
pen = trtl.Turtle()
pen.hideturtle()
pen.penup()
pen.speed(0)

#Draw Yes button
pen.goto(-100, -100)
pen.fillcolor("green")
pen.begin_fill()
for i in range(2):
    pen.forward(80)
    pen.left(90)
    pen.forward(40)
    pen.left(90)
pen.end_fill()
pen.goto(-60, -90)
pen.write("YES", align="center", font=("Arial", 14, "bold"))

#Draw No button
pen.goto(100, -100)
pen.fillcolor("red")
pen.begin_fill()
for i in range(2):
    pen.forward(80)
    pen.left(90)
    pen.forward(40)
    pen.left(90)
pen.end_fill()
pen.goto(140, -90)
pen.write("NO", align="center", font=("Arial", 14, "bold"))

#Display question
pen.goto(0, 200)
pen.write("Do you want to know the rules?", align="center", font=("Arial", 18, "bold"))

#Function to check button clicks
def on_click(x, y):
    global pen
    # YES button area
    if -100 < x < -20 and -100 < y < -60:
        pen.clear()
        t.write("The rules are:")
        writerMove()
        t.write("Get to as close of a score of 21 without going over")
        writerMove()
        t.write("You get 2 cards to start with value on them unless Jack, Queen, King, Ace")
        writerMove()
        t.write("Jack, Queen and King are worth 10pts and Ace is worth 11 unless you would be over 21")
        writerMove()
        t.write("First you have to bet")
        writerMove()
        t.write("You can hit to get 1 more card")
        writerMove()
        t.write("You can stand to keep current amount")
        writerMove()
        t.write("The dealer then flips their card")
        writerMove()
        t.write("If you are closer to 21 but not over you gain what you betted but if you were farther you lose that amount")
        writerMove()
        PlayGame()

    # NO button area
    elif 100 < x < 180 and -100 < y < -60:
        pen.clear()
        BetValue()
        PlayGame()

    #Continue
    elif -200 < x < -120 and 200 < y < 240:
       pen.clear()
       print("continuing")

    #Cashout
    elif 120 < x < 200 and 200 < y < 240:
       pen.clear()
       print("Cashing out")

#Listen for clicks
screen.onclick(on_click)

#Begin Playing
#Chips total = 100
global Chips
Chips = 100
ChipsTotal()
BetValue()
ReplayGame()

#Bet amount question

#Play game
#Hit
#Stand

#Win/Lose Screen


#Keeping whats on the screen there
wn = trtl.Screen()
wn.mainloop()