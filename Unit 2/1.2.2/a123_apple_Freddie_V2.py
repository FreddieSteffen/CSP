#a123_TR_apple_typing_5.py
#Run code in VS Code to be able to access the images.
#Example soulution:
#Code connects to the image of an apple.
#The apple is located on the image of a tree.
#The apple does not draw a line as it falls.
#When A is pressed, the letter A appears on the apple.
#The apple falls to the ground when the A key is pressed.
#The apple and letter disappears after the apple hits the ground.
#When one dissappears, a new apple and letter appear
#The process repeats.

import turtle as trtl
import random as rand
import keyboard

apple_image = "apple.gif" #Store the file name of your shape
ground_height = -200
apple_letter_x_offset = -25
apple_letter_y_offset = -50
screen_width = 400
screen_height = 400
letter_list = list("QWERTYUIOPASDFGHJKLZXCVBNM") #This is the order of QWERTY for the entire alphabet
#It makes it so lambda will basically chose one of the vaulues to display and set as the current_letter

wn = trtl.Screen()
wn.setup(width=1.0, height=1.0)
wn.addshape(apple_image) #Make the screen aware of the new file

wn.bgpic("background.gif")
apple = trtl.Turtle()
apple.penup()
current_letter = "a"
wn.tracer(False)

def reset_apple(active_apple): #Resets the apple back to the top and gets a new letter
  global current_letter
  length_of_list = (len(letter_list) - 1)
  if (length_of_list != 0):
    index = rand.randint(0,length_of_list)
    randx = rand.randint(-200,200)
    active_apple.goto(randx,200)
    current_letter = letter_list.pop(index)
    print(length_of_list)
    print(current_letter)
    draw_apple(active_apple, current_letter) 
  else:
    print("Thanks for playing")

#Given a turtle, set that turtle to be shaped by the image file
def draw_apple(active_apple, letter): #Draws the apple shape
  active_apple.shape(apple_image)
  active_apple.showturtle()
  draw_letter(active_apple, letter)
  wn.update()

def drop_apple(): #Drops the apple from a random x cordinate to the ground (-200)
  wn.tracer(True)
  apple.goto(apple.xcor(), ground_height)
  apple.clear()
  apple.hideturtle()
  wn.tracer(False)
  reset_apple(apple)

def draw_letter(active_apple, letter): #Draws what the letter the user needs to type in
  active_apple.color("black")
  remember_position = active_apple.position()
  active_apple.setpos(active_apple.xcor() + apple_letter_x_offset,active_apple.ycor() + apple_letter_y_offset)
  active_apple.write(letter, font=("Arial", 74, "bold"))
  active_apple.setpos(remember_position)

def check_key(key): #Checks if the letter is correct and drops the apple if it is
  if current_letter.lower() == key:
    drop_apple()  
  if current_letter.upper() == key:
    drop_apple()  

reset_apple(apple)
    
for letter in "qwertyuiopasdfghjklzxcvbnm": #Goes through the letters in QWERTY... till its done picking a random one throughout
  wn.onkeypress(lambda l=letter: check_key(l), letter)

wn.listen()
trtl.mainloop()