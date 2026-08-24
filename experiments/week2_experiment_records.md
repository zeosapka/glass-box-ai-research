# 2. Hafta Deney Kayıtları

Bu dosya, 2. hafta deneylerini hocanın istediği standart deney kayıt formatında tutar. Her deney aynı kayıt şablonunu kullanır; deney içi ayrıntılar ve tablolar ana kaydın altında korunur.

> **Standart deney şablonu:** Deney ID → Tarih → Amaç → Hipotez → Model → Dataset → Seed → Değiştirilen parametre → Kontrol grubu → Müdahale grubu → Sonuç → Accuracy / etki değişimi → Hedef başarım kriteri → Doğrulama sonucu → İstatistiksel anlamlılık (z / persentil, varsa) → Grafik → Yorum → Beklenmeyen sonuç → Commit hash → Sonraki deney.

---

## E06 — Çoklu Seed Devre Tekrarı (Multi-Seed Circuit Replication)

- **Deney ID:** E06
- **Tarih:** 20.08.2026
- **Amaç:** 1. haftada gözlenen aday devrenin Class 0 üzerindeki etkisinin farklı random seed değerlerinde tekrarlanıp tekrarlanmadığını test etmek.
- **Hipotez:** Farklı seed'lerde bağımsız olarak keşfedilen aday devrelerin ablasyonu Class 0 doğruluğunda belirgin düşüş oluşturmalı; random control etkileri aday devreye kıyasla çok daha küçük kalmalıdır.
- **Model:** MNIST MLP `784 → 128 → 64 → 10`; ReLU; Adam; learning rate `0.001`; batch size `64`; epoch `5`.
- **Dataset:** MNIST (`60000` eğitim / `10000` test).
- **Seed:** `42, 0, 7, 123, 2024`.
- **Değiştirilen parametre:** Her seed için `fc2` katmanındaki 64 nörondan Class 0 selectivity açısından en güçlü 5 nöron aday devre seçildi ve aktivasyonları `0` yapılarak ablate edildi.
- **Kontrol grubu:** Her seed için 5 nörondan oluşan random control grubu.
- **Müdahale grubu:** Her seed için bağımsız keşfedilen 5 nöronluk aday devre.
- **Sonuç:** Beş seed'in tamamında aday devre etkisi `≤ -5.0 pp`; ortalama aday etki `-27.6735 pp`, random control ortalaması `-0.3469 pp`, ortalama oran `61.45×`.
- **Accuracy / etki değişimi:** Test accuracy ortalaması `%97.4380`; aday etkileri `-14.8980, -77.8571, -25.2041, -10.6122, -9.7959 pp`.
- **Hedef başarım kriteri:** En az `3/5` seed'de aday devre etkisinin Class 0 doğruluğunda `≤ -5.0 pp` olması ve random control etkisinin belirgin biçimde daha küçük olması.
- **Doğrulama sonucu:** **PASS.** Aday devre kriterini geçen seed `5/5`; aday etkisi tüm seed'lerde eşik altında ve random control etkilerinden belirgin biçimde büyüktür.
- **İstatistiksel anlamlılık (z / persentil, varsa):** Henüz hesaplanmadı; E06 çoklu-seed tekrarlanabilirlik ve etki büyüklüğü testidir.
- **Grafik:** Multi-seed candidate-effect ve random-control karşılaştırması; Week 2 grafiklerinde E06 karşılaştırması.
- **Yorum:** Sonuçlar aday devrenin Class 0 çıktısında nedensel rol oynadığı hipotezini **desteklemektedir**; eksiksiz mekanizma veya formal istatistiksel anlamlılık iddiası değildir.
- **Beklenmeyen sonuç:** Seed 0'da aday etki `-77.8571 pp` ile çok büyüktür; ayrıca random control ile aday arasında `46` ve `47` nöronlarında örtüşme vardır.
- **Commit hash:** Deney kaydında belirtilmemiştir.
- **Sonraki deney:** **E07 — Matched Transformer Internal Representation.**

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

### Deney Özeti

`DATA → MODEL → INTERNAL REPRESENTATION → FEATURE → INTERVENTION → OUTPUT → VERIFICATION`

