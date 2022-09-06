import copy

def get_row(arr, r):
    return arr[r]

def get_col(arr, c):
    return [arr[i][c] for i in range(len(arr))]

def get_diagonal(arr, r, c):
    right_diag, left_diag = [], []
    for j in range(c+1, len(arr)):
        col_diff = j - c
        if r - col_diff >= 0:
            right_diag.append(arr[r - col_diff][j])
        if r + col_diff < len(arr):
            right_diag.append(arr[r + col_diff][j])
    for k in range(c-1, -1, -1):
        col_diff = c - k
        if r - col_diff >= 0:
            left_diag.append(arr[r - col_diff][k])
        if r + col_diff < len(arr):
            left_diag.append(arr[r + col_diff][k])
    return sorted([*right_diag, *left_diag])

def is_pos_valid(arr, r, c):
    row = get_row(arr, r)
    col = get_col(arr, c)
    diag_arr = get_diagonal(arr, r, c)
    if row.count(1) > 1 or col.count(1) > 1 or diag_arr.count(1) > 0:
        return False
    return True

def get_count(arr, num):
    cnt = 0
    for ele in arr:
        for e in ele:
            if e == num:
                cnt+=1
    return cnt

def is_board_valid(arr):
    if get_count(arr, 1) == len(arr):
        return True
    return False

def fill_board(arr, r=0):
    if is_board_valid(arr):
        return True
    for j in range(len(arr[r])):
        arr[r][j] = 1
        if is_pos_valid(arr, r, j):
            res = fill_board(arr, r+1)
            if res is True:
                return True
        arr[r][j] = -1
    return False

def repeat(arr):
    arr_copy = copy.deepcopy(arr)
    res = fill_board(arr_copy)
    if res:
        return arr_copy
    return None