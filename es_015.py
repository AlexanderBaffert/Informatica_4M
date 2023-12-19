#Baffert Alexander 4M


#Inizio delle Classi
class Student:
    def __init__(self,name,surname,age,gender):
        self.name=name
        self.surname=surname
        self.age=age
        self.gender=gender
        self.course_list=[]
    def __str__(self):
        return f"Id of the Student added: Name:{self.name}| Surname:{self.surname} |Age:{self.age} |Gender:{self.gender})"
    def add_course(self,course):
        self.course_list.append(course)
        return "Course added successfully!"
    def remove_course(self,course):
        self.course_list.pop(course)
        return "Course removed successfully!"
    def enrolled_courses(self):
        return len(self.course_list)

class Course:
    def __init__(self,id,uni_name,description):
        self.id=id
        self.uni_name=uni_name
        self.description=description
        self.student_list=[]
    def __str__(self):
        for i in self.student_list:
            print(i)
    def add_student(self,student):
        self.student_list.append(student)
        student.add_course(self)
        return "Student added successfully"
    def remove_student(self,student):
        self.student_list.pop(student)
        student.remove_student(self)
        return "Student removed successfully!"
    def count_enrolled_student(self):
        return len(self.student_list)
    
#Main
studente1=Student("M","C",19,"F")
studente2=Student("D","B",30,"M")
corso1=Course("43656","Corso di Storia","Storia")
print(corso1.add_student(studente1))
print(corso1.add_student(studente2))
corso1.__str__()