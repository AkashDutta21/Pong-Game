import turtle

# Create a window
wn = turtle.Screen()
wn.title("Pong by @itz_akashdutta")
wn.bgcolor("black")
wn.setup(height=600, width=800)
wn.tracer(0) #set the screen update to 0


# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0) # Set the animation speed of paddle A to max speed ---> It will otherwise be very slow
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.penup()
paddle_a.goto(-350, 0)

# Paddle B

# Ball


# Main Game Loop
while True:
    wn.update()
