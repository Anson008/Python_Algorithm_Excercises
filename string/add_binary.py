def add_binary(self, a, b):
    a = a[::-1]
    b = b[::-1]
    i = 0
    curr_digit = ''
    carry = 0
    while i < len(a) and i < len(b):
        temp_sum = int(a[i]) + int(b[i]) + carry
        carry = temp_sum // 2
        curr_digit += str(temp_sum % 2)
        i += 1
    while i < len(a):
        temp_sum = int(a[i]) + carry
        carry = temp_sum // 2
        curr_digit += str(temp_sum % 2)
        i += 1
    while i < len(b):
        temp_sum = int(b[i]) + carry
        carry = temp_sum // 2
        curr_digit += str(temp_sum % 2)
        i += 1
    if carry == 1:
        curr_digit += '1'
    return curr_digit[::-1]