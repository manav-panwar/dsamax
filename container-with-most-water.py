def worker(height):
    nums = height
    n = len(height)
    i, j = 0, n -1
    water = float('-inf')

    while i < j:
        water = max(water, min(nums[i], nums[j]) * (j - i))
        if nums[i] < nums[j]:
            i += 1
        else:
            j -= 1
    
    return water

print(worker(height = [1,1]))