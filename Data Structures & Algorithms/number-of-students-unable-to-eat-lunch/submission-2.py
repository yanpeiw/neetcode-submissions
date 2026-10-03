class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        
        res = len(students)
        count = {0:0, 1:0}
        
        for s in students:
            if s not in count:
                count[s] = 0
            count[s] += 1
        
        for san in sandwiches:
            if count[san] > 0:
                res -= 1
                count[san] -= 1

            else:
                return res

        return res

            
    