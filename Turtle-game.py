# from turtle import Turtle, Screen
#
# tim = Turtle()
# screen = Screen()

# def move_forwards():
#     tim.forward(10)
# def move_backward():
#     tim.backward(10)
#
# def turn_left():
#     new_heading = tim.heading() - 10
#     tim.setheading(new_heading)
#
# def turn_right():
#     new_heading = tim.heading() + 10
#     tim.setheading(new_heading)
#
# def clear():
#     tim.clear()
#     tim.penup()
#     tim.home()
#     tim.pendown()
#
# # screen.listen()
# # screen.onkey(key="space", fun=move_forwards)
# # screen.exitonclick()
#
# screen.listen()
# screen.onkey(move_forwards, "w")
# screen.onkey(move_backward, "s")
# screen.onkey(turn_left, "a")
# screen.onkey(turn_right, "d")
# screen.onkey(clear, "c")
# screen.exitonclick()

from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=320)
user_bet = screen.textinput(title="guess your bet", prompt="Which turtle will win the race? enter a color?")
print(user_bet)

is_race_on = False
y_position = [-80, -40, -0, 40, 80, 120]
colors = ["red", "blue", "yellow", "pink", "purple", "green"]
all_turtle = []

for index_num in range(0, 6):
    tim = Turtle(shape="turtle")
    tim.color(colors[index_num])
    tim.penup()
    tim.goto(x=-230, y=y_position[index_num])
    all_turtle.append(tim)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtle:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner.")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner.")
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

screen.exitonclick()