# Sample list of 7 random integers
numbers = [4, 15, 8, 23, 7, 12, 19]

# Counter for numbers greater than 10
count = 0

# Loop through numbers
for num in numbers:
    if num <= 10:
        continue  # Skip numbers less than or equal to 10
    print(f"Number greater than 10: {num}")
    count += 1

# Print total count
print(f"Total numbers greater than 10: {count}")