MNIST → MLP → `fc2` aktivasyonları → Class 0 selectivity ile seçilen 5 nöron → ablasyon → Class 0 accuracy → 5 seed'de tekrar → **başarı kriteri karşılandı**.

---

## E07 — Eşleştirilmiş Transformer İç Temsil Testi (Matched Transformer Internal Representation)

- **Deney ID:** E07
- **Tarih:** 20.08.2026
- **Amaç:** Eşleştirilmiş cümle grupları ve bağımsız Holdout verisi kullanarak Transformer iç temsilindeki aday boyutların random control boyutlarından daha güçlü ve tekrarlanabilir biçimde ayrışıp ayrışmadığını test etmek.
- **Hipotez:** Discovery'de seçilen aday boyutların L1 ayrışması Holdout'ta da random control boyutlarından belirgin biçimde yüksek kalmalıdır.
- **Model:** DistilGPT-2 tabanlı Transformer; `AutoModel`; son gizli temsil; mean pooling; `768` boyut.
- **Dataset:** 4 eşleştirilmiş concept grubu, toplam `40` cümle; Discovery `20`, Holdout `20`.
- **Seed:** Kaynak kaydında belirtilmemiş.
- **Değiştirilen parametre:** Temsil boyutları değiştirilmedi; Discovery separation ölçümüyle aday boyutlar seçildi.
- **Kontrol grubu:** Adaylarla çakışmayan `20` random control boyutu.
- **Müdahale grubu:** Discovery'de seçilen `[430, 496, 36, 374, 314]` aday boyutları; causal intervention bu deneyde uygulanmadı.
- **Sonuç:** Discovery aday ortalama L1 `2.127904`, control ortalaması `0.123722`; Holdout aday `1.962849`, control `0.124925`; her iki sette de `0/20` control aday ortalamasını geçti.
- **Accuracy / etki değişimi:** Accuracy ölçülmedi; L1 ayrışma ölçüldü. Aday/control oranı Discovery `17.20×`, Holdout `15.71×`.
- **Hedef başarım kriteri:** Aday ortalama L1 değerinden daha yüksek en fazla `5/20` random control bulunması ve sonucun Holdout'ta korunması.
- **Doğrulama sonucu:** **PASS.** Discovery ve Holdout'ta `0/20` control adayı geçti; güçlü ayrışma Holdout'ta korundu.
- **İstatistiksel anlamlılık (z / persentil, varsa):** Henüz hesaplanmadı; 20 random control ve Holdout doğrulaması kullanıldı ancak formal istatistiksel test yapılmadı.
- **Grafik:** Discovery vs. Holdout aday/control L1 sıralama karşılaştırması.
- **Yorum:** Aday boyutlar güçlü temsil düzeyi ayrışması gösterdi; bu sonuç korelatif/temsil düzeyindedir, nedensellik kanıtı değildir.
- **Beklenmeyen sonuç:** Discovery seçim yanlılığı içerebileceğinden Holdout sonucu özellikle önemlidir.
- **Commit hash:** Deney kaydında belirtilmemiştir.
- **Sonraki deney:** **E08 — Graded Transformer Intervention.**

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
- **Amaç:** E07'de keşfedilen aday `496` boyutunda müdahale büyüklüğü ile model çıktısındaki L1 değişimi arasında dose-response ilişkisi olup olmadığını ve etkinin random controls'dan ayrışıp ayrışmadığını test etmek.
- **Hipotez:** Müdahale büyüklüğü arttıkça aday L1 etkisi genel olarak artmalı; kontroller daha zayıf veya düzensiz olmalıdır.
- **Model:** `distilgpt2` causal language model (`AutoModelForCausalLM`), `6` Transformer katmanı, `768` hidden size, hedef `layer 5`.
- **Dataset:** E07 eşleştirilmiş concept cümleleri; mevcut doğrulama akışı tek Discovery cümlesi (`discovery_sentences[0]`) üzerinde uygulandı.
- **Seed:** Kaynak kaydında belirtilmemiş.
- **Değiştirilen parametre:** Hidden-state'te aday/control boyutu `−0.25σ`, `−0.50σ`, `−1.00σ`, `+0.50σ`, `+1.00σ` seviyelerinde kontrollü değiştirildi.
- **Kontrol grubu:** `[434, 161, 541, 219, 408]` random control boyutları.
- **Müdahale grubu:** Aday boyut `496`.
- **Sonuç:** Aday ortalama L1 `0.023454`; Spearman `ρ=0.9487`; control ortalaması `0.003923`; aday 5/5 control'dan daha yüksek.
- **Accuracy / etki değişimi:** Son token olasılık dağılımında L1 değişimi kullanıldı; aday seviyeleri `0.008902, 0.017499, 0.033701, 0.018689, 0.038482`.
- **Hedef başarım kriteri:** Aday `|Spearman ρ| ≥ 0.80`; kontrollerin daha zayıf (`|ρ| < 0.50`) veya düzensiz olması ve aday ortalama L1'nin controls'dan yüksek olması beklenmiştir.
- **Doğrulama sonucu:** **PARTIAL / SUPPORT.** Aday `ρ` ve ortalama L1 kriterlerini geçti; ancak tüm controls'da aynı `ρ=0.9487` görüldüğü için aday özgüllüğü gösterilemedi.
- **İstatistiksel anlamlılık (z / persentil, varsa):** Spearman `p=0.013847` raporlandı; formal özgüllük kanıtı değildir çünkü aynı `ρ/p` tüm controls'da da oluştu.
- **Grafik:** Müdahale büyüklüğüne karşı L1/olasılık değişimi; aday ve controls üst üste.
- **Yorum:** Güçlü dose-response ve daha büyük aday etkisi desteklendi; aday özgüllüğü ve genelleme henüz gösterilmedi.
- **Beklenmeyen sonuç:** Bütün control boyutlarında Spearman `ρ` adayla aynı çıktı; control `408` diğer controls'dan belirgin güçlüydü.
- **Commit hash:** Deney kaydında belirtilmemiştir.
- **Sonraki deney:** **E09 — Random Control Distribution / Statistical Test.**

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
- **Tarih:** Kaynak kaydında belirtilmemiş.
- **Amaç:** Aday `496` boyutunun müdahale etkisinin geniş bir `50` random-control dağılımındaki konumunu test etmek.
- **Hipotez:** Aday etki control dağılımından güçlü biçimde ayrışıyorsa `|z| ≥ 2` ve `percentile ≥ 90%` kriterleri karşılanmalıdır.
- **Model:** `distilgpt2`; hedef katman `layer 5`; hidden size `768`.
- **Dataset:** E08 ile aynı müdahale akışı; kaynakta ayrıca ayrıntılı veri bölümü belirtilmemiştir.
- **Seed:** Kaynak kaydında belirtilmemiş.
- **Değiştirilen parametre:** Aday `496` ve `50` random control boyutunda aynı beş müdahale seviyesinin ortalama L1 etkisi hesaplandı.
- **Kontrol grubu:** Adaydan farklı `50` random control boyutu.
- **Müdahale grubu:** Aday dimension `496`.
- **Sonuç:** Aday ortalama L1 `0.015057`; control ortalaması `0.011293`; control std `0.004407`; z `0.854322`; percentile `%84.00`.
- **Accuracy / etki değişimi:** Aday etkisi control ortalamasından `0.003764` daha yüksek; ancak dağılım ayrışması kriterini karşılamadı.
- **Hedef başarım kriteri:** `|z| ≥ 2` ve `percentile ≥ 90%`.
- **Doğrulama sonucu:** **FAIL.** Her iki istatistiksel ayrışma kriteri de karşılanmadı.
- **İstatistiksel anlamlılık (z / persentil, varsa):** z-score `0.854322`; empirical percentile `%84.00`; formal güçlü ayrışma yok.
- **Grafik:** `figures/week2/e09_statistical_control_distribution.svg` — 50 random-control dağılımı, aday ve control ortalaması işaretli.
- **Yorum:** Deney başarıyla uygulandı; aday control ortalamasından yüksek olsa da güçlü outlier/separation düzeyine ulaşmadı.
- **Beklenmeyen sonuç:** Control dağılımında adaydan daha yüksek etkiler bulundu.
- **Commit hash:** Deney kaydında belirtilmemiştir.
- **Sonraki deney:** **E10 — Grup Müdahalesi.**

