class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        counter = 1
        prefix = ""
        if len(strs) == 1:
            return strs[0]
        if strs == []:
            return ""
        
        max_len = -1
        for i in strs:
            if max_len < len(i):
                max_len = len(i)
            if len(i) == 0:
                return ""
        
        while True:
            for i, str_ in enumerate(strs):
                prefix = str_[0:counter]
                print(prefix)
                if i == 0:
                    prefix_ = prefix
                    continue
                if prefix != prefix_:
                    return prefix[0:counter-1]
            
            if max_len == counter:
                return prefix[0:counter]

            counter += 1
                
            