# 2. Hafta Deney Kayıtları

Bu dosya, 2. hafta deneylerini hocanın istediği standart deney kayıt formatında tutar. Amaç, 1. haftada gözlenen aday özellik/devre etkilerini çoklu seed, eşleştirilmiş veri ve istatistiksel kontroller ile daha savunulabilir hale getirmektir.

---

## E06 — Çoklu Seed Devre Tekrarı (Multi-Seed Circuit Replication)

- **Deney ID:** E06
- **Tarih:** 20.08.2026
- **Amaç:** 1. haftada gözlenen aday devrenin Class 0 üzerindeki etkisinin farklı random seed değerlerinde tekrarlanıp tekrarlanmadığını test etmek.
- **Hipotez:** Eğer aday devrenin Class 0 davranışında gerçek bir mekanistik rolü varsa, farklı seed'lerde bağımsız olarak keşfedilen aday devrelerin ablasyonu Class 0 doğruluğunda belirgin bir düşüş oluşturmalıdır. Random control gruplarının etkisinin aday devreye kıyasla çok daha küçük olması beklenmektedir.
- **Model:** MNIST MLP `784 → 128 → 64 → 10`; ReLU; Adam; learning rate `0.001`; batch size `64`; epoch `5`.
- **Veri Seti:** MNIST (`60000` eğitim / `10000` test).
- **Seed'ler:** `42, 0, 7, 123, 2024`.
- **Değiştirilen parametre:** Her seed için `fc2` katmanındaki 64 nöronun Class 0 selectivity değerlerine göre en güçlü 5 nöron aday devre olarak seçildi ve aktivasyonları `0` yapılarak ablasyon uygulandı. Aynı boyutta random control grubu ile karşılaştırıldı.
- **Kontrol grubu:** Her seed için 5 nörondan oluşan random control grubu.
- **Müdahale grubu:** Her seed için bağımsız keşfedilen 5 nöronluk aday devre.
- **Başarı kriteri:** En az `3/5` seed'de aday devre etkisinin Class 0 doğruluğunda `≤ -5.0 pp` olması ve random control etkisinin belirgin biçimde daha küçük olması.

### Sonuçlar

| Seed | Test Accuracy | Aday Devre | Aday Etki (pp) | Random Control | Random Etki (pp) | Aday/Random Oranı |
|---:|---:|---|---:|---|---:|---:|
| 42 | %97.56 | `[47, 1, 17, 59, 57]` | -14.8980 | `[38, 24, 48, 63, 10]` | +0.1020 | 146.00× |
| 0 | %97.57 | `[46, 47, 38, 53, 8]` | -77.8571 | `[44, 46, 17, 3, 47]` | -2.5510 | 30.52× |
| 7 | %97.45 | `[32, 58, 57, 53, 36]` | -25.2041 | `[47, 14, 15, 18, 0]` | -0.3061 | 82.33× |
| 123 | %97.28 | `[14, 6, 32, 57, 16]` | -10.6122 | `[62, 2, 1, 56, 44]` | +0.3061 | 34.67× |
| 2024 | %97.33 | `[44, 59, 28, 54, 17]` | -9.7959 | `[8, 57, 36, 5, 7]` | +0.7143 | 13.71× |

### Ortalama Sonuçlar

- Ortalama Test Accuracy: **%97.4380**
- Ortalama aday devre etkisi: **-27.6735 pp**
- Ortalama random control etkisi: **-0.3469 pp**
- Ortalama aday/random etki oranı: **61.45×**
- Aday devre kriterini geçen seed: **5/5**
- Random control kriterini geçen seed: **5/5**

### Verification Result

Aday devre etkisi beş seed'in tamamında `-5 pp` eşiğini geçti. Test accuracy değerleri `%97.28–%97.57` aralığında kaldı. Bu sonuçlar, aday devre etkisinin farklı seed'lerde tekrarlandığını ve random control etkilerinden belirgin biçimde büyük olduğunu göstermektedir.

### Statistical Significance

**Henüz hesaplanmadı.** E06, çoklu-seed tekrarlanabilirliği ve müdahale etki büyüklüğünü test etmektedir; tek başına istatistiksel anlamlılık kanıtı olarak değerlendirilmemelidir. Daha geniş random-control dağılımı ve dağılım tabanlı istatistiksel ölçümler sonraki deneylerde kullanılacaktır.

### Unexpected Result

