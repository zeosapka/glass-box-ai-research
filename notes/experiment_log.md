# 1. Hafta Deney Günlüğü

Bu dosya, Colab üzerinde gerçekten çalıştırılmış deneylerin sonuçlarını kaydetmek için kullanılmaktadır. Sonuçlar deneyler tamamlandıktan sonra eklenmiştir.

## 1. Baseline Model

**Amaç:** MNIST üzerinde küçük ve kontrollü bir MLP baseline model oluşturmak ve sonraki Glass Box deneyleri için referans performansı belirlemek.

- Dataset: MNIST
- Train/Test: 60000 / 10000
- Input: 784
- Architecture: `784 → 128 → 64 → 10`
- Aktivasyon: ReLU
- Optimizer: Adam
- Learning rate: `0.001`
- Batch size: `64`
- Epoch: `5`
- Seed: `42`
- Device: CPU
- Eğitim süresi: `57.96 s`
- Test accuracy: **97.56%**

Epoch loss değerleri:

| Epoch | Loss |
|---:|---:|
| 1 | 0.3328 |
| 2 | 0.1354 |
| 3 | 0.0945 |
| 4 | 0.0717 |
| 5 | 0.0558 |

Confusion matrix incelendiğinde diagonal üzerinde yüksek doğru sınıflandırma görülmüştür. Sınıf bazında doğru tahmin sayıları: 0=967, 1=1128, 2=1003, 3=978, 4=970, 5=866, 6=927, 7=1010, 8=946, 9=961.

**Yorum:** Baseline model sonraki internal representation ve intervention deneyleri için yeterli performansı sağlamıştır.

---

## 2. Activation Analysis

**Amaç:** Modelin internal representation yapısını gözlemlemek ve ReLU2 katmanındaki 64 nöronun aktivasyonlarını incelemek.

- `fc2` çıktısı: `[64, 64]`
- `relu2` çıktısı: `[64, 64]`
- Tüm test seti activation matrix: `[10000, 64]`

Bazı nöronların ortalama aktivasyonu yüksek, bazı nöronların ise çok düşük veya sıfıra yakın olduğu gözlenmiştir.

Öne çıkan ortalama aktivasyonlar:

| Nöron | Ortalama aktivasyon |
|---:|---:|
| N62 | 4.661 |
| N61 | 2.601 |
| N54 | 2.559 |
| N47 | 2.540 |

Dead veya düşük aktivasyon gösteren nöronlar arasında N4, N19, N35 ve N58 bulunmaktadır.

**Yorum:** Yüksek ortalama activation tek başına bir nöronun causal importance taşıdığını göstermez.

---

## 3. Class Activation ve Selectivity Analysis

**Amaç:** Hangi nöronların belirli sınıflarda daha seçici aktivasyon gösterdiğini belirlemek.

Selectivity, bir nöronun en yüksek class mean activation değeri ile ikinci en yüksek class mean activation değeri arasındaki fark olarak hesaplanmıştır.

En yüksek selectivity gösteren adaylar:

| Nöron | En yüksek class | Selectivity |
|---:|---:|---:|
| N54 | Class 2 | 3.561 |
| N47 | Class 0 | 3.163 |
| N22 | Class 1 | 2.881 |
| N2 | Class 4 | 2.429 |
| N51 | Class 4 | 2.392 |
| N32 | Class 2 | 2.327 |
| N23 | Class 7 | 2.316 |
| N48 | Class 6 | 2.231 |
| N12 | Class 3 | 2.204 |
| N17 | Class 0 | 2.193 |

**Yorum:** Selectivity candidate feature/neuron seçimi için gözlemsel bir ölçüttür. Selectivity yüksek olması causal importance anlamına gelmez.

---

## 4. Single-Neuron Ablation

**Amaç:** Selectivity sonucu öne çıkan nöronların model davranışına etkisini intervention ile test etmek.

### N54
- Overall baseline: 97.5600%
- Ablated: 97.5300%
- Değişim: **-0.0300 yüzde puanı**
- Class 2 baseline: 97.1899%
- Class 2 ablated: 96.8023%
- Class 2 değişim: **-0.3876 yüzde puanı**

