import re
import getpass
from smart_logger.core.user_db_handler import DBHandler as UserDBHandler

def is_strong_password(password: str) -> bool:
    if len(password) < 12:
        return False
    if not re.search(r"[A-Z]", password):
        return False
    if not re.search(r"[a-z]", password):
        return False
    if not re.search(r"\d", password):
        return False
    if not re.search(r"[!@#$%^&*()\-_=+]", password):
        return False
    if re.search(r"\s", password):
        return False
    return True

def create_logger_user_cli():
    print("=== Smart Logger: Create Admin User ===")
    first_name = input("First Name: ").strip()
    last_name = input("Last Name: ").strip()
    email = input("Email: ").strip()

    while True:
        password = getpass.getpass("Password: ")
        confirm_password = getpass.getpass("Confirm Password: ")

        if password != confirm_password:
            print("Passwords do not match! Try again.")
            continue

        if not is_strong_password(password):
            print(
                "Password too weak! Must be 12+ chars, include uppercase, lowercase, digit, special char."
            )
            continue

        break

    db = UserDBHandler()
    db.create_logger_user(first_name, last_name, email, password)
    print(f"User {email} created successfully!")


def change_password(email: str):
    import getpass
    db = UserDBHandler()
    user = db.get_logger_user_by_email(email)
    if not user:
        print("User not found!")
        return

    while True:
        old_pass = getpass.getpass("Old Password: ")
        if not user.verify_password(old_pass):
            print("Incorrect old password!")
            continue
        break

    while True:
        new_pass = getpass.getpass("New Password: ")
        confirm = getpass.getpass("Confirm New Password: ")

        if new_pass != confirm:
            print("Passwords do not match!")
            continue
        if not is_strong_password(new_pass):
            print("Password too weak!")
            continue
        break

    db.update_user_password(user, new_pass)
    print(f"Password for '{email}' updated successfully!")



def forgot_password(email: str):
    db = UserDBHandler()
    user = db.get_logger_user_by_email(email)
    if not user:
        print("User not found!")
        return

    import secrets
    temp_password = secrets.token_urlsafe(12)
    db.update_user_password(user, temp_password)
    print(f"Temporary password for '{email}': {temp_password}")
    print("Please login and change your password immediately.")
