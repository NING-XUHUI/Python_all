import time

def print_odds():
    for i in range(100):
        if i % 2 == 1:
            print(i)


def count_time_wrapper(func):
    def improved_func():
        start_time = time.perf_counter()
        func()
        end_time = time.perf_counter()
        print("it takes {}s to find all the odds.".format(end_time - start_time))


    return improved_func


if __name__ == '__main__':
    print_odds = count_time_wrapper(print_odds)
    print_odds()
