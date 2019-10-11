MainList = []
n, m = map(int, input().strip().split())
for _ in range(n):
    MainList.append(list(map(int, input().strip().split())))
k = int(input())
MainList.sort(key=lambda x:x[k])
for x in MainList:
    print(*x)
