# Grafik İndeksi (Figure Index)

GitHub'daki doğrulanabilir SVG grafiklerinin deney bağlantıları ve kapsamı.

| Grafik | Deney | İçerik |
|---|---|---|
| `ablation_accuracy.svg` | E04, E15 | Sınıf 0 doğruluğu: tek nöron ablasyonları ve tam aday devre |
| `progressive_circuit_ablation.svg` | E18 | Aday nöron sayısı arttıkça Sınıf 0 doğruluğundaki değişim |
| `circuit_intervention_probability.svg` | E24 / devre düzeyi müdahale | Devre aktivasyon ölçeği ile gerçek Sınıf 0 olasılığı |
| `neuron_intervention_n47.svg` | E05 | N47 aktivasyon ölçeği ile gerçek Sınıf 0 olasılığı |
| `activation_correlation.svg` | E06 | N17–N47 Pearson korelasyonu; yalnızca gözlemsel kanıt |
| `baseline_training_loss.svg` | E01 | 5 epoch temel model eğitim kaybı |
| `candidate_circuit_activation_classes.svg` | E02, E07 | Aday nöronların Sınıf 0–2 ortalama ReLU2 aktivasyonu |
| `class_correct_predictions.svg` | E01 | Karmaşıklık matrisinin köşegenindeki sınıf bazlı doğru tahmin sayıları |
| `selectivity_top10.svg` | E03 | En yüksek 10 nöron seçiciliği; yalnızca aday sıralaması |
| `leave_one_out.svg` | E17 | Her aday nöron çıkarıldığında kalan grubun Sınıf 0 doğruluğu |
| `candidate_group_logit_contribution.svg` | E13 | Aday nöronların Sınıf 0 logitine hesaplamalı katkısı |

## Dil Standardı

Grafik başlıkları, eksen adları, açıklamalar ve lejantlar Türkçe yazılır. Yöntem veya yerleşik teknik terim gerekiyorsa İngilizce terim parantez içinde korunur; sayısal değerler ve deney ID'leri değiştirilmez.

## Veri İlkesi

- Ham verisi doğrulanamayan noktalar eklenmez.
- Grafik başlığı deney kaydıyla aynı terminolojiyi kullanır.
- Grafiklerde “causality proved” gibi aşırı iddialı ifadeler kullanılmaz.
- Bir grafik yalnızca desteklediği sonucu gösterir; yorum kapsamı veri kapsamını aşmaz.
