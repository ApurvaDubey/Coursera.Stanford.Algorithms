'''
About: this program is an implementation of QuickSort
(using left right element as pivot)

@author - Apurva Dubey
'''

import os
import random
from collections import Counter
from random import shuffle
import math

#os.chdir('C:/Users/')

def partition(lst,left,right):
    '''
    Function to find the most common element in the list
    '''    
    pivot = lst[left]

    # set index i, j
    # 'i': is the boundary between 'less than pivot' and 'greater than pivot' i.e. within the scanned part
    # 'j': is the boundary between scanned and unscanned part of the array
    i=left+1

    # run a linear scan of the array starting the second element
    for j in range(left+1,len(lst)):

        # if the element at 'j' is larger than the pivot then let it be
        if lst[j] > pivot:
            pass
        
        # if the element at 'j' is smaller than the pivot
        # then exchange the element at position 'j' with
        # the right element at current position of 'i'
        if lst[j] <= pivot:
            # swap(lst[i],lst[j])
            tmp = lst[i]
            lst[i] = lst[j]
            lst[j] = tmp

            # increment 'i' by one element to the right
            i=i+1
            
    # once the scan is complete, put the pivot element after 'i'
    # so that the pivot is placed in its "rightful" place
    # swap(lst[i-1],pivot)
    tmp = lst[i-1]
    lst[i-1] = lst[left]
    lst[left] = tmp
        
    #print i,"--------------------------"

    return i

def quickSort(lst,left,right,flag=-1):
    '''
    flag = -1 for left index, 0 for median, +1 for right index
    '''

    
    m0 = max(right-left,0)

    #print "m0 is:",lst[left:right+1],m0

    #print "length is:",len(lst), m0
    
    if left < right:

        if flag==0:
            i = lst.index(sorted([lst[int(left+math.ceil((right-left+1)*1.0/2.0))-1],lst[left],lst[right]])[1])

            tmp = lst[i]
            lst[i] = lst[left]
            lst[left] = tmp

        if flag==1:
            tmp = lst[right]
            lst[right] = lst[left]
            lst[left] = tmp
            
        p_index=partition(lst,left,right)
        #print "p_index:",p_index
        
        m1 = quickSort(lst,left,p_index-2,flag)
        #print "m1 is:",m1
        m0 = m0 + m1

        m2 = quickSort(lst,p_index,right,flag)
        #print "m2 is:",m2
        m0 = m0 + m2
    
    else:
        pass

    return m0

def readFile(f):
    '''
    Function to parse the input file
    '''
    file_pointer = open(f, 'r')

    tmp = [int(i.split("\n")[0]) for i in  file_pointer.readlines()]
    input_array = tmp

    return input_array


def example():
    '''
    Run a dummy example to check the correctness of the implementation
    ''' 
    lst = ([i for i in range(0,21)])
    random.shuffle(lst)

    print lst
    print quickSort(lst,0,len(lst)-1,-1)
    
    print "--final sorted list--"
    print lst
   
if __name__=="__main__":

    # read the file
    input_file = 'Week3_QuickSort.txt'
    a = readFile(input_file)

    example()

    print quickSort(a,0,len(a)-1,-1)
    #print a
    #162085 - left most
    #164123 - right most
    #138382 - median


    #size first last median

    #10 25 29 21

    #100 615 587 518

    #1000 10297 10184 8921
