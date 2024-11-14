import turtle
import time
import random

WIDTH, HEIGHT = 500, 500
COLORS = ['red', 'green', 'blue', 'orange', 'yellow', 'black', 'purple', 'pink', 'yellow', 'brown', 'cyan']

def get_number_of_racers():
    while True:
        racers = input("Enter the number of racers (2-10): ")
        
        # Check if input is a digit
        if racers.isdigit():
            racers = int(racers)
            
            # Check if the number is within the specified range
            if 2 <= racers <= 10:
                return racers
            else:
                print("Number not in range 2-10, try again.")
        else:
            print("Input isn't a number, try again.")

def create_turtles(colors):
    turtles = []
    spacingx = WIDTH // (len(colors) + 1)
    for i, color in enumerate(colors):
        racer = turtle.Turtle()
        racer.color(color)
        racer.shape('turtle')
        racer.left(90)
        racer.penup()
        racer.setpos(-WIDTH//2 + (i + 1) * spacingx, -HEIGHT//2  + 20)
        racer.pendown()
        turtles.append(racer)

    return turtles


def init_turtle():
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.title('Turtle Racing!')


# Call the function and print the result
racers = get_number_of_racers()
init_turtle()
random.shuffle(COLORS)
colors = COLORS[:racers]
create_turtles(colors)

