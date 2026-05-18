from collections import defaultdict, deque

def minJumps(arr: list[int]) -> int:

    n = len(arr)
    q = deque([0])
    seen = defaultdict(list)
    distance = 0
    visited = {0}


    for i in range(n):
        seen[arr[i]].append(i)
    
    while q:
        for _ in range(len(q)):
            idx = q.popleft()
                
            if idx == n - 1:
                return distance

            left = idx - 1
            right = idx + 1

            if left >= 0 and left not in visited:
                q.append(left)
                visited.add(left)
            
            if right < n and right not in visited:
                q.append(right)
                visited.add(right)

            for nei in seen[arr[idx]]:
                if nei in visited:
                    continue
                q.append(nei)
                visited.add(nei)
            seen[arr[idx]] = []

        distance += 1
