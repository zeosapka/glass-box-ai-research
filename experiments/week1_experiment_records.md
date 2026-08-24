# 1. Hafta Deney Kayıtları

Bu dosya Week 1'in **5 ana deneyini** standart kayıt altında tutar. Alt çalışmalar ana deneyin `x.1`, `x.2` biçiminde numaralandırılmıştır. Böylece toplam araştırma deneyi E01–E12 olarak korunur; alt analizler ayrı deney ID'si değildir.

## Ortak Koşullar
- Model: MNIST MLP `784 → 128 → 64 → 10`
- Aktivasyon: ReLU
- Optimizer: Adam
- Learning rate: `0.001`
- Batch size: `64`
- Epoch: `5`
- Seed: `42`
- Dataset: MNIST (`60000` eğitim / `10000` test)

---

## 1. Deney — E01: Temel Model (Baseline)

### 1.1 — Temel Model
- **Deney ID:** E01
- **Amaç:** Sonraki iç analiz ve müdahale deneyleri için temel model oluşturmak.
- **Hipotez:** Model MNIST'te yeterli doğruluk sağlayacaktır.
- **Sonuç:** Test doğruluğu **%97.56**; epoch kayıpları `0.3328, 0.1354, 0.0945, 0.0717, 0.0558`.
- **Yorum:** Sonraki Glass Box analizleri için yeterli temel performans sağlandı.

---

## 2. Deney — E02: Aktivasyon Analizi

### 2.1 — Aktivasyon Gözlemi
- **Deney ID:** E02
- **Amaç:** Gizli katman aktivasyonlarını gözlemlemek.
- **Sonuç:** Tam ReLU2 aktivasyon matrisi `[10000,64]`. Öne çıkan ortalama aktivasyonlar: N62 `4.661`, N61 `2.601`, N54 `2.559`, N47 `2.540`. N4, N19, N35 ve N58 düşük/ölü aktivasyon gösterdi.
- **Yorum:** Yüksek aktivasyon tek başına nedensel önem değildir.

---

## 3. Deney — E03: Aday Özellik / Devre Keşfi

### 3.1 — Sınıf Aktivasyonu ve Seçicilik
- Seçicilik = en yüksek sınıf ortalama aktivasyonu − ikinci en yüksek sınıf ortalama aktivasyonu.
- Öne çıkanlar: N54/Sınıf2 `3.561`, N47/Sınıf0 `3.163`, N22/Sınıf1 `2.881`.
- Yorum: Gözlemsel aday-seçim ölçüsüdür; nedensel kanıt değildir.

### 3.2 — Aday Devre Keşfi
- Aday grup: `[47,17,57,53,28]`.
- Sınıf0 çıktı ağırlıkları: N47 `+0.231610`, N17 `+0.237246`, N28 `+0.233466`, N53 `+0.225550`, N57 `+0.186438`.
- Yorum: Çıktı ağırlığı büyüklüğü tek başına nedensel kanıt değildir.

### 3.3 — Aday Grup Katkısı
- Sınıf0 ağırlık toplamı: `+1.114311`.
- Gerçek Sınıf0 ortalama grup katkısı: **+6.197485**.
- Yorum: Katkı kararın yüzdesi değildir; diğer nöronlar ve bias da katkı verir.

### 3.4 — Aday Grubun Tüm Logitlere Katkısı
- Gerçek Sınıf0 örneklerinde aday katkıları: C0 `+6.197485`, C1 `-2.253895`, C3 `-3.120183`, C4 `-3.548902`; diğerleri ham günlükte kayıtlı.
- Yorum: Mekanizma tek bir çıktı düğümüne indirgenemez.

### 3.5 — Korelasyon ve Nedensellik
- N17–N47 Pearson korelasyonu: tüm test `r=0.4485`; Sınıf0 `r=0.7846`.
- Yorum: Korelasyon gözlemsel kanıttır; nedensel iddia için müdahale/ablasyon gerekir.

**E03 genel sonucu:** Sınıf0 ile ilişkili aday nöronlar ve `[47,17,57,53,28]` aday grubu belirlendi; bunlar sonraki E04 ve E05 müdahalelerinin girdisidir.

---

## 4. Deney — E04: Ablasyon ve Devre Müdahaleleri

### 4.1 — Tek Nöron Ablasyonu
- N47 Sınıf0: `%98.6735 → %97.7551` (`-0.9184 pp`).
- N54 Sınıf2: `-0.3876 pp`; N62 Sınıf3: `-0.4950 pp`.

### 4.2 — Birleşik Ablasyon
- N17+N47 genel etki: `-0.3700 pp`.
- Sınıf0 birleşik etki: `-2.7551 pp`.
- Tekil toplam beklentisi: `-1.7347 pp`.
- Non-additive fark: `-1.0204 pp`.

