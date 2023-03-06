#CS-175L-02
#Peter Parrella
#AverageFromInput

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

total = num1 + num2 + num3
average = total / 3

print(f"I read in  1 number(s) Current number is: {num1:8.2f} Total is: {num1:8.2f}")
print(f"I read in  2 number(s) Current number is: {num2:8.2f} Total is: {num1+num2:8.2f}")
print(f"I read in  3 number(s) Current number is: {num3:8.2f} Total is: {total:8.2f}")
print(f"Average: {average:8.1f}")
