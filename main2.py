n = int(input())
result = [0] * (n+1)
result[1] = 1
for i in range(2, n+1):
    result[i] = i + result[i-1]
print(result[n])