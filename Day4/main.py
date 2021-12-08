import re

#Function for checking each bingo board in the list of bingo boards
def check_board(board, drawnum):
    for a in range(len(drawnum)):
        for b in range(len(board)):
            marking_currentboard(board[b], drawnum[a])
            if check_rows(board[b]) or check_columns(board[b]):
                return b, int(drawnum[a])

#Function for marking the matching number to drawn number for each bingo board
def marking_currentboard(currentboard, currentnum):
    for a in range(5):
        for b in range(5):
            if currentboard[a][b] == currentnum:
                currentboard[a].pop(b)
                currentboard[a].insert(b, ' ')

#Function for checking each bingo board for winning row
def check_rows(board):
    count = 0
    for a in range(5):
        if board[a] == [' '] * 5:
            count += 1
    if count:
        return True

#Functions for checking each bingo board for winning column
def check_columns(board):
    for a in range(5):
        if check_particular_column(board, a):
            return True

def check_particular_column(board, index):
    count = ''
    for a in range(5):
        count += board[a][index]
    if count == ' '*5:
        return True

#Function to calculate the final score of the winning board
def sum_board(board):
    total = 0
    for a in range(5):
        for b in range(5):
            total += int(board[a][b].replace(' ', '0'))
    return total

# Data Import Input Data From File
with open('Day4.txt', 'r') as my_file:
    bingo = my_file.read().split("\n")

    #Separating draw numbers from bingo boards
    #Draw numbers
    input_num = bingo[0].split(',')

    #Convert Draw numbers from strings to int
    drawnum = [int(item) for item in input_num]

    #Bingo Boards
    data = list(filter(lambda x: x != '', bingo[1:]))
    rows = []
    boards = []

    #Split each number in each row and Convert each bingo board rows into int
    for item in data:
        rows.append(item.split())

    for i in range(0, len(rows), 5):
        boards.append(rows[:5])
        rows = rows[5:]

    #Part 1
    for i in range(len(boards)-1):
        currentboard, currentnum = check_board(boards, input_num)
        if i == 0:
            part1 = sum_board(boards[currentboard]) * currentnum
        boards.pop(currentboard)
    print(f'The final score for the winning board: {part1}')

    #Part 2
    currentboard, currentnum = check_board(boards, input_num)
    part2 = sum_board(boards[currentboard]) * currentnum
    print(f'\nThe final score for the winning board: {part2}')




