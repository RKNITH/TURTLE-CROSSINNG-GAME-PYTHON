from turtle import Turtle

class Rider(Turtle):
    def __init__(self):
        super().__init__()

        self.shape("turtle")
        self.color("red")
        self.penup()
        self.goto(0, -280)
        self.setheading(90)

    def move(self):
        self.forward(20)

    def goto_home(self):
        self.goto(0, -280)

    def is_at_finish_line(self):
        if self.ycor() >295:
            return True 
        else:
            return False           
