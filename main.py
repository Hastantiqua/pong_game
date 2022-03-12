from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.title('Pong')
screen.bgcolor('black')
screen.tracer(0)

right_paddle = Paddle((350, 0))
left_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(right_paddle.up, 'Up')
screen.onkeypress(right_paddle.down, 'Down')
screen.onkeypress(left_paddle.up, 'w')
screen.onkeypress(left_paddle.down, 's')

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()

    # Detect collision with top or bottom wall.
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with a paddle.
    if ball.xcor() < 330 or ball.xcor() > -330:
        if ball.distance(right_paddle) < 50 and ball.xcor() > 320 or \
                ball.distance(left_paddle) < 50 and ball.xcor() < -320:
            ball.bounce_x()

    # Detect when right paddle misses.
    if ball.xcor() > 400:
        ball.reset_position()
        scoreboard.left_point()

    # Detect when left paddle misses.
    if ball.xcor() < -400:
        ball.reset_position()
        scoreboard.right_point()

screen.exitonclick()
