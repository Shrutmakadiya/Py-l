"""# 1. Age Group Categorization (child, teenager, adult, senior)"""
# age = int(input("Enter Your Age : "))

# if(age < 13):
#     print("Child")
# elif(age < 20):
#     print("Teenager")
# elif(age < 60):
#     print("Adult")
# else:
#     print("Senior")


"""2. Movie Ticket Pricing
   Problem: Movie tickets are priced based on age: $12 for adults (18 and over), $8 for children.Everyone gets a $2 discount on Wednesday.
"""
# age = int(input("Enter Your Age : "))
# day = input("Enter a day : ")

# price = 12 if age >= 18 else 8

# if day == 'wednesday':
#     price -= 2

# print("Ticket price for you is $",price)


"""
Grade Calculator
Problem: Assign a letter grade based on a student's score: A (90-100), B (80-89), C (70-79), D (60-69), F (below 60).
"""
# score = int(input("Enter Your Score : "))

# if score >= 101:
#     print("Please verify your grade again")
#     exit()

# if score >= 90:
#     grade = "A"
# elif score >= 80:
#     grade = "B"
# elif score >= 70:
#     grade = "C"
# elif score >= 60:
#     grade = "D"
# else:
#     grade = "F"

# print("Grade: ", grade)


"""
4.Fruit Ripeness Checker
Problem: Determine if a fruit is ripe, overripe, or unripe based on its color. (e.g., Banana: Green - Unripe, Yellow - Ripe, Brown - Overripe).
"""
# fruit = "Banana"
# color = "Yellow"

# if fruit == "Banana":
#     if color == "Green":
#         print("Unripe")
#     elif color == "Yellow":
#         print("Ripe")
#     elif color == "Brown":
#         print("OverRipe")


"""
5.Weather Activity Suggestion
"""
# weather = "Sunny"

# if weather == "Sunny":
#     activity = "Go for a walk"
# elif weather == "Rainy":
#     activity = "Read a book"
# elif weather == "Snowy":
#     activity = "Build a snowman"

# print(activity)


"""
6.Transportation Mode Selection
Problem: Choose a mode of transportation based on the distance (e.g., <3 km: Walk, 3-15 km: Bike, >15 km: Car).
"""
# distance = 5

# if distance < 3:
#     transport = "Walk"
# elif distance <= 15:
#     transport = "Bike"
# else:
#     transport = "Car"

# print("AI recommends you the transport of: ", transport)


"""
7. Coffee Customization
Problem: Customize a coffee order: "Small", "Medium", or "Large" with an option for "Extra shot" of espresso.
"""
# order_size = input("coffee size (Small, Medium , Large) : ")
# extra_shot = input("Extra Shot (true, false) : ")

# if extra_shot:
#     coffee = order_size + " coffee with an extra shot"
# else:
#     coffee = order_size + " coffee"

# print("Order: ", coffee)


"""
8. Password Strength Checker
Problem: Check if a password is "Weak", "Medium", or "Strong". Criteria: < 6 chars (Weak), 6-10 chars (Medium), >10 chars (Strong).
"""
# password = input("Enter Password : ")
# password_length = len(password)

# if len(password) < 6:
#     strength = "Weak"
# elif len(password) <= 10:
#     strength = "Medium"
# else:
#     strength = "Strong"

# print("Password strength is: ", strength)


"""
9.Leap Year Checker
"""
# year = input("Enter Year : ")

# if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
#     print(year, " is a leap year")
# else:
#     print(year, "is NOT a leap year")


"""
10.Pet Food Recommendation
Problem: Recommend a type of pet food based on the pet's species and age. (e.g., Dog: <2 years - Puppy food, Cat: >5 years - Senior cat food).
"""
# animal = input("Enter animal (dog, cat) : ")
# age = int(input("age of animal (Year) :"))

# if (animal == 'dog'):
#     if(age < 2):
#         print("Puppy food")
#     else:
#         print("Adult food")
# elif (animal == 'cat'):
#     if(age > 5):
#         print("Senior cat food")
#     else:
#         print("Child cat food")
# else:
#     print("Check a valid animal")
#     exit()