### E09 Ana Bulgusu

Candidate `496`'nın ortalama L1 müdahale etkisi random control ortalamasından daha yüksektir (`0.015057` vs. `0.011293`). Ancak aday etki kontrol dağılımından yalnızca `0.854` standart sapma uzaktadır ve empirical percentile değeri `%84`'tür. Kontrol boyutları arasında adaydan daha yüksek etkiler de bulunmaktadır. Bu nedenle `496`, E09'un önceden belirlenen istatistiksel ayrışma kriterlerini karşılamamaktadır.

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

---

## E10 — Grup Müdahalesi (Group Intervention)

- **Deney ID:** E10
- **Tarih:** 21.08.2026
- **Amaç:** 5 boyutluk aday grubun birlikte ablasyon etkisini tekil boyut etkilerinin basit toplamı ve random 5-boyutlu control gruplarıyla karşılaştırmak.
- **Hipotez:** Aday grup random controls'dan daha güçlü olabilir ve/veya birlikte etki tekil etkilerin basit toplamından farklı non-additive davranış gösterebilir.
- **Model:** `distilgpt2` causal language model; hedef `layer 5`; hidden size `768`.
- **Dataset:** Test cümlesi `The cat is sitting on the mat.`
- **Seed:** Kaynak kaydında belirtilmemiş.
- **Değiştirilen parametre:** Aday `[471, 228, 12, 358, 529]` ve control gruplarındaki hidden-state boyutları birlikte `0` yapıldı.
- **Kontrol grubu:** `5` random grup; her biri `5` dimension; toplam `25` farklı control dimension.
- **Müdahale grubu:** Aday 5'li grup `[471, 228, 12, 358, 529]`.
- **Sonuç:** Aday grup etkisi `0.033458`; tekil toplam `0.049894`; non-additive fark `−0.016436`; random control ortalaması `0.051979`; z `−0.789750`; percentile `%20`.
- **Accuracy / etki değişimi:** L1 çıktı değişimi kullanıldı; aday group effect random control ortalamasından daha düşük.
- **Hedef başarım kriteri:** (a) Aday grup random controls'dan belirgin büyük (`z ≥ 2`) ve/veya (b) grup etkisi tekil etkilerin basit toplamından farklı.
- **Doğrulama sonucu:** **PASS / SUPPORT.** Kriter (a) FAIL; kriter (b) PASS/SUPPORT. Bu nedenle yalnızca non-additive davranış desteklenmiştir.
- **İstatistiksel anlamlılık (z / persentil, varsa):** z `−0.789750`, percentile `%20`; yalnızca `5` random grup olduğu için formal anlamlılık kanıtı değildir.
- **Grafik:** `figures/week2/e10_group_effect_comparison.svg` — aday grup, tekil toplam ve random grup etkileri.
- **Yorum:** Aday grubun random controls'dan güçlü olduğu desteklenmedi; birlikte etkinin tekil toplamdan farklı olması non-additive davranışı destekledi.
- **Beklenmeyen sonuç:** Aday grup random control ortalamasının altında kaldı.
- **Commit hash:** Deney kaydında belirtilmemiştir.
- **Sonraki deney:** **E11 — Sentetik True-vs-Spurious Feature Testi.**

