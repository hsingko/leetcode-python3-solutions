class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)

        for idx, val in enumerate(numbers):
            remain = target - val

            left = idx + 1
            right = n - 1
            while left < right:
                mid = (left + right) // 2
                if numbers[mid] == remain:
                    return [idx + 1, mid + 1]
                elif numbers[mid] > remain:
                    right = mid
                else:
                    left = mid + 1
            if numbers[left] == remain:
                return [idx + 1, left + 1]
        return [-1, -1]
