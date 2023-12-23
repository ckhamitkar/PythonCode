from typing import List
def maxProfit(prices: List[int]) -> int:
    return max(map(sub, prices, accumulate(prices, min)))
        
maxProfit([7,1,5,3,6,4])
maxProfit([7,6,4,3,1])