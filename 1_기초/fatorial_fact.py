#팩토리얼 알고리즘
#연속한 숫자의 곱을 구하는 알고리즘
#입력 : n
#출력 : 1부터 n까지 연속한 숫자를 곱한 값
#재귀함수 형태
#자기 자신 함수 호출

def factorial(n):
    if n< =1:
        return 1
    return n * factorial(n-1)

print(factorial(1))
print(factorial(5))
print(factorial(10))
