import time


def hi():
    print('hi')


def timeme(x):
    print(f"Total time {x}")


def main():
    t = time.time
    timeme(t)


main()
