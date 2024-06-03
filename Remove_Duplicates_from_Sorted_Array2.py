def removeDuplicates(nums: list[int]) -> int:
   
    i = 1
    while i< (len(nums)-2):
        if (nums[i] == nums[i-1] and nums[i] == nums[i+1]):
            nums.pop(i)
            i = i-1
        i = i+1
    return (len(nums))
