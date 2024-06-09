def subarray_sum_exists(arr, target):
    if not arr:
        return False
    
    left, right = 0, 0
    current_sum = arr[0]

    while right < len(arr):
        if current_sum == target:
            return True
        elif current_sum < target:
            right += 1
            if right < len(arr):
                current_sum += arr[right]
        else:
            current_sum -= arr[left]
            left += 1
    
    return False

# Example usage:
arr = [4, 2, 7, 1, 9, 5]
target = 17
print(subarray_sum_exists(arr, target))  # Output: True
