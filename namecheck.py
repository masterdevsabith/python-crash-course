name = input("Enter your name: ")


if len(name) < 3:
    print("name must be at least 3 characters long")
elif len(name) > 50:
    print("name must be at most 50 characters long")
else:
    print("name looks good")
