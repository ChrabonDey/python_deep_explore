# age=int(input("Enter your age: "))

# def check_age(age):
#     if age < 18:
#         print("You are a minor.")
#     elif age >= 18 and age < 65:
#         print("You are an adult.")
#     else:
#         print("You are a senior citizen.")
    
# check_age(age) # this will call the function and pass the age variable to it.


#2.
def discount_in_ticket_price(age,price,day):
    if day != "wednesday":
        print("No discount available")
    else:
        if age<18:
            discount=price-(0.5*price)
            print(f"You got a discount of 50%. Your ticket price after discount is: {discount}")
        elif age>=18 and age<65:
            discount=price-(0.2*price);
            print(f"You got a discount of 20%. Your ticket price after discount is: {discount}")
        else:
            print("No discount available for senior citizens.")
            
            
# age=int(input("Enter your age:"))
# price=float(input("Enter the ticket price:"))
# day=input("Enter the day of the week:").lower()
# discount_in_ticket_price(age,price,day)


#3 loop problem solve it using for loop and while loop

x=[1,2,3,4,5,6,6,7,-1,3,4,5]
count=0

for i in x:
    if i>0:
        count+=1
    
print(f"The number of positive integers in the list is: {count}")


