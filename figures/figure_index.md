# Grafik İndeksi (Figure Index)

GitHub'daki doğrulanabilir SVG grafiklerinin deney bağlantıları ve kapsamı.

## Klasör Yapısı

```text
figures/
├── week1/    # Hafta 1 deneyleri ve analiz grafikleri
└── week2/    # Hafta 2 deneyleri ve analiz grafikleri
```

## Hafta 1

| Grafik | Deney | İçerik |
|---|---|---|
| `week1/ablation_accuracy.svg` | E04 | Sınıf 0 doğruluğu: tek nöron ablasyonları ve tam aday devre |
| `week1/progressive_circuit_ablation.svg` | E04 | Aday nöron sayısı arttıkça Sınıf 0 doğruluğundaki değişim |
| `week1/circuit_intervention_probability.svg` | E05 | Devre/aktivasyon ölçeği ile gerçek Sınıf 0 olasılığı |
| `week1/neuron_intervention_n47.svg` | E05 | N47 aktivasyon ölçeği ile gerçek Sınıf 0 olasılığı |
| `week1/activation_correlation.svg` | E03 | N17–N47 Pearson korelasyonu; yalnızca gözlemsel kanıt |
| `week1/baseline_training_loss.svg` | E01 | 5 epoch temel model eğitim kaybı |
| `week1/candidate_circuit_activation_classes.svg` | E03 | Aday nöronların Sınıf 0–2 ortalama ReLU2 aktivasyonu |
| `week1/class_correct_predictions.svg` | E01 | Karmaşıklık matrisinin köşegenindeki sınıf bazlı doğru tahmin sayıları |
| `week1/selectivity_top10.svg` | E03 | En yüksek 10 nöron seçiciliği; yalnızca aday sıralaması |
| `week1/leave_one_out.svg` | E04 | Her aday nöron çıkarıldığında kalan grubun Sınıf 0 doğruluğu |
| `week1/candidate_group_logit_contribution.svg` | E03 | Aday nöronların Sınıf 0 logitine hesaplamalı katkısı |

## Hafta 2

| Grafik | Deney | İçerik |
|---|---|---|
| `week2/e06_candidate_effect_by_seed.svg` | E06 | Farklı seed değerlerinde aday devre ablasyonunun Class 0 accuracy etkisi |
| `week2/e06_candidate_vs_random_control.svg` | E06 | Aday devre ile random control etkilerinin seed bazında karşılaştırması |
| `week2/e06_test_accuracy_by_seed.svg` | E06 | Çoklu seed eğitimlerinde genel model test accuracy stabilitesi |
| `week2/e07_discovery_holdout_ranking.svg` | E07 | Aday boyutların Discovery ve Holdout L1 sıralamalarının karşılaştırması |
| `week2/e08_directional_dose_response.svg` | E08 | Aday ve kontrollerde graded intervention ile müdahale seviyesi–L1 çıktı değişimi ilişkisi |
| `week2/e09_statistical_control_distribution.svg` | E09 | 50 random control boyutunun mean L1 effect dağılımı; aday ve kontrol ortalaması karşılaştırması |
| `week2/e10_group_effect_comparison.svg` | E10 | Aday grup etkisi, tekil etkilerin toplamı ve random grup kontrolleri |
| `week2/e11_true_vs_spurious_accuracy.svg` | E11 | Normal test ile spurious feature kırılmış testte model doğruluğunun karşılaştırması |
| `week2/week1_vs_week2_summary.svg` | Week 1 / Week 2 Summary | Candidate/random control separation oranının Week 1 ve Week 2 arasında karşılaştırması |

## Dil Standardı

Grafik başlıkları, eksen adları, açıklamalar ve lejantlar Türkçe yazılır. Yöntem veya yerleşik teknik terim gerekiyorsa İngilizce terim parantez içinde korunur; sayısal değerler ve deney ID'leri değiştirilmez.

## Veri İlkesi

- Ham verisi doğrulanamayan noktalar eklenmez.
- Grafik başlığı deney kaydıyla aynı terminolojiyi kullanır.
- Grafiklerde “causality proved” gibi aşırı iddialı ifadeler kullanılmaz.
- Bir grafik yalnızca desteklediği sonucu gösterir; yorum kapsamı veri kapsamını aşmaz.
