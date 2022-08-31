from turtle import Turtle


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open('data..txt', 'r') as hscore:
            self.high_score = int(hscore.read())
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 280)
        self.update()

    def update(self):
        self.clear()
        self.write(f"Score: {self.score}   High Score: {self.high_score}", align="center", font=("Arial", 14, "normal"))

    def increase_score(self):
        self.score += 1

    def reset_score(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data..txt", "w") as data:
                data.write(str(self.high_score))

        self.score = 0
        self.update()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER")
