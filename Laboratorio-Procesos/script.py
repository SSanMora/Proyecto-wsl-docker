import multiprocessing
def cpu():
    while True: pass
if __name__=='__main__':
    for _ in range(4): multiprocessing.Process(target=cpu).start()
