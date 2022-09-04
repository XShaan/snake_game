from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        with open("data.txt") as file:
            self.high_score = int(file.read())
        self.hideturtle()
        self.score = 0
        self.goto(0, 280)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {int(self.high_score)}")

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as files:
                files.write(f"{self.score}")
        self.score = 0
        self.update_scoreboard()

