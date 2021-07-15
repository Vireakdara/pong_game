from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.setposition(position)

    def go_up(self):
        paddle_y = self.ycor() + 20
        self.goto(self.xcor(), paddle_y)

    def go_down(self):
        paddle_y = self.ycor() - 20
        self.goto(self.xcor(), paddle_y)
