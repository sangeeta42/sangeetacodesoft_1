#Simple calculator program

#Ask the user for two numbers
num1 = float(input("Enter the first number:"))
num2 = float(input("Enter the second number:"))

#Ask the user to choose an operation 
print("choose the opratin:")
print("1. Addition(+)")
print("2. Subtraction(-)")
print("3. Multiplication(*)")
print("4. division(/)")

choise = input ("enter the your choise  (1/2/3/4):")

#perform the chosen operation 
if choise == '1':
   result = num1 + num2
   print("Result:", result) 
   
elif choise == '2':
     result = num1 - num2 
     print("Result:", result)
   
elif choise == '3':
     result = num1 * num2
     print("Result:", result)

elif choise == '4':
     if num2 != 0:
          result = num1 / num2 
          print("Result:", result) 
else: 
    print("Invalid input")  