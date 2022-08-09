# Check that users enter a number that is more than zero
valid = False
while not valid:
    
    # Ask user to enter a number
    response = float(input("Enter a number: "))

    if response > 0:
        valid = True

    else: 
        print("please enter a number that is more than zero")
        print()


