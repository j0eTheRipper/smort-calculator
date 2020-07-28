from variables import Variables


def command_exec(cmd):
    """Executes the command"""
    if cmd == '/exit':
        print('Bye!')
        quit()
    elif cmd == '/help':
        print('This program calculates all operations. | eg: 1 + 2 * 6 / 5 + (2 - 3) ^ 2')
        print('You can also store values in variables. | eg: x = 2')
    else:
        print('Unknown command')


# Main
calculator = Variables()
print('WELCOME TO THE SMORT CALCULATOR\n\n')
while True:
    usr_input = input('Please enter your expression: ')

    if usr_input.startswith('/'):  # if the user inputs a command
        command_exec(usr_input)
    else:
        if usr_input == '':  # if the user didn't input anything
            continue
        else:
            calculator.main(usr_input)
            continue
