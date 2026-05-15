def worker(nums):

    n = len(nums)
    pre = [1] * n
    post = [1] * n
    outt = [1] * n
        

    for i in range(1, n):
        pre[i] = pre[i - 1] * nums[i - 1]

    for i in range(n-2, -1, -1):
        post[i] = post[i + 1] * nums[i + 1]

    for i in range(n):
        outt[i] = pre[i] * post[i]
        
    return outt
