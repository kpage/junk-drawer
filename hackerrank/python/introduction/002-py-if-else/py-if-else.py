#!/bin/python3

Given an integer, , perform the following conditional actions:

If  is odd, print Weird
If  is even and in the inclusive range of  to , print Not Weird
If  is even and in the inclusive range of  to , print Weird
If  is even and greater than , print Not Weird

N = int(input())
even = N % 2 == 0
odd = not(even)

if odd:
    print("Weird")
elif even and N in range(6, 21):
    print("Weird")
else:
    print("Not Weird")


