colors = ['red', 'blue', 'green', 'yellow', 'orange', 'purple']
STARTING_MOVE =5
MOVE_INCREMENT =10


from turtle import Turtle
import random
class Car():
    def __init__(self):
        
        self.all_cars =[]
        self.car_speed =STARTING_MOVE

    def create_car(self):
        random_chance =random.randint(1, 6)
        if random_chance==1:
            new_car =Turtle("square")
            new_car.shapesize(stretch_wid=1, stretch_len=4)
            new_car.color(random.choice(colors))
            new_car.penup()
            new_car.goto(500, random.randint(-250, 250))

            self.all_cars.append(new_car)

    def move_car(self):
        for car in self.all_cars:
            car.backward(self.car_speed)     


    def level_up(self):
        self.car_speed += MOVE_INCREMENT            


