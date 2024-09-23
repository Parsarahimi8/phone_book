from sqlalchemy import Column, Integer, String
from .db import Base

class Contact(Base):
    __tablename__ = 'contacts'  # Correct the table name declaration
    
    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    phone_number = Column(String, nullable=False, unique=True)
    description = Column(String, nullable=True)  # You had nullable=False, but your schema allows None
