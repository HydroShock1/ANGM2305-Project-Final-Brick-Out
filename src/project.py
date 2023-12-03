# Beginning of Code
# Extreme Brick Out

# Import required library
import turtle

# Create screen
sc = turtle.Screen()
sc.title("Extreme Brick Out")
sc.bgcolor("white")
sc.setup(width=600, height=900)

# The bouncing ball
hit_ball = turtle.Turtle()
hit_ball.speed(40)
hit_ball.shape("circle")
hit_ball.color("blue")
hit_ball.penup()
hit_ball.goto(0, 0)
hit_ball.dx = 5
hit_ball.dy = -5

# paddle bar to keep battle from hitting the bottom
paddle_bar = turtle.Turtle()
paddle_bar.speed(0)
paddle_bar.shape("square")
paddle_bar.color("black")
paddle_bar.shapesize(stretch_wid=2, stretch_len=6)
paddle_bar.penup()
paddle_bar.goto(0, -340)


# Moving the paddle left and right
def paddleright():
    x = paddle_bar.xcor()
    x += 20
    paddle_bar.setx(x)
 
 
def paddleleft():
    x = paddle_bar.xcor()
    x -= 20
    paddle_bar.setx(x)
	
# Keyboard inputs
sc.listen()
sc.onkeypress(paddleright, "Right")
sc.onkeypress(paddleleft, "Left")
 
# The interactivity between the ball and the borders
while True:
	sc.update()

	hit_ball.setx(hit_ball.xcor()+hit_ball.dx)
	hit_ball.sety(hit_ball.ycor()+hit_ball.dy)
	
	# Bouncing off borders
	if hit_ball.ycor() > 445:
		hit_ball.sety(445)
		hit_ball.dy *= -1

	if hit_ball.ycor() < -445:
		hit_ball.goto(0, 0)
		hit_ball.dy *= -1
		
	if hit_ball.xcor() > 280:
		hit_ball.setx(280)
		hit_ball.dx *= -1

	if hit_ball.xcor() < -280:
		hit_ball.setx(-280)
		hit_ball.dx *= -1


