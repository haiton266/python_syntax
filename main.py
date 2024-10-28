class Solution:
    def maxScore(self, s: str) -> int:
        nums = [int(char) for char in s] # Convert str to list int
        n = len(nums)
        sum = [0] * n
        for id, num in enumerate(nums):
            if id == 0:
                sum[id] = num 
            else:
                sum[id] = sum[id - 1] + num
        
        result = 0
        for loc in range(0, n-1):
            result = max(result, loc - sum[loc] + 1 + sum[n-1] - sum[loc])
        return result
    

# TEst
s = "00111"
sol = Solution()
print(sol.maxScore(s)) # 5