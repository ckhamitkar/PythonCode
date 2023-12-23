def longestSubarray(nums):
    max_length = 0  # Initialize the maximum length of subarray with zeros
    left = 0  # Initialize the left pointer
    count_zeros = 0  # Initialize the count of zeros in the subarray

    for right in range(len(nums)):
        if nums[right] == 0:
            count_zeros += 1  # Increment the count of zeros if the current element is zero

        while count_zeros > 1:
            if nums[left] == 0:
                count_zeros -= 1  # Decrement the count of zeros if the left element is zero
            left += 1  # Move the left pointer to the right

        max_length = max(max_length, right - left + 1)  # Update the maximum length of subarray

    return max_length - 1 if max_length > 0 else 0  # Return the maximum length of subarray minus 1 if it is greater than 0, else return 0
