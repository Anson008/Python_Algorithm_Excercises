from stack.my_stack import Stack


def is_valid_parentheses(brackets):
    """
    List implementation.
    Return true if the sequence of brackets is valid, false otherwise.
    :param brackets: a string that contains only '(', '{', '[', ')', '}' and ']'.
    :return: boolean
    """
    left_brackets = []
    matching_bracket = {'(': ')', '{': '}', '[': ']'}
    for b in brackets:
        if b in matching_bracket:
            left_brackets.append(b)
        elif not left_brackets or matching_bracket[left_brackets[-1]] != b:
            return False
        else:
            left_brackets.pop()
    return not left_brackets


def parentheses_checker(brackets):
    """
    Stack implementation.
    Return true if the sequence of brackets is valid, false otherwise.
    :param brackets: a string that contains only '(', '{', '[', ')', '}' and ']'.
    :return: boolean
    """
    left_brackets = Stack()
    matching_bracket = {"(": ")", "{": "}", "[": "]"}
    for b in brackets:
        if b in matching_bracket:
            left_brackets.push(b)
        elif not left_brackets or matching_bracket[left_brackets.peek()] != b:
            return False
        else:
            left_brackets.pop()
    return not left_brackets


if __name__ == "__main__":
    s1 = "({[]})"
    s2 = "{})([]"
    s3 = ""

    print("(List) Is s1 valid?", is_valid_parentheses(s1))
    print("(List) Is s2 valid?", is_valid_parentheses(s2))
    print("(List) Is s3 valid?", is_valid_parentheses(s3))

    print("(Stack) Is s1 valid?", parentheses_checker(s1))
    print("(Stack) Is s2 valid?", parentheses_checker(s2))
    print("(Stack) Is s3 valid?", parentheses_checker(s3))