Seed 0'da aday devre etkisi `-77.8571 pp` ile diğer seed'lerden belirgin biçimde büyüktür. Ayrıca Seed 0 random control grubu `[44, 46, 17, 3, 47]`, aday devre `[46, 47, 38, 53, 8]` ile `46` ve `47` nöronlarında örtüşmektedir. Bu nedenle Seed 0 random control'ü tamamen bağımsız bir kontrol olarak değerlendirilmemelidir. Bu durum E06'nın ana tekrar sonucunu bozmaz; ancak daha güçlü kontrol tasarımına ihtiyaç olduğunu gösterir.

### Yorum

Beş farklı random seed'in tamamında aday devre ablasyonu Class 0 doğruluğunda belirgin düşüş oluştururken random control etkileri çok daha küçük kalmıştır. Sonuçlar, aday devrenin Class 0 çıktısında nedensel bir rol oynadığı hipotezini **desteklemektedir**. Ancak bu deney, istatistiksel anlamlılık veya mekanizmanın eksiksiz olarak çözüldüğü anlamına gelmez.

### Sonraki Deney

**E07 — Matched Transformer Internal Representation:** Eşleştirilmiş concept grupları, discovery/holdout ayrımı ve geniş random-control karşılaştırması ile Transformer iç temsilindeki aday feature'ın test edilmesi.

### Deney Özeti

`DATA → MODEL → INTERNAL REPRESENTATION → FEATURE → INTERVENTION → OUTPUT → VERIFICATION`

MNIST → MLP → `fc2` aktivasyonları → Class 0 selectivity ile seçilen 5 nöron → ablasyon → Class 0 accuracy → 5 seed'de tekrar → **başarı kriteri karşılandı**.

---

## E07 — Eşleştirilmiş Transformer İç Temsil Testi (Matched Transformer Internal Representation)

- **Deney ID:** E07
- **Tarih:** 20.08.2026
- **Amaç:** Eşleştirilmiş cümle grupları ve bağımsız Holdout verisi kullanarak Transformer iç temsilindeki aday boyutların (dimension) random control boyutlarından daha güçlü ve tekrarlanabilir biçimde ayrışıp ayrışmadığını test etmek.
- **Hipotez:** Discovery verisinde seçilen aday boyutların L1 (mutlak fark) ölçümü Holdout verisinde de random control boyutlarından belirgin biçimde yüksek kalmalıdır.
- **Model:** DistilGPT-2 tabanlı Transformer; `AutoModel` ile son gizli temsil (last hidden state) çıkarıldı. Cümle temsili, token temsillerinin ortalaması (mean pooling) ile `768` boyutlu vektör olarak oluşturuldu.
- **Veri Seti:** 4 eşleştirilmiş concept grubu, her grupta 10 cümle; toplam `40` cümle. Discovery `20`, Holdout `20`.
- **Discovery / Holdout tasarımı:** Her concept grubundan `5` cümle Discovery ve `5` cümle Holdout olarak ayrıldı. Cümle yapıları eşleştirildi.
- **Aday keşfi:** Discovery grubundaki grup ortalamaları arasındaki dimension separation ölçümüne göre en güçlü 5 boyut seçildi: `[430, 496, 36, 374, 314]`.
- **Random control:** Aday boyutlarla çakışmayan `20` rastgele boyut seçildi: `[122, 329, 519, 529, 667, 106, 229, 620, 641, 574, 434, 591, 565, 753, 507, 605, 455, 246, 2, 633]`.
- **Değiştirilen parametre:** Bu deneyde temsil boyutları üzerinde henüz causal intervention uygulanmadı. Değerlendirme ölçütü L1 ayrışmasıdır.
- **Başarı kriteri:** Aday ortalama L1 değerinden daha yüksek en fazla `5/20` random control bulunması ve sonucun Holdout verisinde de korunması.

### Discovery Sonuçları

| Ölçüm | Değer |
|---|---:|
| Aday ortalama L1 | **2.127904** |
| Random control ortalama L1 | **0.123722** |
| Random control medyan L1 | **0.113314** |
| Random control maksimum L1 | **0.260242** |
| Aday / control ortalama oranı | **17.199049×** |
| Aday ortalamasını geçen control | **0/20** |
| Başarı kriteri | **True** |

Aday boyutların Discovery L1 değerleri: `430=2.387002`, `496=2.939227`, `36=1.832290`, `374=1.471794`, `314=2.009206`.

### Holdout Sonuçları

| Ölçüm | Değer |
|---|---:|
| Aday ortalama L1 | **1.962849** |
| Random control ortalama L1 | **0.124925** |
| Random control medyan L1 | **0.128080** |
| Random control maksimum L1 | **0.252825** |
| Aday / control ortalama oranı | **15.712222×** |
| Aday ortalamasını geçen control | **0/20** |
| Başarı kriteri | **True** |

