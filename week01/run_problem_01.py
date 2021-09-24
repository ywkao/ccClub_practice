#!/usr/bin/env python

dimension = None
dict_input = {}
dict_map = {}

def create_input(n):
    f = open("input_01.txt", 'w')
    f.write('%d\n' % n)
    for i in range(n*n):
        if (i+1) % n != 0:
            f.write( '%d, ' % i )
        else:
            f.write( '%d\n' % i )
    f.close()

def print_dict(d):
    print('--------------------------------------------------')
    for i in range(dimension):
        info = ""
        for j in range(dimension):
            val = d[i][j]
            if len(info) == 0:
                info = '%d' % (val)
            else:
                info +=  ', %d' % (val) 

            if j+1 == dimension:
                print(info)

def read_input():
    global dimension, dict_input

    f = open("input_01.txt", 'r')
    for i, line in enumerate(f.readlines()):
        if i==0:
            dimension = int(line.strip())
        else:
            content = line.strip().split(', ')
            dict_input[i-1] = {}
            for j, ele in enumerate(content):
                dict_input[i-1][j] = int(ele)

    print_dict(dict_input)

def init_mapping(n):
    d = {}
    for i in range(n):
        d[i] = {}
        for j in range(n):
            d[i][j] = (-1, -1)
    return d

def print_map():
    print('--------------------------------------------------')
    for i in range(dimension):
        info = ""
        for j in range(dimension):
            ival, jval = dict_map[i][j]
            if len(info) == 0:
                info = '(%d,%d)' % (ival, jval)
            else:
                info +=  '  (%d,%d)' % (ival, jval) 

            if j+1 == dimension:
                print(info)

def get_mapping(n):
    global dict_map

    if n == dimension:
        dict_map = init_mapping(n)

    if n > 0:
        offset = int( (dimension - n) / 2 )
        if n > 1:
            for i in range(n-1):
                dict_map[offset][i+offset]               = (i+offset, dimension-1-offset)
                dict_map[dimension-1-offset][i+1+offset] = (i+1+offset, offset)
                dict_map[i+offset][dimension-1-offset]   = (dimension-1-offset, dimension-1-offset-i)
                dict_map[i+1+offset][offset]             = (offset, dimension-1-i-1-offset)

            get_mapping(n-2)

        if n == 1:
            dict_map[offset][offset] = (offset, offset)

def transform():
    dict_out = init_mapping(dimension)
    for i in range(dimension):
        info = ""
        for j in range(dimension):
            iprime, jprime = dict_map[i][j]
            dict_out[iprime][jprime] = dict_input[i][j]

    print_dict(dict_out)

if __name__ == "__main__":
    create_input(5)

    read_input()
    get_mapping(dimension)
    transform()
