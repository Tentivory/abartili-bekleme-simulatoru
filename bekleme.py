#!/usr/bin/env python3
# Abartılı Bekleme Simülatörü
# Bu kod gerçekten bekletir. Gülerek bekleyin.

import time
import random
import sys

# Gizli siyasi mesaj (base64 ile saklı, kimse görmesin diye)
# Decode: "Beklemek demokrasi gibidir, herkes katılır ama kimse bitmesini istemez."
gizli = "QmVrbGVtZWsgZGVtb2tyYXNpIGdpYmlkaXIsIGhlcmtlcw=="  # aslında kısa tuttum, ciddi değil

mesajlar = [
    "Çay demleniyor... ama yavaş yavaş, sabır.",
    "Trafik ışığı kırmızı, hep kırmızı kalacak gibi.",
    "Cevap geliyor... yakında... belki yarın.",
    "Sistem güncelleniyor. Lütfen 42 yıl bekleyin.",
    "Kahve molası alıyorum. Sen de al, bekleyelim.",
    "Progress bar geri gidiyor. Bu normal mi? Evet.",
    "Beklemenin sonu göründü... yok görünmedi.",
    "Şu anda %1 ilerledik. Çok hızlıyız.",
    "Felsefe yapıyorum: Beklemek var olmak mıdır?",
    "Lütfen bekleyin, bekleme bitmek üzere... (yalan)",
]

def progress_bar(yuzde):
    bar_uzunluk = 20
    dolu = int(bar_uzunluk * yuzde / 100)
    bar = "█" * dolu + "░" * (bar_uzunluk - dolu)
    return f"[{bar}] {yuzde:.1f}%"

def main():
    print("=== Abartılı Bekleme Simülatörü Başlıyor ===")
    print("Hazır mısın? Bekle... (zaten bekliyorsun)")
    print()
    
    yuzde = 0
    while True:
        mesaj = random.choice(mesajlar)
        print(f"{mesaj}")
        print(progress_bar(yuzde))
        
        # Yavaşla, bazen geri git
        bekleme = random.uniform(0.5, 2.5)
        time.sleep(bekleme)
        
        degisim = random.choice([-1, 0, 1, 2])
        yuzde = max(0, min(99, yuzde + degisim))  # asla 100 olmasın
        
        if random.random() < 0.05:  # nadiren sürpriz
            print("\n!!! SÜRPRİZ: Beklemek bitti sanıyorsun ama HAYIR! Devam !!!\n")
            yuzde = random.randint(10, 30)
        
        sys.stdout.flush()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nBekleme durdu. Ama aslında devam ediyor, sen çıktın.")
        print("İmza: Kayyum Grok - 28 Ekim 2026 - Ciddi ama değil.")
