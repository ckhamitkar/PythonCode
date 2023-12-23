from typing import List
def maxProduct(nums: List[int]) -> int:
    biggest = 0
    secondBiggest = 0
    
    for i in nums:
        if i > biggest:
            biggest = i
        elif i > secondBiggest:
            secondBiggest = i
            
    return (biggest-1)*(secondBiggest-1)