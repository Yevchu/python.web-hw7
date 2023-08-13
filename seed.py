from connect_db import session
from models import Student, Teacher, Grade, Group, Subject

from random import randint, choice

import faker

STUDENTS = 50
TEACHERS = 5
GROUPS = ["Group A", "Group B", "Group C"]
SUBJECTS = ["Mathematics", "Physics", "Chemistry", "Biology", "History", "Geography", "English"]
fake = faker.Faker()

def insert_data_to_db():
    with session as s:

        groups = []
        for _ in range(1, 4):
            g = Group(name=choice(GROUPS))
            groups.append(g)

        students = []
        for _ in range(STUDENTS):
            st = Student(name=fake.name(), group_id=randint(1, 3), group=choice(groups))
            students.append(st)
        
        teachers = []
        for _ in range(TEACHERS + 1):
            t = Teacher(name=fake.name())
            teachers.append(t)

        subjects = []
        for _ in range(len(SUBJECTS)):
            sub = Subject(name=choice(SUBJECTS), teacher_id=randint(1,5), teacher=choice(teachers), group_id=randint(1, 3))
            subjects.append(sub)

        for student in students:
            for subject in subjects:
                gr = Grade(
                    grade = randint(10, 100),
                    student = student,
                    subject = subject
                )

    s.add_all([g, t, sub, st, gr])
    s.commit()


if __name__ == "__main__":
    insert_data_to_db()
    