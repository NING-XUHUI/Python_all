"""
    给定一个整数数组nums，找到一个具有最大和的连续子数组（数组最少包含一个元素），返回其最大和。
    示例：
    输入：[-2,1,-3,4,-1,2,1,-5,4]
    输出：6
"""

def maxSubArray(nums: List[int]) -> int:
    """
    asd
    """
    n = len(nums)
    for i in range(1, n):
        if nums[i - 1] > 0:
            nums[i] += nums[i - 1]

    return max(nums)


def maxSubArray2(nums: List[int]) -> int:
    cur_sum = max_sum = nums[0]
    for i in range(1, len(nums)):
        cur_sum = max(cur_sum + nums[i], nums[i])
        max_sum = max(max_sum, cur_sum)

    return max_sum
