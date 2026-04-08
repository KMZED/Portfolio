Nums = [1, 2, 3]
class Solution:
    """Solve duplicate number checks."""

    def contains_duplicate(self, nums: list[int]) -> bool:
        Value = {}

        for n in nums:
            if n in Value:
                return True
            Value[n] = True
        return False

solution = Solution()
result = solution.contains_duplicate(Nums)
print(result)