car_functions = ['help', 'start', 'stop', 'quit']
function_input = input('> ').strip().lower()

# if function_input in car_functions and function_input == car_functions[0]:
#     print('''
# help - Show this help message
# start - Start the car
# stop - Stop the car
#           quit - Exit the game
# ''')

while function_input != car_functions[-1]:
    if function_input == car_functions[1]:
        print('Car started... Ready to go!')
    elif function_input == car_functions[0]:
        print('''
            help - Show this help message
            start - Start the car
            stop - Stop the car
            quit - Exit the game
        ''')
    elif function_input == car_functions[2]:
        print('Car stopped.')
    elif function_input == car_functions[-1]:
        print('Exiting the game...')
        break
    else:
        print("I don't understand that command. Type 'help' for assistance.")

    function_input = input('> ').strip().lower()  # Get the next command
