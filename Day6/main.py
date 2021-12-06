with open('Day6.txt') as my_file:
    day6inputlist = my_file.readline().strip()


# Create the countable list for lanternfish
fish_list = list(map(int, day6inputlist.split(',')))

# Calculate the fish
def count_fish(time):
    #Count the fish_list to find the amount of fish base on the internal timer
    fish = [fish_list.count(i) for i in range(9)]
    for i in range(time):
        #Create new fish with a enternal timer starting at 8
        new_fish = fish[8]
        #Decrease the internal timer for each fish
        for j in range(8):
            fish[j - 1] = fish[j]
        #Add the new fish to when the internal timer of a fish return to 6
        fish[7] = new_fish
        fish[6] += fish[8]

    return sum(fish)


# Part 1
inputdays = 80
total1 = count_fish(inputdays)
print(f'After {inputdays} days, there are {total1} lanternfish')

# Part 2
inputdays2 = 256
total2 = count_fish(inputdays2)
print(f'After {inputdays2} days, there are {total2} lanternfish')