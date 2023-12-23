from typing import List
def uniqueOccurrences(arr: List[int]) -> bool:
    occurances = {}
    unique = {}
    for i in arr:
        print(i)
        if i not in occurances:
            occurances[i] = 1
        else:
            occurances[i] += 1
    print(occurances)
    for y in occurances.values():
        print(y)
        if y not in unique:
            unique[y] = 1
        else:
            unique[y] += 1
            print("Not unique value " + str(y))
            return False
    print(unique)
    return True        
uniqueOccurrences([1,2,2,1,1,3])
    
    