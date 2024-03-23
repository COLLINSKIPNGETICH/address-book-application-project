import argparse
import sys
sys.path.append('/home/c3etollins/Desktop/moringa/phase-3/project/address-book-application-project/')  # Add the path to your project directory
from database import create_database
from .commands import add_contact, delete_contact, view_contacts

def main():
    parser = argparse.ArgumentParser(description="Address Book CLI Application")
    parser.add_argument("command", choices=["add", "delete", "view"], help="Command to execute")
    parser.add_argument("--name", help="Name of the contact")
    parser.add_argument("--phone", help="Phone number of the contact")
    parser.add_argument("--email", help="Email address of the contact")
    parser.add_argument("--id", type=int, help="ID of the contact to delete")

    args = parser.parse_args()

    if args.command == "add":
        add_contact(args.name, args.phone, args.email)
    elif args.command == "delete":
        delete_contact(args.id)
    elif args.command == "view":
        view_contacts()

if __name__ == "__main__":
    create_database()
    main()