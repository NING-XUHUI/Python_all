"""
    通过装饰器进行函数增强，只是一种语法糖，本质上跟03完全一致
"""

import time


def count_time_wrapper(func):
    """
        闭包，用于增强函数func：给函数func增强统计事件的功能
    """

    def improved_func():
        start_time = time.perf_counter()
        func()
        end_time = time.perf_counter()
        print("it takes {}'s to find all the odds.".format(end_time - start_time))

    return improved_func


@count_time_wrapper
def print_odds():
    """
    输出0-100之间的所有奇数，并统计函数的执行时间
    """
    for i in range(100):
        if i % 2 == 1:
            print(i)


if __name__ == '__main__':
    print_odds()
