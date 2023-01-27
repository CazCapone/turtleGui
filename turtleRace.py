from turtle import Screen, Turtle
import random

is_racing = False
screen = Screen()
width, height = 500, 400
screen.setup(width, height)

guess = screen.textinput(title="Place your bets!", prompt="Which turtle will win the race? (red/green/blue/orange/yellow/purple) ")
colors = ["red", "green", "blue", "orange", "yellow", "purple"]
y_pos = [150, 90, 30, -30, -90, -150]
turtles = []

# Create all turtles with different colors
for i in range(0, len(colors)):
    t = Turtle(shape="turtle")
    t.color(colors[i])
    t.penup()
    t.goto(-230, y_pos[i])
    turtles.append(t)  

if guess:
    is_racing = True

while is_racing:

    for turtle in turtles:
        if turtle.xcor() > 230:
            is_racing = False
            winner = turtle.pencolor()

            # Create instance for on-screen message 
            message = Turtle()
            message.color("black")
            style = ('Courier', 12, 'italic')
            message.hideturtle()
            
            if winner == guess:
                message.write(f"You have won!", font=style, align='center')
                print(f"You have won! The {winner} turtle is the winner!")
            else:
                message.write(f"You have lost!", font=style, align='center')
                print(f"You have lost! The {winner} turtle is the winner!")
            
        rand_dist = random.randint(0, 10)
        turtle.forward(rand_dist)

screen.exitonclick()