import time
import threading

def program_1():
    for i in range(5):
        print(f"Program 1: Calisiyor: {i + 1}")
        time.sleep(1)  

def program_2():
    for i in range(5):
        print(f"Program 2: Calisiyor: {i + 1}")
        time.sleep(1)  

if __name__ == "__main__":
    thread1 = threading.Thread(target=program_1)
    thread2 = threading.Thread(target=program_2)

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

    print("Her iki programin islemi de tamamlandi.")