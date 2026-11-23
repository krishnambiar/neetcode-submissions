class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dicc = {}
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            if s[i] not in dicc:
                dicc[s[i]] = 1
            else: #alr exists
                dicc[s[i]] += 1
        #if the value is odd, thats not possible 
        for i in range(len(t)):
            if t[i] not in dicc:
                return False
                #dicc[t[i]] = -1
            else: #alr exists
                dicc[t[i]] -= 1
        for value in dicc.values():
            if value != 0:
                return False
        return True
        