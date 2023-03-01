import turtle

# Create a window
wn = turtle.Screen()
wn.title("Pong by @itz_akashdutta")
wn.bgcolor("black")
wn.setup(height=800, width=600)
wn.tracer(0) #set the screen update to 0


# Main Game Loop
while True:
    wn.update()
