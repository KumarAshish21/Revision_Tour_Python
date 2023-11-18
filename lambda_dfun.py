# Dictionaries and students
# This coding exercise has three parts. See them outlined in detail in the coding exercise, as comments.

# Create a dictionary variable, called student .

# Modify a variable, grades , so it contains the value of a dictionary's key.

# Implement a function calculating a total average grade for a class of students.
# Create a variable called student, with a dictionary.
# The dictionary must contain three keys: 'name', 'school', and 'grades'.
# The values for each must be 'Jose', 'Computing', and a tuple with the values 66, 77, and 88.
student = {'name': 'Jose', 'school': 'Computing', 'grades': (66, 77, 88)}

# Assume the argument, data, is a dictionary.
# Modify the grades variable so it accesses the 'grades' key of the data dictionary.
def average_grade(data):
    grades = data['grades']
    return sum(grades) / len(grades)


# Implement the function below
# Given a list of students (a list of dictionaries), calculate the average grade received on an exam, for the entire class
# You must add all the grades of all the students together
# You must also count how many grades there are in total in the entire list
def average_grade_all_students(student_list):
    total = 0
    count = 0
    # for student in student_list:
    #     if 'grades' in student:
    #         for grade in student['grades']:
    #             total = total+grade
    #             count += 1
    #     if count == 0:
    #         return 0
    for student in student_list:
        total += sum(student['grades'])
        count += len(student['grades'])

    return total / count

students = [
    {'name': 'Alice', 'school': 'Engineering', 'grades': (90, 85, 88)},
    {'name': 'Bob', 'school': 'Science', 'grades': (78, 92, 89)},
    # Add more students as needed
]

average = average_grade_all_students(students)
print(f"Average grade for all students: {average}")