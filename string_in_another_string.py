def isSubsequence(s: str, t: str) -> bool:
        s_index = t_index = 0

        while s_index < len(s) and t_index < len(t):
            if s[s_index] == t[t_index]:
                s_index += 1
            t_index += 1
        return s_index == len(s)
            
            
print(isSubsequence("abc","ahbgdc"))
print("===")
print(isSubsequence("abq","ahbgdc"))
print(isSubsequence("ahbgdc","abc"))