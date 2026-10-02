from turtle import Turtle
import random


# Food für die Snake erstellen
class Food(Turtle):
    def __init__(self):
        super().__init__()

        self.shape("circle")
        self.color("yellow")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)  # Größe des Foods anpassen
        self.speed("fastest")

        self.refresh()

    def refresh(self):
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        self.goto(x, y)  # Startposition des Foods zufällig setzen