import turtle
import random
screen = turtle.Screen(500, 500)
pen_colors = ['red', 'orange', 'black', 'blue', 'green']
global count
count = 0
t1 = turtle.Turtle()
t2 = turtle.Turtle()

t1.speed (0) # 1: slowest, 3:slow, 5:normal, 10:fast, :fastest t1.up()
t1.hideturtle()
t2.speed (10)
t2.up()

# registering the image
# as a new shape
turtle.register_shape('./')
# setting the image as cursor
img_turtle.shape('example.gif')

def start_game():
    draw_StartingLine()
    create_player()
    start_rainFall(t1,0)

def start_rainFall (move, c):
    move.fillcolor (random.choice(pen_colors))
    move.begin_fill()
    move.circle(20)
    move.end_fi11()
    while count != 30:
        move.clear()
        move.setheading(270)
        move.forward(10)
        start_rainFall(move, 10)
        screen.update()

def draw_StartingLine():
    t2.color('purple')
    t2. goto(-220, -250)
    t2.down()
    t2.forward (450)
    t2.up()
def create_player():
    t2.goto(0, -238)
    t2.pendown()
    t2.setheading(90)
    #t2.forward (10)

start_game()