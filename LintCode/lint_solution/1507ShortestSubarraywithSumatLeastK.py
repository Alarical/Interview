class Solution:
    """
    @param A: the array
    @param K: sum
    @return: the length
    """
    def shortestSubarray(self, A, K):
        # Write your code here.
        n = len(A)
        dp_sum = [0 for _ in range(n + 1)]
        for i in range(1, n + 1):
            dp_sum[i] = dp_sum[i - 1] + A[i - 1]
        queue = []
        min_length = float('inf')
        for i in range(n + 1):
            if i != 0:
                while len(queue) > 0 and dp_sum[i] <= dp_sum[queue[-1]]:
                    queue.pop()
                print(queue)
                while len(queue) > 0 and dp_sum[i] - dp_sum[queue[0]] >= K:
                    min_length = min(min_length, i - queue[0])
                    queue = queue[1:]
            queue.append(i)
        return -1 if min_length == float('inf') else min_length


