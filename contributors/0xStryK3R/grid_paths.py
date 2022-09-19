class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def uniquePaths(self, A, B):
        # Optimisation, so that iteration is done for from larger of two numbers to m+n-2
        B, A = sorted([A, B])
        path = 1
        for i in range(A, (A + B - 1)):
            path = (path * i) // (i - A + 1)

        return path
