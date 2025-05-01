
n = input()

if len(n) == 4 or len(n)== 7:
    
    if all(digit in {'4', '7'} for digit in n):
            print('YES')
    else:
            print('NO')
else:
    print('NO')
    
    




# chatgpt outcome =>


n = input().strip()
# count how many lucky digits (4 or 7) are in n
x = sum(1 for c in n if c in ('4', '7'))
# it’s nearly lucky if that count is exactly 4 or exactly 7
print("YES" if x in (4, 7) else "NO")
