import copy


ALREADY_CHECKED = -1
MATCH_THRESHOLD = 4


def check(matrix):
    # fall check
    is_fall = False
    for col in range(len(matrix)):
        for row in reversed(range(1, len(matrix[col]))):
            # loop down to up
            if matrix[col][row] == 0 and matrix[col][row - 1] != 0:
                matrix[col][row] = matrix[col][row - 1]
                matrix[col][row - 1] = 0
                is_fall = True

    if is_fall:
        return True

    # delete check
    for col in range(len(matrix)):
        for row in range(len(matrix[col])):
            if matrix[col][row] != 0:
                matrix_copy = copy.deepcopy(matrix)
                match_num = rec_check(matrix_copy, matrix[col][row], col, row)
                if match_num >= MATCH_THRESHOLD:
                    # delete found
                    for col2 in range(len(matrix_copy)):
                        for row2 in range(len(matrix_copy[col2])):
                            # if delete found, there will be ALREADY_CHECKED to delete
                            if matrix_copy[col2][row2] == ALREADY_CHECKED:
                                # change the original matrix to delete
                                matrix[col2][row2] = 0
                    return True

    return False


def rec_check(matrix, kind, col, row):
    count = 0
    # Left
    c = col - 1
    r = row
    if col > 0 and matrix[c][r] == kind:
        count += 1
        matrix[c][r] = ALREADY_CHECKED
        count += rec_check(matrix, kind, c, r)

    # Right
    c = col + 1
    r = row
    if col < len(matrix) - 1 and matrix[c][r] == kind:
        count += 1
        matrix[c][r] = ALREADY_CHECKED
        count += rec_check(matrix, kind, c, r)

    # Up
    c = col
    r = row - 1
    if row > 0 and matrix[c][r] == kind:
        count += 1
        matrix[c][r] = ALREADY_CHECKED
        count += rec_check(matrix, kind, c, r)

    # Down
    c = col
    r = row + 1
    if row < len(matrix[0]) - 1 and matrix[c][r] == kind:
        count += 1
        matrix[c][r] = ALREADY_CHECKED
        count += rec_check(matrix, kind, c, r)

    return count
