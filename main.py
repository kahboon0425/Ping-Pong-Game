from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

# TODO 1: Create the screen
screen = Screen()
screen.bgcolor("black")
screen.title("Ping Pong Game")
screen.setup(width=800, height=600)

# Turn of animation, update the screen everytime
screen.tracer(0)

# TODO 3: Create another paddle
paddleLeft = Paddle((-350,0))
paddleRight = Paddle((350,0))
ball = Ball()
scoreboard = Scoreboard()


screen.listen()
screen.onkey(paddleRight.go_up, "Up")
screen.onkey(paddleRight.go_down, "Down")
screen.onkey(paddleLeft.go_up, "w")
screen.onkey(paddleLeft.go_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # TODO 5: Detect collision with wall and bounce
    if ball.ycor()>280 or ball.ycor()<-280:
        # needs to bounce
        ball.bounce_y()

    # TODO 6: Detect collision with paddle
    # ball.distance(paddle) - measure the distance between center of the ball and center of the paddle
    if ball.distance(paddleRight) < 50 and ball.xcor() > 320 or ball.distance(paddleLeft)< 50 and ball.xcor() < -320:
        ball.bounce_x()

    # TODO 7: Detect when paddle misses
    # Detect Right paddle misses
    if ball.xcor() >380:
        ball.reset_position()
        scoreboard.l_point()

    # Detect Left paddle misses
    if ball.xcor()<-380:
        ball.reset_position()
        scoreboard.r_point()


screen.exitonclick()








# TODO 8: Keep score

