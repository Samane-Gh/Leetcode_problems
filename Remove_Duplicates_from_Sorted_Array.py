def removeDuplicates(nums: list[int]) -> int:
        j = 1                        #keep unrepeated number index --------> then new unrepeated number will be place in this index
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[j] = nums[i]
                j += 1
        return j
    
###################################### Another solution      ##############################################
def removeDuplicates2(nums:list[int]) -> int:
    set_of_nums = set(nums)
    nums.clear()
    for n in set_of_nums:
        nums.append(n)
        nums.sort()
    return len(nums)

    
