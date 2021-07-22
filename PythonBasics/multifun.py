from threading import *
import time
class Apple(Thread):
    def run(self):
        for x in range(10):
            time.sleep(1)
            print('Apple says Hi!')
class Orange(Thread):
    def run(self):
        for x in range(10):
            time.sleep(1)
            print('Orange says Hello!')
apple_obj = Apple()
orange_obj = Orange()
start_time = time.perf_counter()
apple_obj.start()
time.sleep(0.1)
orange_obj.start()
apple_obj.join()
orange_obj.join()
end_time = time.perf_counter()
print(f'Processed in {round(end_time-start_time)} seconds')