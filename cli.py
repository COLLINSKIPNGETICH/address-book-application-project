import argparse
from lib.commands import add_contact, delete_contact, get_contacts

def main():
    parser = argparse.ArgumentParser(description='Address Book CLI')
    parser.add_argument('command', choices=['add', 'delete', 'list'], help='Command to execute')
    parser.add_argument('--name', help='Contact name')
    parser.add_argument('--phone', help='Contact phone number')
    parser.add_argument('--email', help='Contact email address')
    parser.add_argument('--id', help='Contact ID (for delete command)')
    
    args = parser.parse_args()
    
    if args.command == 'add':
        add_contact(args.name, args.phone, args.email)
    elif args.command == 'delete':
        delete_contact(args.id)
    elif args.command == 'list':
        get_contacts()

if __name__ == '__main__':
    main()
