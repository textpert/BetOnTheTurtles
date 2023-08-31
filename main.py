from turtle import Turtle
from turtle import Screen
import random

COLORS=['red','orange','yellow','green','blue','indigo','violet']
FINISH_LINE = 235
turtles= []
screen = Screen()
screen.setup(width=500, height=400)


for _ in range(0,7):
    tim=Turtle()
    tim.penup()
    tim.shape('turtle')
    tim.color(COLORS[_])
    tim.setx(-200)
    tim.sety(150-(_*50))
    turtles.append(tim)

screen.listen()
user_turtle = screen.textinput(title="Bet on a turtle",prompt="Type a color from VIBGYOR")
end_pos_x = False
winner=[]
winner_count = 0
while not end_pos_x:
    for turtle_index in turtles:
        turtle_index.setx(turtle_index.xcor()+random.randint(0,10))
        if turtle_index.xcor() >= FINISH_LINE:
            turtles.remove(turtle_index)
            winner_count += 1
            if winner_count > 3:
                end_pos_x=True
                break
            winner.append(turtle_index.pencolor())

# if user_turtle.lower() != winner.lower():
# if winner[0]== user_turtle:
#     print(f"Winner is {winner[0]} turtles. Collect your prize.")
# else:
#     print(f"Your {user_turtle} turtle lost the race. Winner is {winner[0]} turtle.")


print(f"Winners are: ")
winner_list = enumerate(winner, start= 1)
for (index,win) in winner_list:
    print(f"Position# {index}: {win}")
# print(list(winner_list))


if user_turtle in winner:
    print("Your turtle won a position. Please collect your prize.")
else:
    print("Your turtle did not win this time.")



#
# def move_right():
#     # print(tim.heading())
#     # print(tim.towards(0,0))
#     # print(tim.degrees(90))
#     tim.right(10)
#     # tim.forward(20)
#
#
# def move_up():
#     # tim.setheading(0)
#     tim.forward(20)
#
#
# def move_left():
#     # tim.setheading(270)
#     tim.left(10)
#     # tim.forward(20)
#
#
# def move_down():
#     # tim.setheading(360)
#     tim.backward(20)
#
#
# def clear():
#     tim.clear()
#     tim.reset()
#
#
#
# screen.listen()
# screen.onkey(fun=move_up, key="w")
# screen.onkey(fun=move_left, key="a")
# screen.onkey(fun=move_down, key="s")
# screen.onkey(fun=move_right, key="d")
# screen.onkey(fun=clear, key="space")
#
#


screen.exitonclick()
