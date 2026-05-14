from collections import Counter
def worker(nums):

    maxx = max(nums)

    if len(nums) != maxx + 1:
        return False
        
    c = Counter(nums)

    for i in range(1, maxx):
        if c[i] != 1:
            return False
            
    return c[maxx] == 2

