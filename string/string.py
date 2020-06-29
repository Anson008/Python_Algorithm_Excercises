def remove(string, target):
    """
    Remove chars in target from the string and return a new string.
    :param string: string
    :param target: list. List of characters
    :return: string
    """
    lst = list(string)
    i, j = 0, 0
    while j < len(lst):
        if lst[j] not in target:
            lst[i] = lst[j]
            i += 1
        j += 1
    return ''.join(lst[:i])


def remove_space(string):
    if not string or len(string) == 0:
        return string
    lst = list(string)
    i, j = 0, 0
    while j < len(lst):
        if lst[j] != ' ' or (i != 0 and lst[i - 1] != ' '):
            lst[i] = lst[j]
            i += 1
        j += 1
    if i > 0 and lst[i - 1] == ' ':
        i -= 1
    return ''.join(lst[:i])


def remove_duplicate(string, step):
    if not string or len(string) < 2:
        return string
    lst = list(string)
    i, j = step, step
    while j < len(lst):
        if lst[j] != lst[i - step]:
            lst[i] = lst[j]
            i += 1
        j += 1
    return ''.join(lst[:i])


def eliminate_duplicate(string):
    if len(string) <= 1:
        return string
    stack = []
    j = 0
    while j < len(string):
        if len(stack) > 0 and string[j] == stack[-1]:
            while j < len(string) and string[j] == stack[-1]:
                j += 1
            stack.pop()
        else:
            stack.append(string[j])
            j += 1
    return ''.join(stack)


def reverse_helper(lst, left, right):
    while left < right:
        lst[left], lst[right] = lst[right], lst[left]
        left += 1
        right -= 1


def reverse_string(string):
    lst = list(string)
    reverse_helper(lst, 0, len(lst) - 1)
    i = 0
    left, right = 0, 0
    while i < len(lst):
        if i == len(lst) - 1 or lst[i + 1] == " ":
            right = i
            reverse_helper(lst, left, right)
            left = i + 2
        i += 1
    return ''.join(lst)


def reverse_vowels(string):
    if not input or len(string) == 0:
        return string
    vowels = ['a', 'e', 'i', 'o', 'u']
    lst = list(string)
    left, right = 0, len(lst) - 1
    while left < right:
        if lst[left] in vowels:
            if lst[right] in vowels:
                lst[left], lst[right] = lst[right], lst[left]
                left += 1
                right -= 1
            else:
                right -= 1
        else:
            left += 1
    return ''.join(lst)


def is_palindrome(string):
    """
    input: string input
    return: boolean
    """
    # write your solution here
    if not string or len(string) == 0:
        return True
    left, right = 0, len(string) - 1
    while left < right:
        ascii_left = ord(string[left])
        ascii_right = ord(string[right])
        condition1 = ((48 <= ascii_left <= 57) or (65 <= ascii_left <= 90) or (97 <= ascii_left <= 122))
        condition2 = ((48 <= ascii_right <= 57) or (65 <= ascii_right <= 90) or (97 <= ascii_right <= 122))
        print(condition1)
        if condition1 and condition2:
            if string[left] != string[right]:
                return False
            left += 1
            right -= 1
        if condition1 and (not condition2):
            right -= 1
        if (not condition1) and condition2:
            left += 1
        if (not condition1) and (not condition2):
            left += 1
            right -= 1
    return True


def all_anagrams(sh, lo):
    """
    input: string sh, string lo
    return: Integer[]
    """
    res = []
    if not sh or not lo:
        return res
    ascii_sum = 0
    for s in sh:
        ascii_sum += ord(s)
    lst = list(lo)
    j = 0
    while j < len(lo) - len(sh) + 1:
        i = j
        ascii_key = 0
        while i < j + len(sh):
            ascii_key += ord(lst[i])
            i += 1
        if ascii_key == ascii_sum:
            res.append(j)
        j += 1
    return res


if __name__ == "__main__":
    res1 = remove('student', ['u', 'n'])
    print(res1)

    res2 = remove_space('   aa   bb cc  ')
    print(res2)

    res3 = remove_duplicate('aaabbbccc', 1)
    print(res3)