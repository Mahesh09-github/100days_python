from turtle import Turtle
FONT= ("Arial",24,"normal")
class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0,270)
        self.write(f"Score: {self.score}",align="center",font=FONT)
        self.hideturtle()

    def score_update(self):
        self.score += 1
        self.clear()
        self.increase_score()

    def increase_score(self):
            self.write(f"Score: {self.score}",align="center",font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write("Game Over!!",align="center", font = FONT)
