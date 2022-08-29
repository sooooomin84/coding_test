# 큰 수의 법칙
# N 배열의 길이 / M 더할 수 있는 횟수 / K 가장 큰 수를 연속으로 더할 수 있는 횟수

N, M, K = map(int, input().split())
data = list(map(int, input().split()))
result = 0

data.sort(reverse=True)

first = data[0]
second = data[1]
count = K * (M % K)
result += first * count + second * (M - count)

print(result)