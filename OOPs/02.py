class InterviewbitEmployee:
   def __init__(self, emp_name):
       self.emp_name = emp_name
       
   def introduce(self):
       print("Hello I am " + self.emp_name)
       
emp_1 = InterviewbitEmployee("Mr Employee")
print(emp_1.emp_name)
emp_1.introduce()
