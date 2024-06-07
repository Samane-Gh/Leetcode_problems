def rotate(nums: list[int], k: int) -> None:
        n = len(nums)-1
        for i in range(0,k):
            nums = nums[n:]+nums[:n]
        return nums
        