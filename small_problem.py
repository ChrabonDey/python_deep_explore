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
        if i==5:
            continue
        count+=1
    
# print(f"The number of positive integers in the list is: {count}")


# reverse the string using loop

# te=input("Enter a string: ")
# reversed_st=""
# # for i in range(len(te)-1,-1,-1):
# #      reversed_st=reversed_st + te[i]
# #      print(i,te[i])
# # print(f"The reversed string is: {reversed_st}")

#3 find the first non-repeated character in a string

input_str="HCraobn"

freq = {}

for char in input_str:
    freq[char] = freq.get(char, 0) + 1

non_repeated = []

for char in input_str:
    if freq[char] == 1:
        non_repeated.append(char)
        if len(non_repeated) == 2:
            break

# print(non_repeated[1] if len(non_repeated) > 1 else None)

#factorial Number

def factorial_number(n):
    if n==0 or n==1:
        return 1
    else:
        return n*factorial_number(n-1)
    
# number=int(input("Enter a number to find its factorial: "))

# print(f"The factorial of {number} is:{factorial_number(number)}")

#factorial using while loop
# def factorial_number_while(n):
#     result=1
#     while n>0:
#         result*=n
#         n-=1
        
#     return result

# print(f"The factorial of {number} is:{factorial_number_while(number)}")

number=29

is_prime=True


if number > 1:
    for i in range(2, number):
        if (number % i) ==0:
            is_prime=False
            break
    
    
    
    
        


            
            
           

