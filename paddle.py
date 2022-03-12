from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape('square')
        self.color('white')
        self.penup()
        self.shapesize(stretch_len=5)
        self.setheading(90)
        self.goto(position)

    def up(self):
        if self.ycor() >= 240:
            return
        self.fd(20)

    def down(self):
        if self.ycor() <= -240:
            return
        self.bk(20)
