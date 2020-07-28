from collections import deque


def isint(string):
    try:
        int(string)
    except ValueError:
        return False
    else:
        return True


class Calculator:
    def __init__(self, usr_exp):
        self.usr_exp = usr_exp
        self.infix_exp = ''
        self.postfix_exp = ''
        self.result = 0

    def formatter(self):
        """Formats the user's input to suit the infix2postfix() function"""
        if self.usr_exp.count('(') != self.usr_exp.count(')'):  # Checks the number of parentheses
            return 'Invalid expression'
        elif self.usr_exp.find('(') > self.usr_exp.find(')'):  # Checks the places of parentheses
            return 'Invalid expression'

        self.usr_exp = self.usr_exp.replace(' ', '')
        temp = self.usr_exp[0]
        self.usr_exp = self.usr_exp.replace(self.usr_exp[0], '', 1)

        for i in self.usr_exp:
            if isint(i):
                temp += i
            else:
                temp += ' ' + i + ' '

        self.usr_exp = temp
        temp = ''

        for i in self.usr_exp.split():
            if isint(i):
                temp += ' ' + i + ' '
            else:
                temp += i

        temp = temp.replace('(', ' ( ')
        temp = temp.replace(')', ' ) ')

        for i in temp.split():
            if isint(i):
                self.infix_exp += ' ' + i + ' '
            elif len(i) > 1:
                if i.count('*') > 0 or i.count('/') > 0 or i.count('^') > 0:
                    return 'Invalid expression'
                elif i.count('-') % 2 == 0:
                    self.infix_exp += '+'
                else:
                    self.infix_exp += '-'
            else:
                self.infix_exp += i

        self.infix_exp = self.infix_exp.replace('(', ' ( ')
        self.infix_exp = self.infix_exp.replace(')', ' ) ')

    def infix2postfix(self):
        """Turns the infix expression to a postfix expression"""
        stack = deque()

        def add_to_stack():
            """Adds the operators to the stack"""
            nonlocal stack

            if stack[len(stack) - 1] != '(':
                for _ in range(len(stack)):
                    if stack[len(stack) - 1] != '(':
                        self.postfix_exp += stack.pop() + ' '
            stack.append(i)

        for i in self.infix_exp.split():
            if isint(i):
                self.postfix_exp += i + ' '
            else:
                if i == '+' or i == '-':  # adding the + and - signs to the postfix expression
                    if len(stack) == 0:
                        stack.append(i)
                    else:
                        add_to_stack()
                elif i == '*' or i == '/':
                    if len(stack) == 0:
                        stack.append(i)
                    elif stack[len(stack) - 1] == '*' or stack[len(stack) - 1] == '/' or stack[len(stack) - 1] == '^':
                        add_to_stack()
                    else:
                        stack.append(i)
                elif i == '^':
                    if len(stack) == 0:
                        stack.append(i)
                    elif stack[len(stack) - 1] == '^':
                        add_to_stack()
                    else:
                        stack.append(i)
                elif i == '(':
                    stack.append(i)
                elif i == ')':
                    popped_brackets = 0
                    for _ in range(len(stack)):
                        if stack[len(stack) - 1] != '(':
                            self.postfix_exp += stack.pop() + ' '
                        else:
                            if popped_brackets < 1:
                                stack.pop()
                                popped_brackets += 1
                else:
                    return 'Invalid expression'

        for i in range(len(stack)):
            self.postfix_exp += stack.pop() + ' '

    def calculate(self):
        """Calculates the postfix expression"""
        res_stack = deque()

        for i in self.postfix_exp.split():
            if isint(i):
                res_stack.append(int(i))
            else:
                tmp_res = int(res_stack.pop())
                if i == '*':
                    res_stack.append(int(res_stack.pop()) * tmp_res)
                elif i == '/':
                    res_stack.append(int(res_stack.pop()) // tmp_res)
                elif i == '^':
                    res_stack.append(int(res_stack.pop()) ** tmp_res)
                elif i == '-':
                    res_stack.append(int(res_stack.pop()) - tmp_res)
                elif i == '+':
                    res_stack.append(int(res_stack.pop()) + tmp_res)

        self.result = res_stack.pop()

    def main(self):
        x_ = self.formatter()
        if x_ != 'Invalid expression':
            self.infix2postfix()
            self.calculate()
            return self.result
        else:
            return 'Invalid expression'
