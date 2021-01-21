import time

def count_time(func):
    start_time = time.perf_counter()
    func()
    end_time = time.perf_counter()
    print("it takes {}s to find all the odds.".format(end_time - start_time))


def print_odds():
    for i in range(100):
        if i % 2 == 1:
            print(i)


if __name__ == '__main__':
    count_time(print_odds)