### N47
- Overall baseline: 97.5600%
- Ablated: 97.4600%
- Değişim: **-0.1000 yüzde puanı**
- Class 0 baseline: 98.6735%
- Class 0 ablated: 97.7551%
- Class 0 değişim: **-0.9184 yüzde puanı**

### N62
- Overall baseline: 97.5600%
- Ablated: 97.6400%
- Değişim: **+0.0800 yüzde puanı**
- Class 3 baseline: 96.8317%
- Class 3 ablated: 96.3366%
- Class 3 değişim: **-0.4950 yüzde puanı**

**Yorum:** Ablation sonuçları, seçilen nöronların class-specific model behavior'a katkı sağlayabildiğine dair nedensel kanıt sunmaktadır. Farklı etkiler, activation selectivity'nin tek başına causal importance belirlemek için yeterli olmadığını göstermektedir. N62 kesin bir negative control olarak değerlendirilmemiştir.

---

## 5. Activation Intervention

**Amaç:** Nöron activation değerini kontrollü biçimde azaltıp artırarak output üzerindeki değişimi incelemek.

### N47 → Class 0

| Scale | Overall accuracy | Mean Class 0 probability | True Class 0 probability |
|---:|---:|---:|---:|
| 0.0 | 97.46% | 0.0956 | 0.9640 |
| 0.5 | 97.54% | 0.0968 | 0.9735 |
| 1.0 | 97.56% | 0.0977 | 0.9793 |
| 1.5 | 97.56% | 0.0984 | 0.9829 |
| 2.0 | 97.54% | 0.0990 | 0.9853 |

Activation arttıkça Class 0 probability sistematik olarak artmıştır. Overall accuracy büyük ölçüde sabit kalmıştır.

### N54 → Class 2

| Scale | Overall accuracy | Mean Class 2 probability | True Class 2 probability |
|---:|---:|---:|---:|
| 0.0 | 97.53% | 0.1026 | 0.9583 |
| 0.5 | 97.55% | 0.1034 | 0.9619 |
| 1.0 | 97.56% | 0.1041 | 0.9644 |
| 1.5 | 97.44% | 0.1048 | 0.9662 |
| 2.0 | 97.42% | 0.1056 | 0.9676 |

**Yorum:** Kontrollü activation intervention, ilgili nöronların hedef class output'una katkı sağladığına yönelik daha güçlü causal evidence oluşturmuştur. Bu sonuçlar doğrudan "causality proved" şeklinde yorumlanmamıştır.

---

## 6. Correlation vs Causality

N17 ve N47 activation değerleri arasındaki Pearson correlation:

- Tüm test seti: **0.4485**
- Sadece Class 0: **0.7846**

Class 0 örneklerinde N17 ve N47 activation değerleri arasında belirgin pozitif ilişki gözlenmiştir.

**Yorum:** Bu sonuç observational evidence sağlar. Correlation tek başına causality göstermez; intervention deneyleri bu nedenle ayrıca gerçekleştirilmiştir.

---

## 7. Candidate Circuit Discovery

**Amaç:** Class 0 davranışına birlikte katkı sağlayabilecek distributed feature/circuit adayını belirlemek.

Class 0 için öne çıkan candidate neurons:

`[47, 17, 57, 53, 28]`

Bu nöronlar selectivity, activation intervention ve output weight analizleri kullanılarak aday grup olarak belirlenmiştir.

N47'nin FC3 üzerindeki Class 0 output weight değeri:

- N47 → Class 0: **+0.231610**

Class 0 için en yüksek pozitif output weight değerlerinden bazıları:

- N17: +0.237246
- N28: +0.233466
- N47: +0.231610
- N53: +0.225550
- N57: +0.186438

**Yorum:** Weight değerleri candidate pathway belirlemek için kullanılmıştır; weight magnitude tek başına causal evidence değildir.

---

## 8. Activation Intervention: N17

N17 activation intervention sonuçları:

