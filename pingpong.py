import turtle

screen = turtle.Screen()
screen.title("Ping-Pong Game")
screen.bgcolor("black")
screen.setup(width=1050, height=650)
screen.tracer(0)

middle_line = turtle.Turtle()
middle_line.speed(0)
middle_line.color("white")
middle_line.penup()
middle_line.goto(0, 325)
middle_line.pendown()
middle_line.goto(0, -325)
middle_line.hideturtle()

score_A = 0
score_B = 0

scoreboard = turtle.Turtle()
scoreboard.speed(0)
scoreboard.color("white")
scoreboard.penup()
scoreboard.hideturtle()
scoreboard.goto(0, 260)
scoreboard.write("Player A: {}  VS  Player B: {}".format(score_A, score_B), align="center", font=("Courier", 24, "normal"))

left_paddle = turtle.Turtle()
left_paddle.speed(0)
left_paddle.shape("square")
left_paddle.color("red")
left_paddle.shapesize(stretch_wid=6, stretch_len=1)
left_paddle.penup()
left_paddle.goto(-400, 0)

right_paddle = turtle.Turtle()
right_paddle.speed(0)
right_paddle.shape("square")
right_paddle.color("blue")
right_paddle.shapesize(stretch_wid=6, stretch_len=1)
right_paddle.penup()
right_paddle.goto(400, 0)

ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.5
ball.dy = -0.5

def update_score():
    scoreboard.clear()
    scoreboard.write("Player A: {}  VS  Player B: {}".format(score_A, score_B), align="center", font=("Courier", 24, "normal"))

def move_left_paddle_up():
    y = left_paddle.ycor() + 20
    if y < 290:
        left_paddle.sety(y)

def move_left_paddle_down():
    y = left_paddle.ycor() - 20
    if y > -290:
        left_paddle.sety(y)

def move_right_paddle_up():
    y = right_paddle.ycor() + 20
    if y < 290:
        right_paddle.sety(y)

def move_right_paddle_down():
    y = right_paddle.ycor() - 20
    if y > -290:
        right_paddle.sety(y)

screen.listen()
screen.onkeypress(move_left_paddle_up, "w")
screen.onkeypress(move_left_paddle_down, "s")
screen.onkeypress(move_right_paddle_up, "Up")
screen.onkeypress(move_right_paddle_down, "Down")
screen.onkeypress(screen.bye, "Escape")

while True:
    screen.update()
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
    
    if ball.ycor() > 315 or ball.ycor() < -315:
        ball.dy *= -1

    if ball.xcor() > 435:
        ball.goto(0, 0)
        ball.dy *= -1
        score_A += 1
        update_score()

    if ball.xcor() < -435:
        ball.goto(0, 0)
        ball.dy *= -1
        score_B += 1
        update_score()

    if (ball.dx > 0) and (right_paddle.xcor() - 20 < ball.xcor() < right_paddle.xcor()) and (right_paddle.ycor() + 60 > ball.ycor() > right_paddle.ycor() - 60):
        ball.dx *= -1

    elif (ball.dx < 0) and (left_paddle.xcor() + 20 > ball.xcor() > left_paddle.xcor()) and (left_paddle.ycor() + 60 > ball.ycor() > left_paddle.ycor() - 60):
        ball.dx *= -1


