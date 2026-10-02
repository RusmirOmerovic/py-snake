from turtle import Turtle


# Konstanten und Startpositionen

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

# Schlange-Klasse, die die Segmente der Schlange verwaltet

class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()

    def create_snake(self):
        for position in STARTING_POSITIONS:
            segment = Turtle("square")
            segment.color("white")
            segment.penup()
            segment.goto(position)
            self.segments.append(segment)

    # Bewegung der Schlange
        def move(self):
            for segment_num in range(len(self.segments) - 1, 0, -1):
                new_x = self.segments[segment_num - 1].xcor()
                new_y = self.segments[segment_num - 1].ycor()
                self.segments[segment_num].goto(new_x, new_y)
    
            self.segments[0].forward(20)

    # Steuerung der Schlange
    def go_up(self):
        if self.segments[0].heading() != DOWN:  # Verhindert, dass die Schlange sich umkehrt
            self.segments[0].setheading(UP)

    def go_down(self):
        if self.segments[0].heading() != UP:
            self.segments[0].setheading(DOWN)

    def go_left(self):
        if self.segments[0].heading() != RIGHT:
            self.segments[0].setheading(LEFT)

    def go_right(self):
        if self.segments[0].heading() != LEFT:
            self.segments[0].setheading(RIGHT)
    
