from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional,List

app =FastAPI()

@app.get('/')

def welcome():
    return 'welcome to our site'


class contact(BaseModel):
    id:int
    name:str
    phone_number:int
    email: Optional[str] = None
    
phone_book = list[contact] = []


    
    
@app.post('/contacts')
def create_contact(contact:contact):
    phone_book.append(contact)
    return contact



@app.get('/contacts', response_model=list[contact])

def get_contacts():
    return phone_book



@app.get("/contacts/{contact_id}", response_model=contact)
def get_contact(contact_id: int):
    for contact in phone_book:
        if contact.id == contact_id:
            return contact
    return {"error": "Contact not found"}

    
    
@app.put("/contacts/{contact_id}")
def update_contact(contact_id: int, updated_contact: contact):
    for index, contact in enumerate(phone_book):
        if contact.id == contact_id:
            phone_book[index] = updated_contact
            return updated_contact
    return {"error": "Contact not found"}


@app.delete("/contacts/{contact_id}")
def delete_contact(contact_id: int):
    for index, contact in enumerate(phone_book):
        if contact.id == contact_id:
            del phone_book[index]
            return {"message": "Contact deleted"}
    return {"error": "Contact not found"}


    

        
    

