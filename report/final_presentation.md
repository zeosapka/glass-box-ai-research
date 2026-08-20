# 1. Haftalık Glass Box AI Araştırması — Sunum Planı

## Slayt 1 — Araştırma Problemi
- Black Box AI yalnızca doğru çıktıyı ölçer.
- Glass Box yaklaşımı modelin iç mekanizmasını (internal mechanism) araştırır.
- Ana soru: Model doğru sonucu hangi iç hesaplama mekanizması (internal computational mechanism) üzerinden üretiyor?

## Slayt 2 — Temel Model (Baseline Model)
- Veri seti (dataset): MNIST
- Mimari (architecture): `784 → 128 → ReLU → 64 → ReLU → 10`
- Seed: 42
- Optimizasyon algoritması (optimizer): Adam
- Öğrenme oranı (learning rate): 0.001
- Batch size: 64
- Epoch: 5
- Test doğruluğu (test accuracy): **97.56%**

## Slayt 3 — İç Temsil (Internal Representation)
- ReLU2 aktivasyon matrisi: **10000 × 64**
- Ortalama / maksimum aktivasyon
- Sıfır aktivasyon oranı
- Sınıf bazlı aktivasyon analizi
- Seçicilik ile aday belirleme
- Seçicilik = gözlem; nedensellik değildir.

## Slayt 4 — Nöron Düzeyinde Müdahale
- N47 Sınıf 0 seçiciliği: **3.163**
- N47 ablasyonu: Sınıf 0 doğruluğu **−0.9184 pp**
- N47 aktivasyon ölçeği 0→2: gerçek Sınıf 0 olasılığı **0.9640→0.9853**
- N17 müdahalesi de benzer sistematik etki göstermiştir.

## Slayt 5 — Devre Keşfi
- Aday devre: **[47, 17, 57, 53, 28]**
- Devre ablasyonu: Sınıf 0 doğruluğu **98.6735%→86.6327%**
- Etki: **−12.0408 pp**
- Rastgele kontroller ortalaması: **−0.1122 pp**

## Slayt 6 — Dağıtık Temsil
- Aşamalı ablasyon: 1→5 nöron etkisi **−0.9184→−12.0408 pp**
- Tekli çıkarma: N57 bağlama bağlı etki **−9.0816 pp**
- Aktivasyon yamalama: Sınıf 0 logit değişimi
  - Sınıf 1 hedefi: **+6.0245**
  - Sınıf 2 hedefi: **+4.3068**
- Aday devre güçlü fakat bağlama bağlı ve dağıtıktır.

## Slayt 7 — Mekanistik Doğrulama
- Sınıf bazlı kontrol: Sınıf 0 **−12.0408 pp**
- Sınıf 1: **+0.0881 pp**
- Sınıf 2: **0.0000 pp**
- Devre aktivasyon müdahalesi: gerçek Sınıf 0 olasılığı **0.7644→0.9938**
- Sonuç: nedensel kanıtı destekleyen bulgu; “causality proved” denmemektedir.

## Slayt 8 — Sonuç ve Sonraki Araştırma
- Zincir: **İç Temsil → Özellik → Müdahale → Nedensel Kanıt → Devre Keşfi → Mekanistik Doğrulama**
- Sınırlılıklar: tek model, seed 42, aday seçim yanlılığı, sınırlı tekrar.
- Sonraki deneyler:
  1. Çoklu seed tekrarı (Multi-Seed Replication)
  2. Sentetik gerçek-sahte ilişki veri seti (Synthetic True-vs-Spurious Dataset)
  3. Dağıtık özellik analizi
  4. Genişletilmiş aktivasyon yamalama
  5. Fashion-MNIST doğrulaması
- Uzun vadeli hipotez: **Mekanizma Kökeni / AI Mekanizma Soy Zinciri (Mechanism Provenance / AI Mechanism Lineage)**
  - AI-1 bir ilişki öğrenir.
  - AI-1 çıktıları/sentetik verileri AI-2 eğitiminde kullanılır.
  - AI-2 benzer bir iç özellik öğrenir.
  - Öğrenilen özellik gerçek mekanizmayı mı, yoksa aktarılan bir artifaktı mı temsil ediyor?
