class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if not nums: return 0
        l = 0
        current_sum = 0
        size = sys.maxsize
        for r in range(len(nums)):
            current_sum += nums[r]
            while current_sum >= target:
                size = min(size, r - l + 1)
                current_sum -= nums[l]
                l += 1
        return size if size != sys.maxsize else 0
            