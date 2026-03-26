import turtle
import random


wn = turtle.Screen()
wn.title("Breakout Game")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)


score = 0


paddle = turtle.Turtle()
paddle.speed(0)
paddle.shape("square")
paddle.color("white")
paddle.shapesize(stretch_wid=1, stretch_len=6)
paddle.penup()
paddle.goto(0, -250)


ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("red")
ball.penup()
ball.goto(0, -200)

ball.dx = 3
ball.dy = 3


bricks = []

colors = ["red", "orange", "yellow", "green"]

for row in range(5):
    for col in range(10):
        brick = turtle.Turtle()
        brick.speed(0)
        brick.shape("square")
        brick.color(colors[row % len(colors)])
        brick.shapesize(stretch_wid=1, stretch_len=3)
        brick.penup()
        x = -350 + col * 70
        y = 250 - row * 30
        brick.goto(x, y)
        bricks.append(brick)


pen = turtle.Turtle()
pen.hideturtle()
pen.color("white")
pen.penup()
pen.goto(0, 260)
pen.write(f"Score: {score}", align="center", font=("Arial", 16, "bold"))


def move_left():
    x = paddle.xcor() - 40
    if x < -350:
        x = -350
    paddle.setx(x)

def move_right():
    x = paddle.xcor() + 40
    if x > 350:
        x = 350
    paddle.setx(x)

wn.listen()
wn.onkeypress(move_left, "Left")
wn.onkeypress(move_right, "Right")


while True:
    wn.update()

    
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    
    if ball.xcor() > 390 or ball.xcor() < -390:
        ball.dx *= -1

    if ball.ycor() > 290:
        ball.dy *= -1

    
    if (ball.ycor() > -240 and ball.ycor() < -230) and \
       (ball.xcor() > paddle.xcor() - 60 and ball.xcor() < paddle.xcor() + 60):
        ball.dy *= -1

   
    for brick in bricks:
        if brick.distance(ball) < 35:
            brick.goto(1000, 1000)  
            bricks.remove(brick)
            ball.dy *= -1
            score += 10
            pen.clear()
            pen.write(f"Score: {score}", align="center", font=("Arial", 16, "bold"))

    
    if ball.ycor() < -300:
        pen.goto(0, 0)
        pen.write("GAME OVER", align="center", font=("Arial", 24, "bold"))
        break

wn.mainloop()