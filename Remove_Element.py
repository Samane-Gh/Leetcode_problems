nums = list(int(num) for num in input().strip().split(','))    
print("So which value do you want to remove? ")
val = int(input())
def removeElement(nums: [int], val: int) -> int:
    for i in range(len(nums)):
        if val in nums:
            nums.remove(val)
    return nums

print(removeElement(nums,val))