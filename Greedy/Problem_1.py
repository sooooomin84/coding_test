# 거스름돈 / 사용할 동전 500원,100원, 50원, 10원
# 거슬러 줄 돈: N = 1260
# 거슬러 줄 동전의 수 :  count

N = 1260
count = 0

coins = [500, 100, 50, 10]

for coin in coins:
    count += N // coin  # // 몫 연산자
    N %= coin   # % 나머지 연산자

print(count)