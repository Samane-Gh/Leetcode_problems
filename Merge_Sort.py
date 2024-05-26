
def merge(nums1: list[int], m: int, nums2: list[int], n: int) -> None:
    k = m + n - 1
    i, j = m - 1, n - 1
    while j >= 0:
            if i >= 0 and nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1
    return(nums1)
print(merge(nums1= [1,3,13,0,0,0], m=3, nums2= [2,5,6] , n=3))