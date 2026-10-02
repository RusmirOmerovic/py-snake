from turtle import Turtle, Screen
import time


# Bildschirm erstellen
screen = Screen()
screen.title("Snake")
screen.setup(width=600, height=600)
screen.bgcolor("black")

# Tastatur aktivieren
screen.listen()

screen.onkey(go_up, "Up")
screen.onkey(go_down, "Down")
screen.onkey(go_left, "Left")
screen.onkey(go_right, "Right")

# Game Loop
screen.tracer(0)  # Bildschirm-Updates deaktivieren, um Flackern zu vermeiden
game_is_on = True
while game_is_on:
    screen.update()  # Bildschirm-Updates manuell durchführen
    time.sleep(0.5)  # Kurze Pause, um die Bewegung sichtbar zu machen
    # Körpersegmente folgen dem jeweiligen Vorgänger
    for segment_num in range(len(segments) - 1, 0, -1):
        new_x = segments[segment_num - 1].xcor()
        new_y = segments[segment_num - 1].ycor()
        segments[segment_num].goto(new_x, new_y)

    # Kopf bewegt sich nach vorne
    segments[0].forward(20)



# Programm beenden, wenn das Fenster angeklickt wird
screen.exitonclick()