### Tekil Aday Boyut Sonuçları

| Dimension | Tekil L1 etkisi |
|---:|---:|
| 471 | 0.001824 |
| 228 | 0.003006 |
| 12 | 0.003591 |
| 358 | 0.032780 |
| 529 | 0.008693 |
| **Toplam** | **0.049894** |

### Grup ve Random Kontrol Sonuçları

| Ölçüm | Değer |
|---|---:|
| Aday grup birlikte etkisi | **0.033458** |
| Tekil etkilerin basit toplamı | **0.049894** |
| Non-additive difference | **−0.016436** |
| Joint / individual-sum | **0.670583** |
| Random control ortalaması | **0.051979** |
| Random control standart sapması | **0.023452** |
| Candidate vs. random z-score | **−0.789750** |
| Candidate percentile | **%20** |

Random 5-boyutlu grup etkileri: `0.043100`, `0.066373`, `0.021147`, `0.046709`, `0.082566`.

### E10 Başarı Kriterleri

| Kriter | Sonuç | Değerlendirme |
|---|---:|---|
| (a) Candidate group random kontrollerden belirgin büyük (`z ≥ 2`) | `−0.789750` | **FAIL** |
| (b) Grup etkisi tekil etkilerin basit toplamından farklı | `−0.016436` | **PASS / SUPPORT** |
| Genel E10 değerlendirmesi |  | **PASS / SUPPORT** |

