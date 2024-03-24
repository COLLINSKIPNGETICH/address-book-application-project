from .database import SessionLocal
from .models import Contact

def add_contact(name, phone, email):
    session = SessionLocal()
    contact = Contact(name=name, phone=phone, email=email)
    session.add(contact)
    session.commit()
    session.close()

def delete_contact(contact_id):
    session = SessionLocal()
    contact = session.query(Contact).filter(Contact.id == contact_id).first()
    if contact:
        session.delete(contact)
        session.commit()
    session.close()

def get_contacts():
    session = SessionLocal()
    contacts = session.query(Contact).all()
    session.close()
    return contacts
