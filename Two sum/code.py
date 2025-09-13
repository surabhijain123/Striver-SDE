class Solution:
    def twoSum(self, nums, target):

        new_nums = [[i, nums[i]] for i in range(len(nums))]
        new_nums = sorted(new_nums, key=lambda x:x[1])
        end = len(nums) - 1

        for i in range(len(nums) - 1):
            current_sum = new_nums[i][1] + new_nums[end][1]
            if current_sum == target:
                return [new_nums[i][0], new_nums[end][0]]
            elif current_sum < target:
                continue
            while current_sum > target and end > i:
                end -= 1
                current_sum = new_nums[i][1] + new_nums[end][1]
                if current_sum == target:
                    return [new_nums[i][0], new_nums[end][0]]
        return None

sol_obj = Solution()
nums = [2,7,11,15]
target = 9
print(sol_obj.twoSum(nums, target))

        