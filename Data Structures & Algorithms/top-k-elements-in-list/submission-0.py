class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        # We can use a minheap to store the values 
        # We first must use a counter to keep our key value pairs
        count = {}
        #looping through the array nums, for each num 
        for num in nums:
            #each number will have a specific count
            count[num] = count.get(num, 0) + 1 
        
        # after creating the number : frequency map, use a minheap to pop the numbers with > k frequency
        # currently have number : frequency
        heap = []
        # .keys() gives us 1, 2 ,3
        for num in count.keys():
            # push frequency, key pairs into the heap
            heapq.heappush(heap, (count[num], num))
            # checks if the length of the heap is greater than k, and pops the smallest value inside of the heap, once we finished iterating through the numbers, the heap should contain at least k number of frequency,value pairs.
            if len(heap) > k:
                heapq.heappop(heap)
        res = []
        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        return res
        






        





            
