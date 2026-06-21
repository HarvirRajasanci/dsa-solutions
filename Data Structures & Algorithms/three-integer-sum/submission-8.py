class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        triplets = []

        for i in range(len(nums)):
            if nums[i] > 0:
                break;

            if i > 0 and nums[i] == nums[i - 1]:
                continue

            L, R = i + 1, len(nums) - 1
            while L < R:
                sum = nums[i] + nums[L] + nums[R];

                if sum < 0:
                    L += 1
                elif sum > 0:
                    R -= 1
                else:
                    triplets.append([nums[i], nums[L], nums[R]])
                    L += 1
                    while L < R and nums[L] == nums[L - 1]:
                        L += 1

        return triplets