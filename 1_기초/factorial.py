#팩토리얼 알고리즘
#연속한 숫자의 곱을 구하는 알고리즘
#입력 : n
#출력 : 1부터 n까지 연속한 숫자를 곱한 값

def factorial(n):
    f = 1
    for i in range(1, n+1):
        f = f * i
    return f

print(factorial(1))
print(factorial(5))
print(factorial(10))

