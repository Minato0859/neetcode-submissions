class Solution:
    def isPalindrome(self, s: str) -> bool:
        collapsed_str= s.replace(" ", "")
        str_list = [char for char in collapsed_str if char.isalnum()] 
        #or we could do = list(collapsed_str) and 
        ## //[^a-zA-Z0-9] means "anything that is NOT a letter or number"
        # clean_text = re.sub(r'[^a-zA-Z0-9]', '', text)
        str_listreverse = str_list[::-1]
        str1 = "".join(str_list).lower()
        str2 = "".join(str_listreverse).lower()

        return str1==str2

