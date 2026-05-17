def worker(n, k):

    outt = []

    def bt(start, sol):
        if len(sol) == k:
            outt.append(sol.copy())
            return

        for i in range(start, n + 1):
            sol.append(i)
            bt(i + 1, sol)
            sol.pop()
    
    bt(1, [])
    return outt