### E10 Verification Result

Aday 5'li grubun birlikte ablasyonu `0.033458` L1 çıktı değişimi oluşturmuştur. Random 5'li kontrol gruplarının ortalama etkisi `0.051979` olduğundan aday grup random kontrollerden daha güçlü değildir. Candidate'ın random dağılımdaki konumu `%20` percentile ve `z = −0.789750` olarak ölçülmüştür; dolayısıyla kriter (a) karşılanmamıştır.

Buna karşılık tekil aday boyutların etkilerinin basit toplamı `0.049894` iken birlikte grup etkisi `0.033458` olmuştur. `Joint / individual-sum = 0.670583` ve fark `−0.016436`, birlikte müdahalenin tekil etkilerin basit toplamına eşit olmadığını göstermektedir. Bu sonuç kriter (b) kapsamında **non-additive davranış desteği** olarak kaydedilmiştir.

### Statistical Significance

E10'daki random kontrol sayısı yalnızca `5` olduğu için `z = −0.789750` karşılaştırması sınırlı ve betimseldir; formal istatistiksel anlamlılık kanıtı olarak değerlendirilmemelidir. Kriter (b) ise grup etkisinin tekil etkiler toplamından farklı olduğunu gösterir, ancak bu fark tek başına istatistiksel anlamlılık anlamına gelmez.

### Unexpected Result

Aday grubun random kontrollerden daha güçlü olması beklenirken aday etki random kontrol ortalamasının altında kalmıştır. Buna rağmen birlikte etki tekil etkilerin toplamından daha düşük çıkmış ve belirgin non-additive davranış gözlenmiştir.

### Yorum

E10, aday grubun random kontrol gruplarına göre daha güçlü bir grup etkisi oluşturduğunu **desteklememektedir**. Buna karşılık aday grubun birlikte müdahalesi ile tekil etkilerin basit toplamı arasında belirgin bir fark vardır. Bu nedenle E10, **non-additive grup davranışı açısından PASS / SUPPORT** olarak değerlendirilmiştir; mekanizmanın kanıtlandığı veya istatistiksel anlamlılığın sağlandığı şeklinde yorumlanmamalıdır.

### E10 Grafik

`figures/week2/e10_group_effect_comparison.svg` — aday grubun birlikte etkisini, tekil etkilerin toplamını ve beş random 5-boyutlu kontrol grubunu karşılaştırır; random kontrol ortalaması da gösterilir.

### Sonraki Deney

**E11 — Sentetik True-vs-Spurious Feature Testi:** Bilinen gerçek kural ile spurious (sahte/yanıltıcı) korelasyonlu feature'ı ayıran kontrollü sentetik veri üzerinde Glass Box müdahale metodolojisinin doğrulanması.

---

## E11 — Sentetik True-vs-Spurious Feature Testi (Synthetic True-vs-Spurious Feature Test)

