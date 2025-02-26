from primePy import primes

count = 0
for i in range(100, 1000 + 1, 1):
    if primes.check(i) == True:
        count += 1

print("100부터 1000까지 소수의 총 갯수는", count, "개 입니다.")