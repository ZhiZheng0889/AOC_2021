import re


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
    board = []

    #Split each number in each row and Convert each bingo board rows into int
    for item in data:
        rows.append(list(map(int, item.split())))
    print(rows)

    for i in range(len(data)):
        board.append(rows[0:5])
        rows = rows[5:]
    print(board)

#Convert to ints and create list for each spot on bingo card.  0 indicates a number hasn't been selected, 1 will indicate a number has been selected
for row in range(len(board)):
    for col in range(len(board[row])):
        board[row][col] = [board[row][col], 0]

print(board)


def is_winner(cards):
    j = -6  # J += 6 is at the start of the while loop so when a winner is found, j will still equal the row of the winner
    win = 0
    while j < len(cards) - 6 and win != 1:
        j += 6
        total = 0

        # check if there's a winning row
        for row in range(j, j + 5):
            for col in range(0, 5):
                total = total + cards[row][col][1]
                if total == 5:
                    win = 1
            total = 0  # reset total before re-running loop

            # check if there's a winning column
        total = 0
        for col in range(0, 5):
            for row in range(j, j + 5):
                total += cards[row][col][1]
                if total == 5:
                    win = 1
            total = 0  # reset total before re-running loop

    if win == 0:
        return 0, 0
    if win == 1:
        return 1, j  # 1 indicates a winner, j is the starting row of the winning card


# Function to add a new winner to a list of winners
def last_winner(cards, winners):
    j = -6  # J += 6 is at the start of the while loop so when a winner is found, j will still equal the row of the winner
    win = 0
    while j < len(cards) - 6:
        j += 6
        total = 0

        # check if there's a winning row
        for row in range(j, j + 5):
            for col in range(0, 5):
                total = total + cards[row][col][1]
                if total == 5 and winners.count(j) == 0:
                    winners.append(j)

            total = 0  # reset total before re-running loop

            # check if there's a winning column
        total = 0
        for col in range(0, 5):
            for row in range(j, j + 5):
                total += cards[row][col][1]
                if total == 5 and winners.count(j) == 0:
                    winners.append(j)

            total = 0  # reset total before re-running loop

    return winners


# Run bingo game
winner = 0
i = 0

while winner == 0 and i <= len(drawnum) - 1:
    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col][0] == drawnum[i]:
                board[row][col][1] = 1
    i += 1
    new_list = is_winner(board)
    if new_list[0] == 1:
        winner = 1

sum_unmarked = 0

for row in range(new_list[1], new_list[1] + 5):
    for col in range(0, 5):
        if board[row][col][1] == 0:
            sum_unmarked += board[row][col][0]

print(sum_unmarked * drawnum[i - 1])
