from sqlalchemy.orm import Session
from . import models, schemas

def create_person(db: Session, person: schemas.PersonCreate):
    db_person = models.Contact(
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

def get_contact_by_id(db: Session, contact_id: int):
    return db.query(models.Contact).filter(models.Contact.id == contact_id).first()

def update_person(db: Session, contact_id: int, person: schemas.PersonCreate):
    db_person = db.query(models.Contact).filter(models.Contact.id == contact_id).first()
    if db_person:
        for var, value in vars(person).items():
            setattr(db_person, var, value) if value is not None else None
        db.commit()
        db.refresh(db_person)
        return db_person
    return None

def delete_person(db: Session, contact_id: int):
    db_person = db.query(models.Contact).filter(models.Contact.id == contact_id).first()
    if db_person:
        db.delete(db_person)
        db.commit()
        return db_person  # Return the deleted person for confirmation
    return None
