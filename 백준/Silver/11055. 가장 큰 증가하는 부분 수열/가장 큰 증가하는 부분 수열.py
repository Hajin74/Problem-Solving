n = int(input())
arr = list(map(int, input().split()))

dp = arr.copy()

for i in range(1, n):
    for j in range(i):
        if arr[j] < arr[i]: # 기준 값보다 작다면 증가하는 부분 수열이지
            dp[i] = max(dp[i], dp[j] + arr[i])

print(max(dp))