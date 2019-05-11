#동명이인을 찾는 알고리즘

#두 번 이상 나온 이름 찾기
#입력 : 이름이 n개 들어 있는 리스트
#출력 : 이름 n개 중 반복되는 이름의 집합

def find_same_name(a):
    n = len(a)                      #리스트의 자료 개수를 n에 저장
    result = set()                  #결과를 저장할 빈 집합
    for i in range(0, n-1):         #0부텉 n-2까지 반복하는데 a[n-1]은 이미 앞에서 비교함
        for j in range(i + 1, n):
            if a[i] == a[j]:
                result.add(a[i])
    return result

name = ["Tom", "Jerry", "Mike", "Tom"]
print(find_same_name(name))
name2 = ["Tom", "Jerry", "Mike", "Tom", "Mike"]
print(find_same_name(name2))

#알고리즘 분석
#0번 이름은 n-1번 비교 ~ n-1번 이름은 0번 비교
#전체 횟수는 0번부터 n-1번 까지 합 => 1에서 n까지 합
#n(n-1)/2 -> O(n^2) 빅오표기
