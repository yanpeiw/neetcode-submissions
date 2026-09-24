class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        # nums[i] == nums[j] at indices i and j and abs(i-j) <= k


        window = set()
        L , R = 0, 0 

        for R in range(len(nums)):
            if (R - L) > k:
                window.remove(nums[L])
                L += 1
            if nums[R] in window:
                return True
            window.add(nums[R])
    
        return False