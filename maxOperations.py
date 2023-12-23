from typing import List
def maxOperations(nums: List[int], k: int) -> int:
        d = {}
        count = 0
        for x in nums:
            print("Nums is: " + str(x))
            if d.get(k - x, 0) > 0:
                print("Get is :" +str(d.get(k - x, 0)))
                count+=1
                d[k-x]-=1
            else:
                d[x] = d.get(x, 0) + 1
        return count
maxOperations([1,2,3,4],5)