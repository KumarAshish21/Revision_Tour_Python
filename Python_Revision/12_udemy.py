name = "Bob"
greeting = "Hello, {}"

with_name = greeting.format(name)
with_name_two = greeting.format("Rolf")
print(with_name)
print(with_name_two)

user_age = input("Enter your age: ")
years = int(user_age)

months = years * 12

print(f"Your age, {years}, is equal to {months} months.")

l = ["Bob","Rolf","Anne"]

t = ("Bob","Rolf","Anne")

friends = {"Bob","Rolf","Anne"}
abroad = {"Bob","Rolf"}

local_friends = friends.difference(abroad)
print(local_friends)

set1 = {14, 5, 9, 31, 12, 77, 67, 8}
set2 = {5}
print(set2.intersection(set1))

number = 7

user_input = input("Enter 'y' if you would like to play: ").lower()

if user_input == "y":
    user_number = int(input("Guess our number: "))
    if user_input == number:
        print("You guessed correctly!")
    elif abs(number - user_number) == 1:
        print("You were off by one.")
    else:
        print("Sorry, it's woong!")

