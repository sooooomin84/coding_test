# 숫자 카드 게임

N, M = map(int, input().split())
compare_list = [0, 0]

for i in range(N):
    data = list(map(int, input().split()))
    data.sort()
    if compare_list[1] < data[0]:
        compare_list = [i+1, data[0]]

print(compare_list[1])