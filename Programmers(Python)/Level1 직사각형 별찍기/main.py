import sys

n, m = map(int, sys.stdin.readline().split())

for i in range(m):
    for i in range(n):
        print("*", end="")
    print()