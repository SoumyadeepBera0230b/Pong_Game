import turtle as turtle


# Set up game screen
turtle.title("Pong game")
turtle.setup(400, 300)
turtle.bgcolor("lightblue")


welcome = turtle.Turtle()
welcome.color("black")
welcome.write("Welcome", align='center', font=("Arial", 40, "bold"))

p1 = input("Enter player1 name: ")
p2 = input("Enter player2 name: ")
welcome.clear()
welcome.hideturtle()

border = turtle.Turtle()
border.width(8)


def draw_rec(linecolor, length1=800, length2=600):
    border.penup()
    border.goto(-400, -300)
    border.color(linecolor, "black")
    border.pendown()
    for i in range(2):
        border.forward(length1)
        border.left(90)
        border.forward(length2)
        border.left(90)


border.begin_fill()
draw_rec("orange")
border.end_fill()
border.hideturtle()


# Left Paddle or Paddle 1
paddle1 = turtle.Turtle()
paddle1.shape("square")
paddle1.color("red")
paddle1.shapesize(stretch_wid=5, stretch_len=1)
paddle1.penup()
paddle1.goto(-350, 0)
paddle1.dy = 0

# Right paddle or paddle2
paddle2 = turtle.Turtle()
paddle2.shape("square")
paddle2.color("blue")
paddle2.shapesize(stretch_len=1, stretch_wid=5)
paddle2.penup()
paddle2.goto(350, 0)
paddle2.dy = 0

# Game Rules

game_over = False
winner = None
points = {
    "player1": 0,
    "player2": 0
}
game_rules = {
    "max_points": 3,
    "ball_speed": 3
}


# Creating the Ball
ball = turtle.Turtle()
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.75
ball.dy = 0.75
ballspeed = 10


# Score display
score_display = turtle.Turtle()
score_display.color("white")
score_display.penup()
score_display.hideturtle()
score_display.goto(0, 260)
score_display.write(f"{p1}: 0      {p2}: 0", align="center",
                    font=("Arial", 24, "bold"))

# Function to move paddle1 up


def paddle1_up():
    paddle1.dy = 10

# Function to move paddle1 down


def paddle1_down():
    paddle1.dy = -10

# Function to move paddle2 up


def paddle2_up():
    paddle2.dy = 10

# Function to move paddle2 down


def paddle2_down():
    paddle2.dy = -10


def paddle1_stop():
    paddle1.dy = 0


def paddle2_stop():
    paddle2.dy = 0


# Logic for moving the paddles
# Set up keyboard bindings
turtle.listen()
turtle.onkeypress(paddle1_up, "w")
turtle.onkeypress(paddle1_down, "s")
turtle.onkeypress(paddle2_up, "Up")
turtle.onkeypress(paddle2_down, "Down")

turtle.onkeyrelease(paddle1_stop, "w")
turtle.onkeyrelease(paddle1_stop, "s")
turtle.onkeyrelease(paddle2_stop, "Up")
turtle.onkeyrelease(paddle2_stop, "Down")


# Game mathematical logic

# Game loop
while not game_over:
    # Move paddles and ball
    paddle1.sety(paddle1.ycor() + paddle1.dy)
    paddle2.sety(paddle2.ycor() + paddle2.dy)
    ball.setx(ball.xcor() + ball.dx * ballspeed)
    ball.sety(ball.ycor() + ball.dy * ballspeed)

    # Check for game over conditions
    if points["player1"] == game_rules["max_points"]:
        game_over = True
        winner = p1
    elif points["player2"] == game_rules["max_points"]:
        game_over = True
        winner = p2

    # Check for ball collision with paddles
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle2.ycor() + 50 and ball.ycor() > paddle2.ycor() - 50):
        ball.setx(340)
        ball.dx *= -1
    elif (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle1.ycor() + 50 and ball.ycor() > paddle1.ycor() - 50):
        ball.setx(-340)
        ball.dx *= -1

    # Check for ball going off screen
    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        points["player1"] += 1
    elif ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        points["player2"] += 1

    # Check for ball colliding with top or bottom of screen
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
    elif ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
    print(ball.dy)

    # Update score display
    score_display.clear()
    score_display.write(
        f"{p1}: {points['player1']}    {p2}: {points['player2']}", align="center", font=("Arial", 24, "bold"))

# Game over screen
game_over_display = turtle.Turtle()
game_over_display.color("white")
game_over_display.penup()
game_over_display.hideturtle()
game_over_display.goto(0, 0)
game_over_display.write("Game Over! {} wins!".format(
    winner), align="center", font=("Arial", 36, "normal"))


turtle.done()
# input("Press any key to exit")
