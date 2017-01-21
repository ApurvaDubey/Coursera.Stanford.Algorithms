#!/usr/bin/env python
# merge sort
# @author: Apurva Dubey (apurva.dubey@gmail.com)
# Nov 2016

import random

def karatsuba(x,y):
    if len(str(x)) == 1 or len(str(y)) == 1:
        return x*y
    else:
        n = max(len(str(x)),len(str(y)))
        nby2 = n / 2
	
    a = x / 10**(nby2)
    b = x % 10**(nby2)
    c = y / 10**(nby2)
    d = y % 10**(nby2)
	
    ac = karatsuba(a,c)
    bd = karatsuba(b,d)
    ad_plus_bc = karatsuba(a+b,c+d) - ac - bd
       
    # this little trick, writing n as 2*nby2 takes care of both even and odd n
    prod = ac * 10**(2*nby2) + (ad_plus_bc * 10**nby2) + bd

    return prod

    
def main():

    import random

    for i in range(0,1):
        # create a ranom array of unsorted elements
        num1 = 6982 #random.randint(1,20) #3141592653589793238462643383279502884197169399375105820974944592
        num2 = 6982 #random.randint(1,10000) #2718281828459045235360287471352662497757247093699959574966967627

        # print the unsorted array
        if 1==1:

            print num1, num2
            print "answer using ordinary multiplication"
            print num1*num2

            # print sorted results, using merge sort
            print "Calling Karatsuba...\n----------------"
            print karatsuba(num1,num2)


if __name__ == '__main__':
    main()
    
