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

---

# Hafta 2 — Transformer Sonuçları

## E06 — Çoklu Seed Devre Tekrarı

- 5 seed'in `5/5`'inde aday devre etkisi Class 0 doğruluğunda `≤ -5 pp` eşiğini geçti.
- Ortalama aday devre etkisi: **−27.6735 pp**.
- Ortalama random control etkisi: **−0.3469 pp**.
- Ortalama aday/random etki oranı: **61.45×**.
- Sonuç: **Başarı kriteri karşılandı; formal istatistiksel anlamlılık henüz hesaplanmadı.**

## E07 — Eşleştirilmiş Transformer İç Temsil

- Aday boyutlar: `[430, 496, 36, 374, 314]`.
- Discovery aday ortalama L1: **2.127904**; random control ortalaması **0.123722**; oran **17.20×**.
- Holdout aday ortalama L1: **1.962849**; random control ortalaması **0.124925**; oran **15.71×**.
- Discovery ve Holdout'ta `20` kontrol boyutunun hiçbiri aday ortalamasını geçmedi.
- Sonuç: **Başarı kriteri karşılandı; L1 ayrışması causal intervention değildir.**

## E08 — Kademeli Transformer Müdahalesi

- Causal LM: `distilgpt2`, hedef katman: `layer 5`, hidden size: `768`.
- Aday boyut: `496`.
- Kontroller: `[434, 161, 541, 219, 408]`.
- Müdahale seviyeleri: `−0.25σ`, `−0.50σ`, `−1.00σ`, `+0.50σ`, `+1.00σ`.
- Aday ortalama L1 çıktı değişimi: **0.023454**.
- Kontrol ortalama L1: **0.003923**.
- En güçlü kontrol: `408 → 0.014887`.
- Aday / kontrol ortalama oranı: **5.978×**.
- Aday / en güçlü kontrol oranı: **≈1.58×**.
- Aday Spearman: **ρ = 0.9487**, `p = 0.013847`.
- Beş kontrolün tamamında da **ρ = 0.9487**, `p = 0.013847` elde edildi.
- Adayın basit kontrol percentile değeri: **%100 (5/5 kontrolden yüksek)**.
- Sonuç: **PARTIAL / SUPPORT**.

### E08 Ana Bulgusu

Müdahale büyüklüğü arttıkça model çıktısındaki L1 değişimi genel olarak artmıştır. Bu, aday `496` için güçlü bir **dose-response (doz-cevap)** davranışı göstermektedir. Ancak aynı monoton ilişki bütün kontrol boyutlarında da görüldüğünden, Spearman monotonluğu aday boyuta özgü bir mekanizma kanıtı olarak kullanılamaz.

Adayın ortalama L1 etkisinin tüm beş kontrolden yüksek olması aday lehine ek destek sağlamaktadır; ancak kontrol sayısının yalnızca `5` olması nedeniyle `%100` percentile sonucu sınırlı bir ampirik karşılaştırmadır. E08 tek bir Discovery cümlesi üzerinde yürütüldüğü için farklı cümlelere/Holdout'a genelleme henüz gösterilmemiştir.

### E08 Başarı Kriterleri

| Kriter | Sonuç |
|---|---:|
| Aday `|Spearman ρ| ≥ 0.80` | **PASS** |
| Aday ortalama L1 > tüm kontroller | **PASS** |
| En az bir kontrol `|ρ| < 0.50` | **FAIL** |
| Genel değerlendirme | **PARTIAL / SUPPORT** |

### E08 Sonuç Yorumu

E08, **“müdahale büyüklüğü arttıkça çıktı değişimi artıyor”** hipotezini desteklemektedir. Bununla birlikte bu davranış modelin genel müdahale duyarlılığıyla da açıklanabildiğinden, **dose-response tek başına aday özgüllüğü sağlamamaktadır**. Daha geniş random-control dağılımı ve dağılım tabanlı istatistiksel test için sonraki adım **E09**'dur.

## E09 — İstatistiksel Kontrol Testi (Statistical Control Test)

- Aday boyut: `496`.
- Model: `distilgpt2`, hedef katman: `layer 5`, hidden size: `768`.
- Random control sayısı: **50**; aday boyut kontrol grubundan çıkarıldı.
- Müdahale seviyeleri: `−0.25σ`, `−0.50σ`, `−1.00σ`, `+0.50σ`, `+1.00σ`.
- Her boyut için beş müdahale seviyesinin ortalama L1 çıktı değişimi scalar effect olarak kullanıldı.
- Aday ortalama L1 etkisi: **0.015057**.
- Kontrol ortalama L1 etkisi: **0.011293**.
- Kontrol standart sapması: **0.004407**.
- Z-score: **0.854322**.
- Empirical percentile: **84.00%**.
- Sonuç: **FAIL** — önceden belirlenen `|z| ≥ 2` ve `percentile ≥ 90%` kriterlerinin hiçbiri karşılanmadı.

