#최대값을 구하는 알고리즘

def find_max(a):   #리스트 길이(자료 개수)를 구하는 함수
    max_v = a[0]
    for i in range(1, n):
        if a[i] > max_v:
            max_v = a[i]
        return max_v

v = [17, 92, 18, 33, 58, 7, 33, 42]
print(find_max(v))