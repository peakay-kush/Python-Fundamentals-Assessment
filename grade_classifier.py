# Grade Classifier
# Ask the user for their test score
score = int(input("Enter your test score (0–100): "))

# Check the score range
if 80 <= score <= 100:
    print("Excellent")
elif 50 <= score <= 79:
    print("Good")
elif 0 <= score <= 49:
    print("Needs Improvement")
else:
    print("Invalid score entered.")

