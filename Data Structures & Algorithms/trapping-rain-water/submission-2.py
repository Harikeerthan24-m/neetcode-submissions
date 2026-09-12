class Solution:
    def trap(self, height: List[int]) -> int:

    # brute force 
    # pseudocode
        # max left finding from the left and right
        # for each in upto before i 
        # for each check upto next after i 
        # find the min of those left and right max 
        # find the water level by min - current height 
        # only add the > 0 for the total water finding 
    
    # code
        # total = 0 
        # n = len(height)
        # for i in range(n):
        #     # skip the left and right value which has one side walls 
        #     if i == 0 or i == n-1:
        #         continue

        #     max_left , max_right = 0 , 0 
            
        #     # find the max left
        #     for left in range(i):
        #         if height[left] > max_left:
        #             max_left = height[left]

        #     # find the max right
        #     for right in range(i+1,n):
        #         if height[right] > max_right:
        #             max_right = height[right]


        #     # find the water level 
        #     water_level = min(max_left,max_right) - height[i]
        #     # print(f"i == {i} , {height[i]} | max_left : {max_left} , max_right : {max_right} , min_value : {min(max_left,max_right)} - height : {height[i]} ==> water_level = {water_level}")

        #     if water_level > 0:
        #         total+=water_level

        # return total


        # optimal 
        # pseudocode
        # while l > r
        # move inwards for the short walls -> l < r or r < l 
        # check current position is a max or not 
        # find the water level - max - current position

        total = 0 
        l , r = 0 , len(height)-1
        max_left , max_right = height[l] , height[r]

        while l < r :
            # moving towards short walls left and right
            if height[l] <= height[r]:
                l+=1
                # check current position is max 
                if height[l] > max_left:
                    max_left = height[l]

                water_level = max_left - height[l]

                if water_level > 0:
                    total+=water_level
            
            else:
                r-=1
                # check current position is max 
                if height[r] > max_right:
                    max_right = height[r]

                water_level = max_right - height[r]

                if water_level > 0:
                    total+=water_level

        return total

            


            







        