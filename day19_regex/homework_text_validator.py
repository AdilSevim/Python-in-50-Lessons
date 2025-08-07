"""
Day 19, Homework: Text Validator Program

Purpose: Create a text validator that checks email addresses and phone numbers using regex.
We use regular expressions to validate common text patterns.

Expected output when run:
Text Validator
1. Validate email
2. Validate phone
3. Extract email parts
4. Exit
Choose an option (1-4): [user input]
[Based on user input, appropriate validation is performed]
"""

import text_validator


def main():
    """Run the text validator program."""
    while True:
        print("\nText Validator")
        print("1. Validate email")
        print("2. Validate phone")
        print("3. Extract email parts")
        print("4. Exit")
        
        choice = input("Choose an option (1-4): ")
        
        if choice == "1":
            email = input("Enter email to validate: ")
            if text_validator.validate_email(email):
                print("Valid email address!")
            else:
                print("Invalid email address!")
        elif choice == "2":
            phone = input("Enter phone number to validate: ")
            if text_validator.validate_phone(phone):
                print("Valid phone number!")
            else:
                print("Invalid phone number!")
        elif choice == "3":
            email = input("Enter email to parse: ")
            parts = text_validator.extract_email_parts(email)
            if parts:
                username, domain, extension = parts
                print(f"Username: {username}")
                print(f"Domain: {domain}")
                print(f"Extension: {extension}")
            else:
                print("Invalid email format!")
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid option!")


if __name__ == "__main__":
    main()