### 4.3 — Aday Devre Ablasyonu
- `[47,17,57,53,28]` birlikte ablate edildi.
- Sınıf0: `%98.6735 → %86.6327`.
- **Etki: `-12.0408 pp`.**

### 4.4 — Sınıfa Özgü Devre Kontrolü
- Sınıf1: `+0.0881 pp`.
- Sınıf2: `0.0000 pp`.
- Sınıf0 etkisinin kontrollere göre belirgin olduğu gözlendi.

### 4.5 — Tekli Çıkarma / Leave-One-Out
- N47 `-5.9184 pp`; N17 `-5.9184 pp`; N57 `-9.0816 pp`; N53 `-6.5306 pp`; N28 `-6.6327 pp`.
- En güçlü bağlamsal etki N57: `-9.0816 pp`.

### 4.6 — Aşamalı Devre Ablasyonu
- Grup boyutu 1→5 etkileri: `-0.9184, -2.7551, -3.8776, -6.6327, -12.0408 pp`.
- Yorum: Dağıtık/toplamsal olmayan davranışla uyumludur.

### 4.7 — Rastgele Kontroller / Mekanistik Doğrulama
- Aday devre: `-12.0408 pp`.
- Rastgele kontrol ortalaması: `-0.1122 pp`.
- Yorum: Aday etki random kontrollere göre çok daha büyüktür; tek seed nedeniyle genelleme yapılmaz.

**E04 genel sonucu:** Ablasyon, grup müdahalesi ve random-control karşılaştırması aday devrenin Class 0 davranışıyla nedensel olarak ilişkili olduğuna güçlü destek verir; eksiksiz/tek devre iddiası yapılmaz.

---

## 5. Deney — E05: Aktivasyon Müdahalesi ve Yamalama

### 5.1 — Aktivasyon Müdahalesi
- N47 gerçek Sınıf0 olasılığı `0.9640 → 0.9853` (ölçek `0→2`).
- N54 gerçek Sınıf2 olasılığı `0.9583 → 0.9676`.

### 5.2 — Aktivasyon Yamalama
- N17: `+0.00000119 ± 0.00000396`.
- N47: `+0.00000024 ± 0.00000072`.
- N17+N47: `+0.00000247 ± 0.00000731`.
- Yorum: Tek nöronlar davranış aktarımı için yeterli değildir; dağıtık temsil hipotezini destekleyen gözlemdir.

### 5.3 — Dağıtık Özellik Yamalama
- Top-1: `+0.00000024`.
- Top-3: `+0.00001863`.
- Top-5: `+0.00546138`.
- Yorum: Top-5 etkisi artmıştır; yüksek standart sapma nedeniyle tek başına kesin devre değildir.

### 5.4 — Sınıfa Özgü Yamalama Kontrolü
- Sınıf1 hedefi: `+0.00887395 ± 0.03161188`.
- Sınıf2 hedefi: `+0.00536434 ± 0.02391533`.
- Yorum: Aday grup yalnızca Sınıf0'a özgü değildir; etki bağlama bağlıdır.

### 5.5 — Logit Düzeyinde Yamalama
- Sınıf1 hedefinde Sınıf0 logiti: `+6.024506 ± 1.621096`.
- Sınıf2 hedefinde Sınıf0 logiti: `+4.306821 ± 1.859204`.
- Yorum: Softmax doygunluğunun gizlediği etki logit düzeyinde daha görünürdür; bağlama bağlıdır.

**E05 genel sonucu:** Kontrollü aktivasyon müdahalesi ve patching, aday grubun çıktı davranışına katkısını destekler; patching sonuçları dağıtık ve bağlama bağlı temsil olasılığını gösterir.

---

## Week 1 Sonuç Özeti

- Baseline test accuracy: **%97.56**.
- Aday grup: `[47,17,57,53,28]`.
- Aday devre ablasyonu: **−12.0408 pp** Class 0.
- Random control ortalaması: **−0.1122 pp**.
- Aktivasyon müdahalesi ve patching, aday iç temsilin çıktıyla ilişkisini müdahale yoluyla destekledi.
- Bilimsel sınır: sonuçlar tek seed ve sınırlı veri tasarımına dayandığından Week 2'de multi-seed, holdout ve geniş random-control doğrulaması gerekliydi.

## Kaynak ve Tekrar Üretilebilirlik
- Ayrıntılı ham sayısal kayıt: `notes/experiment_log_week1.md`.
- Grafikler: `figures/week1/`.
- Bu dosya **5 ana Week 1 deneyi** ve bunların alt analizlerini kaydeder.
