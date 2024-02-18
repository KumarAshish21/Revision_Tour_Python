# Data Types: int, float, str, bool
"""
Object Types / Data Types
• Number: 1234, 3.1415, 3+4j, 0b111, Decimal, FractionO
• String : 'spam', "Bob's", b'alx01c', u'sp|xc4m'
• List: [1, [2, 'three'], 4.5], list(range(10))
• Tuple: (1, 'spam', 4, 'U'), tuple('spam'), namedtuple
• Dictionary : {'food': 'spam', 'taste': 'yum'}, dict(hours=10)
• Set : set('abc'), {'a', 'b', 'c'}
• File : open('eggs.txt'), open(r'C:\ham.bin', 'wb')
• Boolgan: True, False
• None : None
• Funtions, modules, classes
• Advance: Decorators, Generators, Iterators, MetaProgramming
"""

# Python Internal Working
# Python is a dynamically typed language, which means that you don't have to declare the type of the variable when you declare it.

# # . Age Group Categorization
# age = int(input("Enter your age: "))
#
# if age < 13:
#     print("You are a child")
# elif age < 13 or age <= 20:
#     print("You are a teenager")
# elif age >20  and age < 50:
#     print("You are an adult")
# else:
#     print("You are a Senior Citizen")

# 72. Movie Ticket Pricing
# Problem: Movie tickets are priced based on age: $12 for adults (18 and over),
# $8 for children. Everyone gets a $2 discount on Wednesday.

# age = int(input("Enter your age: "))
# day = "Wednesday"
# price = 12 if age >= 18 else 8
# if day == "Wednesday":
#     price -= 2
# print(f"Your ticket price is: ${price}")

# 73. Grade Calculator
# Problem: Assign a letter grade based on a student's score: A (90-100), B (80-89),
# C (70-79), D (60-69), F (below 60).

# score = int(input("Enter your score: "))
#
# if score >= 101:
#     print("Please Varify your score")
#     exit()
#
# if score >= 90:
#     grade = "A"
# elif score >= 80 and score <= 89:
#     grade = "B"
# elif score >= 70 and score <= 79:
#     grade = "C"
#
# elif score >= 60 and score <= 69:
#     grade = "D"
# else:
#     grade = "F"
#
# print(f"Your grade is: {grade}")


# Fruit Ripeness Checker
# Problem: Determine if a fruit is ripe, overripe, or unripe based on its color.
# (e.g., Banana: Green - Unripe,
# Yellow - Ripe, Brown - Overripe)

# fruit = input("Enter the fruit: ")
# color = input("Enter the color: ")
#
# if fruit == "Banana":
#     if color == "Green":
#         print("The Banana is Unripe")
#     elif color == "Yellow":
#         print("The Banana is Ripe")
#     elif color == "Brown":
#         print("The Banana is Overripe")
#     else:
#         print("The Banana is not yet ripe")
# else:
#     print("The fruit is not a Banana")

# Weather Activity Suggestion
# Problem: Suggest an activity based on the weather
# (e.g., Sunny - Go for a walk, Rainy - Read a book,
# Snowy - Build a snowman).

# whether = input("Enter the whether: ")
#
# if whether == "Sunny":
#     print("Go for a walk")
# elif whether == "Rainy":
#     print("Read a book")
# elif whether == "Snowy":
#     print("Build a snowman")
# else:
#     print("Stay at home")

# Transportation Mode Selection
# Problem: Choose a mode of transportation based on the distance
# (e.g., <3m: Walk, 3-15 km: Bike, >15 km: Car).

# distance = float(input("Enter the distance: "))
#
# if distance < 3:
#     print("Walk")
# elif distance >= 3 and distance <= 15:
#     print("Bike")
# elif distance > 15:
#     print("Car")
# else:
#     print("Stay at home")

# Coffee Customization
# Problem: Customize a coffee order: "Small", "Medium", or "Large" with
# an option for "Extra shot" of
# espresso.

# size = input("Enter the size of the coffee: ")
# extra_shot = input("Do you want an extra shot? (yes/no): ")
#
# if extra_shot:
#     extra_shot = True
#     coffee =  size + "coffee with an extra shot"
# else:
#     coffee = size + "coffee"
# print(f"Your order is: {coffee}")

# Password Strength Checker
# Problem: Check if a password is "Weak", "Medium", or "Strong". Criteria: < 6 chars (Weak), 6-10 chars
# (Medium), >10 chars (Strong).

# password = input("Enter the password: ")
# length = len(password)
# if length > 10:
#     print("Please enter a password less than 10 characters.")
#     exit()
# if length < 6:
#     strength = "Weak"
# elif length >= 6 and length <= 10:
#     strength = "Medium"
# else:
#     strength = "Strong"
# print(f"Your password is: {strength}")

