import time


def hi():
    print('hi')


def timeme(x):
    t = time.time()
    print(f"Total time {t}")
    x()


def main():

    timeme(hi)


main()
