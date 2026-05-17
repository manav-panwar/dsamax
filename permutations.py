def worker(nums):
    
    outt = []
    n = len(nums)
    used = [False] * n

    def bt(sol):

        if len(sol) == n:
            outt.append(sol[:])
            return

        for i in range(n):

            if used[i]:
                continue

            used[i] = True
            sol.append(nums[i])
            bt(sol)

            used[i] = False
            sol.pop()
    
    bt([])
    return outt