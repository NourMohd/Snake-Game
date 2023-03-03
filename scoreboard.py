from turtle import Turtle



class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(0,270)
        with open("data.txt", "r") as file:
            self.high_score = int(file.read())
        self.score = 0
        self.update_scoreboard()

    def refresh(self):
        if self.score > self.high_score:
            self.high_score = self.score
            new_score = str(self.score)
            with open("data.txt", "w") as file:
                file.write(new_score)
        self.update_scoreboard()


    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} , High Score = {self.high_score}", False, "center",
                   font=('Arial', 18, 'normal'))


    def add_point(self):
        self.score += 1
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", False, "center", font=('Arial', 18, 'normal'))

    def difficulty(self, difficulty):
        if difficulty == 'easy':
            return 0.09
        elif difficulty == 'medium':
            return 0.07
        elif difficulty == 'hard':
            return 0.05
        else:
            return 0

