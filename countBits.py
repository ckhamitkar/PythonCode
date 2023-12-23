from typing import List
def countBits(n: int) -> List[int]:
    num = {}
    for i in range(0,n+1):
        # print(i)
        num[i] = 0
        s = list(bin(i))
        for j in range(2,len(s)):
            # print(s[j])
            if s[j] == '1':
                num[i] += 1
                # print(num[i])
        # print("\n")
    # print(num)
    bits = num.values()
    # print(bits)
    return bits
countBits(8)