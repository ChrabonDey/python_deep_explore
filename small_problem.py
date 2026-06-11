age=int(input("Enter your age: "))

def check_age(age):
    if age < 18:
        print("You are a minor.")
    elif age >= 18 and age < 65:
        print("You are an adult.")
    else:
        print("You are a senior citizen.")
    
check_age(age) # this will call the function and pass the age variable to it.

