from functools import wraps
from time import sleep


def delay(seconds):
    print(f'Sleeping for {seconds} second(s)')
    sleep(seconds)

    def inner_function(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print('[START]')

            output = func(*args, **kwargs)

            print('[END]')

            return output

        return wrapper

    return inner_function


@delay(seconds=2)
def say_something(word):
    print(word)


def main():
    say_something('hello')


if __name__ == '__main__':
    main()
