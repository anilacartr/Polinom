def polinom_hesapla(katsayilar, x):
    """
    Verilen katsayılar ve x değeri için polinomun sonucunu hesaplar.
    :param katsayilar: Polinomun katsayıları (örneğin, [3, 0, 2] -> 3x^2 + 0x + 2)
    :param x: Polinomda hesaplanacak x değeri
    :return: Polinomun sonucu
    """
    sonuc = 0
    for i, katsayi in enumerate(katsayilar[::-1]):  # Katsayıları ters çevir (sabit terim en başta)
        sonuc += katsayi * (x ** i)
    return sonuc

def menuyu_goster():
    print("\n--- Polinom Hesaplama Programı ---")
    print("1. Polinom Hesapla")
    print("2. Çıkış")

def main():
    while True:
        menuyu_goster()
        secim = input("Lütfen bir seçenek girin (1 veya 2): ")

        if secim == "1":
            try:
                # Kullanıcıdan polinomun katsayılarını al
                katsayilar = list(map(float, input("Polinomun katsayılarını boşlukla ayırarak girin (örneğin, 3 0 2): ").split()))
                x = float(input("Polinomda hesaplanacak x değerini girin: "))

                # Polinomu hesapla ve sonucu göster
                sonuc = polinom_hesapla(katsayilar, x)
                print(f"Polinomun sonucu (x = {x}): {sonuc}")
            except ValueError:
                print("Geçersiz giriş! Lütfen sayısal değerler girin.")
        elif secim == "2":
            print("Programdan çıkılıyor...")
            break
        else:
            print("Geçersiz seçenek! Lütfen 1 veya 2 girin.")

if __name__ == "__main__":
    main()