| Scale | Accuracy | Mean Class 0 probability | True Class 0 probability |
|---:|---:|---:|---:|
| 0.0 | 97.50% | 0.0954 | 0.9619 |
| 0.5 | 97.53% | 0.0967 | 0.9726 |
| 1.0 | 97.56% | 0.0977 | 0.9793 |
| 1.5 | 97.55% | 0.0984 | 0.9835 |
| 2.0 | 97.53% | 0.0991 | 0.9863 |

Scale 0→2 arasında true Class 0 probability **+0.0244** artmıştır.

**Yorum:** N17 activation'ının artırılması Class 0 probability'sini sistematik olarak artırmıştır. Bu, N17 → Class 0 output pathway için causal evidence'i desteklemektedir.

---

## 9. N17 + N47 Combined Ablation

- Baseline overall accuracy: **97.5600%**
- N17 + N47 ablation: **97.1900%**
- Değişim: **-0.3700 yüzde puanı**

Tekli ablation değişimleri:

- N17: -0.0600 pp
- N47: -0.1000 pp
- Basit toplam: -0.1600 pp
- Combined: -0.3700 pp

**Yorum:** Combined ablation etkisinin tekli etkilerin basit toplamından daha büyük olması non-additive behavior olabileceğini düşündürmektedir. Bu sonuç doğrudan interaction'ın kanıtlandığı şeklinde yorumlanmamıştır.

Class 0 özelinde:

- N17 ablation: -0.8163 pp
- N47 ablation: -0.9184 pp
- N17 + N47: -2.7551 pp
- Beklenen basit toplam: -1.7347 pp
- Non-additive fark: **-1.0204 pp**

**Yorum:** Sonuçlar N17 ve N47'nin Class 0 behavior içerisinde functional interaction veya shared representation gösterebileceğini desteklemektedir.

---

## 10. Activation Patching

### Tek örnek

Class 0 source → Class 1 target:

- Normal Class 0 probability: 0.000002
- N17 patch: 0.000010, değişim +0.000008
- N47 patch: 0.000003, değişim +0.000001
- N17 + N47 patch: 0.000018, değişim +0.000016

Prediction Class 1 olarak kalmıştır.

### Multi-sample

50 Class 0 source / 50 Class 1 target pair:

| Patch | Mean probability change | Std |
|---|---:|---:|
| N17 | +0.00000119 | 0.00000396 |
| N47 | +0.00000024 | 0.00000072 |
| N17 + N47 | +0.00000247 | 0.00000731 |

**Yorum:** Tek nöronların Class 0 behavior'ını tek başına transfer etmek için yeterli olmadığı görülmüştür. Bu sonuç distributed representation hipotezini destekleyen gözlemlerden biridir.

---

## 11. Distributed Feature Patching

Class 0 selectivity temelinde seçilen Top-5 grup:

`[47, 17, 57, 53, 28]`

50 Class 0 source → 50 Class 1 target pair:

| Grup | Mean Class 0 probability change | Std |
|---|---:|---:|
| Top-1 (N47) | +0.00000024 | 0.00000072 |
| Top-3 (N47,N17,N57) | +0.00001863 | 0.00006229 |
| Top-5 | +0.00546138 | 0.02484783 |

**Yorum:** Top-5 grubunda patch etkisinin belirgin biçimde artması, Class 0 signal'ının distributed bir representation üzerinden taşınabileceğini düşündürmektedir. Yüksek standart sapma nedeniyle sonuç tek başına kesin bir circuit tanımlamamaktadır.

---

## 12. Class-Specific Patching Control

Top-5 candidate group:

`[47,17,57,53,28]`

30 Class 0 source ile 30 Class 1 ve 30 Class 2 target üzerinde test edilmiştir.

- Class 1 target → Class 0 probability değişimi: **+0.00887395 ± 0.03161188**
- Class 2 target → Class 0 probability değişimi: **+0.00536434 ± 0.02391533**

