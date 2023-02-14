from turtle import Turtle

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        # making the ball speed faster and faster (the smaller the value the fastest)
        self.move_speed = 0.1

    # TODO 4: Create the ball and make it move
    def move(self):
        new_x = self.xcor()+self.x_move
        new_y = self.ycor()+self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *= 0.9
        # e.g. if we start out with value of 5, speed will be 4.5 --> 4.09)

    def reset_position(self):
        self.goto(0,0)
        # once one player has lost, reset the ball speed to the original value
        self.move_speed = 0.1
        self.bounce_x()


