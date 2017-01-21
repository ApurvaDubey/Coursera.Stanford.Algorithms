#!/usr/bin/env python
# merge sort
# @author: Apurva Dubey (apurva.dubey@gmail.com)
# Nov 2016

import random

def merge(left_sorted, right_sorted):
    """
    Takes two sorted arrays and merges the results using
    two-finger technique. 

    Inputs
    ------
    left_sorted : a sorted list numeric values
    right_sorted : a sorted list numeric values

    Output
    ------
    A merged list of sorted values, created
    from left_sorted and right_sorted
    """

    len_left = len(left_sorted)
    len_right = len(right_sorted)

    # define the final result as an empty array
    merged = []

    # define pointer for left and rigth sorted arrays
    walk_left = 0
    walk_right = 0

    # keep working till the merged list hasn't totally
    # consumed the two smaller lists
    while (len(merged) < len_left + len_right):

        # in case the left list is exhausted
        if walk_left == len_left:
            merged = merged + right_sorted[walk_right:]
            break

        # in case the right list is exhausted
        elif walk_right == len_right:
            merged = merged + left_sorted[walk_left:]
            break

        # if both lists have elements to go 
        else:
            # if the element in left list is smaller than
            # the one in right list
            if left_sorted[walk_left] < right_sorted[walk_right]:
                merged.append(left_sorted[walk_left])
                walk_left = walk_left + 1

            # if the element in left list is bigger than
            # the one in right list
            elif left_sorted[walk_left] > right_sorted[walk_right]:
                merged.append(right_sorted[walk_right])
                walk_right = walk_right + 1

            # if the elements in both lists are equal
            else:
                merged.append(left_sorted[walk_left])
                merged.append(right_sorted[walk_right])
                walk_left = walk_left + 1
                walk_right = walk_right + 1
        
    return merged # return the final merged array thus obtained


def merge_sort(arr):
    """
    Sorts an array of numbers using merge sort algorithm

    Inputs
    ------
    arr: a list of unsorted numeric values

    Output
    ------
    A list of sorted values
    """
    
    n = len(arr) # find the length of array

    # base case
    if n==1:
        return arr
    
    else:
        left_sorted =  merge_sort(arr[:n/2]) # take the left half and sort it
        right_sorted = merge_sort(arr[n/2:]) # take the right half and sort it

        # combine left and right sorted halves, merge them and send the results back
        return merge(left_sorted,right_sorted) 

def main():

    # create a ranom array of unsorted elements
    arr = [random.randint(10,2000) for i in xrange(100)]

    # print the unsorted array
    print "unsorted array"
    print arr

    # print sorted results, using merge sort
    print "\n----------------\nCalling merge sort...\n----------------"
    print merge_sort(arr)


if __name__ == '__main__':
    main()
    
