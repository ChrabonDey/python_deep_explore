
def multiplication(n):
     i=1
     while i<=10:
         print(f"{n}*{i}={n*i}")
         i+=1
     else:
         print("This is the multiplication")


n=int(input("Enter the number which you want to see multiplication: "))

multiplication(n)