# Deney İndeksi (Experiment Index)

Bu indeks, araştırmadaki **ana deneyleri** tek noktadan gezinmek için kullanılır. Alt analizler ana deney altında `x.1`, `x.2` biçiminde tutulur; ayrı deney ID'si değildir.

## Toplam Deney Yapısı

- **Week 1:** E01–E05 = 5 ana deney
- **Week 2:** E06–E12 = 7 ana deney
- **Toplam:** **12 ana deney**

Bu nedenle Week 2'nin E06–E12 numaralandırması Week 1 ile çakışmaz ve `E13–E19` gibi bağımsız ana deney ID'leri kullanılmaz.

## 1. Hafta

| ID | Ana deney | Alt çalışmalar | Ana ölçüm / sonuç | Standart kayıt |
|---:|---|---|---|---|
| E01 | Temel model (baseline) | 1.1 | MNIST test accuracy **97.56%** | `experiments/week1_experiment_records.md` |
| E02 | Aktivasyon analizi | 2.1 | `10000×64` ReLU2 aktivasyon matrisi | `experiments/week1_experiment_records.md` |
| E03 | Aday özellik / devre keşfi | 3.1–3.5 | `[47,17,57,53,28]` aday grubu; selectivity + korelasyon | `experiments/week1_experiment_records.md` |
| E04 | Ablasyon ve devre müdahaleleri | 4.1–4.7 | Aday devre Class 0 etkisi **−12.0408 pp**; random **−0.1122 pp** | `experiments/week1_experiment_records.md` |
| E05 | Aktivasyon müdahalesi ve yamalama | 5.1–5.5 | Kontrollü activation intervention + patching / logit etkileri | `experiments/week1_experiment_records.md` |

### Week 1 alt çalışma yapısı

- **E03:** 3.1 sınıf aktivasyonu/seçicilik; 3.2 aday devre keşfi; 3.3 grup katkısı; 3.4 tüm logitlere katkı; 3.5 korelasyon/nedensellik.
- **E04:** 4.1 tek nöron ablasyonu; 4.2 birleşik ablasyon; 4.3 aday devre ablasyonu; 4.4 sınıfa özgü kontrol; 4.5 leave-one-out; 4.6 progressive ablation; 4.7 random controls.
- **E05:** 5.1 activation intervention; 5.2 activation patching; 5.3 distributed feature patching; 5.4 class-specific patching control; 5.5 logit-level patching.

## 2. Hafta

| ID | Ana deney | Ana ölçüm / sonuç | Standart kayıt |
|---:|---|---|---|
| E06 | Çoklu seed devre tekrarı | Ortalama aday **−27.6735 pp**; random **−0.3469 pp**; 5/5 kriter | `experiments/week2_experiment_records.md` |
| E07 | Eşleştirilmiş Transformer iç temsil | Holdout aday/random **15.71×**; 0/20 controls exceeded candidate | `experiments/week2_experiment_records.md` |
| E08 | Kademeli Transformer müdahalesi | Aday L1 **0.023454**; PARTIAL / SUPPORT | `experiments/week2_experiment_records.md` |
| E09 | Genişletilmiş istatistiksel kontrol | `z=0.854322`, percentile `84%`; **FAIL** | `experiments/week2_experiment_records.md` |
| E10 | Grup müdahalesi | Non-additive ratio `0.670583`; **PASS / SUPPORT** | `experiments/week2_experiment_records.md` |
| E11 | Sentetik true-vs-spurious feature | Accuracy drop **15.55 pp**; **PASS / SUPPORT** | `experiments/week2_experiment_records.md` |
| E12 | Local LLM / Ollama | Llama 3.2 1B; 3 prompt; mechanistic evidence=False | `experiments/week2_experiment_records.md` |

## Notlar ve ön çalışmalar

- `notes/transformer_initial_probe.md` — Week 2 öncesindeki ilk Transformer keşif denemesi; **ana deney ID'si değildir**.
- `notes/ten_day_plan_week1.md` — tarihsel Week 1 başlangıç planı.
- `notes/ten_day_plan_week2.md` — PDF'deki Week 2 on günlük plan.
- `notes/experiment_log.md` — Week 1 ayrıntılı günlük.
- `notes/experiment_log_week2.md` — Week 2 ayrıntılı günlük.
- `notes/week2_delivery_addendum.md` — Week 2 teslim öncesi son kalite kontrol eki; E06 başarı kriteri, E07 z-score/percentile doğrulaması, E12 kullanım amacı ve reproducibility notlarını içerir.

## Kaynak Gerçeği

- Week 1 standart deney kayıtları: `experiments/week1_experiment_records.md`
- Week 2 standart deney kayıtları: `experiments/week2_experiment_records.md`
- Week 1 ayrıntılı günlük: `notes/experiment_log.md`
- Week 2 ayrıntılı günlük: `notes/experiment_log_week2.md`
- Grafik kayıtları: `figures/figure_index.md`
- Week 2 teslim kalite kontrolü: `notes/week2_delivery_addendum.md`

Week 2 standart deney kayıtlarında aynı şablona ek olarak **Başarım Kriteri (Success Criterion)**, **Doğrulama Sonucu (Verification Result)**, **İstatistiksel Anlamlılık (Statistical Significance)** ve **Commit Hash** alanları kullanılmaktadır.
