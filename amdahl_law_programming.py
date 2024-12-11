import matplotlib.pyplot as plt

def amdahl_law(p, n):
    return 1 / ((1 - p) + (p / n))

def main():
    p = float(input("Paralellestirilebilen kismin oranini giriniz(0 ile 1 arasi): "))
    while p < 0 or p > 1:
        print("Lutfen 0 ile 1 arasında bir deger giriniz.")
        p = float(input("Paralellestirilebilen kismin oranini giriniz(0 ile 1 arasi): "))

    max_cores = int(input("Maksimum islemci sayisini giriniz: "))

    cores = list(range(1, max_cores + 1))
    speedups = [amdahl_law(p, n) for n in cores]
    print("\nCekirdek Sayisi - Hizlanma")
    for n, s in zip(cores, speedups):
        print(f"{n:>13} - {s:.2f}")

    plt.figure(figsize=(14, 7))
    plt.plot(cores, speedups, marker='1', linestyle='-', color='r')
    plt.title(f"Amdahl Yasasi Hizlanma Grafigi", fontsize=22)
    plt.xlabel("Cekirdek Sayisi", fontsize=10)
    plt.ylabel("Hizlanma", fontsize=10)
    plt.grid(True)
    plt.xticks(range(1, max_cores + 1))
    plt.show()

if __name__ == "__main__":
    main()