### E09 Ana Bulgusu

Candidate `496`'nın ortalama L1 müdahale etkisi random control ortalamasından daha yüksektir (`0.015057` vs. `0.011293`). Ancak aday etki kontrol dağılımından yalnızca `0.854` standart sapma uzaktadır ve empirical percentile değeri `%84`'tür. Kontrol boyutları arasında adaydan daha yüksek etkiler de bulunmaktadır. Bu nedenle `496`, E09'un önceden tanımlanan istatistiksel ayrışma kriterlerini karşılamamaktadır.

### E09 Başarı Kriterleri

| Kriter | Sonuç |
|---|---:|
| `|z| ≥ 2` | **FAIL** (`0.854322`) |
| `percentile ≥ 90%` | **FAIL** (`84.00%`) |
| Genel E09 kriteri | **FAIL** |

### E09 Yorum

E09'un başarısız olması deneyin uygulanamadığı anlamına gelmez; deney başarıyla tamamlanmış ve adayın random-control dağılımındaki konumu ölçülmüştür. Sonuç, `496` boyutunun kontrol ortalamasından daha yüksek bir müdahale etkisine sahip olduğunu, ancak bu etkinin istatistiksel olarak güçlü bir outlier/separation düzeyine ulaşmadığını göstermektedir. Bu nedenle E09, aday `496` için güçlü istatistiksel özgüllük iddiasını **desteklememektedir**.

### E09 Grafik

`figures/week2/e09_statistical_control_distribution.svg` — 50 random control boyutunun mean L1 effect dağılımı; aday `496` ve kontrol ortalaması referans çizgileriyle gösterilmiştir.

## E10 — Grup Müdahalesi (Group Intervention)

- Aday grup: `[471, 228, 12, 358, 529]`.
- Model: `distilgpt2` causal language model; hedef katman `layer 5`; hidden size `768`.
- Test cümlesi: `The cat is sitting on the mat.`
- Müdahale yöntemi: Hedef katmandaki seçilen hidden-state boyutları birlikte `0` yapılarak grup ablasyonu uygulandı.
- Tekil aday boyut etkileri: `471=0.001824`, `228=0.003006`, `12=0.003591`, `358=0.032780`, `529=0.008693`.
- Tekil etkilerin basit toplamı: **0.049894**.
- Birlikte aday grup etkisi: **0.033458**.
- Non-additive difference: **−0.016436**.
- Joint / individual-sum oranı: **0.670583**.
- Random kontrol grubu sayısı: `5`; her grup `5` farklı dimension içerir ve aday boyutlarla çakışmaz.
- Random grup etkileri: `0.043100`, `0.066373`, `0.021147`, `0.046709`, `0.082566`.
- Random control ortalaması: **0.051979**.
- Random control standart sapması: **0.023452**.
- Candidate vs. random z-score: **−0.789750**.
- Candidate percentile: **%20**.

### E10 Başarı Kriterleri

| Kriter | Sonuç | Değerlendirme |
|---|---:|---|
| (a) Candidate group random kontrollerden belirgin büyük (`z ≥ 2`) | `−0.789750` | **FAIL** |
| (b) Grup etkisi tekil etkilerin basit toplamından farklı | `−0.016436` | **PASS / SUPPORT** |
| Genel E10 değerlendirmesi |  | **PASS / SUPPORT** |

### E10 Ana Bulgusu

Aday 5'li grubun birlikte ablasyonu `0.033458` L1 çıktı değişimi oluşturmuştur. Bu etki random 5'li kontrol gruplarının ortalamasından (`0.051979`) daha düşük olduğu için candidate group'un random kontrollere göre daha güçlü bir grup etkisi oluşturduğu desteklenmemiştir. Candidate'ın random dağılımdaki konumu `%20` percentile ve `z = −0.789750` olarak ölçülmüştür.

Buna karşılık tekil aday boyutların etkilerinin basit toplamı `0.049894` iken birlikte grup etkisi `0.033458` olmuştur. `Joint / individual-sum = 0.670583` sonucu, birlikte müdahalenin tekil etkilerin basit toplamına eşit olmadığını ve **non-additive** davranış gözlendiğini göstermektedir.

Bu sonuç istatistiksel anlamlılık veya mekanizmanın kanıtlandığı anlamına gelmez. Özellikle random kontrol sayısının `5` olması nedeniyle z-score karşılaştırması sınırlı ve betimseldir. E10'un desteklediği nokta, bu deney tasarımında grup etkisinin additif olmamasıdır.

### E10 Grafik

`figures/week2/e10_group_effect_comparison.svg` — aday grubun birlikte etkisini, tekil etkilerin toplamını ve beş random 5-boyutlu kontrol grubunu karşılaştırır; random kontrol ortalaması, `z = −0.7898` ve `%20` percentile bilgileri görsel olarak işaretlenmiştir.
