# Week 1 Glass Box AI Araştırması — 5–10 Dakikalık Sunum Planı

## Slayt 1 — Problem ve Amaç
- Glass Box AI: doğru çıktının yanında modelin iç hesaplama mekanizmasını incelemek.
- Araştırma zinciri: **DATA → MODEL → INTERNAL REPRESENTATION → FEATURE → INTERVENTION → OUTPUT**.
- İlk hafta küçük ve kontrollü MNIST MLP üzerinde çalışıldı.

## Slayt 2 — Baseline
- MNIST `60000/10000`.
- MLP `784 → 128 → ReLU → 64 → ReLU → 10`.
- Adam, LR `0.001`, batch `64`, 5 epoch, seed `42`.
- Test accuracy: **97.56%**.
- ReLU2 aktivasyon matrisi: `10000×64`.

## Slayt 3 — Aday Özellik / Devre Keşfi (E03)
- Sınıf seçiciliği ve çıktı bağlantıları incelendi.
- Aday grup: **`[47,17,57,53,28]`**.
- N47 Class 0 selectivity: `3.163`.
- N17–N47 Pearson korelasyonu: genel `0.4485`, Class 0 `0.7846`.
- Korelasyon tek başına nedensellik olarak kabul edilmedi.

## Slayt 4 — Ablasyon ve Devre Müdahaleleri (E04)
- N47 tek ablasyon: **−0.9184 pp** Class 0.
- Aday devre ablasyonu: **−12.0408 pp**.
- Random control ortalaması: **−0.1122 pp**.
- Sınıf1 kontrolü: `+0.0881 pp`; Sınıf2: `0.0000 pp`.
- Progressive ablation: `−0.9184 → −12.0408 pp`.

## Slayt 5 — Aktivasyon Müdahalesi ve Yamalama (E05)
- N47 gerçek Class 0 olasılığı: `0.9640 → 0.9853`.
- N17 gerçek Class 0 olasılığı: `0.9619 → 0.9863`.
- Top-5 patching etkisi: `+0.00546138` ortalama Class 0 olasılık değişimi.
- Logit-level patching: `+6.0245` ve `+4.3068` Class 0 logit etkileri.

## Slayt 6 — Mekanistik Doğrulama
- Aday grup random kontrollere göre çok daha büyük etki oluşturdu.
- Aday devre: **−12.0408 pp**.
- Random mean: **−0.1122 pp**.
- Devre aktivasyon ölçeği `0→2`: gerçek Class 0 olasılığı `0.7644→0.9938`.
- Sonuç: Güçlü destek; fakat eksiksiz devre veya evrensel mekanizma iddiası yapılmadı.

## Slayt 7 — Sınırlılıklar
- Tek seed: `42`.
- Küçük MNIST MLP.
- Aday seçiminde gözlemsel ölçümler.
- Patching kapsamı sınırlı.
- Eksiksiz devre kanıtı yok.

## Slayt 8 — Week 2'ye Geçiş
- Ana sorunlar: seed'e bağımlılık, selection bias ve sınırlı random controls.
- Week 2 hedefi: **multi-seed + matched discovery/holdout + graded intervention + 50 controls + group intervention + synthetic validation + local LLM**.
- Ana soru: aday mekanizma farklı tekrarlar ve bağımsız kontroller altında da korunuyor mu?
