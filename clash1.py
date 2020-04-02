import sys
w, d, outer = "welcome", "*", 1
o = int(outer)
l = len(w)+2+2*o
m = 2*o+1
for j in range(m):
    if j != m//2 :
        for i in range(l):
            print(d, end="")
    else :
        print()
        print(d+d, w, d+d)
