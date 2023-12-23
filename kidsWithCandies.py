from typing import List
def kidsWithCandies(candies: List[int], extraCandies: int) -> List[bool]:
        output = [False]*len(candies)
        maxcandies = max(candies)
        for i in range(0,len(candies)):
            if candies[i] + extraCandies >= maxcandies:
                output[i] = True
        print(output)
        return output
    
kidsWithCandies([2,3,5,1,3],3)