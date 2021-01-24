"""
    假设你正在爬楼梯，需要n阶你才能到达楼顶。
    每次你可以爬1阶或2阶，你有多少种不同的方法爬到楼顶
    示例1:
    输入：2
    输出：2
    1.1阶 + 1阶
    2.2阶
"""
from typing import Dict

def climbStairs1(n: int) -> int:
    """
        递归：超时
    """
    if n == 1:
        return 1
    if n == 2:
        return 2

    return climbStairs1(n - 1) + climbStairs1(n - 2)


def Memo(n: int, memo: Dict[int, int]) -> int:
    if memo[n] > 0:
        return memo[n]
    if n == 1:
        memo[n] = 1
    elif n == 2:
        memo[n] = 2
    else:
        memo[n] = Memo(n - 1, memo) + Memo(n - 2, memo)
    return memo[n]

def climbStairs2(n: int) -> int:
    """
        存储中间结果：避免重复运算
    """
    memo = {}
    for i in range(1, n + 1):
        memo[i] = 0
    return Memo(n, memo)   

def climbStairs3(n: int) -> int:
    """
        动态规划
    """
    memo = {}
    for i in range(1, n + 1):
        memo[i] = 0

    memo[1] = 1
    memo[2] = 2
    for i in range(3, n + 1):
        memo[i] = memo[i - 1] + memo[i - 2]

    return memo[n]

def climbStairs4(n: int) -> int:
    """
        滚动数组
    """
    if n == 1:
        return 1

    first = 1
    second = 2
    for i in range(3, n + 1):
        third = first + second
        first = second
        second = third

    return second








