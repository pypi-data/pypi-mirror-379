import turtle
import time

def run_pong_game():
    """Runs the single-player Pong game."""
    # Set up the screen
    screen = turtle.Screen()
    screen.title("Single Player Pong")
    screen.bgcolor("black")
    screen.setup(width=600, height=600)
    screen.tracer(0)

    # Paddle
    paddle = turtle.Turtle()
    paddle.speed(0)
    paddle.shape("square")
    paddle.color("white")
    paddle.shapesize(stretch_wid=1, stretch_len=5)
    paddle.penup()
    paddle.goto(0, -250)

    # Ball
    ball = turtle.Turtle()
    ball.speed(0)
    ball.shape("circle")
    ball.color("white")
    ball.penup()
    ball.goto(0, 100)
    # Adjusted initial speed to be even slower for a more comfortable start
    ball.dx = 0.2
    ball.dy = -0.2

    # Score
    score = 0

    # Scoreboard
    pen = turtle.Turtle()
    pen.speed(0)
    pen.shape("square")
    pen.color("white")
    pen.penup()
    pen.hideturtle()
    pen.goto(0, 260)
    pen.write("Score: 0", align="center", font=("Courier", 24, "normal"))

    # Function to move the paddle
    def paddle_right():
        x = paddle.xcor()
        if x < 240:
            x += 20
            paddle.setx(x)

    def paddle_left():
        x = paddle.xcor()
        if x > -240:
            x -= 20
            paddle.setx(x)

    # Function to increase the ball's speed gradually
    def increase_speed():
        nonlocal ball
        # Reduced speed increase to prevent it from getting too fast too quickly
        ball.dx *= 1.007
        ball.dy *= 1.007

    # Keyboard bindings
    screen.listen()
    screen.onkeypress(paddle_right, "Right")
    screen.onkeypress(paddle_left, "Left")

    # Main game loop
    while True:
        screen.update()

        # Move the ball along both x and y axes
        ball.setx(ball.xcor() + ball.dx)
        ball.sety(ball.ycor() + ball.dy)

        # Border checking
        if ball.xcor() > 290 or ball.xcor() < -290:
            ball.dx *= -1
            
        if ball.ycor() > 290:
            ball.dy *= -1
            
        # Paddle and ball collision
        if (ball.dy < 0) and (ball.ycor() > -250) and (ball.ycor() < -240) and (abs(ball.xcor() - paddle.xcor()) < 50):
            ball.dy *= -1
            score += 1
            increase_speed()
            pen.clear()
            pen.write("Score: {}".format(score), align="center", font=("Courier", 24, "normal"))
            
        # Game over
        if ball.ycor() < -280:
            # Clear everything on the screen and write the Game Over message
            # ball.hideturtle()
            # paddle.hideturtle()
            # pen.clear()

            # Write "GAME OVER" text
            pen.goto(0, 50)
            pen.write("GAME OVER", align="center", font=("Courier", 40, "normal"))
            
            # Write final score
            pen.goto(0, -50)
            pen.write("Final Score: {}".format(score), align="center", font=("Courier", 24, "normal"))
            
            # This line keeps the window open long enough to show the message
            screen.update()
            time.sleep(3)
            # Now safely break the loop
            break

    screen.bye()

# Run the game
# if __name__ == "__main__":
#     run_pong_game()