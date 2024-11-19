class Solution:
  def maximumSubarraySum(self, nums: List[int], k: int) -> int:
    n = len(nums)
    max_sum = 0
    temp_sum = 0
    left_index = 0
    elements = set()

    for right_index in range(n):
      if nums[right_index] not in elements:
        temp_sum += nums[right_index]
        elements.add(nums[right_index])

        # Length of subarray reach k
        if right_index - left_index + 1 == k:
          # Calculate num
          max_sum = max(temp_sum, max_sum)

          # Shift left_index for next check
          temp_sum -= nums[left_index]
          elements.remove(nums[left_index])
          left_index += 1

      # New num is already exist
      else:
        # Shift left_index to make the sub_array has distinct num
        while nums[left_index] != nums[right_index]:
          temp_sum -= nums[left_index]
          elements.remove(nums[left_index])
          left_index += 1

        # Shift 1 more since nums[left_index] == nums[right_index] 
        left_index += 1

    return max_sum
