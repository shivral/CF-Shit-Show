import threading

threading.stack_size(10 ** 8)
t = threading.Thread(target=main)
t.start()
t.join()
