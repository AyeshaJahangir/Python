def search(nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        start=0
        end=len(nums)        
        while start < end:
            middle=start+((end-start)/2)
            if target==nums[middle]:
                return middle
            elif  target < nums[middle]:
                end=middle
            else:
                start=middle+1
        return -1
