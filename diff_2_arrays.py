from typing import List
def findDifference(nums1: List[int], nums2: List[int]) -> List[List[int]]:
    set1 = []
    set2 = []
    for i in nums1:
        if i not in nums2 and i not in set1:
            set1.append(i)
    print(set1)
      
    for j in nums2:
        if j not in nums1 and j not in set2:
            set2.append(j)
    print(set2)
    set = [set1,set2]
    print(set)

findDifference([1,2,3],[2,4,6])
findDifference([1,2,3,3],[1,1,2,2])