**Yorum:** Candidate group yalnızca Class 0 örneklerinde etkili değildir. Class 1 ve Class 2 target'larda da Class 0 probability artışı oluşturmuştur. Bu nedenle grup Class 0-exclusive circuit olarak tanımlanmamıştır; daha doğru yorum, Class 0 logit'ine güçlü fakat context-dependent katkı sağlayan distributed candidate representation olduğudur.

---

## 13. Logit-Level Patching

Top-5 candidate group ile Class 0 logit değişimi:

- Class 1 target: **+6.024506 ± 1.621096**
- Class 2 target: **+4.306821 ± 1.859204**

**Yorum:** Probability değerlerindeki küçük değişimler softmax saturation nedeniyle mekanizmanın gerçek etkisini olduğundan küçük gösterebilir. Logit seviyesinde candidate group'un Class 0 output'una güçlü bir etkisi gözlenmiştir. Ancak etki Class 0-exclusive değildir.

---

## 14. Candidate Group Output Contribution

Candidate neurons:

`[47,17,57,53,28]`

Class 0 logit için activation × output weight katkıları, 100 Class 0 örneği üzerinde:

| Nöron | Ortalama activation | Class 0 weight | Ortalama katkı |
|---:|---:|---:|---:|
| N47 | 7.1442 | +0.231610 | +1.654675 |
| N17 | 5.1893 | +0.237246 | +1.231128 |
| N57 | 4.3655 | +0.186438 | +0.813899 |
| N53 | 5.7294 | +0.225550 | +1.292274 |
| N28 | 5.1635 | +0.233466 | +1.205509 |
| **Toplam** | | | **+6.197485** |

**Yorum:** Candidate group Class 0 logit'ine önemli miktarda pozitif computational contribution sağlamaktadır. Bu değer model kararının yüzdesi olarak yorumlanmamıştır; diğer 59 nöron ve bias da output logit'ine katkıda bulunmaktadır.

---

## 15. Candidate Group Class Comparison

Candidate group'un Class 0 logit contribution toplamı:

| Gerçek sınıf | Candidate group → Class 0 logit katkısı |
|---|---:|
| Class 0 | **+6.197485** |
| Class 1 | +0.736779 |
| Class 2 | +2.432718 |

Class 0 / Class 1 katkı oranı yaklaşık **8.4×** olmuştur.

**Yorum:** Candidate group Class 0'a güçlü biçimde biased bir contribution göstermektedir; ancak Class 0-exclusive değildir. Class 2'de de belirgin katkı görülmüştür.

---

## 16. Candidate Group Contribution to All Output Logits

100 örnek üzerinden candidate group'un activation × weight contribution toplamları:

### True Class 0

| Output class | Katkı |
|---:|---:|
| 0 | +6.197485 |
| 1 | -2.253895 |
| 2 | +0.218861 |
| 3 | -3.120183 |
| 4 | -3.548902 |
| 5 | -1.585979 |
| 6 | +0.040571 |
| 7 | +0.004093 |
| 8 | -0.406147 |
| 9 | -0.499234 |

True Class 0 örneklerinde candidate group en güçlü pozitif katkıyı Class 0 logit'ine sağlamış ve bazı rakip class logit'lerini negatif yönde etkilemiştir.

### True Class 1

| Output class | Katkı |
|---:|---:|
| 0 | +0.736779 |
| 1 | +0.047394 |
| 2 | +0.186111 |
| 3 | -0.569736 |
| 4 | -0.423243 |
| 5 | -0.438194 |
| 6 | +0.187347 |
| 7 | -0.031152 |
| 8 | -0.157257 |
| 9 | -0.241223 |

### True Class 2

| Output class | Katkı |
|---:|---:|
| 0 | +2.432718 |
| 1 | -0.592691 |
| 2 | +1.046666 |
| 3 | -1.604063 |
| 4 | -1.731053 |
| 5 | -0.610796 |
| 6 | +0.175417 |
| 7 | +0.284477 |
| 8 | -0.078404 |
| 9 | -0.979717 |

**Yorum:** Candidate group'un davranışı class ve context'e bağlıdır. True Class 0 örneklerinde Class 0 logit'ine güçlü pozitif katkı verirken bazı rakip logits üzerinde negatif katkı göstermektedir.

