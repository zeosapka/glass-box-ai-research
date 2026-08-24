# Week 1 — Glass Box AI Araştırma Raporu

## 1. Amaç

Week 1'in amacı, küçük ve kontrollü bir MNIST MLP üzerinde iç temsilleri gözlemlemek, aday özellik/devreleri keşfetmek ve kontrollü müdahale ile çıktıya etkilerini ölçmektir.

## 2. Model ve Baseline

- MNIST: `60000` eğitim / `10000` test
- MLP: `784 → 128 → ReLU → 64 → ReLU → 10`
- Adam, LR `0.001`, batch `64`, 5 epoch, seed `42`
- Test accuracy: **97.56%**

## 3. Ana Deneyler

### E01 — Temel Model
Baseline model başarıyla kuruldu ve sonraki iç analizler için referans oluşturuldu.

### E02 — Aktivasyon Analizi
ReLU2 aktivasyon matrisi `10000×64` olarak çıkarıldı. Aktivasyon büyüklüğünün tek başına nedensel önem olmadığı görüldü.

### E03 — Aday Özellik / Devre Keşfi
Sınıf seçiciliği, çıktı ağırlıkları, grup katkısı ve korelasyon analizleri ile `[47,17,57,53,28]` aday grubu belirlendi. N17–N47 korelasyonu tüm testte `r=0.4485`, Sınıf0'da `r=0.7846` idi; korelasyon tek başına nedensellik olarak yorumlanmadı.

### E04 — Ablasyon ve Devre Müdahaleleri
- N47 tek ablasyonu: **−0.9184 pp** Sınıf0.
- Aday devre ablasyonu: **−12.0408 pp** Sınıf0.
- Random control ortalaması: **−0.1122 pp**.
- Sınıf1 kontrolü: `+0.0881 pp`; Sınıf2: `0.0000 pp`.
- Progressive ablation: `−0.9184 → −12.0408 pp`.

Sonuç: Aday grubun Sınıf0 davranışıyla güçlü nedensel ilişkisini destekleyen kanıt elde edildi; ancak eksiksiz devre veya genellenebilir mekanizma iddiası yapılmadı.

### E05 — Aktivasyon Müdahalesi ve Yamalama
N47 gerçek Sınıf0 olasılığı ölçek `0→2` arasında `0.9640→0.9853` oldu. Logit-level patching ile Sınıf0 logitinde `+6.0245` ve `+4.3068` değişimler gözlendi. Patching sonuçları dağıtık ve bağlama bağlı temsil olasılığını destekledi.

## 4. Sonuç

Week 1, `DATA → MODEL → INTERNAL REPRESENTATION → FEATURE → INTERVENTION → OUTPUT` zincirini küçük kontrollü bir modelde kurdu. En önemli aday grup `[47,17,57,53,28]` oldu. Tek seed ve sınırlı kontrol tasarımı nedeniyle Week 2'de multi-seed, discovery/holdout ve geniş random-control doğrulaması planlandı.

## 5. Sınırlılıklar

- Tek eğitim seed'i (`42`).
- Küçük MNIST MLP.
- Aday seçiminde gözlemsel ölçümlerin kullanılması.
- Patching kapsamının sınırlı olması.
- Eksiksiz devre kanıtı bulunmaması.

## 6. Veri ve kod

Standart deney kayıtları: `experiments/week1_experiment_records.md`.
Ayrıntılı Week 1 günlük: `notes/experiment_log.md`.
Grafikler: `figures/week1/`.
