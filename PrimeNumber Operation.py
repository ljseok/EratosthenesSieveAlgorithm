import math

m, n = map(int, input().split()) # m --> 시작 n --> 끝
array = [True for i in range(1000001)] # 처음에는 모든 수가 소수인것으로 판정
array[1] = 0 # 소수가 아님

for i in range(2, int(math.sqrt(n))+1): # 2부터 n의 제곱근 까지 모든 수를 확인한다
    if array[i] == True: # 소수일 경우
        j = 2
        while i * j <= n:
            array[i*j] = False
            j += 1

for i in range(m, n+1): # 모든 소수를 출력
    if array[i]:
        print(i)