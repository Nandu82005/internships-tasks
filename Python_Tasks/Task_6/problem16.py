# Problem 16: Set .issuperset() Operation
# Hacker ranker Link: <paste the link from your task list>

# Enter your code here. Read input from STDIN. Print output to STDOUT

A = set(map(int, input().split()))
n = int(input())

result = True

for _ in range(n):
    other_set = set(map(int, input().split()))
    if not A > other_set:
        result = False
        break

print(result)
