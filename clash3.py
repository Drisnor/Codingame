import sys

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())
# To debug: print("Debug messages...", file=sys.stderr)
cpt=0
for i in range(n):
    row = input()
    if str(i) in row :
        cpt += 1
print(cpt)

"""
n = int(input())
r = 0
for i in range(n):
    a = list(map(int, input().split()))
    for x in a:
        r += x == i
print(r)
"""


"""
n = int(input())
c=0
for i in range(n):
    c += input().count('{}'.format(i))

# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)

print(c)
"""
