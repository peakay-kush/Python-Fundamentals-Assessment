user_input = input("Enter any value: ")

# Try to detect type
# First, check if it's an integer
if user_input.isdigit():
    value = int(user_input)
    print(f"You entered: {value}")
    print("Data type: int")

# Check if it's a float (contains a decimal)
elif "." in user_input and user_input.replace(".", "").isdigit():
    value = float(user_input)
    print(f"You entered: {value}")
    print("Data type: float")

# Otherwise, treat as string
else:
    print(f"You entered: {user_input}")
    print("Data type: str")

