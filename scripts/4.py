import re

# input data
input_data = list(range(108457, 562042))

#########################################################
# Functions
#########################################################

def getRegex(n=2):

    '''Return a regular expression that checks for
    repeating numbers at least n number of times'''
    
    # build a regex for testing doubles
    regex = list(range(1, 10))
    regex = [str(x) + "{" + str(n) + "}" for x in regex]
    regex = "|".join(regex)
    return(regex)
    
def checkDoubles(digits):

    '''Check in digits for repeating numbers. At least
    twice'''

    regex = getRegex(n=2)
    # if there is no double then re.findall()
    # will return an empty list. Test on this
    if len(re.findall(regex, str(digits))) == 0:
        doubles = False
    else:
        doubles = True
    return(doubles)

def reCheckDoubles(digits):

    '''Check for repeating numbers in digits and if there
    are repeats then check for the additional conditions
    i.e. 1) Are all numbers the same - Not valid
         2) Are there triple numbers? If yes then make sure
            there isn't more than one triplet and leave
            in those that also have a doublet'''
    
    # For Part 2. Urgh. I got very bogged down with this
    # bit. 
    
    # does it satisdy having doubles?
    if checkDoubles(digits):
        # are all numbers the same
        if len(re.findall(getRegex(n=6), str(digits))) == 1:
            valid = False
        # check for triples
        regex = getRegex(n=3)
        triples = re.findall(regex, str(digits))
        # double triples not allowed
        if len(triples) == 2:
            valid = False
        # a single triple
        elif len(triples) == 1:
            # get doubles in whats left of string after
            # subbing the  triples number with non matching string
            digits2 = str(digits).replace(triples[0][0], "-")
            if checkDoubles(digits2):
                valid = True
            else:
                valid = False
        else:
            valid = True
    else:
        valid = False
    return(valid)

def checkIncreasing(digits):

    '''Check that the numbers in digits are increasing
    or staying the same'''
    
    # can make digits a list and check
    # if they increase or decrease. Has
    # to be a string to make a list but can
    # convert back later
    digits = list(str(digits))
    previous_digit = 0
    is_it_true = []
    for digit in digits:
        if int(digit) >= int(previous_digit):
            is_it_true.append(True)
            previous_digit = digit
        else:
            is_it_true.append(False)
            previous_digit = digit
    # check if all are true i.e each is increasing
    # compared to the previous
    if all(is_it_true):
        increasing = True
    else:
        increasing = False
    return(increasing)

########################################################
# Part 1
########################################################

valid = 0
for digits in input_data:
    if checkDoubles(digits) and checkIncreasing(digits):
        valid += 1
print("Part1\nAnswer = ", valid)

########################################################
# Part 2
########################################################

valid = 0
for digits in input_data:
    if reCheckDoubles(digits) and checkIncreasing(digits):
        valid += 1
print("Part2\nAnswer = ", valid)
        
        


    
