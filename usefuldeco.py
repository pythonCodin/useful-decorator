import time
def duration(func):
    def wrapper():
        print('started')
        time.sleep(1)
        start = time.time()
        func()
        print('ended')
        end = time.time()
        time.sleep(1)
        print(f'Duration: {(end - start)}')

    return wrapper()
