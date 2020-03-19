class Solution:
    def longestPalindrome1(self, s: str) -> int:
        d = {}
        for i in s:
            if i not in d:
                d[i] = 1
            else:
                d[i] += 1
        count = 0
        for j in d:
            count += d[j] // 2 * 2
            if d[j] % 2 == 1 and count % 2 == 0:
                count += 1
        return count

    def longestPalindrome2(self, s: str) -> int:
        d = {}
        count = 0
        for i in s:
            if (i not in d) or d[i] == 0 :
                d[i] = 1
            else:
                count += 2
                d[i] = 0
        for j in d.values():
            if j == 1 :
                count +=1
                break
        return count
