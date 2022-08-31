MOVE_DISTANCE = 20
UP = 90
RIGHT = 0
DOWN = 270
LEFT = 180

from turtle import Turtle


class Snake:
    def __init__(self):
        self.starting_segments = 3
        self.all_segments = []
        x_pos = 0

        for _ in range(self.starting_segments):
            new_seg = Turtle(shape="square")
            new_seg.color("white")
            new_seg.penup()
            new_seg.goto(x_pos, 0)
            x_pos -= 20
            self.all_segments.append(new_seg)

        self.snake_head = self.all_segments[0]
        self.snake_tail = self.all_segments[-1]

    def move(self):
        for seg_num in range(len(self.all_segments) - 1, 0, -1):
            new_x = self.all_segments[seg_num - 1].xcor()
            new_y = self.all_segments[seg_num - 1].ycor()
            self.all_segments[seg_num].goto(new_x, new_y)

        self.snake_head.forward(MOVE_DISTANCE)

    def extend(self):
        direction = self.snake_tail.heading()
        if direction == UP:
            new_seg_x = self.all_segments[-1].xcor()
            new_seg_y = self.all_segments[-1].ycor() - 20
        elif direction == DOWN:
            new_seg_x = self.all_segments[-1].xcor()
            new_seg_y = self.all_segments[-1].ycor() + 20
        elif direction == LEFT:
            new_seg_x = self.all_segments[-1].xcor() + 20
            new_seg_y = self.all_segments[-1].ycor()
        elif direction == RIGHT:
            new_seg_x = self.all_segments[-1].xcor() - 20
            new_seg_y = self.all_segments[-1].ycor()

        new_seg = Turtle(shape="square")
        new_seg.color("white")
        new_seg.penup()
        new_seg.goto(new_seg_x, new_seg_y)

        self.all_segments.append(new_seg)

    def up(self):
        if self.snake_head.heading() != DOWN:
            self.snake_head.setheading(90)

    def down(self):
        if self.snake_head.heading() != UP:
            self.snake_head.setheading(DOWN)

    def left(self):
        if self.snake_head.heading() != RIGHT:
            self.snake_head.setheading(LEFT)

    def right(self):
        if self.snake_head.heading() != LEFT:
            self.snake_head.setheading(RIGHT)

    def reset(self):
        for seg in self.all_segments:
            seg.goto(1000, 1000)
        self.all_segments.clear()
        x_pos = 0
        for _ in range(self.starting_segments):
            new_seg = Turtle(shape="square")
            new_seg.color("white")
            new_seg.penup()
            new_seg.goto(x_pos, 0)
            x_pos -= 20
            self.all_segments.append(new_seg)

        self.snake_head = self.all_segments[0]
        self.snake_tail = self.all_segments[-1]

