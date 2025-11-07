colors = ["red", "green", "yellow"]
fruits = ["apple", "banana", "pear"]

# Counter for total combinations
count = 0

# Nested loops
for color in colors:
    for fruit in fruits:
        print(f"{color} : {fruit}")
        count += 1

# Print total combinations
print(f"Total combinations printed: {count}")

