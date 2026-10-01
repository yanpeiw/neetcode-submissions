class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        # both arrays are strictly increasing

        # m is the number of valid elements in nums1 
        # n is the number of elements in nums2
        nums1[m:] = nums2[:n]
        nums1.sort()
        
            


            


            


        
        
        