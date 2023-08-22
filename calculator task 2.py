
# define calculations functions 
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

print("\n\n*************** Calculator *************")
print("\n Press 1. for Add \n Press 2. for Subtract \n Press 3. for Multiply \n Press 4. for Divide")

while True:
    option = input("\nEnter Choice (1,2,3,4): ")

    if option in ('1', '2', '3', '4'):
        try:
            no1 = float(input("Enter first number: "))
            no2 = float(input("Enter second number: "))
        except ValueError:
            print("Please enter a number.")
            continue

        if option == '1':
            print(no1, "+", no2, "=", add(no1, no2))

        elif option == '2':
            print(no1, "-", no2, "=", subtract(no1, no2))

        elif option == '3':
            print(no1, "*", no2, "=", multiply(no1, no2))

        elif option == '4':
            print(no1, "/", no2, "=", divide(no1, no2))
        
        more = input("Let's do next calculation? (yes/no): ")
        if more == "no":
          break
    else:
        print("Please select valid choice")
        
