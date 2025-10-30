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

PlayerOptions = ["Hit", "Stand", "bet"]

Options = PlayerOptions[0]

#Variables
CardName = ""

TempPlayerValue = 0
TempDealerValue = 0

PlayerScore = 0
DealerScore = 0
Chips = 100

max_chars = 8

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

def MainGameCreate():
   global PlayerScore
   global DealerScore
   t.hideturtle()
   t.penup()
   t.goto(-200,200)
   t.write("Dealer", font=("Arial", 14, "bold"))

   t.goto(160,200)
   t.write(str(player_name), font=("Arial", 14, "bold"))

   t.goto(-200,-160)
   t.write("Dealer Score:", DealerScore, font=("Arial", 14, "bold"))

   t.goto(160,-160)
   t.write(f"{player_name} Score: {PlayerScore}", font=("Arial", 14, "bold"))
   global Options
   pen.fillcolor("grey")
   pen.penup()
   pen.goto(-85,-200)
   pen.pendown()
   pen.begin_fill()
   for i in range(2):
     pen.forward(80)
     pen.left(90)
     pen.forward(40)
     pen.left(90)
   pen.end_fill()
   pen.write("Hit", align="center", font=("Arial", 14, "bold"))
   pen.fillcolor("grey")
   pen.penup()
   pen.goto(5,-200)
   pen.pendown()
   pen.begin_fill()
   for i in range(2):
     pen.forward(80)
     pen.left(90)
     pen.forward(40)
     pen.left(90)
   pen.end_fill()
   pen.write("Stand", align="center", font=("Arial", 14, "bold"))

def Cashout(): #NOT WORKING YET
   global Chips
   chipsT = trtl.Turtle()
   chipsT.hideturtle()
   chipsT.penup()
   chipsT.speed(0)
   chipsT.goto(0,160)
   chipsT.write("You got", Chips, "Chips.")

#Actual Blackjack game
def Blackjack():
  global CardValue
  global TempPlayerValue
  global CardSuit
  global CardName
  global Chips
  global bet

  CardValue = rand.choice(NumList)
  CardSuit = rand.choice(SuitsList)
  FaceCardValue()
  TempPlayerValue = CardValue
  PlayerScore = PlayerScore + TempPlayerValue
  print(player_name, "score is", PlayerScore)
  if PlayerScore > 21:
    if CardName == "Ace":
      PlayerScore = PlayerScore - 10
    else:
      Chips = Chips - int(bet)
      print("Chips:", Chips)
      PlayerScore = 0
      pen.clear()
      pen.penup()
      pen.goto(-20,100)
      pen.write("You lost", align="center", font=("Arial", 20, "bold"))
      ReplayGame()

def Dealer():
  global CardValue
  global TempDealerValue
  global DealerScore
  global CardSuit
  global Chips

  while DealerScore < 17:
    CardValue = rand.choice(NumList)
    CardSuit = rand.choice(SuitsList)
    FaceCardValue()
    TempDealerValue = CardValue
    DealerScore = DealerScore + TempDealerValue
    pen.clear()
    t.clear()
    wn.update()

  if DealerScore < PlayerScore and DealerScore <= 21 and PlayerScore <= 21:
    Chips = Chips + int(bet)
  if DealerScore == PlayerScore and DealerScore <= 21 and PlayerScore <= 21:
    Chips = Chips
  if DealerScore > PlayerScore and DealerScore <= 21 and PlayerScore <= 21:
    Chips = Chips - int(bet)
  print("Dealer score is", DealerScore)
  print("Chips:", Chips)

def writerMove():
  t.speed(0)
  t.hideturtle()
  t.penup()
  t.setheading(90)
  t.back(20)
  t.pendown()

#Game Portion

#Start Screen
#Get the users name
t.penup()
t.goto(-160,250)
t.pendown()
t.write("Black Jack Simplified", font=("Arial", 35, "bold"))
player_name = trtl.textinput("Name", "Enter your name, with max char "+str(max_chars))
player_name = player_name[:max_chars]

while "," in player_name or len(player_name)==0 or "1" in player_name or "2" in player_name or "3" in player_name or "4" in player_name or "5" in player_name or "6" in player_name or "7" in player_name or "8" in player_name or "9" in player_name:
  player_name = trtl.textinput("Name", "Please do not use a comma, nothing, or number Enter your name")

#Ask if they want rules
def YesNoButtons():
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

screen = trtl.Screen()

#Create a turtle for text and buttons
pen = trtl.Turtle()
pen.hideturtle()
pen.penup()
pen.speed(0)

YesNoButtons()

#Function to check button clicks
def on_click(x, y):
    global pen
    # YES button area
    if -100 < x < -20 and -100 < y < -60:
        pen.clear()
        t.penup()
        t.goto(-100,160)
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
        ReplayGame()

    # NO button area
    elif 100 < x < 180 and -100 < y < -60:
        pen.clear()
        BetValue()
        ReplayGame()

    #Continue
    elif -200 < x < -120 and 200 < y < 240:
       pen.clear()
       MainGameCreate()

    #Cashout
    elif 200 < x < 280 and 200 < y < 240:
       pen.clear()
       Cashout()

    #Hit
    elif -85 < x < -5 and -200 < y < -160:
      Blackjack()

    #Pass
    elif 5 < x < 85 and -200 < y < -160:
      Dealer()
      ReplayGame()

#Listen for clicks
screen.onclick(on_click)

#Begin Playing
Blackjack()
#Bet amount question
def BetValue():
  global bet
  global Chips
  bet = trtl.textinput("Bet", "How much do you want to bet")
  if bet.isnumeric():
    if int(bet) <= Chips:
      ReplayGame()
    else: 
      bet = trtl.textinput("Bet", "Please enter only valid numbers")
  else:
    bet = trtl.textinput("Bet", "Please enter only valid numbers")

#Play game

#Hit

#Stand

#Win/Lose Screen
def ReplayGame():
  global PlayerScore
  global DealerScore

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
  PlayerScore = 0
  DealerScore = 0

#Keeping whats on the screen there
wn = trtl.Screen()
wn.mainloop()