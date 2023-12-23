from typing import List
def twoSum(nums: List[int], target: int) -> List[int]:
        for i in range(0,len(nums)):
            for j in range (i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    print(str(i) + str(j))
                    return [i,j]
        return []
    
twoSum([2,7,11,15],9)