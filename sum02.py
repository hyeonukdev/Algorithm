# 1부터 n까지 연속된 숫자의 합을 구하는 알고리즘

def sum(n):
    return n * (n+1) // 2 # //는 정수 나눗셈을 의미

print(sum(10))
print(sum(100))