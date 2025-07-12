phone_no = input("your phone no: ")
digits_mapping = {
    '1': 'one',
    '2': 'two',
    '3': 'three',
    '4': 'four',
    '5': 'five',
    '6': 'six',
    '7': 'seven',
    '8': 'eight',
    '9': 'nine'
}
in_text = ""
for n in phone_no:
    no_in_text = digits_mapping.get(n)
    in_text += no_in_text + " "

print(in_text)
