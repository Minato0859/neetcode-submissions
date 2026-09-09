class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        lookup_hash = dict()
        for index, anagram in enumerate(strs):
            sorted_anag = sorted(list(anagram))
            sorted_anag = "".join(sorted_anag)
            if lookup_hash.get(sorted_anag) != None:
                lookup_hash[sorted_anag].append(anagram)
            else:
                lookup_hash[sorted_anag] = [anagram]
        
        return list(lookup_hash.values())

