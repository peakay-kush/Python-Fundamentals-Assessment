user_profile = {
    "name": "Peter Kuria",
    "email": "peakaykush@gmail.com",
    "verified": False
}

# Ask user for verification status
verify = input("Has the user verified their account? (yes/no): ").lower()

# Check response
if verify == "yes":
    user_profile["verified"] = True
    print("Updated profile:", user_profile)
else:
    print("Verification pending.")

