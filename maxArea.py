from typing import List
def maxArea(height: List[int]) -> int:
# Get the minimum of two heights and multiple that with the distance in i to get the area
# We want to return the maximim area that can hold water
    mArea = 0
    for index1, i in enumerate(height):
        for index2, j in enumerate(height):
            if index1 != index2:
                minht = min(i,j)
                length = abs(index1-index2)
                tmp = minht * length
                if tmp > mArea:
                    mArea = tmp
    return mArea
    
    
maxArea([1,8,6,2,5,4,8,3,7])
                