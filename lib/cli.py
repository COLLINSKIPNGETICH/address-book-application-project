from models import Contact
from database import SessionLocal

def add_contact(name, phone, email):
    db = SessionLocal()
    contact = Contact(name=name, phone=phone, email=email)
    db.add(contact)
    db.commit()
    db.close()

def delete_contact(contact_id):
    db = SessionLocal()
    db.query(Contact).filter(Contact.id == contact_id).delete()
    db.commit()
    db.close()

def view_contacts():
    db = SessionLocal()
    contacts = db.query(Contact).all()
    for contact in contacts:
        print(f"ID: {contact.id}, Name: {contact.name}, Phone: {contact.phone}, Email: {contact.email}")
    db.close()
