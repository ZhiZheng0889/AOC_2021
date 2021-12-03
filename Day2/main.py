#import re to more efficiently create a list from the text file
import re

#Open day 2 input text file
my_file = open("Day2.txt", "r")

#Create a list to put the inputs from Day2.txt into
day2inputlist = []

#Looping the inputs into the list
for line in my_file:
    stripped_line = line.strip()
    line_list = stripped_line.split()
    day2inputlist.append(line_list)

my_file.close()

#Part 1
i = 0
x_axis = 0
y_axis = 0
aim = 0
for i in range(i, len(day2inputlist)):
    try:
        if day2inputlist[i][0] == 'forward':
            horizontal = int(day2inputlist[i][1])
            x_axis = x_axis + horizontal

        elif day2inputlist[i][0] == 'down':
            depth = int(day2inputlist[i][1])
            y_axis = y_axis + depth

        elif day2inputlist[i][0] == 'up':
            depth = int(day2inputlist[i][1])
            y_axis = y_axis - depth


    except ValueError:
        print("Oops!  That was no valid number.  Try again...")

finaldist = x_axis * y_axis
print(f'After following these instructions, '
      f'you would have a horizontal position of {x_axis} and a depth of {y_axis}. '
      f'(Multiplying these together produces {finaldist}.)')

#Part 2
i = 0
x_axis = 0
y_axis = 0
aim = 0
aimdepth = 0
for i in range(i, len(day2inputlist)):
    try:
        if day2inputlist[i][0] == 'forward':
            horizontal = int(day2inputlist[i][1])
            x_axis = x_axis + horizontal
            newaim = aim * horizontal
            aimdepth = aimdepth + newaim
            print(aimdepth)

        elif day2inputlist[i][0] == 'down':
            depth = int(day2inputlist[i][1])
            y_axis = y_axis + depth
            aim = aim + depth

        elif day2inputlist[i][0] == 'up':
            depth = int(day2inputlist[i][1])
            y_axis = y_axis - depth
            aim = aim - depth


    except ValueError:
        print("Oops!  That was no valid number.  Try again...")

finaldist = aimdepth * x_axis
print(f'Multiplying these produces {finaldist}.')