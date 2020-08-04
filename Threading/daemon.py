import threading
import time


def testing():
    while True:
        print("Testing Daemon")
        time.sleep(0.5)


t1 = threading.Thread(target=testing, daemon=False)
# t1 = threading.Thread(target=testing, daemon = True)
t1.start()
time.sleep(2)
exit(0)
