k, n, w = map(int,input().split())
#w ko loop kiya

for i in range(1,w+1):
    n = n - (k*i)

if n < 0:
    print(-n)
else:
    print(0)










