import turtle

WIDTH, HEIGHT = 500, 500

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

def init_turtle():
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.title('Turtle Racing!')


# Call the function and print the result
racers = get_number_of_racers()
init_turtle()
