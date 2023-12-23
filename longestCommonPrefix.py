from typing import List
def longestCommonPrefix( strs: List[str]) -> str:
        ans=""
        strs=sorted(strs)
        print(strs)
        first=strs[0]
        last=strs[-1]
        for i in range(min(len(first),len(last))):
            if(first[i]!=last[i]):
                return ans
            ans+=first[i]
        return ans 
                      
longestCommonPrefix(["flower","flow","flight"])
longestCommonPrefix(["dog","racecar","car"])