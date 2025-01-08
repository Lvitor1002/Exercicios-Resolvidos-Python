'''
Sistema de Cadastro de Alunos
Crie um sistema de cadastro de alunos para uma escola, utilizando orientação a objetos. 
O sistema deve permitir ao usuário adicionar novos alunos, visualizar informações dos alunos cadastrados, como nome, idade e notas, calcular médias de notas e gerar relatórios de desempenho dos alunos.
'''
class Student:
    def __init__(self, name, age, grades):
        self.name = name
        self.age = age
        self.grades = grades

    def average_grade(self):
        return sum(self.grades) / len(self.grades)

class SchoolSystem:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def get_student_info(self, name):
        for student in self.students:
            if student.name == name:
                return f"Nome: {student.name}, Idade: {student.age}, Notas: {student.grades}"
        return "Aluno não encontrado."

    def calculate_average_grade(self, name):
        for student in self.students:
            if student.name == name:
                return student.average_grade()
        return "Aluno não encontrado."

# Exemplo de uso:
school = SchoolSystem()
student1 = Student("João", 16, [8, 9, 7])
student2 = Student("Maria", 17, [6, 7, 8])
school.add_student(student1)
school.add_student(student2)
print(school.get_student_info("João"))
print("Média de notas de João:", school.calculate_average_grade("João"))
