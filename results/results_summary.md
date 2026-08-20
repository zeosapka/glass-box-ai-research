# Deneysel Sonuç Özeti

## Temel Model

- MNIST: `60000` eğitim / `10000` test
- Mimari (architecture): `784 → 128 → ReLU → 64 → ReLU → 10`
- Seed: 42
- Adam, öğrenme oranı (LR) 0.001, batch 64, 5 epoch
- Test doğruluğu (test accuracy): **97.56%**
- Kaydedilen epoch eğitim kaybı: `0.3328, 0.1354, 0.0945, 0.0717, 0.0558`

## İç Temsil

- ReLU2 test aktivasyon matrisi: `10000 × 64`
- Aday Sınıf 0 grubu: `[47,17,57,53,28]`
- N47 seçiciliği: `3.1630`
- N17 seçiciliği: `2.1927`

## Nöron Düzeyi Kanıt

| Müdahale | Sonuç |
|---|---:|
| N47 ablasyonu — Sınıf 0 | −0.9184 pp |
| N17 ablasyonu — Sınıf 0 | −0.8164 pp |
| N47 aktivasyon ölçeği 0→2 — gerçek Sınıf 0 olasılığı | 0.9640 → 0.9853 |
| N17 aktivasyon ölçeği 0→2 — gerçek Sınıf 0 olasılığı | 0.9619 → 0.9863 |

## Devre Düzeyi Kanıt

| Test | Sonuç |
|---|---:|
| Aday devre ablasyonu — Sınıf 0 | **−12.0408 pp** |
| Rastgele kontroller ortalaması | −0.1122 pp |
| Aday ve rastgele ortalama farkı | −11.9286 pp |
| Sınıf 1 kontrolü | +0.0881 pp |
| Sınıf 2 kontrolü | 0.0000 pp |
| Tekli çıkarmada en güçlü bağlamsal etki | N57, −9.0816 pp |
| Aşamalı ablasyon | −0.9184 → −12.0408 pp |
| Sınıf 1 hedefi logit yamalama | +6.0245 Sınıf 0 logiti |
| Sınıf 2 hedefi logit yamalama | +4.3068 Sınıf 0 logiti |
| Devre müdahalesi ölçeği 0→2 | 0.7644 → 0.9938 gerçek Sınıf 0 olasılığı |

## Yorum

Aday grup `[47,17,57,53,28]`, dağıtık ve Sınıf 0'a eğilimli bir iç mekanizma için güçlü nedensel kanıtı (causal evidence/support) desteklemektedir. Grup yalnızca Sınıf 0'a özgü değildir ve eksiksiz veya tek devre olduğu iddia edilmemektedir. Gözlem, müdahale ve kontrol sonuçları kavramsal olarak ayrı tutulmuştur.

## Tekrar Üretilebilirlik Notu

Yukarıdaki özgün sayısal sonuçlar tamamlanmış Colab deneylerinden kaydedilmiştir. Güncellenen temel model notebook'u artık eksik öğrenme eğrisi grafiklerini oluşturmak için epoch düzeyinde eğitim/test kaybı ve doğruluk da kaydetmektedir. Bu yeni eğriler deneysel sonuç kabul edilmeden önce Colab'da çalıştırılmalıdır.
