#!/bin/python

# Enter your code here. Read input from STDIN. Print output to STDOUT

n = int(raw_input())

if n % 2 != 0:
    print "Weird"
else:
    if n >= 2 and n <= 5:
        print "Not Weird"
    elif n >= 6 and n <= 20:
        print "Weird"
    elif n > 20:
        print "Not Weird"