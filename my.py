num1 = float(input("enter the first number :"))
operator = input("enter an operator(+,-,*,/,)")
num2 = float(input("Enter the second number:"))
if operator =='+':
    result = num1 + num2
    print(f"{num1}+{num2} = {result}")
    elif operator =='-':
        result = num1-num2
        print(f"{num1}-{num2} = {result}")
        elif operator == '*':
            result = num1 * num2
            print(f"{num1}*{num2}={result}")
  if operator =='/':
                result = num1/num2
                print(f"{num1}/{num2}={result}")
            else:
                print("Error:Division by zero is not allowed.")
            else:
print("invalid operator.Please use +,-,* or /.")