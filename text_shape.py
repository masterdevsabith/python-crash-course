numbers = [5, 2, 5, 2, 2]
letter = 'x'

# for number in numbers:
#     print('x'*number)


# new way

for number in numbers:
    output = ''
    for x_count in range(number):
        output += 'x'
    print(output)
