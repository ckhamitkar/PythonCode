from typing import List
def singleNumber(nums: List[int]) -> int:
        ans = 0
        for i in nums:
            ans = ans ^ i
        print(ans)
        return ans
        
singleNumber([2,2,1])
singleNumber([4,1,2,1,2])