---

## 17. Candidate Circuit Ablation

Candidate circuit:

`[47,17,57,53,28]`

Class 0 üzerinde beş nöronun birlikte ablation edilmesi:

- Baseline Class 0 accuracy: **98.6735%**
- Ablated Class 0 accuracy: **86.6327%**
- Değişim: **-12.0408 yüzde puanı**

### Class-specific control

| Sınıf | Baseline | Ablated | Değişim |
|---:|---:|---:|---:|
| Class 0 | 98.6735% | 86.6327% | **-12.0408 pp** |
| Class 1 | 99.3833% | 99.4714% | **+0.0881 pp** |
| Class 2 | 97.1899% | 97.1899% | **0.0000 pp** |

**Yorum:** Candidate circuit ablation Class 0 davranışında güçlü bir düşüş oluştururken Class 1 ve Class 2 üzerindeki etkiler minimal kalmıştır. Bu sonuç candidate circuit'in Class 0 behavior'a güçlü katkı sağladığına yönelik nedensel kanıtı desteklemektedir.

---

## 18. Leave-One-Out Ablation

Baseline Class 0 accuracy: **98.6735%**

Candidate circuit'ten tek bir nöron çıkarılarak kalan dört nöronun birlikte ablation edildiği test:

| Çıkarılan nöron | Kalan grup ile Class 0 accuracy | Değişim |
|---:|---:|---:|
| N47 | 92.7551% | -5.9184 pp |
| N17 | 92.7551% | -5.9184 pp |
| N57 | 89.5918% | **-9.0816 pp** |
| N53 | 92.1429% | -6.5306 pp |
| N28 | 92.0408% | -6.6327 pp |

**Yorum:** N57, diğer dört nöron zaten ablation edilmişken en büyük ek etkiyi göstermiştir. Bu sonuç N57'nin tek başına en önemli nöron olduğu anlamına gelmez; contribution'ın circuit context'ine bağlı olduğunu göstermektedir.

---

## 19. Single-Neuron Ablation: Candidate Circuit Comparison

Class 0 baseline: **98.6735%**

| Nöron | Single-neuron ablation değişimi |
|---:|---:|
| N47 | -0.9184 pp |
| N17 | -0.8164 pp |
| N57 | -0.2041 pp |
| N53 | -0.5102 pp |
| N28 | -0.6123 pp |

Leave-One-Out ile Single-Neuron Ablation arasındaki fark:

| Nöron | Single | Leave-One-Out | Context difference |
|---:|---:|---:|---:|
| N47 | -0.9184 | -5.9184 | -5.0000 pp |
| N17 | -0.8164 | -5.9184 | -5.1020 pp |
| N57 | -0.2041 | -9.0816 | -8.8775 pp |
| N53 | -0.5102 | -6.5306 | -6.0204 pp |
| N28 | -0.6123 | -6.6327 | -6.0204 pp |

**Yorum:** Single-neuron ve Leave-One-Out sonuçları arasındaki büyük farklar, candidate circuit içerisindeki contribution'ın context-dependent ve non-additive olduğunu desteklemektedir.

---

## 20. Progressive Circuit Ablation

Candidate order:

`[47,17,57,53,28]`

| Ablation edilen nöron sayısı | Grup | Class 0 accuracy | Değişim |
|---:|---|---:|---:|
| 1 | [47] | 97.7551% | -0.9184 pp |
| 2 | [47,17] | 95.9184% | -2.7551 pp |
| 3 | [47,17,57] | 94.7959% | -3.8776 pp |
| 4 | [47,17,57,53] | 92.0408% | -6.6327 pp |
| 5 | [47,17,57,53,28] | 86.6327% | **-12.0408 pp** |

**Yorum:** Candidate group genişledikçe Class 0 accuracy'deki düşüş artmıştır. Bu sonuç distributed ve non-additive bir circuit davranışı ile uyumludur. Ancak progressive ablation sırası belirli bir order'a bağlı olduğu için artışlar doğrudan intrinsic neuron importance olarak yorumlanmamıştır.

