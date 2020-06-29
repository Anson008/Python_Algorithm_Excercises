def decode_string(s):
    str_stack = []
    count_stack = []
    string = ''
    i = 0
    while i < len(s):
        if s[i].isdigit():
            count = 0
            while s[i].isdigit():
                count = count * 10 + int(s[i])
                i += 1
        elif s[i].isalpha():
            string += s[i]
            i += 1
        elif s[i] == "[":
            count_stack.append(count)
            str_stack.append(string)
            string = ""
            i += 1
        else:
            count = count_stack.pop()
            string = str_stack.pop() + string * count
            i += 1
    return string

