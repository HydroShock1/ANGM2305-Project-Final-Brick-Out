# Beginning of Code
# Extreme Brick Out

# Import required library
import turtle
import time
import random

def main():
    # Instances of the classes
    game_screen = GameScreen()
    ball = Ball()
    paddle = PaddleBar()

    # Keyboard inputs
    game_screen.screen.listen()
    game_screen.screen.onkeypress(paddle.move_right, "Right")
    game_screen.screen.onkeypress(paddle.move_left, "Left")

    # Initialize Score
    current_score = 0

    # Display Score
    score_display = turtle.Turtle()
    score_display.speed(0)
    score_display.color("black")
    score_display.penup()
    score_display.hideturtle()
    score_display.goto(-220, 420)
    score_display.write("High Score : {}".format(current_score), align="center", font=("Calibri", 18, "normal"))

    # Spawn Breakable Blocks
    breakable_blocks = []
    for _ in range(5):
        x = random.randint(-200, 200)
        y = random.randint(100, 300)
        block = BreakableBlock(x, y)
        breakable_blocks.append(block)

    # The interactivity between the ball and the borders
    while current_timer >= 0:
        start_time = time.time()

        game_screen.screen.update()

        ball.ball.setx(ball.ball.xcor() + ball.ball.dx)
        ball.ball.sety(ball.ball.ycor() + ball.ball.dy)

        # Bouncing off borders
        if ball.ball.ycor() > 445:
            ball.ball.sety(445)
            ball.ball.dy *= -1

        if ball.ball.ycor() < -445:
            ball.ball.goto(0, 0)
            ball.ball.dy *= -1
            current_score -= 1
            score_display.clear()
            score_display.write("High Score : {}".format(current_score), align="center", font=("Calibri", 18, "normal"))

        if ball.ball.xcor() > 280:
            ball.ball.setx(280)
            ball.ball.dx *= -1

        if ball.ball.xcor() < -280:
            ball.ball.setx(-280)
            ball.ball.dx *= -1

        # Paddle Bar Collision
        if (-350 < ball.ball.ycor() < -330 and paddle.paddle.xcor() -60 < 
            ball.ball.xcor() < paddle.paddle.xcor() + 60):
            ball.ball.sety(-330)
            ball.ball.dy *= -1

        # Check collisions of breakable blocks
        for block in breakable_blocks:
            if (block.block.ycor() + 10 > ball.ball.ycor() > block.block.ycor() - 10 and
                    block.block.xcor() - 50 < ball.ball.xcor() < block.block.xcor() + 50):
                block.respawn()
                ball.ball.dy *= -1
                current_score += 1
                score_display.clear()
                score_display.write("High Score: {}".format(current_score), align="center", font=("Calibri", 18, "normal"))

        # Elapsed Time with delay
        elapsed_time = time.time() - start_time
        time.sleep(max(0, 0.01 - elapsed_time)) 


# Update time accordingly until timer reaches zero
def update_timer():
    global current_timer
    timer_display.clear()
    timer_display.write("Time: {}s".format(current_timer), align="center", font=("Calibri", 18, "normal"))
    current_timer -= 1
    if current_timer > 0:
        turtle.ontimer(update_timer, 1000)
    else:
        game_over_display = turtle.Turtle()
        game_over_display.speed(0)
        game_over_display.color("red")
        game_over_display.penup()
        game_over_display.hideturtle()
        game_over_display.goto(0, 0)
        game_over_display.write("GAME OVER", align="center", font=("Calibri", 24, "normal"))
        time.sleep(5)
        turtle.bye()  # Closes Game

# Create Screen
class GameScreen:
    def __init__(self):
        self.screen = turtle.Screen()
        self.screen.title("Extreme Brick Out")
        self.screen.bgcolor("white")
        self.screen.setup(width=600, height=900)

# Create Breakable Blocks
class BreakableBlock:
    def __init__(self, x, y):
        self.block = turtle.Turtle()
        self.block.speed(0)
        self.block.shape("square")
        self.block.color("green")
        self.block.shapesize(stretch_wid=3, stretch_len=3)
        self.block.penup()
        self.block.goto(x, y)

    # After block breaks, spawn a new one in a random place
    def respawn(self):
        x = random.randint(-200, 200)
        y = random.randint(100, 300)
        self.block.goto(x, y)
        self.block.showturtle()

# The bouncing ball
class Ball:
    def __init__(self):
        self.ball = turtle.Turtle()
        self.ball.speed(40)
        self.ball.shape("circle")
        self.ball.color("blue")
        self.ball.penup()
        self.ball.goto(0, 0)
        self.ball.dx = 5
        self.ball.dy = -5

# Paddle Bar to keep ball from hitting the bottom
class PaddleBar:
    def __init__(self):
        self.paddle = turtle.Turtle()
        self.paddle.speed(0)
        self.paddle.shape("square")
        self.paddle.color("black")
        self.paddle.shapesize(stretch_wid=1, stretch_len=5)
        self.paddle.penup()
        self.paddle.goto(0, -340)

    # Moving the paddle left and right
    def move_right(self):
        x = self.paddle.xcor()
        x += 20
        self.paddle.setx(x)

    def move_left(self):
        x = self.paddle.xcor()
        x -= 20
        self.paddle.setx(x)

    

if __name__ == "__main__":

    # Initialize Timer
    current_timer = 60

    # Display Timer
    timer_display = turtle.Turtle()
    timer_display.speed(0)
    timer_display.color("black")
    timer_display.penup()
    timer_display.hideturtle()
    timer_display.goto(220, 420)
    timer_display.write("Time: {}s".format(current_timer), align="center", font=("Calibri", 18, "normal"))

    # Update Timer
    turtle.ontimer(update_timer, 1000)

    main()
        
