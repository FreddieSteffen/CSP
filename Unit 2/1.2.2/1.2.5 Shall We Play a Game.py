#1.2.5 Shall We Play a Game Summitive
#Blackjack/Slots Game
import turtle as trtl
import random as rand
import leaderboard as lb

t = trtl.Turtle()

#Lists
SuitsList = ["Heart", "Diamond", "Spades", "Clubs"]
NumList = [1,2,3,4,5,6,7,8,9,10,11,12,13]

TempNumList = NumList
TempSuitsList = SuitsList

#Variables
CardValue = 0
CardName =""

PlayerTotalValue = 0
HouseTotalValue = 0

#Functions
def FaceCardValue():
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
  if CardValue == 2:
    CardValue = 2
    CardName = str(CardValue)
  if CardValue == 3:
    CardValue = 3
    CardName = str(CardValue)
  if CardValue == 4:
    CardValue = 4
    CardName = str(CardValue)
  if CardValue == 5:
    CardValue = 5
    CardName = str(CardValue)
  if CardValue == 6:
    CardValue = 6
    CardName = str(CardValue)
  if CardValue == 7:
    CardValue = 7
    CardName = str(CardValue)
  if CardValue == 8:
    CardValue = 8
    CardName = str(CardValue)
  if CardValue == 9:
    CardValue = 9
    CardName = str(CardValue)
  if CardValue == 10:
    CardValue = 10
    CardName = str(CardValue)


#Game Portion

#Start Screen
#Get the users name
#Ask if they want rules
#If they want rules then give them

#Begin Playing
#Chips total = 100
#Bet amount question
#Play game
#Hit
#Stand

#Win/Lose Screen


#Keeping whats on the screen there
wn = trtl.Screen()
wn.mainloop()