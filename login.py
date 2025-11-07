# Login Simulation
# Stored credentials
stored_email = "peakaykush@gmail.com"
stored_password = "12345678"

# Ask user for input
email = input("Enter your email: ")
password = input("Enter your password: ")

# Check credentials
if email == stored_email and password == stored_password:
    print("Login successful!")
else:
    print("Invalid credentials!")

