def brute_force_search(nums, target):
    for i, num in enumerate(nums):
        if num == target:
            return i  # Return the index if the target is found
    return -1  # Return -1 if the target is not found

# Example usage:
numbers = [4, 2, 7, 1, 9, 5]
target_number = 7
index = brute_force_search(numbers, target_number)
if index != -1:
    print(f"Target number {target_number} found at index {index}.")
else:
    print(f"Target number {target_number} not found.")