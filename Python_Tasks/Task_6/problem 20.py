# Problem: Validating Phone Numbers
# Hacker Rank Link: https://www.hackerrank.com/challenges/validating-the-phone-number/problem



# Enter your code here. Read input from STDIN. Print output to STDOUT

import re

N = int(input())

for _ in range(N):
    number = input()
    if re.fullmatch(r'[789]\d{9}', number):
        print("YES")
    else:
        print("NO")
