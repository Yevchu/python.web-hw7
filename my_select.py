from connect_db import session
from models import Student, Teacher, Grade, Group, Subject
from sqlalchemy import func, desc
from seed import SUBJECTS
from random import choice, randint
import sys

def select_1():
    r = session.query(Student.name, func.round(func.avg(Grade.grade), 2).label('avg_grade'))\
        .select_from(Grade).join(Student).group_by(Student.id).order_by(desc('avg_grade')).limit(5).all()
    return r

def select_2():
    r = session.query(Student.name, Subject.name, func.round(func.avg(Grade.grade)).label('avg_grade'))\
        .select_from(Student).join(Grade).join(Subject).group_by(Student.id, Subject.id).where(Subject.name == choice(SUBJECTS)).order_by(desc('avg_grade')).limit(1).all()
    return r

def select_3():
    r = session.query(Group.name, Subject.name, func.round(func.avg(Grade.grade)).label('avg_grade'))\
        .select_from(Student).join(Group, Student.group_id == Group.id).join(Grade, Student.id == Grade.student_id).join(Subject, Grade.subject_id == Subject.id).where(Subject.name == choice(SUBJECTS)).group_by(Group.name, Subject.name).all()
    return r
def select_4():
    r = session.query(func.avg(Grade.grade).label('avg_grade'))\
        .select_from(Grade).all()
    return r

def select_5():
    r = session.query(Subject.name, Teacher.name)\
        .select_from(Subject).join(Teacher, Subject.teacher_id == Teacher.id).where(Teacher.name == Teacher.name).all()
    return r

def select_6():
    r = session.query(Student.name)\
        .select_from(Student).where(Group.id == randint(1, 3)).all()
    return r

def select_7():
    r = session.query(Student.name, Grade.grade)\
        .select_from(Student).join(Grade, Student.id == Grade.student_id).join(Subject, Grade.subject_id == Subject.id).where(Student.group_id == Group.id, Subject.name == choice(SUBJECTS)).all()
    return r

def select_8():
    r = session.query(Teacher.id, Teacher.name, func.round(func.avg(Grade.grade), 2).label('avg_grade'))\
        .select_from(Teacher).join(Subject, Teacher.id == Subject.teacher_id).join(Grade, Subject.id == Grade.subject_id).group_by(Teacher.id).where(Teacher.id == randint(1, 8)).all()
    return r

def select_9():
    r = session.query(Subject.name, Student.name)\
        .select_from(Student).join(Grade, Student.id == Grade.student_id).join(Subject, Grade.subject_id == Subject.id).where(Student.id == randint(1, 100)).distinct().all()
    return r

def select_10():
    r = session.query(Subject.name, Teacher.name, Student.name)\
        .select_from(Student).join(Grade, Student.id == Grade.student_id).join(Subject, Grade.subject_id == Subject.id).join(Teacher, Subject.teacher_id == Teacher.id).where(Student.id == randint(50, 100), Teacher.id == randint(8, 15)).distinct().all()
    return r

def main(args):
    function_name = args 
    arguments = ()
    try:
        result = eval(f"{function_name}{arguments}")
        print("Результат виклику функції:", result)
    except NameError:
        print("Функція не знайдена")


if __name__ == "__main__":
    order = sys.argv[1]
    main(order)