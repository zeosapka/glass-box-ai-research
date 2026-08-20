# E09 — İstatistiksel Kontrol Testi (Statistical Control Test)

- **Deney ID:** E09
- **Tarih:** 21.08.2026
- **Amaç:** E08'de incelenen aday `496` boyutunun müdahale etkisinin daha geniş bir random-control dağılımından istatistiksel olarak ayrışıp ayrışmadığını test etmek.
- **Hipotez:** Eğer candidate `496` kontrol boyutlarından özel bir mekanistik etkiye sahipse, ortalama L1 müdahale etkisinin random-control dağılımının belirgin biçimde üzerinde olması beklenmektedir.
- **Model:** `distilgpt2` causal language model; hedef katman `layer 5`; hidden size `768`.
- **Aday boyut:** `496`.
- **Random control:** Aday boyut hariç `50` rastgele dimension.
- **Müdahale seviyeleri:** `−0.25σ`, `−0.50σ`, `−1.00σ`, `+0.50σ`, `+1.00σ`.
- **Etki ölçütü:** Her dimension için beş müdahale seviyesindeki L1 çıktı değişimlerinin ortalaması.
- **Başarı kriteri:** `|z| ≥ 2` ve empirical percentile `≥ 90%`.

## Sonuçlar

| Ölçüm | Değer |
|---|---:|
| Candidate mean L1 effect | **0.015057** |
| Control mean L1 effect | **0.011293** |
| Control standard deviation | **0.004407** |
| Z-score | **0.854322** |
| Empirical percentile | **84.00%** |
| `|z| ≥ 2` | **FAIL** |
| `percentile ≥ 90%` | **FAIL** |
| Genel E09 kriteri | **FAIL** |

## Verification Result

Candidate `496`'nın ortalama L1 etkisi random-control ortalamasından daha yüksektir (`0.015057` vs. `0.011293`). Ancak aday etki kontrol dağılımından yalnızca `0.854` standart sapma uzaktadır ve empirical percentile değeri `%84`'tür. Dolayısıyla önceden belirlenen E09 istatistiksel ayrışma kriterleri karşılanmamıştır.

## Statistical Significance

E09'un tanımlı z-score ve percentile kriterleri karşılanmamıştır. Bu sonuç, candidate `496` için güçlü istatistiksel özgüllük iddiasını desteklememektedir. Bu deneyde FAIL sonucu deneyin uygulanamadığı anlamına gelmez; ölçüm ve kontrol karşılaştırması başarıyla tamamlanmıştır.

## Yorum

Candidate `496`, random-control ortalamasından daha yüksek bir müdahale etkisi göstermektedir. Bununla birlikte kontrol dağılımında candidate'dan daha yüksek etkiler bulunduğu için `496` güçlü bir istatistiksel outlier değildir. Sonuç, E08'deki candidate-specific effect magnitude gözlemini daha temkinli hale getirmektedir: müdahale etkisi vardır, ancak bu etkinin random-control dağılımından yeterince ayrıştığı gösterilememiştir.

## Grafik

`figures/week2/e09_statistical_control_distribution.svg` — 50 random control dimension'ın mean L1 effect dağılımı; candidate `496` ve control mean referans çizgileriyle gösterilmiştir.

## Deney Özeti

`MODEL → INTERNAL REPRESENTATION → FEATURE (496) → INTERVENTION → L1 OUTPUT CHANGE → 50 RANDOM CONTROLS → Z-SCORE / PERCENTILE → VALIDATION`
