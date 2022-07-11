n = int(input())
a = 1  # 분자
b = 1  # 분모
cnt = 1
while n>0 : 
    plus = 1
    minus = cnt
    for _ in range(cnt) : 
        if cnt % 2 == 1 : 
            a = minus
            minus -= 1
            b = plus
            plus += 1
            n -= 1
            if n<=0 : 
                break
        else : 
            a = plus
            plus += 1
            b = minus
            minus -= 1
            n -= 1
            if n<=0 : 
                break

    cnt += 1

print(str(a)+'/'+str(b))
