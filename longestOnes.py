from typing import List
import math
def longestOnes(nums: List[int], k: int) -> int:
        left = 0
        zeros = 0
        res = -(math.inf)

        for right in range(len(nums)):
            if nums[right] == 0:
                zeros += 1

            while zeros > k:
                if nums[left] == 0:
                    zeros -= 1
                left += 1
            res = max(res, right - left + 1)
        print(res)
        return res    
    
        # left_ptr, right_ptr, numlen = 0, 1, len(nums)
        # ct, max_ct = 0, 0
        # zero_ct = 0
        # while (left_ptr < numlen and right_ptr < numlen):
        #     if nums[left_ptr] == 0:
        #         left_ptr += 1
        #     elif nums[left_ptr] == 1:
        #         ct += 1
        #     if nums[right_ptr] == 1:
        #         right_ptr += 1
        #         ct += 1
        #     elif nums[right_ptr] == 0:
        #         if ct > max_ct:
        #             max_ct = ct
        #             zero_ct += 1
        #             while zero_ct <= k and right_ptr < numlen:
        #                 right_ptr += 1
        #                 if nums[right_ptr] == 0:
        #                     right_ptr += 1
        #                     ct += 1
        #                 elif nums[right_ptr] == 1:
        #                     right_ptr += 1
        #                     ct += 1
        # print(str(ct))                            
                
longestOnes([1,1,1,0,0,0,1,1,1,1,0],2)