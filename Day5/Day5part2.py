with open('Day5.txt') as file:
    day5inputlist = file.read().splitlines()

#Create a tuple to hold the 'map' for coordinates
seen = {}

#Loop through the input list of coordination for vent endpoint
for line in day5inputlist:
    #Split each line to get coordinates for each endpoint for the vent
    line = line.split(' -> ')
    begin, end = line

    #Split the coordinate for each end point to get the x and y axis
    x1, y1 = begin.split(',')
    x2, y2 = end.split(',')

    #Convert the x and y axises to int
    x1= int(x1)
    x2 = int(x2)
    y1 = int(y1)
    y2 = int(y2)

    #Checking the vertical line vents
    if x1 == x2:
        x = x1

        #Determine the max y locations while building the map
        start = min(y1, y2)
        end = max(y1, y2) + 1

        #Loop coordinates and build out map to see if there are any overlappping vents
        for y in range(start, end):
            seen[(x, y)] = seen.get((x, y), 0) + 1

    #Checking the horizontal line vents
    elif y1 == y2:
        y = y1

        #Determine the max x locations while building coord_list
        start = min(x1, x2)
        end = max(x1, x2) + 1

        #Loop coordinates and build out map to see if there are any overlapping vents
        for x in range(start, end):
            seen[(x, y)] = seen.get((x, y), 0) + 1

    #Checking the diagonal line vents
    else:
        #Determine the x and y axises for mapping diagonal vents
        if x1 > x2:
            x1, x2 = x2, x1
            y1, y2 = y2, y1
        startX, endX = x1, x2
        startY, endY = y1, y2
        x = startX
        y = startY

        #Loop coordinates and build out map to see if there are any overlappping vents
        if y2 > y1:
            while x <= endX and y <= endY:
                seen[(x, y)] = seen.get((x, y), 0) + 1
                x += 1
                y += 1

        #Loop coordinates and build out map to see if there are any overlappping vents
        else:
            while x <= endX and y >= endY:
                seen[(x, y)] = seen.get((x, y), 0) + 1
                x += 1
                y -= 1

count = 0

for overlap in seen.values():
    if overlap > 1:
        count += 1
print(f'There are total of {count} vent overlapping each')