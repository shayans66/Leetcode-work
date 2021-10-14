class Solution:
    def numSquares(self, n: int) -> int:
        arr = [n] * (n+1)
        arr[0] = 0
        
        for i in range(1, n+1):
            for s in range(1, i+1):
                squared = s*s
                if i-squared < 0:
                    break
                # arr[i] = min(arr[i], 1+arr[i - squared])
                if 1+arr[i-squared] < arr[i]:
                    arr[i] = arr[i-squared]+1
            # print(arr)
        return arr[n]