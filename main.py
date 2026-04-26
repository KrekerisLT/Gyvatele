import turtle
import time
import random
import os
from abc import ABC, abstractmethod

FOLDER_PATH = os.path.dirname(os.path.realpath(__file__))
FILE_PATH = os.path.join(FOLDER_PATH, "highscore.txt")

class ScoreManager:
    """Singleton pattern užtikrina, kad žaidime būtų tik vienas taškų valdytojas."""
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(ScoreManager, cls).__new__(cls)
            cls._instance.__initialized = False
        return cls._instance

    def __init__(self):
        if not self.__initialized:
            self.__score = 0
            self.__high_score = self.__load_high_score()
            self.__initialized = True

    def __load_high_score(self):
        """Skaito iš failo (File I/O)."""
        if os.path.exists(FILE_PATH):
            with open(FILE_PATH, "r") as f:
                try:
                    return int(f.read())
                except ValueError:
                    return 0
        return 0

    def __save_high_score(self):
        """Rašo į failą (File I/O)."""
        with open(FILE_PATH, "w") as f:
            f.write(str(self.__high_score))

    def get_score(self):
        return self.__score

    def get_high_score(self):
        return self.__high_score

    def add_score(self):
        self.__score += 1
        if self.__score > self.__high_score:
            self.__high_score = self.__score
            self.__save_high_score()

    def reset_score(self):
        self.__score = 0

class GameObject(ABC):
    """Abstrakti bazinė klasė žaidimo objektams."""
    def __init__(self, shape, color):
        self.obj = turtle.Turtle()
        self.obj.speed(0)
        self.obj.shape(shape)
        self.obj.color(color)
        self.obj.penup()

    @abstractmethod
    def reset_position(self):
        """Abstraktus metodas, kurį privalo implementuoti vaikinės klasės."""
        pass


class Food(GameObject):
    def __init__(self):
        super().__init__("circle", "#E74C3C")
        self.obj.shapesize(stretch_wid=0.8, stretch_len=0.8)
        self.reset_position()

    def reset_position(self):
        x = random.randint(-14, 14) * 20
        y = random.randint(-14, 14) * 20
        self.obj.goto(x, y)


class SnakeSegment(GameObject):
    def __init__(self):
        super().__init__("square", "#2CAD62")
        self.obj.shapesize(stretch_wid=0.9, stretch_len=0.9)

    def reset_position(self):
        self.obj.goto(1000, 1000)

class Snake:
    def __init__(self):
        self.head = turtle.Turtle()
        self.head.speed(0)
        self.head.shape("square")
        self.head.color("#2ECC71")
        self.head.penup()
        self.head.goto(0, 0)
        self.__direction = "stop"
        
        self.segments = []

    def get_direction(self):
        return self.__direction

    def set_direction(self, new_dir):
        if new_dir == "up" and self.__direction != "down":
            self.__direction = "up"
        elif new_dir == "down" and self.__direction != "up":
            self.__direction = "down"
        elif new_dir == "left" and self.__direction != "right":
            self.__direction = "left"
        elif new_dir == "right" and self.__direction != "left":
            self.__direction = "right"

    def move(self):
        x, y = self.head.xcor(), self.head.ycor()
        if self.__direction == "up":
            y += 20
        elif self.__direction == "down":
            y -= 20
        elif self.__direction == "left":
            x -= 20
        elif self.__direction == "right":
            x += 20
        self.head.goto(x, y)

    def render_segments(self):
        for i in range(len(self.segments) - 1, 0, -1):
            self.segments[i].obj.goto(self.segments[i-1].obj.pos())
        if len(self.segments) > 0:
            self.segments[0].obj.goto(self.head.pos())

    def add_segment(self):
        self.segments.append(SnakeSegment())

    def reset(self):
        time.sleep(0.5)
        self.head.goto(0, 0)
        self.__direction = "stop"
        for segment in self.segments:
            segment.reset_position()
        self.segments.clear()


def draw_border():
    """Nupiešia žaidimo lauko rėmelį."""
    border_pen = turtle.Turtle()
    border_pen.speed(0)
    border_pen.color("black") 
    border_pen.penup()
    border_pen.goto(-295, -295)
    border_pen.pendown()
    border_pen.pensize(3)
    for _ in range(4):
        border_pen.forward(590)
        border_pen.left(90)
    border_pen.hideturtle()


def main():
    win = turtle.Screen()
    win.title("Gyvatėlė")
    win.bgcolor("white")
    win.setup(width=650, height=675)
    win.tracer(0)

    draw_border()

    snake = Snake()
    food = Food()
    score_manager = ScoreManager()

    pen = turtle.Turtle()
    pen.speed(0)
    pen.color("black")
    pen.penup()
    pen.hideturtle()
    pen.goto(0, 300)

    def update_scoreboard():
        pen.clear()
        pen.write(f"Taškai: {score_manager.get_score()}  Rekordas: {score_manager.get_high_score()}", 
                  align="center", font=("Courier", 24, "normal"))
    update_scoreboard()

    win.listen()
    win.onkeypress(lambda: snake.set_direction("up"), "w")
    win.onkeypress(lambda: snake.set_direction("down"), "s")
    win.onkeypress(lambda: snake.set_direction("left"), "a")
    win.onkeypress(lambda: snake.set_direction("right"), "d")

    while True:
        win.update()
        if abs(snake.head.xcor()) > 290 or abs(snake.head.ycor()) > 290:
            score_manager.reset_score()
            update_scoreboard()
            snake.reset()

        if snake.head.distance(food.obj) < 20:
            food.reset_position()
            snake.add_segment()
            score_manager.add_score()
            update_scoreboard()

        snake.render_segments()
        snake.move()

        for segment in snake.segments:
            if segment.obj.distance(snake.head) < 20:
                score_manager.reset_score()
                update_scoreboard()
                snake.reset()

        time.sleep(0.125)

if __name__ == "__main__":
    main()
