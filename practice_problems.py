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

"""
6.Task : Write a Function
An extra day is added to the calendar almost every four years as February 29, and the day is called a leap day. It corrects the calendar for the fact that our planet takes approximately 365.25 days to orbit the sun. A leap year contains a leap day.

In the Gregorian calendar, three conditions are used to identify leap years:
The year can be evenly divided by 4, is a leap year, unless:
The year can be evenly divided by 100, it is NOT a leap year, unless:
The year is also evenly divisible by 400. Then it is a leap year.
This means that in the Gregorian calendar, the years 2000 and 2400 are leap years, while 1800, 1900, 2100, 2200, 2300 and 2500 are NOT leap years. 

Given a year, determine whether it is a leap year. If it is a leap year, return the Boolean True, otherwise return False.

Note that the code stub provided reads from STDIN and passes arguments to the is_leap function. It is only necessary to complete the is_leap function.

Input Format
Read year, the year to test.

Output Format
The function must return a Boolean value (True/False). Output is handled by the provided code stub.
"""
#Solution
def is_leap(year):
    leap = False
    
    if (year % 400 == 0) and (year % 100 == 0):
        leap = True
    elif (year % 4 ==0) and (year % 100 != 0):
        leap = True
    else:
        leap = False
    
    return leap

year = int(input())
print(is_leap(year))

"""
7. Task : Prit Function
Without using any string methods, try to print the following:
123....n
Note that "....." represents the consecutive values in between.

Example
n = 5
Print the string 12345.
"""
#Solution
if __name__ == '__main__':
    n = int(input())
    for i in range(1, n+1):
        print(i, end="")
"""
8.Task : Find the Runner-Up Score
Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. You are given n scores. Store them in a list and find the score of the runner-up.

Input Format
The first line contains n. The second line contains an array A[] of n integers each separated by a space.
Output Format
Print the runner-up score.
"""
#Solution
if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    
arr1 = list(set(arr))
arr1.sort()

print(arr1[-2])
