class Solution:
    def findJudge(self, n: int, relation: List[List[int]]) -> int:
        trust_count = [0] * (n + 1)
        trusted_count = [0] * (n + 1)

        for u, v in relation:
            trust_count[u] += 1
            trusted_count[v] += 1

        for num in range(1, n + 1):
            if trusted_count[num] == n - 1 and trust_count[num] == 0:
                return num
        return -1


s = Solution()
print(s.findJudge(2, [[1, 2]])) # 2