from turtle import Screen
from snake import Snake
from food import Food
import time
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=400, height=400)
screen.bgcolor("black")
screen.title("SSSnake")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()
t_count = 0.05
screen.listen()
screen.onkeypress(snake.up, "Up")
screen.onkeypress(snake.down, "Down")
screen.onkeypress(snake.left, "Left")
screen.onkeypress(snake.right, "Right")
game_on = True
scoreboard.write_score()
while game_on:
    screen.update()
    time.sleep(t_count)

    snake.move()

    if snake.head.distance(food) < 20:
        food.refresh()
        snake.extend()
        scoreboard.write_score()
        t_count = t_count - 0.001

    if snake.head.xcor() > 185 or snake.head.xcor() < -185 or snake.head.ycor() > 185 or snake.head.ycor() < -185:
        # game_on = False
        scoreboard.reset()
        snake.reset()
        t_count = 0.05

    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            # game_on = False
            scoreboard.reset()
            snake.reset()
            t_count = 0.05


screen.exitonclick()
