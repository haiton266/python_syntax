# https://leetcode.com/problems/word-pattern/description/?envType=problem-list-v2&envId=hash-table

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        pattern_to_s = {}
        s_to_pattern = {}
        s = s.split()
        
        # Check if lengths of pattern and s are different
        if len(pattern) != len(s):
            return False
        
        for pat, word in zip(pattern, s):
            if pat not in pattern_to_s and word not in s_to_pattern:
                pattern_to_s[pat] = word
                s_to_pattern[word] = pat
            elif pattern_to_s.get(pat) != word or s_to_pattern.get(word) != pat:
                return False
        
        return True

# Example usage
print(Solution().wordPattern("abba", "dog cat cat dog"))