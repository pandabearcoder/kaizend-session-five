import random
from time import sleep


def looper():
    for num in range(5):
        random_sleep = random.randint(1, 5)
        print(num)
        print(f'Sleeping for {random_sleep} second(s)')
        sleep(2)


def main():
    looper()


if __name__ == '__main__':
    main()
