#Baffert Alexander 4M
#classi
class Student:
    def __init__(self, nome, cognome, genere, eta):
        self.nome = nome
        self.cognome = cognome
        self.genere = genere
        self.eta = eta

class Aula:
    def __init__(self, id, school_name, descrizione):
        self.id = id
        self.school_name = school_name
        self.descrizione = descrizione
        self.student_list = []  

    def aggiungi_student(self, student_list):
        self.student_list.append(student_list)

    def rimuovi_student(self, student_list):
        if student_list in self.student_list:
            self.student_list.remove(student_list)
        else:
            print(f"{student_list.nome} {student_list.cognome} non è presente nella classe.")

    def conta_student_list_iscritti(self):
        return len(self.student_list)

#Main
student1 = Student("Matteo", "R", "M", 16)
student2 = Student("Mario", "B", "M", 17)
aula1 = Aula("4M", "IsissGobetti", "informatica")
#aggiunta studenti e rimozzione di essi
aula1.aggiungi_student(student1)
aula1.aggiungi_student(student2)
print("Numero di studenti iscritti nel corso sono:", aula1.conta_student_list_iscritti())
aula1.rimuovi_student(student2)
print("Numero di studenti iscritti dopo la rimozione:", aula1.conta_student_list_iscritti())