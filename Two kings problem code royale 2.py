d1 = [-1, -1, -1, 0, 0, 1, 1, 1]
d2 = [-1, 0, 1, -1, 1, -1, 0, 1]

def printBoard(board):
    [print(' '.join(str(_) for _ in x)) for x in board]
    print()

def newBoard():
    return [[0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0]]


def underAttack(board, x, y):
    for d in range(8):
        i, j = x + d1[d], y + d2[d]
        while i >= 0 and i < 8 and j >= 0 and j < 8:
            if board[i][j] == 2:
                return True
            elif board[i][j] == 1:
                break

            i += d1[d]
            j += d2[d]

    return False


def moveKing(board, k, pos):
    board2 = []
    for i in board:
        board2.append(i[:])

    xpos = [x1, x2][k] + d1[pos]
    ypos = [y1, y2][k] + d2[pos]

    if k == 0 and xpos >= 0 and xpos < 8 and ypos >= 0 and ypos < 8 and not (xpos == x2 and ypos == y2):
        board2[x1][y1] = 0
        board2[xpos][ypos] = 1
        return board2, xpos, ypos

    elif k == 1 and xpos >= 0 and xpos < 8 and ypos >= 0 and ypos < 8 and not (xpos == x1 and ypos == y1):
        board2[x2][y2] = 0
        board2[xpos][ypos] = 1
        return board2, xpos, ypos

    return False, 0, 0


def check(queens):

    board = newBoard()
    board[x1][y1] = board[x2][y2] = 1
    for q in queens:
        board[q[0]][q[1]] = 2


    # try if kings are under attack
    if (not underAttack(board, x1, y1)) or (not underAttack(board, x2, y2)):
        return False

    # try if king can escape
    for king in range(2):
        for direc in range(8):
            board2, x, y = moveKing(board, king, direc)

            if king == 0 and board2 and ((not underAttack(board2, x, y)) or (not underAttack(board2, x2, y2))):
                return False
            elif king == 1 and board2 and ((not underAttack(board2, x, y)) or (not underAttack(board2, x1, y1))):
                return False

    return True


def solve():
    global k1, k2, x1, y1, x2, y2
    x1, y1, x2, y2 = [int(x) for x in input().split()]
    k1, k2 = x1 * 8 + y1, x2 * 8 + y2

    board = newBoard()
    board[x1][y1] = board[x2][y2] = 1

    # 2 pieces
    for i in range(63):
        if i == k1 or i == k2:
            continue
        row, col = i // 8, i % 8
        for j in range(i + 1, 64):
            if j == k1 or j == k2:
                continue
            row1, col1 = j // 8, j % 8
            if check([(row, col), (row1, col1)]):
                return 2

    # 3 pieces
    for i in range(62):
        if i == k1 or i == k2:
            continue
        row, col = i // 8, i % 8
        for j in range(i + 1, 63):
            if j == k1 or j == k2:
                continue
            row1, col1 = j // 8, j % 8
            for k in range(j + 1, 64):
                if k == k1 or k == k2:
                    continue
                row2, col2 = k // 8, k % 8
                if check([(row, col), (row1, col1), (row2, col2)]):
                    return 3

    # 4 pieces always possible
    return 4


for i in range(int(input())):
    print(solve())
