# Beginning of Code
# Extreme Brick Out

# Import required library
import turtle

# Create Screen
class GameScreen:
    def __init__(self):
        self.screen = turtle.Screen()
        self.screen.title("Extreme Brick Out")
        self.screen.bgcolor("white")
        self.screen.setup(width=600, height=900)

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
sketch = turtle.Turtle()
sketch.speed(0)
sketch.color("black")
sketch.penup()
sketch.hideturtle()
sketch.goto(0, 0)
sketch.write("High Score : 0", align="center", font=("Calibri", 24, "normal"))

# The interactivity between the ball and the borders
while True:
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
        