Aday boyutların Holdout L1 değerleri: `430=2.453163`, `496=3.000549`, `36=1.849851`, `374=1.108517`, `314=1.402164`.

### Verification Result

Discovery ve Holdout sonuçlarının ikisinde de `20` random control boyutunun hiçbiri adayların ortalama L1 değerini geçmedi. Aday/control ortalama oranı Discovery'de **17.20×**, Holdout'ta **15.71×** olarak ölçüldü. Adayların güçlü L1 ayrışması Holdout verisinde korunmuştur.

### Statistical Significance

**Henüz hesaplanmadı.** E07'deki 20 random control karşılaştırması ve Discovery/Holdout ayrımı, aday özelliğin seçime bağlı tek bir gözlem olmadığını test etmek için kullanılmıştır. Ancak bu sonuç tek başına formal istatistiksel anlamlılık veya nedensellik kanıtı değildir. Daha geniş random-control dağılımı ve z-score/percentile gibi dağılım tabanlı ölçümler sonraki deneylerde uygulanacaktır.

### Methodological Note

Aday boyutlar Discovery verisindeki dimension separation ölçümüne göre seçildiği için Discovery L1 sonucu seçim yanlılığı (selection bias) içerebilir. Bu nedenle Holdout sonucu özellikle önemlidir. Ayrıca mevcut E07 sonucu L1 temsil ayrışmasını göstermektedir; **causal intervention henüz uygulanmamıştır**. Gerçek nedensel test için aday boyutların modelin gerçek iç aktivasyonları üzerinde kontrollü biçimde değiştirilmesi ve model çıktısındaki değişimin ölçülmesi gerekmektedir.

### Yorum

E07 sonuçları, Discovery'de seçilen `[430, 496, 36, 374, 314]` boyutlarının eşleştirilmiş veri üzerinde random control boyutlarından çok daha yüksek L1 ayrışmasına sahip olduğunu ve bu ayrışmanın bağımsız Holdout verisinde de korunduğunu göstermektedir. Bu sonuçlar aday temsil boyutlarının ilgili concept gruplarını ayırt eden güçlü adaylar olduğu hipotezini **desteklemektedir**. Ancak L1 ayrışması korelatif/temsil düzeyinde bir bulgudur; nedensellik iddiası için intervention gereklidir.

### Sonraki Deney

**E08 — Graded Representation Intervention:** Aday boyutlar ve random control boyutları üzerinde `−0.25σ`, `−0.5σ`, `−1σ`, `+0.5σ`, `+1σ` düzeylerinde kontrollü müdahale uygulanarak müdahale büyüklüğü ile çıktı/temsil değişimi arasındaki ilişki test edilecektir.

### Deney Özeti

`DATA → MODEL → INTERNAL REPRESENTATION → FEATURE → L1 VALIDATION → DISCOVERY/HOLDOUT → VERIFICATION`

40 eşleştirilmiş cümle → Transformer → 768 boyutlu son gizli temsil → Discovery'de separation ile seçilen 5 aday → L1 ölçümü → 20 random control → Discovery ve Holdout doğrulaması → **başarı kriteri karşılandı; causal intervention sonraki deneyde**.

---

## E08 — Kademeli Transformer Müdahalesi (Graded Transformer Intervention)

- **Deney ID:** E08
- **Tarih:** 21.08.2026
- **Amaç:** E07'de keşfedilen Transformer iç temsil boyutlarından aday `496` üzerinde kontrollü kademeli müdahaleler uygulayarak müdahale büyüklüğü ile model çıktısındaki değişim (L1) arasında dose-response ilişkisi bulunup bulunmadığını test etmek ve sonucu random control boyutlarıyla karşılaştırmak.
- **Hipotez:** Müdahale büyüklüğü arttıkça aday boyutun model çıktısındaki L1 değişiminin yaklaşık monoton biçimde artması beklenmektedir. Kontrol boyutlarında daha zayıf veya düzensiz bir ilişki beklenmektedir.
- **Model:** `distilgpt2` tabanlı causal language model (`AutoModelForCausalLM`), `6` Transformer katmanı, `768` hidden size, hedef müdahale katmanı `layer 5`.
- **Veri Seti:** E07'deki eşleştirilmiş concept cümleleri kullanıldı. E08 doğrulama akışında tek bir Discovery cümlesi (`discovery_sentences[0]`) üzerinde kontrollü müdahale uygulandı. Bu nedenle sonuç, E08'in mevcut tek-cümlelik doğrulama/pilot uygulamasıdır; geniş cümle örneklemiyle genelleme iddiası yapılmamaktadır.
- **Aday boyut:** `496`.
- **Kontrol boyutları:** `[434, 161, 541, 219, 408]`.
- **Müdahale seviyeleri:** `−0.25σ`, `−0.50σ`, `−1.00σ`, `+0.50σ`, `+1.00σ`.
- **Çıktı ölçütü:** Son token logits'inden elde edilen olasılık dağılımının baseline'a göre L1 değişimi.
- **Müdahale yöntemi:** Hedef Transformer katmanının hidden-state çıktısında seçilen boyut kontrollü olarak `intervention_level × σ` kadar değiştirildi; ardından modelin ileri yayılımı (forward pass) ile son token olasılıkları yeniden hesaplandı.
- **Başarı kriteri:** Aday için `|Spearman ρ| ≥ 0.80`; kontrollerin daha zayıf (`|ρ| < 0.50`) veya düzensiz olması beklenmektedir. Ek karşılaştırma olarak adayın ortalama L1 etkisinin kontrol dağılımından yüksek olması incelenmiştir.

