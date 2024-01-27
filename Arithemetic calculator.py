while True:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operator = input("Enter the operator (+, -, *, /)= ")
    add = num1 + num2
    sub = num1 - num2
    multiply = num1 * num2
    Divide = num1 / num2
    if operator == '+':
        print(add)
    elif operator == '-':
        print(sub)
    elif operator == '*':
        print(multiply)
    elif operator == '/':
        print(Divide)
    else:
        print("Invalid operator.")
        continue
    user = input("Do you want to continue ? (yes/no): ")
    if user == 'no':
        print("Exiting")
        break
    if user == 'yes':
        continue
    else:
        print("invalid input")
        break
