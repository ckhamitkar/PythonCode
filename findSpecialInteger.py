from typing import List
def findSpecialInteger(arr: List[int]) -> int:
        arr_ct = {}
        ttl_length = len(arr)
        for i in range(0,ttl_length):
            if arr[i] in arr_ct.keys():
                arr_ct[arr[i]] += 1
            else:
                arr_ct[arr[i]] = 1
        for j in arr_ct.keys():
            if arr_ct[j]/ttl_length > 0.25:
                print(j)    
                return(j)
findSpecialInteger([1,2,2,6,6,6,6,7,10])