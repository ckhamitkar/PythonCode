from typing import List
def findMaxAverage(nums: List[int], k: int) -> float:
        current_sum = sum(nums[:k])
        max_average = current_sum / k

        for i in range(k, len(nums)):
            current_sum = current_sum - nums[i - k] + nums[i]
            max_average = max(max_average, current_sum / k)
            
        return max_average          
print(str(findMaxAverage([1,12,-5,-6,50,3],4)))
print(str(findMaxAverage([0,1,1,3,3],4)))
print(str(findMaxAverage([5],1)))
print(str(findMaxAverage([-1],1)))
print(str(findMaxAverage([1,4,2,3,2],5)))