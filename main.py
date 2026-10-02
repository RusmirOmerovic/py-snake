from turtle import Screen
from snake import Snake
import time
from food import Food


# Bildschirm erstellen
screen = Screen()
screen.title("Snake")
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(0)  # Bildschirm-Updates deaktivieren, um Flackern zu vermeiden

# Spielobjekte erstellen
snake = Snake()
food = Food()

# Tastatur aktivieren
screen.listen()

screen.onkey(snake.go_up, "Up")
screen.onkey(snake.go_down, "Down")
screen.onkey(snake.go_left, "Left")
screen.onkey(snake.go_right, "Right")

# Game Loop
game_is_on = True

while game_is_on:
    screen.update()  # Bildschirm-Updates manuell durchführen
    time.sleep(0.5)  # Kurze Pause, um die Bewegung sichtbar zu machen

    snake.move()  # Schlange bewegen



# Programm beenden, wenn das Fenster angeklickt wird
screen.exitonclick()

