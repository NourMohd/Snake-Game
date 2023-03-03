from turtle import Turtle

FORWARD_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


class Snake:
    def __init__(self):
        self.tims = []
        self.create_snake()
        self.head = self.tims[0]

    def create_snake(self):
        squares = []

        x = 0
        for _ in range(3):
            tim = Turtle("square")
            tim.color("yellow")
            tim.speed("fastest")
            tim.penup()
            tim.setx(x)
            x -= 20
            self.tims.append(tim)

    def extend(self):
        new_turtle = Turtle("square")
        new_turtle.color("yellow")
        new_turtle.penup()
        new_turtle.goto(self.tims[-1].position())
        self.tims.append(new_turtle)

    def move(self):
        for tims_num in range(len(self.tims) - 1, 0, -1):
            new_x = self.tims[tims_num - 1].xcor()
            new_y = self.tims[tims_num - 1].ycor()
            self.tims[tims_num].goto(new_x, new_y)
        self.tims[0].forward(FORWARD_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def wall_coll_check(self):
        if self.head.xcor() > 290 or self.head.xcor() < -290 or self.head.ycor() > 290 or self.head.ycor() < -290:
            return 1

    def tail_collision_check(self):
        for tim in self.tims[1:]:
            if self.head.distance(tim) < 12:
                return 1
