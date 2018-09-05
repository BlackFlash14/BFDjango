def count_evens(nums):
  cnt = 0
  for i in range(len(nums)):
   if nums[i]%2 == 0:
      cnt = cnt + 1
  return cnt

def big_diff(nums):
  return abs(min(nums) - max(nums))

  def sum13(nums):
    while 13 in nums:
      if nums.index(13) < len(nums) - 1:
        nums.pop(nums.index(13) + 1)
      nums.pop(nums.index(13))

    return sum(nums)
