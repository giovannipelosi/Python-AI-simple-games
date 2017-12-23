import numpy

print ("TIC TAC TOE!")

sizeRow = 4
sizeCol = 3

seq = 3  # number of points in a line


def verifyVictory(board, player):
    """

    :rtype: object
    """

    """for i in range(0, sizeRow, 1):
        for j in range(0, sizeCol, 1):
            print board[i][j]
    print ("h")
    """
    result = 0
    result = result + verify(board, player)  # rows
    if result > 0:
        return 1
    result = result + verify(zip(*board), player)  # cols  # zip produce the transpose of the function
    if result > 0:
        return 1
    result = result + verifyDiag1(board, player)
    if result > 0:
        return 1
    result = result + verifyDiag2(board, player)
    if result > 0:
        return 1
    else:
        return 0


def verify(board, player):  # used to check both the columns and the rows
    for i in board:
        if verifyLine(i, player) == player:
            return 1
    return 0


def verifyDiag1(board, player):  # used to check the main diagonal
    line = []
    for i in xrange(0, sizeRow):

        for j in xrange(0, sizeCol):
            # add constraints
            if i + j < sizeRow:
                # print board[i + j][j]
                line.append(board[i + j][j])
        # print(line)
        if verifyLine(line, player) == player:
            return 1

        line = []
    # print ("end vertical part")
    for i in xrange(0, sizeCol):
        for j in xrange(0, sizeRow):
            # add constraints
            if i + j < sizeCol:
                # print board[j][i+j]
                line.append(board[i + j][j])
        #print(line)
        if verifyLine(line, player) == player:
            return 1
        line = []
    return 0


def verifyDiag2(board, player):  # used to check the reverse diagonal
    # first block (starting from the last column)
    line = []
    for i in xrange(0, sizeRow):
        for j in xrange(0, sizeCol):
            # add constraints
            if i + j < sizeRow and sizeCol - j - 1 >= 0:
                # print board[i + j][j]
                line.append(board[i + j][sizeCol - j - 1])
        # print(line)
        line = []
        if verifyLine(line, player) == player:
            return 1
    # print ("end vertical part")
    # second block (starting from the row)
    line = []
    for i in xrange(0, sizeCol):
        for j in xrange(0, sizeRow):
            # add constraints
            if i - j >= 0:
                # print board[j][i+j]
                line.append(board[j][i - j])

        # print(line)
        if verifyLine(line, player) == player:
            return 1
        line = []
    return 0


def verifyLine(line, player): #  used to check if a line contain a victory sequence with length = seq (global variable)
    counter = 0
    for i in line:
        # print (i)
        if i == player:
            counter = counter + 1
            # print ("counter " , counter)
        if counter == seq:
            return player
        if i != player:
            counter = 0

    else:
        return -1


board1 = [[1, 0, 1], [1, 1, 0], [1, 0, 1]]
board2 = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]
board3 = [[1, 0, 1], [1, 0, 0], [0, 1, 1], [0, 0, 1]]
# print (verifyVictory(board, 1))
# print("result : ", verifyDiag1(board3, 1))
#verifyDiag2(board2, 1)

p = 1

print ("has player " + str(p) + " won? : " + str(verifyVictory(board3,p)))

