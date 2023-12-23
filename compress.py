from typing import List
def compress(chars: List[str]) -> int:
    seti = chars[0]
    ending = {}
    starting = {}
    starting[chars[0]] = 0
    ending[chars[0]] = 0
    for i in range(1,len(chars)):
        if chars[i-1] != chars[i]:
            seti = seti + chars[i]
            ending[chars[i-1]] = i-1
            starting[chars[i]] = i
    ending[seti[-1]] = len(chars)-1
    d = []
    for k in list(seti):
        v = ending[k] - starting[k] + 1
        d.append(k)
        if v != 1:
            d.append(str(v))
    print(d)
    return len(d)

        
    

        
        
            
    
compress(["a","a","b","b","c","c","c"]) # ["a2b2c3"]
compress(["a"]) # [a]
compress(["a","b","b","b","b","b","b","b","b","b","b","b","b"]) # ["ab12"]
