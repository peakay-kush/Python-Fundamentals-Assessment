myFamily = {
    "father": {"name": "steve", "year": 1978},
    "mother": {"name": "nancy", "year": 1976}
}

member = input("Enter a family member (father/mother): ").lower()

if member in myFamily:
    name = myFamily[member]["name"]
    year = myFamily[member]["year"]
    print(f"{member.title()}'s name is {name} and was born in {year}.")
else:
    print("Family member not found.")

