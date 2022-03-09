def sort_list(nums: list[int]) -> list[int]:
    n = len(nums)
    i = 0
    j = 0

    while i < n - 1:
        k = n - i - 1
        j = 0
        while j < k:
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
            j += 1
        i += 1
    return nums


print(sort_list([64, 35, 25, 12, 22, 11, 90]))
