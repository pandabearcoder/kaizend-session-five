from time import sleep


def looper(seconds=2):
    for num in range(5):
        print(num)
        print(f'Sleeping for {seconds} second(s)')
        sleep(2)


def main():
    looper()


if __name__ == '__main__':
    main()
