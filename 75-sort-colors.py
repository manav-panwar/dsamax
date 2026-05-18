def worker(nums):
    l, m, r = 0, 0, len(nums) - 1

    while m <= r:
        if nums[m] == 2:
            nums[m], nums[r] = nums[r], nums[m]
            r -= 1
        elif nums[m] == 1:
            m += 1
        else:
            nums[l], nums[m] = nums[m], nums[l]
            m += 1
            l += 1
    
    return nums