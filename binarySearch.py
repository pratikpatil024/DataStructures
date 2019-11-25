def binarySearch(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    if len(nums) == 0:
        return -1

    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1

# nums = [1,3,5,7,11,13,15,17,24,30,37,49]
# target = 20
# print(binarySearch(nums,target))


# def binarySearch(nums, target):
#     """
#     :type nums: List[int]
#     :type target: int
#     :rtype: int
#     """
#     if len(nums) == 0:
#         return -1
#
#     left, right = 0, len(nums)
#     while left < right:
#         mid = (left + right) // 2
#         if nums[mid] == target:
#             return mid
#         elif nums[mid] < target:
#             left = mid + 1
#         else:
#             right = mid
#
#     # Post-processing:
#     # End Condition: left == right
#     if left != len(nums) and nums[left] == target:
#         return left
#     return -1
