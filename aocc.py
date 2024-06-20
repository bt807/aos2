import os
import time

def create_zombie():
    pid = os.fork()
    if pid > 0:
        
        print(f"Родительский процесс. PID: {os.getpid()}")
        print(f"Создан дочерний процесс-зомби с PID: {pid}")
        time.sleep(10)
        print("Родительский процесс завершен.")
    else:
        
        print(f"Дочерний процесс. PID: {os.getpid()}")
        print("Дочерний процесс завершен.")
        os._exit(0)

if __name__ == '__main__':
    create_zombie()
    time.sleep(30)
    print("Программа завершена.")
