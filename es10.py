#Baffert 4M Es10
#--------------------------------------

# The task is to create a Person class and two classes that inherit from it: Student and Teacher.
# In this exercise, Person is the main class and Student and Teacher are subclasses that inherit from Person.
# The introduce method is overridden in the subclasses to provide different introductions for students and teachers.

#--------------------------------------
#Class Persona
#classe generale
class Person:
    def __init__(self,name,age) -> None:
        self.name=name
        self.age=age
    def introduce():
        print(f"My name is {teacher.name}, im {teacher.age} and I teach {teacher.subject}")
#Class Student
class Student:
    def __init__(self,name, age,grade) -> None:
        super.__init__(self,name,age) 
        self.grade=grade
    def introduce():
        print(f"My name is {student.name}, im {student.age} and im in {student.grade}grade")
#Class Teacher
class Teacher:    
    def __init__(self,name, age,subject):
        super.__init__(self,name,age)
        self.subject=subject
    def introduce():
        super().introduce()
#--------------------------------------
#Main
student = Student("Tom",15,10)
print(student.introduce())
teacher = Teacher("Math")
print(teacher.introduce())