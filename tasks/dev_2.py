from timeit import default_timer as timer


def measure_time(func):
    """
    This decorator is supposed to measure execution time of given function
    :return: String with measured time in seconds
    """

    def inner():
        start = timer()
        func()
        stop = timer()
        return f"{stop - start} s"

    return inner


"""
Copy given functions and add decorator 
"""


@measure_time
def pretty_fast():
    return sum([x for x in range(100_000)])


@measure_time
def little_bit_slower():
    nums = []
    for i in range(1_000):
        for j in range(1_000):
            nums.append(i + j)


@measure_time
def very_slow():
    nums = []
    for i in range(1_000):
        for j in range(1_000):
            for z in range(1_000):
                nums.append(i + j + z)


def print_results():
    """
    Auxiliary function to print results of each function with one call
    """
    print(pretty_fast())
    print(little_bit_slower())
    print(very_slow())