- **Deney ID:** E11
- **Tarih:** 21.08.2026
- **Amaç:** Bilinen gerçek kural ile spurious korelasyonlu feature'ın ayrıştırılabildiği kontrollü sentetik veri üzerinde modelin spurious feature'a bağımlılığını test etmek.
- **Hipotez:** Normal testte yüksek accuracy elde edilmeli; spurious feature rastgeleleştirildiğinde gerçek feature sabit kalmasına rağmen ölçülebilir accuracy düşüşü oluşmalıdır.
- **Model:** `Linear(2,16) → ReLU → Linear(16,8) → ReLU → Linear(8,2)`; toplam `202` parametre.
- **Dataset:** Sentetik ikili sınıflandırma; `N_TRAIN=5000`, `N_TEST=2000`, `SEED=42`.
- **Seed:** `42`.
- **Değiştirilen parametre:** Normal testte spurious feature korunurken, broken testte yalnızca spurious feature rastgele `0/1` değerleriyle değiştirildi.
- **Kontrol grubu:** Normal test; gerçek feature ve gerçek etiketler korunmuş durumda.
- **Müdahale grubu:** Spurious-broken test; yalnızca spurious feature rastgeleleştirildi.
- **Sonuç:** Train `%96.04`, normal test `%95.95`, spurious-broken `%80.40`; accuracy drop `15.55 pp`.
- **Accuracy / etki değişimi:** `%95.95 → %80.40`, yani `−15.55 pp`.
- **Hedef başarım kriteri:** Normal test accuracy `≥90%` ve spurious feature bozulduğunda performans değişiminin nicel olarak raporlanması.
- **Doğrulama sonucu:** **PASS / SUPPORT.** Normal test `%95.95` ile eşiği geçti ve kontrollü broken test `−15.55 pp` düşüş gösterdi.
- **İstatistiksel anlamlılık (z / persentil, varsa):** Hesaplanmadı; deney kontrollü sentetik müdahale karşılaştırmasıdır.
- **Grafik:** `figures/week2/e11_true_vs_spurious_accuracy.svg` — normal vs. spurious-broken accuracy.
- **Yorum:** Modelin normal koşullarda spurious feature'dan yararlandığını destekler; modelin tamamen spurious feature'a bağımlı olduğu söylenemez.
- **Beklenmeyen sonuç:** İlk gürültülü sentetik tasarımda model yaklaşık rastgele seviyede kaldı; temiz deterministik gerçek-feature tasarımıyla deney yeniden çalıştırıldı ve nihai sonuç bu tasarımdan raporlandı.
- **Commit hash:** Deney kaydında belirtilmemiştir.
- **Sonraki deney:** **E12 — Local LLM / Ollama.**

### Veri Doğrulama

- Gerçek feature → label doğruluğu: **%100.00**
- Train spurious correlation: **0.9524**
- Normal test spurious correlation: **0.9475**
- Spurious-broken test korelasyonu: **0.4965**

### Sonuçlar

| Ölçüm | Değer |
|---|---:|
| Train accuracy | **%96.04** |
| Normal test accuracy | **%95.95** |
| Spurious-broken accuracy | **%80.40** |
| Accuracy drop | **15.55 pp** |

### Başarı Kriterleri

| Kriter | Sonuç | Değerlendirme |
|---|---:|---|
| Normal test accuracy `≥ 90%` | `%95.95` | **PASS** |
| Spurious feature bozulduğunda performans değişiminin ölçülmesi | `−15.55 pp` | **PASS** |
| Genel E11 değerlendirmesi |  | **PASS / SUPPORT** |

### Verification Result

Model eğitim verisinde `%96.04`, normal testte `%95.95` doğruluk elde etti. Gerçek feature değiştirilmeden yalnızca spurious feature rastgeleleştirildiğinde test accuracy `%80.40`'a düştü. Böylece performans **15.55 yüzde puanı** azaldı. Müdahale, modelin spurious feature'dan yararlandığını destekleyen kontrollü bir davranış değişimi oluşturmuştur.

### Yorum

E11 sonucu, modelin yalnızca gerçek feature'a dayanmadığını; normal koşullarda spurious feature'dan da yararlandığını desteklemektedir. Ancak spurious feature'ın kırılmasından sonra doğruluk `%80.40` seviyesinde kaldığı için modelin tamamen spurious feature'a bağımlı olduğu söylenemez. Gerçek feature modelin tahmininde hâlâ anlamlı bir rol oynamaktadır.

Bu deneyin değeri, bilinen gerçek kural ve bilinen spurious korelasyon sayesinde müdahale sonucunun yorumlanabilir olmasıdır. Sonuç **spurious feature kullanımına dair deneysel destek** olarak kaydedilmiştir; tek başına genel nedensellik veya mekanizma çözümü iddiası değildir.

### Methodological Note

