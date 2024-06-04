def majorityElement(nums: list[int]) -> int:
    my_dict = dict()
    n = int(len(nums)/2 + 1)
    for i in nums:
        my_dict[i] = nums.count(i)
        if my_dict[i] >= n: 
            key = list(filter(lambda x: my_dict[x] == my_dict[i], my_dict))[0]
            return (key)
