import time


def count_time_wrapper(func):
    def improve_func(*args, **kwargs):     # 增强函数应该把所有接收到的参数传给原函数
        start_time = time.perf_counter()
        ret = func(*args, **kwargs)
        end_time = time.perf_counter()
        print("It takes {}'s to find all odds".format(end_time - start_time))
        return ret

    return improve_func


def count_odds(lim=100):
    cnt = 0
    for i in range(lim):
        if i % 2 == 1:
            cnt += 1

    return cnt


if __name__ == '__main__':
    print("增强前")
    print(count_odds(10000))
    print("---------------")
    print("增强后")
    count_odds = count_time_wrapper(count_odds)
    print(count_odds(10000))