İlk sentetik veri üretim denemesinde gerçek feature'a eklenen gürültü nedeniyle model öğrenme davranışı yaklaşık rastgele seviyede kalmıştır. Bu tasarım sorunu gözlendikten sonra deney, bilinen gerçek kuralın deterministik olduğu ve spurious feature'ın kontrollü biçimde `%95` korelasyon taşıdığı temiz sentetik veri tasarımıyla yeniden çalıştırılmıştır. Sonuçlar temiz tasarım üzerinden raporlanmıştır; başarısız ilk tasarım metodolojik hata olarak korunmalı, nihai E11 sonucu ile karıştırılmamalıdır.

### E11 Grafik

`figures/week2/e11_true_vs_spurious_accuracy.svg` — normal test ile spurious-broken test accuracy değerlerini karşılaştırır.

---

## E12 — Local LLM / Ollama

- **Deney ID:** E12
- **Tarih:** Kaynak kaydında belirtilmemiş.
- **Amaç:** Küçük bir local LLM üzerinde farklı prompt türlerinin çalıştırılabildiğini göstermek ve modelin kendi açıklamalarının gerçek iç mekanizma kanıtı olarak değerlendirilmemesi gerektiğini belgelemek.
- **Hipotez:** Local LLM üç farklı prompt türünü çalıştırabilecek; ancak öz-açıklamalar gerçek mekanistik kanıt olarak kabul edilmemelidir.
- **Model:** `llama3.2:1b` via Ollama.
- **Dataset:** Prompt tabanlı test; `3` prompt.
- **Seed:** Kaynak kaydında belirtilmemiş.
- **Değiştirilen parametre:** Prompt türü: factual, reasoning, glass_box; internal intervention uygulanmadı.
- **Kontrol grubu:** Yok; davranışsal prompt karşılaştırması.
- **Müdahale grubu:** Yok; model iç aktivasyonuna müdahale edilmedi.
- **Sonuç:** Ollama kuruldu, `llama3.2:1b` indirildi ve 3 prompt başarıyla işlendi. Yanıt süreleri `26.55 s`, `80.12 s`, `105.01 s`.
- **Accuracy / etki değişimi:** Accuracy veya mekanistik etki ölçülmedi; yalnızca gözlenebilir yanıtlar ve çalışma süreleri kaydedildi.
- **Hedef başarım kriteri:** Local execution'ın başarıyla tamamlanması ve model öz-açıklamalarının mekanistik kanıt olarak yanlış yorumlanmaması.
- **Doğrulama sonucu:** **PASS (local execution) / mechanistic evidence: FALSE.** Üç prompt işlendi; gerçek iç mekanizma kanıtı elde edilmedi.
- **İstatistiksel anlamlılık (z / persentil, varsa):** Uygulanmadı.
- **Grafik:** Bu deney için kaynak kaydında ayrı grafik belirtilmemiştir.
- **Yorum:** Local LLM demonstration başarılıdır; modelin kendi iç süreç açıklamaları mekanistik kanıt değildir.
- **Beklenmeyen sonuç:** P3 glass_box yanıtında model, knowledge graph gibi gerçekte bu modelin mekanizmasını temsil etmeyen ifadeler de üretti; bu, öz-açıklamaların güvenilir mekanistik kanıt olmadığını daha da açık hale getirdi.
- **Commit hash:** Deney kaydında belirtilmemiştir.
- **Sonraki deney:** **Yok — Week 2 deneyleri E12 ile tamamlandı.**

### Ortam ve Çalıştırma

- Ollama başlangıçta kurulu değildi.
- `zstd` bağımlılığı kurulduktan sonra Ollama başarıyla kuruldu.
- Ollama server başarıyla başlatıldı.
- `llama3.2:1b` modeli başarıyla indirildi ve çalıştırıldı.

### Promptlar

#### P1 — factual

`What is a transformer model in artificial intelligence? Explain briefly.`

Model, Transformer mimarisini NLP görevlerinde kullanılan bir sinir ağı mimarisi olarak açıkladı. Yanıt süresi: **26.55 s**.

#### P2 — reasoning

`Why might a language model give different answers to two very similar questions?`

Model; eğitim verisi sınırlılıkları, bağlam, belirsizlik, dilsel varyasyonlar ve sorgu niyeti gibi çeşitli nedenler sundu. Yanıt süresi: **80.12 s**.

