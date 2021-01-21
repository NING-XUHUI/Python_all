def wrapper1(func1):
    print("setup func1")

    def improved_func1():
        print("do func1")
        func1()

    return improved_func1


def wrapper2(func2):
    print("setup func2")

    def improved_func2():
        print("do func2")
        func2()

    return improved_func2


@wrapper1
@wrapper2
def original_func():
    pass


if __name__ == "__main__":
    original_func()