### Aday 496 Sonuçları

| Müdahale | L1 çıktı değişimi |
|---:|---:|
| `−0.25σ` | **0.008902** |
| `−0.50σ` | **0.017499** |
| `−1.00σ` | **0.033701** |
| `+0.50σ` | **0.018689** |
| `+1.00σ` | **0.038482** |

- Aday ortalama L1: **0.023454**
- Spearman `ρ`: **0.9487**
- Spearman `p`: **0.013847**
- Kontrol dağılımındaki percentile: **%100** (`5/5` kontrol boyutundan daha yüksek)

### Kontrol Sonuçları

| Kontrol | Ortalama L1 | Spearman `ρ` | Spearman `p` |
|---:|---:|---:|---:|
| `408` | 0.014887 | 0.9487 | 0.013847 |
| `434` | 0.001757 | 0.9487 | 0.013847 |
| `541` | 0.001511 | 0.9487 | 0.013847 |
| `161` | 0.000810 | 0.9487 | 0.013847 |
| `219` | 0.000652 | 0.9487 | 0.013847 |

- Kontrol ortalama L1: **0.003923**
- En güçlü kontrol: `408` → **0.014887**
- Aday / kontrol ortalama L1 oranı: **5.978×**
- Aday / en güçlü kontrol oranı: yaklaşık **1.58×**

### Verification Result

Aday `496`, beş random control boyutunun tamamından daha yüksek ortalama L1 çıktı değişimi göstermiştir. Adayın ortalama L1 etkisi `0.023454`, kontrol ortalaması `0.003923` ve en güçlü kontrol `0.014887` olarak ölçülmüştür. Adayın kontrol dağılımındaki basit ampirik percentile değeri `%100` olmuştur.

Adayda müdahale büyüklüğü arttıkça L1 değişiminin genel olarak arttığı görülmüştür. Örneğin `−0.25σ → 0.008902`, `−0.50σ → 0.017499`, `−1.00σ → 0.033701` ve `+0.50σ → 0.018689`, `+1.00σ → 0.038482` sonuçları dose-response davranışıyla uyumludur.

### Statistical Significance

E08 sonucu **formal istatistiksel anlamlılık kanıtı olarak değerlendirilmemelidir**. Spearman `ρ = 0.9487` ve `p = 0.013847` adayı destekleyen tek başına özgül bir test değildir; çünkü beş kontrol boyutunun tamamında da aynı `ρ = 0.9487` ve `p = 0.013847` elde edilmiştir. Bu nedenle monoton dose-response davranışı modelin müdahale büyüklüğüne genel duyarlılığını yansıtıyor olabilir.

### Success Criteria Verification

| Kriter | Sonuç | Değerlendirme |
|---|---:|---|
| Aday `|Spearman ρ| ≥ 0.80` | `0.9487` | **PASS** |
| Aday ortalama L1 > tüm kontrol boyutları | `0.023454 > 0.014887` | **PASS** |
| En az bir kontrol `|ρ| < 0.50` | Yok; tüm kontroller `0.9487` | **FAIL** |
| Genel E08 değerlendirmesi |  | **PARTIAL / SUPPORT** |

### Unexpected Result

