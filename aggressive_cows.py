class Solution:
    def solve(self, A, B):
        N = len(A)
        def check(min_distance):
            last_pos = A[0]
            cows = 1
            for i in range(1,N):
                if A[i] - last_pos >= min_distance:
                    last_pos = A[i]
                    cows+=1
            return (cows >= B)

        A.sort()
        left = 1
        right = A[-1] - A[0]
        best_ans = 0
        while left <= right:
            mid = ( left + right ) // 2
            # check viability
            # meaning, is it possible to arrange N cows such that 
            # distance is mid
            # So if we cant arrange N cows, we shift left
            # OR if we can manage more than N cows, we shift right
            if check(mid):
                best_ans = mid
                left = mid + 1
            else:
                right = mid - 1


        return best_ans