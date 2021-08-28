class Solution:
    def hammingWeight(self, n: int) -> int:
        # arr = [0] * (n+1)
        # for i in range(1, n+1):
        #     # if i is odd add 1, elif i is even dont add
        #     arr[i] = arr[i//2] + i%2
        # return arr[n]
        return bin(n).count('1')