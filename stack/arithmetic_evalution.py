import operator


def arithmetic_expression_evaluation(terms):
    """
    Assuming terms is not empty and they can form a valid arithmetic expression.
    Return the result after evaluation.
    :param terms: only contain '(', ')', '+', '-', '*', '/', non-negative integers.
    :return:
    """
    operands = []
    operators = []
    ops = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.truediv}
    for term in terms:
        if term == '(':
            continue
        elif term == ')':
            right, left = operands.pop(), operands.pop()
            operands.append(ops[operators.pop()](left, right))
        elif term in ops:
            operators.append(term)
        else:
            operands.append(int(term))
    return operands[0]


a1 = "(4+(5*6))"
res1 = arithmetic_expression_evaluation(a1)
print(res1)
