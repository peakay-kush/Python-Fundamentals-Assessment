# Admission Fee Calculator
# Ask for user details
name = input("Enter your name: ")
age = int(input("Enter your age: "))

# Check age range and assign fee
if age < 12:
    fee = 100
elif 12 <= age <= 18:
    fee = 200
else:
    fee = 300

# Output the result
print(f"{name} pays {fee} KES for admission.")
