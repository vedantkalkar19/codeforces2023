"""
input - n,h 

n times number 
if n times > h  - count as 2 
else count as 1 

add
"""

n, h = map(int,input().split())
l = map(int,input().split())
width = 0


for i in l:
    if i <= h:
        width += 1
    else:
        width +=2

print(width)