Tüm kontrol boyutlarında Spearman `ρ` değerinin aday ile aynı çıkması (`0.9487`), monotonluk ölçütünün aday boyuta özgü olmadığını gösterdi. Bu nedenle E08'de dose-response varlığı gösterilmiş olsa da dose-response'un tek başına aday mekanizmaya özgü olduğu sonucuna varılmadı. Ayrıca kontrol `408`, `0.014887` ortalama L1 ile diğer kontrollerden belirgin biçimde güçlü çıktı ve adayın etkisinin özgüllüğü konusunda daha geniş kontrol dağılımına ihtiyaç olduğunu gösterdi.

### Methodological Note

E08'in mevcut uygulaması tek bir Discovery cümlesi üzerinde gerçekleştirildiği için sonuçların farklı cümlelere ve Holdout verisine genellenmesi henüz gösterilmemiştir. Ayrıca yalnızca `5` kontrol boyutu kullanılmıştır. Bu nedenle `%100` percentile sonucu yalnızca “5 kontrolün 5'inden daha yüksek” şeklinde yorumlanmalıdır. Daha geniş kontrol dağılımı ve dağılım tabanlı istatistiksel testler sonraki deneyde uygulanacaktır.

### Yorum

E08, seçilen aday boyut `496` üzerinde **müdahale büyüklüğü arttıkça model çıktısındaki L1 değişiminin genel olarak arttığını** göstermiştir. Adayın ortalama etkisi beş kontrolün tamamından daha yüksek olsa da aynı monoton ilişki bütün kontrollerde de gözlendiğinden, Spearman monotonluğu aday özgüllüğü için yeterli değildir. Bu nedenle deney **PARTIAL / SUPPORT** olarak değerlendirilmiştir: adayın güçlü dose-response ve daha büyük etki büyüklüğü gösterdiği desteklenmiş, ancak dose-response davranışının aday boyuta özgü olduğu gösterilememiştir.

Bu sonuç **nedenselliğin kanıtlandığı** anlamına gelmez; kontrollü hidden-state müdahalesi ile çıktı değişimi arasında mekanistik kanıt yönünde bir adım sağlar.

### Sonraki Deney

**E09 — Random Control Distribution / Statistical Test:** Aday `496` etkisinin çok daha geniş bir random-control dağılımındaki konumunu test etmek; `50` random control ile kontrol ortalaması, standart sapma, z-score ve percentile hesaplamak.

### Deney Özeti

`DATA → MODEL → INTERNAL REPRESENTATION → FEATURE → INTERVENTION → OUTPUT → VERIFICATION`

E07 eşleştirilmiş cümleler → `distilgpt2` causal LM → layer 5 hidden state → candidate dimension `496` → `±σ` kademeli müdahale → son token olasılıklarında L1 değişimi → 5 random control → **güçlü dose-response ve daha büyük aday etkisi desteklendi; aday özgüllüğü PARTIAL / SUPPORT**.

---

## E09 — İstatistiksel Kontrol Testi (Statistical Control Test)

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

### Sonuçlar

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

### Verification Result

Candidate `496`'nın ortalama L1 etkisi random-control ortalamasından daha yüksektir (`0.015057` vs. `0.011293`). Ancak aday etki kontrol dağılımından yalnızca `0.854` standart sapma uzaktadır ve empirical percentile değeri `%84`'tür. Dolayısıyla önceden belirlenen E09 istatistiksel ayrışma kriterleri karşılanmamıştır.

### Statistical Significance

E09'un tanımlı z-score ve percentile kriterleri karşılanmamıştır. Bu sonuç, candidate `496` için güçlü istatistiksel özgüllük iddiasını desteklememektedir. Bu deneyde FAIL sonucu deneyin uygulanamadığı anlamına gelmez; ölçüm ve kontrol karşılaştırması başarıyla tamamlanmıştır.

### Yorum

Candidate `496`, random-control ortalamasından daha yüksek bir müdahale etkisi göstermektedir. Bununla birlikte kontrol dağılımında candidate'dan daha yüksek etkiler bulunduğu için `496` güçlü bir istatistiksel outlier değildir. Sonuç, E08'deki candidate-specific effect magnitude gözlemini daha temkinli hale getirmektedir: müdahale etkisi vardır, ancak bu etkinin random-control dağılımından yeterince ayrıştığı gösterilememiştir.

### Grafik

`figures/week2/e09_statistical_control_distribution.svg` — 50 random control dimension'ın mean L1 effect dağılımı; candidate `496` ve control mean referans çizgileriyle gösterilmiştir.

### Deney Özeti

`MODEL → INTERNAL REPRESENTATION → FEATURE (496) → INTERVENTION → L1 OUTPUT CHANGE → 50 RANDOM CONTROLS → Z-SCORE / PERCENTILE → VALIDATION`
