# Program to check the largest number among 3

num1 = float(input("Enter the first number:"))

num2 = float(input("Enter the second number:"))

num3 = float(input("Enter the third number"))

if (num1 > num2) and (num1 > num3):
    print(num1, "is the greatest among 3 numbers.")

elif(num2 > num1) and (num2 > num3):
    print(num2,"is the greatest nummber among 3 numbers.")

else:
    print(num3, "is the greatest number among 3 numbers.") 