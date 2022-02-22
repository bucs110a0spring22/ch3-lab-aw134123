import turtle               #1. import modules
import random
import time

#Part A
window = turtle.Screen()       # 2.  Create a screen
window.bgcolor('lightblue')

# 3.  Create two turtles
michelangelo = turtle.Turtle()    
leonardo = turtle.Turtle()
michelangelo.color('orange')
leonardo.color('blue')
michelangelo.shape('turtle')
leonardo.shape('turtle')

# 4.  Pick up the pen so we don’t get lines
michelangelo.up()          
leonardo.up()
michelangelo.goto(-100,20)
leonardo.goto(-100,-20)

## 5. your code goes here
michelangelo.down()
leonardo.down()
michelangelo.forward(random.randint(0,100))
leonardo.forward(random.randint(0,100))
time.sleep(1)
michelangelo.goto(-100,20)
leonardo.goto(-100,-20)
michelangelo.clear()
leonardo.clear()

for turtle_step in range(0,10):
  michelangelo.forward(random.randint(0,10))
  leonardo.forward(random.randint(0,10))
  time.sleep(0.3)
time.sleep(.5)
michelangelo.goto(0,0)
leonardo.goto(0,0)
michelangelo.clear()
michelangelo.hideturtle()
leonardo.clear()


#Part B - complete part B here
# van_gogh = turtle.Turtle()
# rembrandt = turtle.Turtle()
# van_gogh.color('yellow')
# rembrandt.color('brown')
# van_gogh.shape('turtle')
# rembrandt.shape('turtle')
# turtle_roster = [michelangelo, leonardo, van_gogh, rembrandt]
# turtle_killed = random.choice(turtle_roster)
# turtle_roster.remove(turtle_killed)
# turtle_spared = random.choice(turtle_roster)
# def change_color():
#     #R = random.random()
#     #B = random.random()
#     #G = random.random()

#     #turtle.color(R, G, B)
# turtle_spared.color()
# turtle_spared.shae('turtle')


for side in [3, 4 , 6, 9, 12]:
  side_length = random.randint(10, 50)
 
  for i in range (0, side):
    leonardo.forward(side_length)
    leonardo.right(360/side)
    
  
  
  leonardo.clear()  
 
  
  
  


window.exitonclick()
