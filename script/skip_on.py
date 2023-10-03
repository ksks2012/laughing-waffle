import time

from script.win32_click import WIN32_API

def skip_on():
    win32 = WIN32_API()
    x = 200
    y = 975

    i = 0
    while i < 2:
        time.sleep(1)
        win32.tap((x, y))
        print(f"[skip_on] tap {x=} {y=}")
        i += 1


if __name__ == "__main__":
    time.sleep(5)
    skip_on()
    