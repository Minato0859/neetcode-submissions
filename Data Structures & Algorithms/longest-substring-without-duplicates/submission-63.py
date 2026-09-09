class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        substr_set = set()
        left = 0
        right = 1
        if len(s) > 0:
            substr_set.add(s[left])
        else:
            return 0
        current_count =1
        max_count = 1
        
        while right < len(s):
            if s[right] not in substr_set:
                current_count +=1
                substr_set.add(s[right])
                right+=1
                max_count = max(current_count, max_count)

            else:
                valid_substr = False
                while not valid_substr and left<right:
                    
                    substr_set.remove(s[left])
                    left+=1
                    current_count -=1
                    # substring = s[left:right+1]
                    # substring_set = 
                    valid_substr = True if (right-left)  == len(substr_set) else False
        
        return max_count
            

                

           

            
       