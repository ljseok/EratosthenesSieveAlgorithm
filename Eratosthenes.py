import math

n = 1000 # 2부터 1000 까지의 소수를 판별
array = [True for i in range(n+1)] # 처음에는 모든 수가 소수인것으로 판정

for i in range(2, int(math.sqrt(n)) +1): # 2부터 n의 제곱근 까지 모든 수를 확인한다
    if array[i] == True: # i가 소수인 경우
        # i를 제외한 i의 배수를 제거
        j = 2
        while i * j <= n:
            array[i * j] = False
            j += 1

for i in range(2, n+1): # 모든 수를 출력
    if array[i]:
        print(i, end=' ')
