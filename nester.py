#!/usr/bin/env python3
'''module provides a function nester() 
Prints out python any lists to stdout.
'''

def nester(the_list):
    '''Takes a positional argument, any python list
    Returns each item in the provided list recursively on it's own line.
    '''
    for each_item in the_list:
        if isinstance(each_item, list):
            nester(each_item)
        else:
            print(each_item)




