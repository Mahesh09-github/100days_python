from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.move_back()

    def move_back(self):
        self.penup()
        self.go_to_start()
        self.setheading(90)
        self.y_cor = 0

    def move(self):
        self.y_cor = self.ycor()
        self.y_cor += MOVE_DISTANCE
        self.goto(0,self.y_cor) 

    def go_to_start(self):
        self.goto(STARTING_POSITION)
    def is_at_finish_line(self):

        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False
        
    