#### P3 — glass_box

`What kinds of internal information might a language model use when generating an answer?`

Model contextualized embeddings, tokenization, training data ve model parameters gibi çeşitli unsurlardan bahsetti. Yanıt süresi: **105.01 s**.

**Önemli metodolojik not:** P3'teki model öz-açıklaması gerçek iç mekanizmanın doğrudan kanıtı olarak kabul edilmemiştir. Modelin kendi üretmiş olduğu açıklamalar ile gerçek hesaplama mekanizması arasında ayrım yapılmalıdır.

### Glass Box Değerlendirmesi

- Local execution: **True**
- Prompt count: **3**
- Internal intervention: **False**
- Mechanistic evidence: **False**

### Sonuç

Local LLM başarıyla çalıştırılmış ve üç farklı prompt türüne cevap vermiştir. Çıktılar gözlenebilir davranış farklılıklarını göstermektedir; ancak cevapların kendisi modelin gerçek iç mekanizmalarına dair mekanistik kanıt oluşturmaz. Özellikle modelin kendi iç süreçleri hakkında verdiği açıklamalar mekanistik kanıt olarak kullanılmamalıdır.

**Genel E12 değerlendirmesi:** Local LLM demonstration **başarılı**; mekanistik/causal Glass Box kanıtı **elde edilmedi**.

---

## Week 1 vs Week 2 — Metodolojik Özet

- **Week 1 candidate/random separation:** **107.32×**; tek seed (`seed=42`).
- **Week 2 multi-seed candidate/random separation:** **79.77×**; `5` seed (`42, 0, 7, 123, 2024`) üzerinden ortalama etki büyüklükleri kullanılmıştır.
- Week 2'de tek seed yaklaşımından çoklu seed tekrarına, geniş random-control karşılaştırmalarına ve Discovery/Holdout ayrımına geçilmiştir.
- E07'de aday boyutların güçlü L1 ayrışması Holdout verisinde korunmuştur.
- E09'da aday `496` için daha geniş 50-control dağılımı kullanılmış ve önceden belirlenen istatistiksel ayrışma kriterleri karşılanmamıştır (`z=0.854322`, `%84` percentile).
- E10'da grup müdahalesinde non-additive davranış gözlenmiş, ancak aday grubun random gruplardan daha güçlü olduğu gösterilememiştir.
- E11'de kontrollü sentetik veri üzerinde spurious feature bozulmasının **15.55 pp** accuracy düşüşüne yol açtığı gösterilmiştir.
- E12'de küçük bir local LLM başarıyla çalıştırılmış, ancak modelin öz-açıklamaları mekanistik kanıt olarak kabul edilmemiştir.

### Week 1 → Week 2 Genel Yorum

Week 1'de aday özellik/devre etkisi için güçlü bir başlangıç gözlemi elde edilirken, Week 2 aynı araştırma çizgisini daha kontrollü ve doğrulanabilir hale getirmiştir. Özellikle çoklu seed, Discovery/Holdout ayrımı, random-control dağılımları ve sentetik bilinen-kural testi, gözlenen iç temsil etkilerinin yalnızca tek bir örneğe bağlı olmadığını sınamak için eklenmiştir. Bununla birlikte E09 gibi başarısız istatistiksel ayrışma sonuçları özellikle korunmuş ve sonuçlar yalnızca destekledikleri ölçüde yorumlanmıştır.

### Week 1 vs Week 2 Grafik

`figures/week2/week1_vs_week2_summary.svg` — candidate/random control separation oranını Week 1 ve Week 2 arasında karşılaştırır; Week 1 için `1 seed`, Week 2 için `5 seeds` kapsamı ayrıca gösterilir.

---

## Kaynak ve Tekrar Üretilebilirlik

- Ayrıntılı ham sayısal kayıt: `notes/experiment_log_week2.md`.
- Week 2 grafikler: `figures/week2/`.
- Bu dosya E06–E12 deneylerini hocanın standart deney kayıt şablonuyla tutar.
- Eksik tarih, seed, commit hash veya ölçüm uydurulmamıştır.
