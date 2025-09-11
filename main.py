import datetime

def zaman():
    """Bugünün tarihi ve 2 hafta sonrası"""
    bugun = datetime.datetime.now()
    iki_hafta_sonra = bugun + datetime.timedelta(weeks=2)
    return bugun.strftime("%d-%m-%Y %H:%M"), iki_hafta_sonra.strftime("%d-%m-%Y %H:%M")

def mainMenu():
    while True:
        print("""
        HALK KÜTÜPHANESİNE HOŞGELDİNİZ

        1 - Üyelik İşlemleri
        2 - Kitap İşlemleri
        3 - Çıkış
        """)
        secim = input("Lütfen yapmak istediğiniz işlemi seçiniz: ")

        if secim == "1":
            uyelik_islemleri()
        elif secim == "2":
            kitap_islemleri()
        elif secim == "3":
            print("Programdan çıkılıyor...")
            break
        else:
            print("Hatalı giriş! Tekrar deneyiniz.")

def uyelik_islemleri():
    while True:
        print("""
        ÜYELİK İŞLEMLERİ MENÜSÜ

        1 - Üye Ekle
        2 - Üye Sil
        3 - Üye Listele
        4 - Ana Menüye Dön
        """)
        secim = input("İşlem seçiniz: ")

        if secim == "1":
            print("Üye ekleme işlemi yapılacak (henüz yazmadık).")
        elif secim == "2":
            print("Üye silme işlemi yapılacak.")
        elif secim == "3":
            print("Üye listeleme işlemi yapılacak.")
        elif secim == "4":
            break
        else:
            print("Hatalı seçim!")

def kitap_islemleri():
    while True:
        print("""
        KİTAP İŞLEMLERİ MENÜSÜ

        1 - Kitap Ekle
        2 - Kitap Sil
        3 - Kitap Listele
        4 - Kitap Ara
        5 - Kitap Ödünç Ver
        6 - Kitap Geri Al
        7 - Ana Menüye Dön
        """)
        secim = input("İşlem seçiniz: ")

        if secim == "1":
            print("Kitap ekleme işlemi yapılacak.")
        elif secim == "2":
            print("Kitap silme işlemi yapılacak.")
        elif secim == "3":
            print("Kitap listeleme işlemi yapılacak.")
        elif secim == "4":
            print("Kitap arama işlemi yapılacak.")
        elif secim == "5":
            baslangic, bitis = zaman()
            print(f"Kitap ödünç verildi. Başlangıç: {baslangic}, Teslim tarihi: {bitis}")
        elif secim == "6":
            print("Kitap geri alındı.")
        elif secim == "7":
            break
        else:
            print("Hatalı seçim!")

# Programı başlat
uye_menu()