# Write a Program to input 2 numbers & print their sum.
num1 = int(input("Enter 1st number = "))
num2 = int(input("Enter 2nd number = "))
print("Your addition is =",num1+num2)

# WAP to input side of a square & print its area.
sideLength = int(input("Enter side length of square = "))
print("Your area of square is =",sideLength ** 2)

# WAP to input 2 floating point numbers & print their average.
num1 = float(input("Enter a 1st number = "))
num2 = float(input("Enter a 2nd number = "))
avg = (num1+num2)/2
print("Your average is =",avg)

#WAP to input 2 int numbers, a and b.Print True if a is greater than or equal to b. If not print False.
a = int(input("Enter number of a = "))
b = int(input("Enter number of b = "))
if(a>=b):
    print("True")
else:
    print("False")