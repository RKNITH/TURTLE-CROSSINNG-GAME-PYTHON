from turtle import Turtle, Screen
from rider import Rider
from scoreboard import Score
from cars import Car
import time




screen =Screen()

rider =Rider()
score =Score()
car =Car()

screen.setup(width=600, height=600)
screen.title("Car crossing game")
screen.setup(width=1000, height=600)
screen.tracer(0)

screen.listen()
screen.onkey(rider.move, "Up")


is_game_on =True
while is_game_on:
    screen.update()
    time.sleep(0.1)

    car.create_car()
    car.move_car()

    for van in car.all_cars:
        if van.distance(rider) <20:
            is_game_on=False
            score.game_over()

    if rider.is_at_finish_line():
        rider.goto_home()
        car.level_up()
        score.increase_score()





screen.mainloop()

