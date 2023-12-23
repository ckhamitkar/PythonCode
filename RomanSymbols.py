from typing import List
# RomanSymbols
def romanToInt(s: str) -> int:
        symbols = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        doubles = {'IV': 4, 'IX': 9, 'XC': 90, 'CD': 400, 'CM': 900, 'XL': 40}
        total = 0
        i = 0
        # print(symbols)
        # print(doubles) 
        # print(doubles.keys())
        # print(symbols.keys())
        # print(symbols['I'])
        # print(doubles['IV'])
        while i < len(s):
            # print("Now at element " + s[i] + "\n")
            if i + 1 < len(s):
                tmp = s[i] + s[i+1] 
                if tmp in doubles.keys():
                    # print(tmp)
                    # print(doubles[tmp])
                    total = total + doubles[tmp]
                    i += 2
                    # print("The Total is " + str(total))
                    continue
            if s[i] in symbols.keys():
                # print(symbols[s[i]])
                total = total + symbols[s[i]]
                i += 1
                # print("The Total is " + str(total))
                continue
        
        print("The Total is " + str(total))     
        return total
        
romanToInt("LVIII")

print("------------\n\n")

romanToInt("IV")

print("------------\n\n")

romanToInt("MCMXCIV")
                

            
        


