# i-1까지 채워졌을 때, i에서의 경우는 1*2 한 가지
# i-2까지 채워졌을 때, i에서의 경우는 2*1 + 2*1, 2*2 2가지
# ai = ai-1 + ai-2 * 2
n = int(input())

d = [0] * (n+1)

d[1] = 1
d[2] = 3
for i in range(3, n+1):
    d[i] = (d[i-1] + d[i-2] *2) % 796796

print(d)