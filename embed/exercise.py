def debug_input_and_output(func):
    def wrapper(*args, **kwargs):
        print(f'[INPUT] Args: {args}')
        print(f'[INPUT] Kwargs: {kwargs}')
        output = func(*args, **kwargs)
        print(f'[OUTPUT]: {output}')

    return wrapper


@debug_input_and_output
def say_something(word):
    print(word)


def main():
    say_something('hello')


if __name__ == '__main__':
    main()
