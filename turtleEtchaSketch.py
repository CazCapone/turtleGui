from turtle import Screen, Turtle

t = Turtle()
screen = Screen()
distance = 10
angle = 10

def move_forward():
    t.forward(distance)

def move_backward():
    t.backward(distance)

def move_clockwise():
    t.right(angle)

def move_counter_clockwise():
    t.left(angle)

def clear_screen():
    t.clear()
    t.reset()

screen.listen()
screen.onkey(move_forward, "w")
screen.onkey(move_backward, "s")
screen.onkey(move_counter_clockwise, "a")
screen.onkey(move_clockwise, "d")
screen.onkey(clear_screen, "c")
screen.exitonclick()