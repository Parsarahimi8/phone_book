from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from .db import engine, Base, get_db
from .routers import contacts  # Ensure the router is imported correctly
from . import crud

# Create the SQLite database and tables
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Include the router for contact operations
app.include_router(contacts.router, prefix="/contacts", tags=["contacts"])

@app.get("/", tags=["contacts"])
async def read_all_contacts(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """
    Returns all contacts at the root URL ('/')
    """
    return crud.get_all_contacts(db=db, skip=skip, limit=limit)
