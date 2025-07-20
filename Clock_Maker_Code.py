import turtle

wn = turtle.Screen()
wn.title("Clock Display")
clck = turtle.Turtle() # sets the variable for the turtle
hour = int(input("Enter an hour here: " ))
minute = int(input("Enter a minute here: "))

for a in range(12):
    for b in range(10): # Drawing the clock
        clck.forward(4)
        clck.left(3)
    clck.left(90) # Drawing the tick marks in the clock
    clck.forward(11)
    clck.right(180)
    clck.forward(10)
    clck.left(90)
    
clck.left(90) # Going to the center of the clock
clck.penup()
clck.forward(76)
clck.pendown()

clck.speed(2) # Setting the new speed

clck.right(minute*6) # Drawing the minute  hand
clck.forward(60)
clck.left(180)
clck.forward(60)
clck.right(180 - minute*6)

clck.right(hour*30 + minute/2) # Turning the turtle to the direction of the hour hand
clck.forward(e40) # Drawing the hour hand 
clck.left(180)

clck.hideturtle() # Hiding the ugly turtle from sight

wn.mainloop()
