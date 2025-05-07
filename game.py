import turtle
import random
# Set up the screen
screen = turtle.Screen()
screen.setup(width=500, height=500)

pen_colors = ['red', 'orange', 'black', 'blue', 'green']
global count
count = 0
t1 = turtle.Turtle()
t2 = turtle.Turtle()
playButton = turtle.Turtle()

t1.speed (0) # 1: slowest, 3:slow, 5:normal, 10:fast, :fastest t1.up()
t1.hideturtle()
t2.speed (10)
t2.up()

# registering the image
# as a new shape
#turtle.register_shape('./')
# setting the image as cursor
#img_turtle.shape('example.gif')

def play_game():
    playButton.clear()  # Clear the button after clicking
    draw_StartingLine()
    create_player()
    start_rainFall(t1,0)

def start_rainFall (move, c):
    move.fillcolor (random.choice(pen_colors))
    move.begin_fill()
    move.circle(20)
    move.end_fill()
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

def draw_button():
    # Create a button using a turtle object

    playButton.hideturtle()
    playButton.penup()
    playButton.goto(-50, 200)  # Position of the button
    playButton.pendown()
    playButton.fillcolor("lightblue")
    playButton.begin_fill()
    for _ in range(2):  # Draw a rectangle
        playButton.forward(100)
        playButton.left(90)
        playButton.forward(50)
        playButton.left(90)
    playButton.end_fill()
    playButton.penup()
    playButton.goto(-30, 215)  # Position text inside the button
    playButton.write("Play", align="center", font=("Arial", 16, "bold"))

    # Add click detection for the button
    def button_click(x, y):
        if -50 <= x <= 50 and 200 <= y <= 250:  # Check if click is inside the button
            play_game()

    screen.onclick(button_click)

# Call the draw_button function to display the button
draw_button()

turtle.mainloop()
