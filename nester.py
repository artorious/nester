#!/usr/bin/env python3
'''module provides a function nester() 
Prints out python any lists to stdout.
'''

def nester(the_list, level=0):
    '''Takes a positional arg the_list, any python list.  
    Second optional arg level,  inserts tab-stops when a nested list is 
    encountered.

    Returns each item in the provided list recursively on it's own line.
    '''
    for each_item in the_list:
        if isinstance(each_item, list):
            nester(each_item, level + 1) # Increament indent level on each recursive call
        else:
            for tab_stop in range(level): # No. of tab-stops used
                print('\t', end='') # Display a TAB char for each level of inentation
            print(each_item)

