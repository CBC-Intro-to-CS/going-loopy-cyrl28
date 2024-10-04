# first you must declare a function
"""
def testfunc():
    fname = "Linus"
    lname = "Cyr"
    print(f"Hello, {fname} {lname}")

testfunc()
print("Hello")

def flattened_cans(name,cans):
    total_cans = 0
    for week in range(1, 53):
        total_cans = total_cans + cans
        print(f"{name} week {week} = {total_cans} cans")

flattened_cans("Linus",107)

age = int(input("What is your age: "))
def silly_age_joke(age):
    if age >= 10 and age <= 13:
        print("What is 13 + 49 + 84 + 155 + 97? A headache!")
    else:
        print("huh?")

silly_age_joke(age)


def favorite_book(title):
    print(f"One of my favorite books is {title}.")

book = input("What is your favorite book")
favorite_book(book)


def describe_pet(animal_type, pet_name):
     Display information about a pet. 
    print(f"\nI have a {animal_type}.")
    print(f"\nMy {animal_type}'s name is {pet_name.title()}")

describe_pet("dog", "John")

pet = input("What type of pet do you have: ")
name = input("What is the name of your pet: ")

describe_pet(pet, name)
"""

def get_formatted_name(first_name, last_name):
    full_name = f"{first_name} {last_name}"
    return full_name.title()

while True:
    print("enter 'q' at any time to quit")
    fname = input("What is your first name: ")
    if fname == 'q':
        break
    lname = input("What is your last name: ")
    if lname == 'q':
        break

    student = get_formatted_name(fname, lname)
    print(f" Hello, {student}!")