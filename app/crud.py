from sqlalchemy.orm import Session
from . import models, schemas

def create_person(db: Session, person: schemas.PersonCreate):
    db_person = models.Contact(  # Ensure you're using the correct model name
        first_name=person.first_name,
        last_name=person.last_name,
        phone_number=person.phone_number,
        description=person.description
    )
    db.add(db_person)
    db.commit()
    db.refresh(db_person)
    return db_person

def get_person_by_name(db: Session, first_name: str, last_name: str):
    return db.query(models.Contact).filter(models.Contact.first_name == first_name, models.Contact.last_name == last_name).first()

def get_all_contacts(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Contact).offset(skip).limit(limit).all()
