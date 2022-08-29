# 1이 될 때까지

N, K = map(int, input().split())
count = 0

if N % K == 0:
    while True:
        N /= K
        count += 1
        if N == 1:
            break
else:
    count += N % K
    N -= N % K
    while True:
        N /= K
        count += 1
        if N == 1:
            break

print(count)