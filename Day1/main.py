#import re to more efficiently create a list from the text file
import re

#Open day 1 input text file
my_file = open("Day1.txt", "r")

#Create a list to put the inputs from Day1.txt into
day1inputlist = []

#Looping the inputs into the list
for line in my_file:
    day1inputlist = list(map(int, re.findall('\d+', my_file.read())))
my_file.close()

print(day1inputlist)
#Part 1 of the AOC Day 1 question
#i equal to the counter for locating the integers in the list
i = 0
#j is the counter for keeping track of increased measurement
j = 0

#Looping through the list to find increase and decrease for each measurement
for i in range(i, len(day1inputlist)):

    try:
        if i == 0:
            print(day1inputlist[i], '(N/A - no previous measurement)')

        elif day1inputlist[i-1] < day1inputlist[i]:
            j = j + 1
            print(day1inputlist[i], '(Increased)', j)

        elif day1inputlist[i-1] > day1inputlist[i]:
            print(day1inputlist[i], '(Decreased)')

        elif day1inputlist[i-1] == day1inputlist[i]:
            print(day1inputlist[i], '(No Change)')

    except ValueError:
        print("Oops!  That was no valid number.  Try again...")

print(f'In this example, there are {j} measurements that are larger than the previous measurement.')

#Part 2 of the AOC Day 1 question
#h equal to the counter for locating the integers in the list
h = 0
#k is the counter for keeping track of increased measurement for the sum of three variable sliding windows
k = 0
#Create a list to store the sums of three variable sliding windows
windowsum = []
#Loop through input list to append to windowsum list, then check if the sum have increased, decreased, or not change
for h in range(h, len(day1inputlist)-2):
    try:
        test = day1inputlist[h] + day1inputlist[h+1] + day1inputlist[h+2]
        windowsum.append(test)
        if h == 0:
            print(windowsum[h], '(N/A - no previous measurement)')

        elif windowsum[h-1] < windowsum[h]:
            k = k + 1
            print(windowsum[h], '(Increased)', k)

        elif windowsum[h-1] > windowsum[h]:
            print(windowsum[h], '(Decreased)')

        elif windowsum[h-1] == windowsum[h]:
            print(windowsum[h], '(No Change)')

    except ValueError:
        print("Oops!  That was no valid number.  Try again...")
print(f'In this example, there are {k} sums that are larger than the previous sum.')

input('Press ENTER to exit')
