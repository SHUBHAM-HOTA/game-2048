import random

def start_game():
    mat = []
    for i in range(4):
        mat.append([0]*4)
    return mat

def add_new_2(mat):
    r = random.randint(0,3)
    c = random.randint(0,3)
    while (mat[r][c]!=0):
        r = random.randint(0,3)
        c = random.randint(0,3)
    mat[r][c] = 2
    

def get_current_state(mat):
    #checking if won
    for i in range(4):
        for j in range(4):
            if (mat[i][j]==32):
                return "WON"

    #searching for empty spaces
    for i in range(4):
        for j in range(4):
            if (mat[i][j])==0:
                return "GAME NOT OVER"

    #checking all rows and cols exept lasr row and col
    for i in range(3):
        for j in range(3):
            if (mat[i][j]==mat[i][j+1] or mat[i][j]==mat[i+1][j]):
                return "GAME NOT OVER"

    #checking for last col
    for i in range(3):
        if mat[i][3]==mat[i+1][3]:
            return "GAME NOT OVER"

    #checking for last row
    for j in range(3):
        if mat[3][j]==mat[3][j+1]:
            return "GAME NOT OVER"

    return "LOST"        

def compress(mat):
    changed = False
    new_mat = []
    for i in range(4):
        new_mat.append([0]*4)

    #compressing the mat in new_mat
    for i in range(4):
        position = 0
        for j in range(4):
            if mat[i][j]!= 0:
                new_mat[i][position] = mat[i][j]
                
                if j != position:
                    changed = True
                position += 1
    return new_mat,changed

def merge(mat):
    changed = False
    for i in range(4):
        for j in range(3):
            if mat[i][j]==mat[i][j+1] and mat[i][j]!=0 :
                mat[i][j] = (mat[i][j])*2
                mat[i][j+1] = 0
                changed = True
    return mat,changed 

def reverse(mat):
    new_mat = []
    for i in range(4):
        new_mat.append([])
        for j in range(4):
            new_mat[i].append(mat[i][4-j-1]) 
    return new_mat          

def transpose(mat):
    new_mat = []
    for i in range(4):
        new_mat.append([])
        for j in range(4):
            new_mat[i].append(mat[j][i]) 
    return new_mat

def move_up(grid):
    transposed = transpose(grid)
    compresed,changed1 = compress(transposed)
    merged,changed2 = merge(compresed)
    changed = changed1 or changed2
    comp_after_merge,temp = compress(merged)
    tran_after_all = transpose(comp_after_merge)
    return tran_after_all,changed

def move_down(grid):
    transposed = transpose(grid)
    reverseed = reverse(transposed)
    compresed,changed1 = compress(reverseed)
    merged,changed2 = merge(compresed)
    changed = changed1 or changed2
    comp_after_merge,temp = compress(merged)
    rev_after_all = reverse(comp_after_merge)
    tran_after_all = transpose(rev_after_all)
    return tran_after_all,changed

def move_right(grid):
    reverseed = reverse(grid)
    compresed,changed1 = compress(reverseed)
    merged,changed2 = merge(compresed)
    changed = changed1 or changed2
    comp_after_merge,temp = compress(merged)
    rev_after_all = reverse(comp_after_merge)
    return rev_after_all,changed

def move_left(grid):
    compresed,changed1 = compress(grid)
    merged,changed2 = merge(compresed)
    changed = changed1 or changed2
    comp_after_merge,temp = compress(merged)
    return comp_after_merge,changed