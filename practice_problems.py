# 1. Write a program to print Hello World
#Solution
print("Hello World")

"""
2.Task : Python If Else
Given an integer, , perform the following conditional actions:

If n is odd, print Weird
If n is even and in the inclusive range of 2 to 5, print Not Weird
If n is even and in the inclusive range of 6 to 20, print Weird
If n is even and greater than 20, print Not Weird

Input Format:
A single line containing a positive integer, n.

Output Format
Print Weird if the number is weird. Otherwise, print Not Weird.
"""
#Solution
n = int(input())
if n % 2 == 1:
    print("Weird")
if n % 2 == 0:
    if n >= 2 and n<=5:
        print("Not Weird")
    if n >= 6 and n <= 20:
        print("Weird")
    if n>20:
        print("Not Weird")

"""
3.Task : Arithmetic Operators
The provided code stub reads two integers from STDIN, a and b. Add code to print three lines where:

1.The first line contains the sum of the two numbers.
2.The second line contains the difference of the two numbers (first - second).
3.The third line contains the product of the two numbers.
"""

#Solution
a = int(input())
b = int(input())
print(a+b)
print(a-b)
print(a*b)

"""
4.Task : Division
The provided code stub reads two integers, a and b, from STDIN.

Add logic to print two lines. The first line should contain the result of integer division, a // b. The second line should contain the result of float division, a /b .

No rounding or formatting is necessary.
"""
#Solution
a = int(input())
b = int(input())

print(a//b)
print(a/b)

"""
5.Task : Loops
The provided code stub reads an integer, n, from STDIN. For all non-negative integers i<n, print i^2.

Input Format
The first and only line contains the integer, n.

Output Format
Print n lines, one corresponding to each i.
"""

#Solution
n = int(input())
for i in range(0, n):
    print(i*i)
