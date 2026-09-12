class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # brute force
        n = len(numbers) - 1
        # for i in range(n):
        #     for j in range(i+1,n):
        #         if numbers[i] + numbers[j] == target:
        #             return [i+1,j+1]

        # optimal
        l , r = 0 , n

        while l < r:
            if numbers[l] + numbers[r] > target:
                r-=1 
            elif numbers[l] + numbers[r] < target:
                l+=1
            else:
                return [l+1,r+1]
