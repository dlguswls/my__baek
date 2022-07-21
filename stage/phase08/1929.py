M, N = map(int, input().split())
for i in range(M, N+1) : 
    no_sosu = 0
    if i >= 2 : 
        for k in range(2, i) : 
            if i%k == 0 : 
                no_sosu += 1
                break
    else : 
        no_sosu += 1
    if no_sosu == 0 : 
        print(i)