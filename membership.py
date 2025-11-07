# List of available cars
cars = ["jeep", "suv", "sedan"]

# Ask user for a car name
car_name = input("Enter a car type: ").lower()  # convert to lowercase for consistency

# Check membership
if car_name in cars:
    print("We have that car type!")
else:
    print("Sorry, not available.")

