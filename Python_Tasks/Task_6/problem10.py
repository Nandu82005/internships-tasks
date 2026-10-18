# Problem 10: Designer Door Mat
# Hacker Rank Link: <paste the link from your task list>

# Enter your code here. Read input from STDIN. Print output to STDOUT

N, M = map(int, input().split())

for i in range(1, N, 2):
    print(('.|.' * i).center(M, '-'))

print('WELCOME'.center(M, '-'))

for i in range(N - 2, 0, -2):
    print(('.|.' * i).center(M, '-'))
