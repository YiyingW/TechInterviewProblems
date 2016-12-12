# 3Sum

'''
Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? 
Find all unique triplets in the array which gives the sum of zero.
'''
from collections import defaultdict

def threeSum1(nums):
    num_dict={}
    value_index_dict = defaultdict(list)
    for i, num in enumerate(nums):
        num_dict[i] = num
        value_index_dict[num].append(i)


    num_2_dict={}
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            num_2_dict[(i, j)] = num_dict[i] + num_dict[j]
    result = set()
    final_result = set()
    for k in num_2_dict:
        if -1*num_2_dict[k] in value_index_dict:
            for index in value_index_dict[-1*num_2_dict[k]]:
                if index != k[0] and index != k[1]:
                    entry = [k[0],k[1], index]
                    entry=tuple(sorted(entry))
                    result.add(entry)
                    numbers = tuple(sorted([num_dict[entry[0]],num_dict[entry[1]],num_dict[entry[2]]]))
                    final_result.add(numbers)
    output = []
    for item in final_result:
        output.append(list(item))


    return output

S = [-1, 0, 1, 2, -1, -4]
#print threeSum1(S)

class Solution(object):

    def threeSum(self, nums):
        nums.sort() # sort the list in place
        res = []
        length = len(nums)
        for i in range(0, length-2):
            if i and nums[i] == nums[i-1]: # because you don't want duplicate
                continue # not do anything, next for loop option
            target = nums[i] * -1
            left, right = i + 1, length - 1
            while left < right:
                if nums[left] + nums[right] == target:
                    res.append([nums[i], nums[left], nums[right]])
                    right -= 1
                    left += 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                elif nums[left] + nums[right] > target:
                    right -= 1
                else:
                    left += 1

        return res 




ans = Solution()
print ans.threeSum(S)






















