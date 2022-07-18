N = int(input())
nums = list(map(int, input().split()))

for i in nums : 
    if i < 2 : 
        N -= 1
        pass
    for k in range(2, i//2) : 
        if i%k == 0 : 
            N -= 1
            break
print(N)
# 실험실험
