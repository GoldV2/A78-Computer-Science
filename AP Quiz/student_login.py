from random import randrange

students = []
ids = []

class Student:
    def __init__(self, f_name, l_name, birth, grade, race, sex):
        self.f_name = f_name
        self.l_name = l_name
        self.birth = birth
        self.grade = grade
        self.race = race
        self.sex = sex
        self.id = False
        self.email = False


    def create_id(self):
        self.id = randrange(100000, 999999)

        while self.id in ids:
            self.id = randrange(100000, 999999)

        ids.append(self.id)
        print('Student ID was created succesfully')

    def create_email(self):
        self.email = self.f_name[0] + self.l_name[0] + str(self.id) + '@ucvts.org'
        print('Student email was created succesfully')

    def display(self):
        print(f"""
Student Name: {self.f_name} {self.l_name}
ID: {self.id}
E-mail: {self.email}
Grade: {self.grade}
Birthday: {self.birth}
Race: {self.race}
Sex: {self.sex}
""")

def create_student(f_name, l_name, birth, grade, race, sex):
    students.append(Student(f_name, l_name, birth, grade, race, sex))
    print(f'Student {f_name} {l_name} was created succesfully')

    students[-1].create_id()
    students[-1].create_email()

def delete_student(ide):
    for student in students:
        if student.id == ide:
            sure = int(input(f"Please input '1' to continue or '0' to cancel the deletion of {student.f_name} {student.l_name}\n\n>>> "))
            
            if sure == 1:
                students.remove(student)

                print(f"{student.f_name} {student.l_name} has beem deleted")
            
            else:
                print('Deletion cancelled')

        return

    print('Student ID could not be recognized')

def find_student(ide):
    for student in students:
        if student.id == ide:
            student.display()
            return

    print('Student ID could not be recognized')

def manage_students():
    action = int(input("""
Welcome to the Student Manager
Enter the corresponding number for each action
0: find student
1: create student
2: delete student\n\n>>> """))

    if action == 0:
        print('Current IDS')
        for student in students:
            print(f"{student.f_name} {student.l_name}: {student.id}")

        ide = int(input("What is the student's ID?\n\n>>> "))
        find_student(ide)

        manage_students()

    elif action == 1:
        f_name = input("Input the student's first name\n\n>>> ")
        l_name = input("Input the student's last name\n\n>>> ")
        birth = input("Input the student's birth day\n\n>>> ")
        grade = input("Input the student's grade\n\n>>> ")
        race = input("Input the student's race\n\n>>> ")
        sex = input("Input the student's sex\n\n>>> ")

        create_student(f_name, l_name, birth, grade, race, sex)

        manage_students()

    elif action == 2:
        print('Current IDS')
        for student in students:
            print(f"{student.f_name} {student.l_name}: {student.id}")

        ide = int(input('Please enter the student\'s ID\n\n>>> '))
        delete_student(ide)

        manage_students()

manage_students()