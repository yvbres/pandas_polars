import time


def log_performance(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        execution_time = time.time() - start_time
        print(f"function '{func.__name__}' took {execution_time:.4f}"
              " s to execute.")
        return result
    return wrapper


@log_performance
def calculate_total():
    total = 0
    for i in range(1, 1_000_000):
        total += i
    return total


if __name__ == '__main__':
    _ = calculate_total()
