class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        val_pos = {}

        for i in range(len(nums2)): 
            val_pos[nums2[i]] = i
        
        mapping = [0]*len(nums1)
        
        for i in range(len(nums1)):
            if nums1[i] in val_pos:
                mapping[i] = val_pos[nums1[i]]

        return mapping 


        
        