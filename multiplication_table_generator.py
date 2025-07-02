main_number = int(input("number for multiplication table: "))
upto = range(1, 11)
for number in upto:
    print(f"{number} x {main_number} = {number * main_number}")
