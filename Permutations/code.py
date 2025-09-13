all_l = []
class Solution:
    
    def permuteinternal(self, l, curr_l):
        global all_l
        if len(l) == 0:
            all_l.append(curr_l)
        else:    
            for i in range(len(l)):
                self.permuteinternal(l[:i] + l[i+1:], curr_l + [l[i]])
    
    def permute(self, nums):
        global all_l
        self.permuteinternal(nums, [])
        new_l = []
        for i in all_l:
            new_l.append(tuple(i))
        new_l2 = set(new_l)
        new_l3 = []
        for i in new_l2:
            new_l3.append(list(i))
        return new_l3