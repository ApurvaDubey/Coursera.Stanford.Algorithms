'''
    Program to count the number of inversions in an array
'''

import os
os.chdir('C:/Users/Tulika/Documents/01-DataScience/Algorithms/03-Codes/Course1')

def mergeCount(a,b):
    '''
    Input: two sorted lists
    Output: merged list, and count of inversions found
    '''

    c = [0]*(len(a)+len(b))
    #print "len of c ", len(c)
    cntInv = 0
    i = 0
    j = 0
    k = 0
    
    while k < (len(a)+len(b)):

        if i==len(a): # a has exhausted
            c[k] = b[j]
            j = j + 1
            k = k + 1

        elif j==len(b): # b has exahausted
            c[k] = a[i]
            i = i + 1
            k = k + 1

        elif a[i] < b[j]: # a < b
            c[k] = a[i]
            i = i+1
            k = k+1

        elif b[j] < a[i]: # b < a
            c[k] = b[j]
            j = j+1
            k = k+1
            cntInv = cntInv + (len(a) - i)

        elif b[j] == a[i]: # a==b
            c[k] = b[j]
            j = j+1
            k = k+1

            c[k] = a[i]
            i = i+1
            k = k+1

        else:
            print "error!"

        #print "k is ", k, c
    return c,cntInv


def mergeSortCount(a,leftIndex, rightIndex):
    '''
    Input: an array with left and right index
    Output: merged list, and count of inversions found
    '''
    
    # base case
    if (rightIndex - leftIndex == 1): # i.e. there is only one element
        return [a[leftIndex]],0 # 0 is count of inverstions

    if (rightIndex - leftIndex > 1):
        midIndex = (leftIndex + rightIndex)/2

        L,cntInvL = mergeSortCount(a,leftIndex, midIndex)
        R,cntInvR = mergeSortCount(a,midIndex, rightIndex)
        M,cntInvM = mergeCount(L,R)

    return (M,cntInvL+cntInvR+cntInvM)

def readFile(f):
    file = open(f, 'r')

    input_array = [int(i) for i in  file.readlines()]

    return input_array

if __name__=="__main__":

    input_file = 'Week2_IntegerArray.txt'
    a = readFile(input_file)
    #print a
    #a = [4,6,1,3,1]
    leftIndex = 0
    rightIndex = len(a)
    sorted_array,cntInv = mergeSortCount(a,leftIndex,rightIndex)

    print "Total inversions found are:",cntInv


