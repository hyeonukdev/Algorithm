# 1부터 n까지 연속된 숫자의 합을 구하는 알고리즘

def sum(n) :
    s = 0
    for i in range(1, n+1):
        s = s + i
    return s

print(sum(10))
print(sum(100))