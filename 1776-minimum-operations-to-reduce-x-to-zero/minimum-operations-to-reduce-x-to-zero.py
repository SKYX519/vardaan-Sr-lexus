class Solution:
    def minOperations(self, nums, x):
        total = sum(nums)
        target = total - x

        # Impossible to keep anything
        if target < 0:
            return -1

        # If target is 0, remove everything
        if target == 0:
            return len(nums)

        left = 0
        current_sum = 0
        max_length = -1

        for right in range(len(nums)):
            current_sum += nums[right]

            # Shrink window if sum becomes too large
            while current_sum > target and left <= right:
                current_sum -= nums[left]
                left += 1

            # Found a valid subarray
            if current_sum == target:
                max_length = max(max_length, right - left + 1)

        if max_length == -1:
            return -1

        return len(nums) - max_length