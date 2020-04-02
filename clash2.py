import sys
import string
"""
s = input().lower()
f = input()
"""
s = "sAmMyJr".lower()
f = "Xxxxx, Xx."
print(f,file=sys.stderr)
print(s,file=sys.stderr)
#print(dir(string),file=sys.stderr)
c=0
for i in range(len(f)):
    if f[i].isupper() and f[i] == 'X':
        print(s[c].upper(),end='')
        c+=1
    elif not f[i] in 'x':#string.ascii_letters:
        print(f[i],end='')
    else:
        print(s[c],end='')
        c+=1
