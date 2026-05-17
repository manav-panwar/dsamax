def worker(candidates, target):

    outt = []
    n = len(candidates)

    def bt(start, remaining, sol):

        if remaining == 0:
            outt.append(sol[:])
            return
        
        for i in range(start, n):

            if candidates[i] > remaining:
                break

            sol.append(candidates[i])

            bt(i, remaining - candidates[i], sol)

            sol.pop()

    bt(0, target, [])
    return outt
