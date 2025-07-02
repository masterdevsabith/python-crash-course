number = int(input("Enter a number: "))
starting_number = 1

sum_of_numbers = 0
while starting_number <= number:
    sum_of_numbers += starting_number
    starting_number += 1
print(f"The sum of numbers from 1 to {number} is: {sum_of_numbers}")
