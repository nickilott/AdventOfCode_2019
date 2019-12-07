import re
import itertools

################################
# Function to coordinates
################################

def getCoords(current_position, direction, distance):

    # need to use current coordinates as
    # baseline
    current_x = current_position[0]
    current_y = current_position[1]
    distance = distance + 1

    # determine what to add to what depending on direction
    # If its Up or Right then just add distance to y or x coord
    # If its Down or Left then subtract from y or  coord
    if direction == "D":
        xcoords = [x for x in list(itertools.repeat(current_x, distance))]
        ycoords = [current_y - i for i in range(distance)]
    elif direction == "U":
        xcoords = [x for x in list(itertools.repeat(current_x, distance))]
        ycoords = [current_y + i for i in range(distance)]
    elif direction == "L":
        ycoords = [x for x in list(itertools.repeat(current_y, distance))]
        xcoords = [current_x - i for i in range(distance)]
    elif direction == "R":
        ycoords = [x for x in list(itertools.repeat(current_y, distance))]
        xcoords = [current_x + i for i in range(distance)]
    coords = [(x,y) for x, y in zip(xcoords, ycoords)]
    return(coords[1:])
    
################################
# Create directionSet class
################################

# I decided to create a class just because I thought it would be neater as each
# Wire has its own attributes and methods that can be used again and again

class Wire(object):

    # initialise class with directions and distances
    # from input - these are e.g. "D1", "U5" etc
    def __init__(self, directions):
        self.directions = [re.findall("[A-Z]", x)[0] for x in directions]
        self.distances = [int(re.findall("[0-9].*", x)[0]) for x in directions]
        
    def getCoordinates(self):
        # Each wire has coordinates for its path so can
        # specify here - start at x=0,y=0
        coordinates = [(0, 0)]
        for direction, distance in zip(self.directions, self.distances):
            current_position = coordinates[-1]
            coordinates.extend(getCoords(current_position, direction, distance))
        coordinates = coordinates[1:]
        return(coordinates)

    def crosswire(self, DSet):
        # intersect the two coordinates from Wire objects to find
        # out where they cross - all crosses
        return(set(self.getCoordinates()).intersection(set(DSet.getCoordinates())))

    def nsteps(self, target_coord):
        # calculate the number of steps it takes to
        # get to a coordinate i.e go through the
        # coordinates until you hit the target and
        # then stop. Increment at each step
        nsteps = 0
        for coord in self.getCoordinates():
            if not coord == target_coord:
                nsteps += 1
            else:
                break
        # have to catch the 1 that is the
	        # final location i.e + 1 to nsteps
        return(nsteps + 1)
    
# Part 1
# read input data
input_data = [x[:-1] for x in open("input3.txt").readlines()]

# First line was wire 1 and second line was wire 2 so
# are the first two elements of the list
w1 = input_data[0].split(",")
w2 = input_data[1].split(",")

# Create Wire objects
wire1 = Wire(w1)
wire2 = Wire(w2)

# find minimum from crosswire i.e intersection of two wire paths
print("Part 1\nAnswer = ", min([abs(x[0]) + abs(x[1]) for x in wire1.crosswire(wire2)]))

####################################################
# Part 2
####################################################

# Addded a method nsteps to the Wire class above
# Iterate over the intersections and get the sum of the
# number of steps - uses a list comprehension. Although there
# is a lot of code upfront, the use of a class in this instance
# I think was worth it.
sumsteps = [wire1.nsteps(coord) + wire2.nsteps(coord) for coord in wire1.crosswire(wire2)]
print("Part 2\nAnswer = ", min(sumsteps))

