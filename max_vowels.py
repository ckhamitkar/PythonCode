def max_vowels(s: str, k: int) -> int:
    vowels = {'a', 'e', 'i', 'o', 'u'}
    max_vowels = 0
    left = 0
    vowels_count = 0

    # Iterate through the string using a sliding window approach
    for right in range(len(s)):
        # Check if the current character is a vowel
        if s[right] in vowels:
            vowels_count += 1

        # Check if the window size is equal to k
        if right - left + 1 == k:
            # Update the maximum vowel count
            max_vowels = max(max_vowels, vowels_count)
            
            # If the leftmost character in the window is a vowel, decrement the vowel count
            if s[left] in vowels:
                vowels_count -= 1
            
            # Move the window by incrementing the left pointer
            left += 1

    return max_vowels
