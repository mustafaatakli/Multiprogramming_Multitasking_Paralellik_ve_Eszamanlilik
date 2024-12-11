from multiprocessing import Process
import threading
import time

def kare_hesaplama(sayi):
    print(f"Hesaplaniyor... (Thread/Process ID:{threading.get_ident()}):{sayi} -> {sayi*sayi}")
    time.sleep(1)

def coklu_programlama():
    sayilar = [1,2,3,4,5,6]
    print("Coklu Programlama Islemi Baslatildi.(Thread)...\n")
    thread_list = []
    for sayi in sayilar:
        t=threading.Thread(target=kare_hesaplama, args=(sayi,))
        thread_list.append(t)
        t.start()

    for t in thread_list:
        t.join()
    print("\nCoklu Programlama Islemi Tamamlandi.")

def coklu_islemci():
    sayilar = [1,2,3,4,5,6]
    print("Coklu Islemci Basladi.(Process)...\n")
    process_list = []
    for sayi in sayilar:
        islem = Process(target=kare_hesaplama, args=(sayi,))
        process_list.append(islem)
        islem.start()

    for islem in process_list:
        islem.join()
    print("\nCoklu Islemci Tamamlandi.")

if __name__ == "__main__":
    coklu_programlama()
    coklu_islemci()