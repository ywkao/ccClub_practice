#!/usr/bin/env python

index = 0
counters = [1] # eg. [1, 10, 100]
output = [1]
nCalls = 1 # double check total stored numbers
flag = 1

def init_record(value):
    global index, counters, output, nCalls
    output.append(value)
    counters.append(value)
    nCalls += 1

def record(value):
    global index, counters, output, nCalls
    output.append(value)
    counters[index] = value
    nCalls += 1

def shift_back():
    # flag == 3
    global flag, index, counters
    index -= 1
    if index > -1:
        value = counters[index]
        if value % 10 != 9:
            # record
            value += 1
            record(value)
            # action
            flag = 1 # add_digit()
        else:
            flag = 3 # shift_back()
    else:
        flag = 0 # termination

def tick_digit():
    # flag == 2
    global flag, index, counters
    value = counters[index] + 1

    if value <= given_number:
        record(value)

        # next action
        if value % 10 != 9:
            flag = 2 # tick_digit()
        else:
            flag = 3 # shift_back()

    else:
        flag = 3 # shift_back()

def add_digit():
    # flag == 1
    global flag, index, counters

    value = counters[index] * 10
    if value <= given_number:
        index += 1

        if index == len(counters):
            # increase digit
            init_record(value)
        else:
            # update value
            record(value)

        flag = 1 # add_digit()
    else:
        flag = 2 # tick_digit()

if __name__ == "__main__":
    given_number = 30000 
    given_number = int(input())

    while flag != 0:
        if flag == 1:
            add_digit()
        if flag == 2:
            tick_digit()
        if flag == 3:
            shift_back()

    print( output )
    #print( ">>> nCalls = ", nCalls )
