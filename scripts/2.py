import itertools

def opcode(opcode_type=1, input1=1, input2=1, output_pos=3, full=[]):

    if opcode_type == 1:
        res = full[input1]+full[input2]
    elif opcode_type == 2:
        res = full[input1]*full[input2]
    full[output_pos] = res        
    return (full)

def chunked_iterable(iterable, size):
    it = iter(iterable)
    while True:
        chunk = tuple(itertools.islice(it, size))
        if not chunk:
            break
        yield chunk

##############################################################################
##############################################################################
## Part 1
##############################################################################
##############################################################################
        
# run the code changing the input        
input_data = [int(x) for x in open("input2.txt").readlines()[0].split(",")]
input_data[1] = 12
input_data[2] = 2

def defineOutput(input_data, size=4):
    for i in chunked_iterable(input_data, size):
        if i[0] == 99:
            continue
        if len(i) < 4:
            break
        newopt = (opcode(opcode_type=i[0],
                         input1=i[1],
                         input2=i[2],
                         output_pos=i[3],
                         full=input_data))
    return(newopt)

print("Part1\n", defineOutput(input_data, size=4))

##############################################################################
##############################################################################
## Part 2
##############################################################################
##############################################################################

def reset():
    return([int(x) for x in open("input2.txt").readlines()[0].split(",")])

input_data = [int(x) for x in open("input2.txt").readlines()[0].split(",")]
for x, y in itertools.permutations(range(0,99), 2):
    input_data[1] = x
    input_data[2] = y
    res = defineOutput(input_data, size=4)
    if res[0] == 19690720:
        print("Part2\n", "noun =", x, "verb =", y, "\n", "Answer = ", 100*x+y)
        break
    else:
        input_data = reset()
        


