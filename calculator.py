# Ask the user to enter the first number
num1 = float(input("Enter the first number: "))

# Ask the user to enter the second number
num2 =float(input("Enter the second number:"))

# Ask the user to enter the operation
operator = input("Enter an operator (+, -, *, /) :")
# Check which operation the user chose
if operator == "+":
   result =num1 + num2

elif operator == "-":
    result =num1 - num2

elif operator == "*":
    result = num1 * num2

elif operator == "/":
    result = num1 / num2

else:
    result = "invalid operator"

print("result:", result) 

