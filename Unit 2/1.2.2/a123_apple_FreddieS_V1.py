#a123_apple_FreddieS_V1.py
import turtle as trtl
#Setup
appleImage = "apple.gif" #Store the file name of your shape
pearImage = "pear.gif"

wn = trtl.Screen()
wn.setup(width=1.0, height=1.0)
wn.addshape(appleImage) #Make the screen aware of the new file
wn.addshape(pearImage)
wn.bgpic("background.gif")
apple = trtl.Turtle()

#Functions
#given a turtle, set that turtle to be shaped by the image file
def draw_apple(active_apple):
  active_apple.shape(appleImage)
  wn.update()

def appleFall(active_apple):
  active_apple.goto(active_apple.xcor(), -200)

def dropApple():
  apple.goto(apple.xcor(), -200) 

#Function calls
draw_apple(apple)
apple.penup()

wn.onkeypress(dropApple, "a")

wn.listen()
wn.mainloop()