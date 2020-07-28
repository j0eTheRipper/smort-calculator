from calculator import Calculator


class Variables:
    def __init__(self):
        self.usr_input = None
        self.variables = dict()

    def assign_var(self, usr_input):
        self.usr_input = usr_input
        if self.usr_input.count('=') == 1:
            self.usr_input = self.usr_input.replace(' ', '').split('=')
            if self.usr_input[0].isalpha():
                if self.usr_input[1].isdigit():
                    self.usr_input[1] = int(self.usr_input[1])
                    self.variables[self.usr_input[0]] = self.usr_input[1]
                elif self.usr_input[1].isalpha():
                    if self.variables.get(self.usr_input[1]):
                        self.variables[self.usr_input[0]] = self.variables[self.usr_input[1]]
                    else:
                        print('Unknown variable')
                else:
                    print('Invalid assignment')
            else:
                print('Invalid identifier')
        else:
            print('Invalid assignment')

    def get_var(self, usr_input):
        self.usr_input = usr_input
        self.usr_input = self.usr_input.replace(' ', '')

        if self.usr_input.isalpha():
            if self.usr_input in self.variables:
                return self.variables[self.usr_input]
            else:
                return 'Unknown variable'
        else:
            return 'Invalid identifier'

    def eval_vars(self, usr_input):
        self.usr_input = usr_input
        equation = str()
        operators = {'+', '-', '*', '/', '^', '(', ')', ' '}

        for i in self.usr_input:
            if i not in operators and not i.isdigit():
                if self.get_var(i) == 'Unknown variable' or self.get_var(i) == 'Invalid identifier':
                    return self.get_var(i)
                else:
                    equation += f'({self.get_var(i)}) '
            elif i in operators or i.isdigit():
                equation += i

        calculator = Calculator(equation)
        return calculator.main()

    def main(self, usr_input):
        self.usr_input = usr_input
        if '=' in self.usr_input:
            self.assign_var(self.usr_input)
        elif self.usr_input.replace(' ', '').isalpha():
            print(self.get_var(self.usr_input))
        elif '-' in self.usr_input or '+' in self.usr_input or '*' in self.usr_input \
                or '/' in self.usr_input or '(' in self.usr_input or ')' in self.usr_input:
            print(self.eval_vars(self.usr_input))
        elif self.usr_input.isdigit():
            print(self.eval_vars(self.usr_input))