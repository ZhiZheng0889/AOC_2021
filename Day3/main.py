#Open day 3 input text file
my_file = open("Day3.txt", "r")

#Create a list to put the inputs from Day1.txt into
day3inputlist = []

#Looping the inputs into the list
for line in my_file:
    day3inputlist = my_file.read().split()
my_file.close()
inputlen = len(day3inputlist[0])


#Part 1 of the AOC Day 3 question
def part1():
    gammarate = ""
    epsilonrate = ""

    i = 0
    #Looping through the list to find the most and least common bit in the corresponding position of the binary numbers
    while i < inputlen:
        try:
            input = [digit[i] for digit in day3inputlist]
            if input.count("0") > input.count("1"):
                gammarate += "0"
                epsilonrate += "1"
            else:
                gammarate += "1"
                epsilonrate += "0"

            i = i + 1

        except ValueError:
            print('Oops! That was no valid number. Try again...')

    print(f'The power consumption of the submarine is {int(gammarate, 2)*int(epsilonrate, 2)}!')

part1()

#Part 2 of the AOC Day 3 question
class Part2:
    def oxygen(self):
        #Create a copy list of day 3 input
        inputlist = day3inputlist.copy()
        try:
            #Looping through day 3 inputlist to create new list by finding most common value (0 or 1) in the current bit position, and keep only numbers with that bit in that position
            for i in range(inputlen):
                #Loop termination when there is only one binary left in list
                if len(inputlist) == 1:
                    break

                # Create new lists to hold binaries for 0 and 1 in corresponding position
                binary1 = []
                binary0 = []
                for binarynum in inputlist:
                    # Looping through inputlist to place binary numbers into seperate list based on bit(1 or 0) at corresponding position
                    if binarynum[i] == "1":
                        binary1.append(binarynum)
                    elif binarynum[i] == "0":
                        binary0.append(binarynum)

                #Keeping the list with the most common bit at corresponding position
                #If 0 and 1 are equally common, keep values with a 1 in the position being considered.
                if len(binary1) >= len(binary0):
                    inputlist = binary1.copy()
                elif len(binary1) < len(binary0):
                    inputlist = binary0.copy()

            return int(inputlist[0], 2)

        except ValueError:
            print('Oops! That was no valid number.  Try again...')

    #Looping through day 3 inputlist to create new list by finding least common value (0 or 1) in the current bit position, and keep only numbers with that bit in that position
    def co2scrub(self):
        inputlist = day3inputlist.copy()
        try:
            for i in range(inputlen):
                #Loop termination when there is only one binary left in list
                if len(inputlist) == 1:
                    break

                #Create new lists to hold binaries for 0 and 1 in corresponding position
                binary1 = []
                binary0 = []
                #Looping through inputlist to place binary numbers into seperate list based on bit(1 or 0) at corresponding position
                for binarynum in inputlist:
                    if binarynum[i] == "1":
                        binary1.append(binarynum)
                    elif binarynum[i] == "0":
                        binary0.append(binarynum)

                # Keeping the list with the least common bit at corresponding position
                #If 0 and 1 are equally common, keep values with a 0 in the position being considered.
                if len(binary1) >= len(binary0):
                    inputlist = binary0.copy()
                elif len(binary1) < len(binary0):
                    inputlist = binary1.copy()

            return int(inputlist[0], 2)

        except ValueError:
            print('Oops! That was no valid number. Try again...')

print(f'The life support rating of the submarine is {Part2.oxygen(inputlen) * Part2.co2scrub(inputlen)}!')