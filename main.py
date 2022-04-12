import time
import tkinter
import turtle

# ! Configure window
wn = turtle.Screen()
wn.title("Pong game using turtle by www.azizbekDev.com")
wn.bgcolor("#000000")
wn.setup(width=800, height=600)
wn.tracer(0)
root_win = wn.cv._rootwindow or tkinter.Tk()
root_win.resizable(False, False)

# !Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("#ffffff")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)
player_a_score = 0
# !Paddle b
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("#ffffff")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)
player_b_score = 0

# !Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("#f3f3f3")
ball.penup()
ball.goto(0, 0)
ball.dx = .6
ball.dy = .6

# !Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("#ffffff")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)


# ! Functionality
def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)
def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)
def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)
def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)

# ! keyboard binding
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_down, "Down")

# ! Run
if __name__ == "__main__":
    while True:
        wn.update()

        # ! Moving the ball
        ball.setx(ball.xcor() + ball.dx)
        ball.sety(ball.ycor() + ball.dy)

        # ! border checking
        if ball.ycor() > 290:
            ball.sety(290)
            ball.dy *= -1

        if ball.ycor() < -290:
            ball.sety(-290)
            ball.dy *= -1

        if ball.xcor() > 390:
            ball.goto(0, 0)
            ball.dx *= -1
            time.sleep(.1)
            player_a_score += 1
        
        if ball.xcor() < -390:
            ball.goto(0, 0)
            ball.dx *= -1
            time.sleep(.1)
            player_b_score += 1

        # ! Paddle and ball collisions

        if ball.xcor() > 340 and ball.xcor() < 350 and (ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() -50):
            ball.setx(340)
            ball.dx *= -1

        if ball.xcor() < -340 and ball.xcor() > -350 and (ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() -50):
            ball.setx(-340)
            ball.dx *= -1
            
        
        pen.clear()
        pen.write(f"Player A: {player_a_score}  Player B: {player_b_score}", align="center", font=("Courier", 24, "normal"))