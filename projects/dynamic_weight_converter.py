weight = float(input("Weight: "))
unit = input("(L)bs or (K)g: ").strip().lower()

if unit == 'l':
    converted_weight = weight/2.205
    print(f"{weight} pounds is {converted_weight:.2f} kilograms.")
elif unit == 'k':
    converted_weight = weight * 2.205
    print(f"{weight} pounds is {converted_weight:.2f} kilograms.")
else:
    converted_weight = None
    print("Invalid unit. Please enter 'L' for pounds or 'K' for kilograms.")
