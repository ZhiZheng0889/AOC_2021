#Open day 7 input text file
with open('Day7.txt') as my_file:
    #Read the text file
    day7inputlist = my_file.readline().strip()

#Create a list to store input elements as int
crabmarine = list(map(int, day7inputlist.split(',')))

#Create lists to store the sums for cost of each outcomes when crab submarines spend to align to each position
fuel_sums = []
new_fuel_sums = []

#Loop through the each position within the range of the crab submarines positions
for i in range(min(crabmarine), max(crabmarine)+1):
    fuel = 0
    total_fuel = 0
    new_fuel_cost = 0

    #Loop through each crab submarine to see how much it cost for it to travel specific position
    for j in range(len(crabmarine)):

        #Use abs() function to make sure travel distance(difference) will be positive
        fuel = abs(crabmarine[j] - i)
        #Part 1
        total_fuel = total_fuel + fuel
        #Part 2
        new_fuel_cost = new_fuel_cost + fuel * (fuel + 1) / 2

    #Append each total fuel cost for all crab submarines to travel to certain position
    fuel_sums.append(int(total_fuel))
    new_fuel_sums.append(int(new_fuel_cost))

print(f'The cheapest possible total fuel cost for part 1: {min(fuel_sums)}')
print(f'The cheapest possible total fuel cost for part 2: {min(new_fuel_sums)}')