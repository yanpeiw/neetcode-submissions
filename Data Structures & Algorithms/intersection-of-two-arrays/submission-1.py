class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        #converted the arrays to sets

        set1 = set(nums1)
        set2 = set(nums2)
        
        #initialized a result array

        res = []

        # for every number in set1, check if the number in set1 exists in set2, if true, add number to result arr
        for num in set1:
            if num in set2:
                res.append(num)
        
        return res