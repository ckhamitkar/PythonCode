from typing import List
def pivotIndex(nums: List[int]) -> int:
    s,count=sum(nums),0
    for ind in range(len(nums)):
        count+=nums[ind]
        if count==s:
            return ind
        s-=nums[ind]
        return -1

pivotIndex([1,7,3,6,5,6])
pivotIndex([1,2,3])
pivotIndex([2,1,-1])