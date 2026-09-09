class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        else:
            list_s = sorted(list(s))
            list_t = sorted(list(t))
            if list_s == list_t:
                return True
            else:
                return False
            
            
