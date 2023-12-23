from typing import List
def kidsWithCandies(candies: List[int], extraCandies: int) -> List[bool]:
        output = []
        if len(output) == len(candies): 
            return output
        if candies[0] + extraCandies >= max(candies):
            kidsWithCandies()

    
kidsWithCandies([2,3,5,1,3],3)