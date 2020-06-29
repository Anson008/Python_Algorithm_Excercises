def decode_string(string):
    string_stack = []
    concat_stack = []
    s = ''
    i = 0
    while i < len(string):
        if string[i].isdigit():
            concat = int(string[i])
        elif string[i].isalpha():
            s += string[i]
        elif string[i] == "[":
            concat_stack.append(concat)
            string_stack.append(s)
            s = ''
        else:
            concat = concat_stack.pop()
            ret = string_stack.pop()
            s = ret + s * concat
        i += 1
    return s


if __name__ == "__main__":
    s1 = "10[a]"
    print("res1:", decode_string(s1))

    s2 = "3[a]2[bc]"
    print("res2:", decode_string(s2))