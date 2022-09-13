import turtle
import os


def pad_a_up():
    y = pad_a.ycor()
    y += 20
    pad_a.sety(y)


def pad_a_down():
    y = pad_a.ycor()
    y -= 20
    pad_a.sety(y)


def pad_b_up():
    y = pad_b.ycor()
    y += 20
    pad_b.sety(y)


def pad_b_down():
    y = pad_b.ycor()
    y -= 20
    pad_b.sety(y)


def score_upd():
    pen.clear()
    pen.write(f'Player A: {score_a}  Player B: {score_b}', align='center', font=('Courier', 24, 'normal'))


win = turtle.Screen()
win.bgcolor('black')
win.title('Pong')
win.setup(width=800, height=600)
win.tracer(0)

# pad_a
pad_a = turtle.Turtle()
pad_a.shape('square')
pad_a.color('white')
pad_a.speed(0)
pad_a.shapesize(stretch_wid=5, stretch_len=1)
pad_a.penup()
pad_a.goto(-350, 0)

# pad_b
pad_b = turtle.Turtle()
pad_b.shape('square')
pad_b.color('white')
pad_b.speed(0)
pad_b.shapesize(stretch_wid=5, stretch_len=1)
pad_b.penup()
pad_b.goto(350, 0)

# ball
ball = turtle.Turtle()
ball.shape('square')
ball.color('white')
ball.speed(0)
ball.penup()
ball.goto(0, 0)
ball.dx = 0.4
ball.dy = 0.4

# score
score_a = 0
score_b = 0
pen = turtle.Turtle()
pen.speed(0)
pen.color('White')
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write(f'Player A: {score_a}  Player B: {score_b}', align='center', font=('Courier', 24, 'normal'))

# keyboard bindings
win.listen()
win.onkeypress(pad_a_up, key='w')
win.onkeypress(pad_a_down, key='s')
win.onkeypress(pad_b_up, key='Up')
win.onkeypress(pad_b_down, key='Down')


# Main loop
while True:
    win.update()

    # Moving the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border check for ball
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        # os.system("D:\Pyton projects\LearnPythonSixGames\Pong\\bounce.mp3")

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        # os.system("D:\Pyton projects\LearnPythonSixGames\Pong\\bounce.mp3")

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        score_upd()

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        score_upd()

    # Border check for pads
    if pad_a.ycor() > 260:
        pad_a.sety(260)

    if pad_a.ycor() < -260:
        pad_a.sety(-260)

    if pad_b.ycor() > 260:
        pad_b.sety(260)

    if pad_b.ycor() < -260:
        pad_b.sety(-260)

    # pad and ball collisions
    if (ball.xcor() > 340 and ball.xcor() < 350)\
            and (ball.ycor() < pad_b.ycor()+40) and ball.ycor() > pad_b.ycor()-40:
        ball.setx(340)
        # os.system("aplay bounce.mp3&")
        ball.dx *= -1.03

    if (ball.xcor() < -340 and ball.xcor() > -350)\
            and (ball.ycor() < pad_a.ycor()+40) and ball.ycor() > pad_a.ycor()-40:
        ball.setx(-340)
        # os.system("aplay bounce.mp3&")
        ball.dx *= -1.03

