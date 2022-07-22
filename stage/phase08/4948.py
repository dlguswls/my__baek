# 시간 초과
arr_all = []
while True : 
    arr = []
    num = int(input())
    if num == 0 : 
        break
    for n in range(num+1, 2*num+1) : 
        if n == 1 : 
            continue
        for i in range(2, int(n*0.5)+1) : 
            if n%i==0 : 
                break
        else : 
            arr.append(n)
    arr_all.append(len(arr))
for i in arr_all : 
    print(i)
