Phonebook API
Description
The Phonebook API is a CRUD (Create, Read, Update, Delete) application built with FastAPI and SQLAlchemy to manage contact information. It allows users to create, retrieve, update, and delete contact details such as names, phone numbers, and descriptions.

Features
Create a new contact
Update contact details
Delete a contact by ID

project designrd by :
Python with FastAPI for building the API
SQLAlchemy for database ORM
SQLite for the database

API Endpoints
Here is a list of the main API endpoints:

1. Create a Contact
POST /contacts/
2. Get a Contact by Name
GET /contacts/
3. Get All Contacts 
GET /contacts/?skip=0&limit=100
4. Get a Contact by ID
GET /contacts/{contact_id}
5. Update a Contact
PUT /contacts/{contact_id}
Body (same as create contact)
6. Delete a Contact
DELETE /contacts/{contact_id}