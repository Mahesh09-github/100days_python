from turtle import Turtle
sp_list = [(0,0),(-20,0),(-40,0)]
move_distance = 20

class Snake:
    def __init__(self):
        self.segments=[]
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in sp_list:
            self.add_segment(position)
    def add_segment(self,position):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend_snake(self):
        self.add_segment(self.segments[-1].position())
    
    def move(self):
        for seg in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg - 1].xcor()
            new_y = self.segments[seg - 1].ycor()
            self.segments[seg].goto(new_x,new_y)
        self.segments[0].forward(move_distance)
    
    def up(self):
        if self.head.heading() != "Down":
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != "Up":
            self.head.setheading(270)
    def left(self):
        if self.head.heading() != "Right":
            self.head.setheading(180)
    def right(self):
        if self.head.heading() != "Left":
            self.head.setheading(0)
    