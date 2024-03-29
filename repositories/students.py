from sqlalchemy.orm import Session
from models import models


def get_students(db: Session):
    return db.query(models.Student).all()


def get_student(db: Session, student_id: int):
    return db.query(models.Student).filter(models.Student.id == student_id).first()


def delete_student(db: Session, student_id: int):
    db.query(models.Student).filter(
        models.Student.id == student_id).delete()
    db.commit()
    return True


def get_student_by_identification_card(db: Session, identification_card: str):
    return db.query(models.Student).filter(models.Student.identification_card == identification_card).first()


def update_student_can_vote(db: Session, student_id: int, can_vote: bool):
    db_student = db.query(models.Student).filter(
        models.Student.id == student_id).first()
    db_student.can_vote = can_vote
    db.commit()
    db.refresh(db_student)
    return db_student


def get_voters(db: Session):
    return db.query(models.Student).filter(models.Student.can_vote == False).count()


def get_pending_voters(db: Session):
    pending_voters = db.query(models.Student).filter(
        models.Student.can_vote == True).count()
    print(pending_voters)
    return pending_voters


def get_students_by_course(db: Session, course_id: int):
    return db.query(models.Student).filter(models.Student.course_id == course_id).all()
