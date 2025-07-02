lock_status = input("Is your account locked? (Y)es / (N)o: ").strip().lower()
password = input("Enter your password: ")

default_password = "admin123"
is_locked = False

if lock_status == 'y':
    is_locked = True
else:
    is_locked = False


if not is_locked and password == default_password:
    print("Login successful.")
else:
    print("Not successful")
