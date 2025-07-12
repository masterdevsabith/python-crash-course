started = False

while True:
    command = input("> ").strip().lower()
    if command == 'start':
        if started:
            print("car already started")
        else:
            started = True
            print('car started')
    elif command == 'stop':
        if not started:
            print('car already stopped')
        else:
            started = False
            print('car stopped')
    elif command == 'help':
        print('''
help - show this help message
start - start the car
stop - stop the car
quit - quit this program''')
    elif command == 'quit':
        break
    else:
        print("I don't understand that")
