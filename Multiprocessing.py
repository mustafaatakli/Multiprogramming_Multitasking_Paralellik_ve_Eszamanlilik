from multiprocessing import Process
import os
import time

def islem_yap(sayi):
    print(f"Islemci: {os.getpid()} - Sayi: {sayi}, Kare: {sayi * sayi}")
    time.sleep(2)

if __name__ == "__main__":
    sayilar = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    islemler = []

    for sayi in sayilar:
        islem = Process(target=islem_yap, args=(sayi,))
        islemler.append(islem)
        islem.start()

    for islem in islemler:
        islem.join() 
        
    print("\nTüm islemler tamamlandi.")