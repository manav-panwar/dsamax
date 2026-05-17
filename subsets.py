def worker(nums):

    outt = []
    sol = []
    n = len(nums)

    def bt(i):

        if i == n:
            outt.append(sol[:])
            return

        sol.append(nums[i])
        bt(i + 1)

        sol.pop()
        bt(i + 1)
    
    bt(0)
    return outt