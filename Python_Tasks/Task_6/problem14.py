# Problem 14: Set .intersection() Operation
# Hacker Rank Link: https://www.hackerrank.com/challenges/py-set-intersection-operation/problem

# Enter your code here. Read input from STDIN. Print output to STDOUT

n = int(input())
english = set(map(int, input().split()))

b = int(input())
french = set(map(int, input().split()))

print(len(english.intersection(french)))
