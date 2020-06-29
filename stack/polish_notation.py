from stack.my_stack import Stack


def infix_to_postfix(infix_expr):
    precedence = {"(": 1, "-": 2, "+": 2, "/": 3, "*": 3}
    operators = Stack()
    postfix_list = []
    infix_list = infix_expr.split()

    for token in infix_list:
        if token not in "+-*/()":
            postfix_list.append(token)
        elif token == "(":
            operators.push(token)
        elif token == ")":
            top_token = operators.pop()
            while top_token != "(":
                postfix_list.append(top_token)
                top_token = operators.pop()
        else:
            while (not operators.is_empty()) and (precedence[operators.peek()] > precedence[token]):
                postfix_list.append(operators.pop())
            operators.push(token)

    while not operators.is_empty():
        postfix_list.append(operators.pop())
    return " ".join(postfix_list)


def postfix_eval(postfix_expr):
    operand = Stack()
    tokens = postfix_expr.split()
    for token in tokens:
        if token not in "+-*/()":
            operand.push(int(token))
        else:
            operand2 = operand.pop()
            operand1 = operand.pop()
            result = do_math(token, operand1, operand2)
            operand.push(result)
    return operand.pop()


def do_math(operator, operand1, operand2):
    if operator == "+":
        return operand1 + operand2
    elif operator == "-":
        return operand1 - operand2
    elif operator == "*":
        return operand1 * operand1
    else:
        return operand1 / operand2


if __name__ == "__main__":
    e1 = "a + b * c"
    e2 = "a * b + c * d"
    print(infix_to_postfix(e1))
    print(infix_to_postfix(e2))

    e3 = "( 17 + 8 ) / ( 3 + 2 )"
    print(postfix_eval(infix_to_postfix(e3)))