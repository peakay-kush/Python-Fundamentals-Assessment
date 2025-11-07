correct_password = "peakay"
attempts = 0
max_attempts = 3

while attempts < max_attempts:
    password = input("Enter your password: ")
    
    if password == correct_password:
        print("Access granted")
        break  # Exit loop when correct
    else:
        attempts += 1
        print("Wrong password, try again")
        
    if attempts == max_attempts:
        print("Account locked.")

