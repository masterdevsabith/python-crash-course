first_num = int(input("Enter first number: "))
second_num = int(input("Enter second number: "))

if first_num > second_num:
    print(f"{first_num} is greater than {second_num}")
elif second_num > first_num:
    print(f"{second_num} is greater than {first_num}")
else:
    print(f"{first_num} is equal to {second_num}")
