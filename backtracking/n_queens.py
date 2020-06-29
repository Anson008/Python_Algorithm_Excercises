def is_compatible(previous_columns, current_column, current_row):
    for previous_row in range(current_row):
        if previous_columns[previous_row] == current_column or \
           current_row - previous_row == abs(current_column - previous_columns[previous_row]):
            return False
    return True


def bt(answers, columns, row, n):
    if row == n:
        answers.append(columns[:])
        answers.append(['.' * p + 'Q' + '.' * (n - 1 - p) for p in columns])
        return
    for column in range(n):
        if is_compatible(columns, column, row):
            columns.append(column)
            bt(answers, columns, row + 1, n)
            columns.pop()
    return


def solve_n_queen(n):
    answers, columns = [], []
    bt(answers, columns, 0, n)
    return answers


if __name__ == "__main__":
    res = solve_n_queen(4)
    print(res)