---

## 21. Circuit Discovery Summary

| Deney | Hedef | Sonuç | Yorum |
|---|---|---|---|
| Selectivity | Class 0 | N47,N17,N57,N53,N28 seçildi | Candidate feature group |
| Single-Neuron Ablation | Class 0 | N47: -0.9184 pp | Individual contribution |
| Circuit Ablation | Class 0 | -12.0408 pp | Strong distributed circuit effect |
| Class-Specific Control | Class 1 | +0.0881 pp | Minimal effect |
| Class-Specific Control | Class 2 | 0.0000 pp | No measurable effect |
| Leave-One-Out | Class 0 | N57: -9.0816 pp | Context-dependent contribution |
| Progressive Ablation | Class 0 | -0.9184 → -12.0408 pp | Distributed/non-additive effect |
| Activation Patching | Class 0 logit | Class 1 target: +6.0245 | Candidate group increases Class 0 logit |
| Activation Patching | Class 0 logit | Class 2 target: +4.3068 | Context-dependent effect |
| Random Control | Class 0 | Control: 0.0000 pp | Candidate effect is not reproduced by random group |

---

## 22. Mechanistic Validation: Random Control

**Amaç:** Candidate circuit etkisinin rastgele seçilmiş nöronlardan kaynaklanmadığını kontrol etmek.

Candidate circuit:

`[47,17,57,53,28]`

Random control group:

`[42,7,1,50,18]`

Sonuçlar:

| Grup | Class 0 accuracy | Değişim |
|---|---:|---:|
| Baseline | 98.6735% | — |
| Candidate circuit ablation | 86.6327% | **-12.0408 pp** |
| Random control ablation | 98.6735% | **0.0000 pp** |

Candidate circuit ile random control arasındaki fark:

**-12.0408 yüzde puanı**

**Yorum:** Random control grubunda Class 0 accuracy değişmezken candidate circuit ablation güçlü bir düşüş oluşturmuştur. Bu sonuç, candidate circuit'in Class 0 behavior'a katkısının rastgele nöron seçimine bağlı olmadığını ve belirlenen grubun ilgili mekanizmaya katkı sağladığını destekleyen güçlü nedensel kanıt sunmaktadır.

Bu sonuç, candidate circuit'in modeldeki tek veya tamamlanmış Class 0 mechanism olduğunu kanıtlamaz.

---

## Genel Bilimsel Değerlendirme

Bu deney serisinde temel metodolojik zincir şu şekilde ilerlemiştir:

**Internal Representation → Observation → Feature/Selectivity Analysis → Candidate Neurons → Intervention → Ablation/Patching → Output Change → Repeated Tests → Causal Evidence → Candidate Circuit → Mechanistic Validation**

Ana bulgu, Class 0 davranışına katkı sağlayan `[47,17,57,53,28]` nöron grubunun farklı intervention yöntemlerinde tutarlı biçimde etkili olduğunun gözlenmesidir. Özellikle candidate circuit ablation sonucundaki **-12.0408 yüzde puanlık** Class 0 accuracy düşüşü ve random control grubunda **0.0000 yüzde puanlık** değişim, candidate mechanism için güçlü destek sağlamaktadır.

Bununla birlikte sonuçlar, modeldeki tüm Class 0 computation'ının yalnızca bu beş nörondan oluştuğunu göstermemektedir. Bulgular **candidate circuit / candidate mechanism** olarak raporlanmalıdır.

## Bilimsel Terminoloji Notu

- Correlation ≠ causality.
- Ablation ve intervention sonuçları "causal evidence/support" olarak ifade edilmelidir.
- Weight magnitude tek başına causal importance değildir.
- Activation × weight, computational contribution ölçümü olarak değerlendirilmelidir; tek başına causal importance değildir.
- Candidate circuit, kesin olarak complete circuit olarak adlandırılmamalıdır.
- Class-specific control ve random control sonuçları mechanistic validation açısından destekleyici kontrollerdir.
