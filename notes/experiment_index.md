# Deney İndeksi (Experiment Index)

Bu indeks, araştırmadaki deney kayıtlarının tek noktadan gezinilmesini sağlar.

## 1. Hafta

| ID | Deney | Ana ölçüm | Standart kayıt |
|---:|---|---|---|
| E01 | Temel model (baseline) | Test doğruluğu %97.56 | `experiments/week1_experiment_records.md` |
| E02 | Aktivasyon analizi | `10000×64` ReLU2 matrisi | `experiments/week1_experiment_records.md` |
| E03 | Sınıf aktivasyonu / seçicilik | Aday sıralaması | `experiments/week1_experiment_records.md` |
| E04 | Tek nöron ablasyonu | N47 Sınıf0 −0.9184 pp | `experiments/week1_experiment_records.md` |
| E05 | Aktivasyon müdahalesi | N47 Sınıf0 olasılığı 0.9640→0.9853 | `experiments/week1_experiment_records.md` |
| E06 | Korelasyon ve nedensellik | r=0.4485 genel, 0.7846 Sınıf0 | `experiments/week1_experiment_records.md` |
| E07 | Aday devre keşfi | [47,17,57,53,28] | `experiments/week1_experiment_records.md` |
| E08 | Birleşik ablasyon | Toplamsal olmayan etki | `experiments/week1_experiment_records.md` |
| E09 | Aktivasyon yamalama | Top-1/2 nöron yamalama etkileri | `experiments/week1_experiment_records.md` |
| E10 | Dağıtık özellik yamalama | Top-1/3/5 aktarımı | `experiments/week1_experiment_records.md` |
| E11 | Sınıfa özgü yamalama kontrolü | Bağlama bağlı kontrol | `experiments/week1_experiment_records.md` |
| E12 | Logit düzeyinde yamalama | +6.0245 / +4.3068 Sınıf0 logiti | `experiments/week1_experiment_records.md` |
| E13 | Aday grup katkısı | Sınıf0 katkısı +6.197485 | `experiments/week1_experiment_records.md` |
| E14 | Tüm logitlere katkı | Adayın tüm çıktılardaki etkisi | `experiments/week1_experiment_records.md` |
| E15 | Aday devre ablasyonu | Sınıf0 −12.0408 pp | `experiments/week1_experiment_records.md` |
| E16 | Sınıfa özgü devre kontrolü | Sınıf1 +0.0881 pp, Sınıf2 0 | `experiments/week1_experiment_records.md` |
| E17 | Tekli çıkarma | N57 −9.0816 pp | `experiments/week1_experiment_records.md` |
| E18 | Aşamalı ablasyon | 1→5 nöron −0.9184→−12.0408 pp | `experiments/week1_experiment_records.md` |
| E19 | Rastgele kontroller / mekanistik doğrulama | Rastgele ortalama −0.1122 pp; aday −12.0408 pp | `experiments/week1_experiment_records.md` |

## Kaynak Gerçeği

- Ayrıntılı ham sayısal kayıt: `notes/experiment_log.md`
- Standart deney kayıtları: `experiments/week1_experiment_records.md`
- Grafik kayıtları: `figures/figure_index.md`

2. hafta deneylerinde aynı şablona ek olarak **Başarım Kriteri (Success Criterion)**, **Doğrulama Sonucu (Verification Result)**, **İstatistiksel Anlamlılık (Statistical Significance)** ve **Commit Hash** alanları kullanılacaktır.
