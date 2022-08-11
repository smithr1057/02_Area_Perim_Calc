# functions go here

# checks input is a number 
def num_check(question):
    # Check that users enter a number that is more than zero
    valid = False
    while not valid:

        error = "please enter a number that is more than zero"

        try:
        
            # Ask user to enter a number
            response = float(input(question))

            # checks number is more than zero
            if response > 0:
                return response

            # outputs error if input is invalid
            else: 
                print(error)
                print()

        except ValueError:
            print(error)


# Main routine goes here
width = num_check("Width: ")
height = num_check("Height: ")
print()
print("Width", width)
print("Height", height)
print()