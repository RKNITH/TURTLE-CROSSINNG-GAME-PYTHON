from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.level =0
        self.color("black")  
        self.penup()
        self.goto(0, 270)
        self.write(f"level: {self.level}", align= "center", font=("arial", 24, "bold"))
        self.hideturtle()


    def increase_score(self):
        self.clear()
        self.level +=1
        self.write(f"level: {self.level}", align= "center", font=("arial", 24, "bold"))


    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=("arial", 24, "bold"))    

