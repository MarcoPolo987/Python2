import time


def hi():
    print('hi')


def timestamp(func):
    print(time.ctime())
    func()


def main():
    timestamp(hi)


main()
