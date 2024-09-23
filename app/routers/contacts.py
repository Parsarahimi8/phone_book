from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from .. import models, schemas, crud
from ..db import get_db

router = APIRouter()

# Route to create a contact
@router.post("/create", response_model=schemas.PersonOut)
def create_contact(person: schemas.PersonCreate, db: Session = Depends(get_db)):
    db_person = crud.get_person_by_name(db, first_name=person.first_name, last_name=person.last_name)
    if db_person:
        raise HTTPException(status_code=400, detail="Person with this name already exists")
    return crud.create_person(db=db, person=person)

# Route to search for a contact by name
@router.get("/search", response_model=schemas.PersonOut)
def search_contact(first_name: str, last_name: str, db: Session = Depends(get_db)):
    db_person = crud.get_person_by_name(db, first_name=first_name, last_name=last_name)
    if db_person is None:
        raise HTTPException(status_code=404, detail="Person not found")
    return db_person

# Route to get all contacts
@router.get("/", response_model=List[schemas.PersonOut])
def get_all_contacts(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_all_contacts(db=db, skip=skip, limit=limit)
