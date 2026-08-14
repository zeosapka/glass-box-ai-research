# 1. Hafta Deney Günlüğü

Bu dosya, Colab üzerinde gerçekten çalıştırılmış Glass Box AI deneylerinin sonuçlarını kaydetmektedir. Deneyler küçük ve kontrollü bir MNIST MLP üzerinde yürütülmüştür.

## 1. Baseline Model

- Dataset: MNIST (60000 train / 10000 test)
- Architecture: `784 → 128 → 64 → 10`
- Activation: ReLU
- Optimizer: Adam
- Learning rate: `0.001`
- Batch size: `64`
- Epoch: `5`
- Seed: `42`
- Device: CPU
- Training time: `57.96 s`
- Test accuracy: **97.56%**

Epoch loss: `0.3328, 0.1354, 0.0945, 0.0717, 0.0558`.

Confusion matrix diagonal was strong. Correct predictions by class: `0=967, 1=1128, 2=1003, 3=978, 4=970, 5=866, 6=927, 7=1010, 8=946, 9=961`.

**Yorum:** Baseline model sonraki internal representation ve intervention deneyleri için yeterli performansı sağlamıştır.

## 2. Activation Analysis

ReLU2 activation output shape: `[64, 64]`; complete test activation matrix: `[10000, 64]`.

Öne çıkan ortalama aktivasyonlar: N62 `4.661`, N61 `2.601`, N54 `2.559`, N47 `2.540`. N4, N19, N35 ve N58 çok düşük/dead activation göstermiştir.

**Yorum:** Yüksek mean activation tek başına causal importance göstermez.

## 3. Class Activation ve Selectivity

Selectivity = en yüksek class mean activation − ikinci en yüksek class mean activation.

| Neuron | Top class | Selectivity |
|---:|---:|---:|
| N54 | 2 | 3.561 |
| N47 | 0 | 3.163 |
| N22 | 1 | 2.881 |
| N2 | 4 | 2.429 |
| N51 | 4 | 2.392 |
| N32 | 2 | 2.327 |
| N23 | 7 | 2.316 |
| N48 | 6 | 2.231 |
| N12 | 3 | 2.204 |
| N17 | 0 | 2.193 |

**Yorum:** Selectivity candidate neuron/feature seçimi için observational bir ölçüttür; causal importance değildir.

## 4. Single-Neuron Ablation

### N54
- Overall: `97.5600% → 97.5300%` (`-0.0300 pp`)
- Class 2: `97.1899% → 96.8023%` (`-0.3876 pp`)

### N47
- Overall: `97.5600% → 97.4600%` (`-0.1000 pp`)
- Class 0: `98.6735% → 97.7551%` (`-0.9184 pp`)

### N62
- Overall: `97.5600% → 97.6400%` (`+0.0800 pp`)
- Class 3: `96.8317% → 96.3366%` (`-0.4950 pp`)

**Yorum:** Ablation results provide causal evidence/support that selected neurons contribute to class-specific model behavior. N62 kesin bir negative control olarak değerlendirilmemiştir.

## 5. Activation Intervention

### N47 → Class 0

| Scale | Accuracy | Mean C0 probability | True C0 probability |
|---:|---:|---:|---:|
| 0.0 | 97.46% | 0.0956 | 0.9640 |
| 0.5 | 97.54% | 0.0968 | 0.9735 |
| 1.0 | 97.56% | 0.0977 | 0.9793 |
| 1.5 | 97.56% | 0.0984 | 0.9829 |
| 2.0 | 97.54% | 0.0990 | 0.9853 |

### N54 → Class 2

| Scale | Accuracy | Mean C2 probability | True C2 probability |
|---:|---:|---:|---:|
| 0.0 | 97.53% | 0.1026 | 0.9583 |
| 0.5 | 97.55% | 0.1034 | 0.9619 |
| 1.0 | 97.56% | 0.1041 | 0.9644 |
| 1.5 | 97.44% | 0.1048 | 0.9662 |
| 2.0 | 97.42% | 0.1056 | 0.9676 |

**Yorum:** Controlled activation intervention, ilgili neuron → output pathway için daha güçlü causal evidence sağlamıştır; sonuçlar causality proved şeklinde ifade edilmemiştir.

## 6. Correlation vs Causality

N17–N47 Pearson correlation:
- All test samples: **0.4485**
- Class 0 only: **0.7846**

**Yorum:** Correlation observational evidence sağlar. Causal claim için intervention ve ablation gereklidir.

## 7. Candidate Circuit Discovery

Class 0 için candidate group:

`[47, 17, 57, 53, 28]`

N47 → Class 0 output weight: `+0.231610`.
Diğer candidate Class 0 weights: N17 `+0.237246`, N28 `+0.233466`, N53 `+0.225550`, N57 `+0.186438`.

**Yorum:** Output weights candidate pathway belirlemede kullanılmıştır; weight magnitude tek başına causal evidence değildir.

## 8. N17 Activation Intervention

| Scale | Accuracy | Mean C0 probability | True C0 probability |
|---:|---:|---:|---:|
| 0.0 | 97.50% | 0.0954 | 0.9619 |
| 0.5 | 97.53% | 0.0967 | 0.9726 |
| 1.0 | 97.56% | 0.0977 | 0.9793 |
| 1.5 | 97.55% | 0.0984 | 0.9835 |
| 2.0 | 97.53% | 0.0991 | 0.9863 |

Scale `0→2` arasında true Class 0 probability `+0.0244` artmıştır.

**Yorum:** N17 activation artışı Class 0 probability'sini sistematik olarak artırmıştır; N17 → Class 0 pathway için causal evidence'i destekler.

## 9. N17 + N47 Combined Ablation

Overall accuracy: `97.5600% → 97.1900%`, değişim `-0.3700 pp`.

Single effects: N17 `-0.0600 pp`, N47 `-0.1000 pp`; basit toplam `-0.1600 pp`.

Class 0: N17 `-0.8163 pp`, N47 `-0.9184 pp`, combined `-2.7551 pp`; expected additive `-1.7347 pp`; non-additive fark `-1.0204 pp`.

**Yorum:** Non-additivity possible functional interaction veya shared representation düşündürmektedir; doğrudan interaction kanıtlanmış değildir.

## 10. Activation Patching

Class 0 source → Class 1 target tek örnek testinde N17, N47 ve N17+N47 patch'leri Class 0 probability'sini küçük miktarlarda artırmış, fakat prediction Class 1 olarak kalmıştır.

50 source/target pair testinde:

| Patch | Mean probability change | Std |
|---|---:|---:|
| N17 | +0.00000119 | 0.00000396 |
| N47 | +0.00000024 | 0.00000072 |
| N17+N47 | +0.00000247 | 0.00000731 |

**Yorum:** Tek nöronlar Class 0 behavior transferi için yeterli değildir; distributed representation hipotezini destekleyen bir gözlemdir.

## 11. Distributed Feature Patching

Top-5 candidate: `[47,17,57,53,28]`.

50 Class 0 source → 50 Class 1 target:

| Group | Mean C0 probability change | Std |
|---|---:|---:|
| Top-1 | +0.00000024 | 0.00000072 |
| Top-3 | +0.00001863 | 0.00006229 |
| Top-5 | +0.00546138 | 0.02484783 |

**Yorum:** Top-5 etkisinin artması distributed representation adayı oluşturur; yüksek std nedeniyle tek başına definitive circuit değildir.

## 12. Class-Specific Patching Control

Top-5 candidate group için:
- Class 1 target → Class 0 probability: `+0.00887395 ± 0.03161188`
- Class 2 target → Class 0 probability: `+0.00536434 ± 0.02391533`

**Yorum:** Candidate group Class 0-exclusive değildir. Class 0 logit'ine güçlü fakat context-dependent katkı sağlayan distributed candidate representation olarak değerlendirilmiştir.

## 13. Logit-Level Patching

Top-5 group ile Class 0 logit değişimi:
- Class 1 target: **+6.024506 ± 1.621096**
- Class 2 target: **+4.306821 ± 1.859204**

**Yorum:** Softmax saturation probability etkisini küçük gösterebilir. Logit seviyesinde candidate group'un Class 0 output'una güçlü etkisi görülmüştür; etki context-dependent'dır.

## 14. Candidate Group Weight / Contribution Analysis

Candidate group'un Class 0 output weights toplamı: **+1.114311**.

100 Class 0 örneğinde mean activation × Class 0 weight katkıları:

| Neuron | Mean activation | Weight | Mean contribution |
|---:|---:|---:|---:|
| N47 | 7.1442 | +0.231610 | +1.654675 |
| N17 | 5.1893 | +0.237246 | +1.231128 |
| N57 | 4.3655 | +0.186438 | +0.813899 |
| N53 | 5.7294 | +0.225550 | +1.292274 |
| N28 | 5.1635 | +0.233466 | +1.205509 |
| **Total** | | | **+6.197485** |

Bu değer decision'ın yüzdesi olarak yorumlanmamıştır; diğer 59 neuron ve bias da katkı vermektedir.

Candidate group Class 0 logit contribution:
- True Class 0: `+6.197485`
- True Class 1: `+0.736779`
- True Class 2: `+2.432718`

**Yorum:** Group Class 0-biased fakat Class 0-exclusive değildir.

## 15. Candidate Group Contribution to All Logits

True Class 0 örneklerinde candidate group katkıları:
`C0 +6.197485, C1 -2.253895, C2 +0.218861, C3 -3.120183, C4 -3.548902, C5 -1.585979, C6 +0.040571, C7 +0.004093, C8 -0.406147, C9 -0.499234`.

True Class 1 örneklerinde C0 katkısı `+0.736779`; True Class 2 örneklerinde `+2.432718`.

**Yorum:** Group Class 0'u güçlü biçimde desteklerken bazı competitor logits'i de bastırmaktadır; mekanizma tek output node ile sınırlı değildir.

## 16. Candidate Circuit Ablation

Candidate `[47,17,57,53,28]` birlikte ablate edildiğinde:

- Class 0 baseline: `98.6735%`
- Ablated: `86.6327%`
- Change: **-12.0408 pp**

**Yorum:** Candidate group'un Class 0 behavior'a güçlü distributed circuit-level katkısı vardır. Bu grup definitive complete circuit olarak ilan edilmemiştir.

## 17. Class-Specific Circuit Control

Candidate circuit ablation:
- Class 1: `99.3833% → 99.4714%`, `+0.0881 pp`
- Class 2: `97.1899% → 97.1899%`, `0.0000 pp`

**Yorum:** Class 0 etkisi diğer iki kontrol sınıfına göre belirgin biçimde daha büyüktür.

## 18. Leave-One-Out Analysis

Class 0 baseline: `98.6735%`.

| Removed neuron | Remaining group accuracy | Change |
|---:|---:|---:|
| N47 | 92.7551% | -5.9184 pp |
| N17 | 92.7551% | -5.9184 pp |
| N57 | 89.5918% | -9.0816 pp |
| N53 | 92.1429% | -6.5306 pp |
| N28 | 92.0408% | -6.6327 pp |

**Yorum:** N57 leave-one-out context'inde en güçlü etkiyi göstermiştir. Bu, single-neuron importance ile group-context importance'ın aynı sıralamayı vermediğini gösterir.

## 19. Single-Neuron Candidate Comparison

Class 0 baseline `98.6735%`:

| Neuron | Ablated accuracy | Change |
|---:|---:|---:|
| N47 | 97.7551% | -0.9184 pp |
| N17 | 97.8571% | -0.8164 pp |
| N57 | 98.4694% | -0.2041 pp |
| N53 | 98.1633% | -0.5102 pp |
| N28 | 98.0612% | -0.6123 pp |

**Yorum:** Single-neuron rank N47 > N17 > N28 > N53 > N57 iken leave-one-out rank farklıdır. Bu context-dependent/non-additive contribution ile uyumludur.

## 20. Progressive Circuit Ablation

| Group size | Group | Class 0 accuracy | Change |
|---:|---|---:|---:|
| 1 | [47] | 97.7551% | -0.9184 pp |
| 2 | [47,17] | 95.9184% | -2.7551 pp |
| 3 | [47,17,57] | 94.7959% | -3.8776 pp |
| 4 | [47,17,57,53] | 92.0408% | -6.6327 pp |
| 5 | [47,17,57,53,28] | 86.6327% | -12.0408 pp |

**Yorum:** Group büyüdükçe etki belirginleşmiştir. Sonuç distributed/non-additive behavior ile uyumludur; sıra-dependent olduğu için ara artışlar intrinsic neuron importance olarak yorumlanmamıştır.

## 21. Circuit Discovery Summary

Candidate circuit: `[47,17,57,53,28]`.

- Selectivity: Class 0-biased candidate identification
- Single ablation: N47 `-0.9184 pp`
- Circuit ablation: `-12.0408 pp`
- Class 1 control: `+0.0881 pp`
- Class 2 control: `0.0000 pp`
- Leave-One-Out: N57 `-9.0816 pp`
- Progressive ablation: `-0.9184 → -12.0408 pp`
- Activation patching: Class 0 logit `+6.0245` on Class 1 targets, `+4.3068` on Class 2 targets

**Yorum:** Bulgular, Class 0 behavior ile ilişkili distributed candidate circuit için güçlü mekanistik kanıt sağlamaktadır; complete circuit olduğu henüz kanıtlanmamıştır.

## 22. Mechanistic Validation — Random Control

Candidate group `[47,17,57,53,28]` ile 10 random control groups karşılaştırılmıştır.

- Candidate Class 0 change: **-12.0408 pp**
- Random groups mean change: **-0.1122 pp**
- Random minimum: `-0.9184 pp`
- Random maximum: `+0.2041 pp`
- Candidate − random mean: **-11.9286 pp**

**Yorum:** Candidate circuit etkisinin rastgele neuron seçiminin doğal varyasyonundan kaynaklanma ihtimalini azaltan güçlü control evidence elde edilmiştir.

## 23. Class-Wise Mechanistic Validation

Candidate circuit `[47,17,57,53,28]` ablation sonuçları:

| Class | Baseline | Ablated | Change |
|---:|---:|---:|---:|
| 0 | 98.6735% | 86.6327% | **-12.0408 pp** |
| 1 | 99.3833% | 99.4714% | +0.0881 pp |
| 2 | 97.1899% | 97.1899% | 0.0000 pp |
| 3 | 96.8317% | 97.8218% | +0.9901 pp |
| 4 | 98.7780% | 99.1853% | +0.4073 pp |
| 5 | 97.0852% | 96.6368% | -0.4484 pp |
| 6 | 96.7641% | 96.5553% | -0.2088 pp |
| 7 | 98.2490% | 98.0545% | -0.1946 pp |
| 8 | 97.1253% | 96.8172% | -0.3080 pp |
| 9 | 95.2428% | 93.7562% | -1.4866 pp |

**Yorum:** En büyük negatif etki Class 0'da görülmüştür. Group Class 0-biased'dır fakat Class 0-exclusive değildir.

## 24. Circuit-Level Activation Intervention

Candidate circuit `[47,17,57,53,28]` activation scale edilmiştir.

| Scale | Accuracy | Mean C0 probability | True C0 probability |
|---:|---:|---:|---:|
| 0.0 | 96.2700% | 0.075105 | 0.764420 |
| 0.5 | 97.3300% | 0.092623 | 0.938316 |
| 1.0 | 97.5600% | 0.097675 | 0.979257 |
| 1.5 | 97.5400% | 0.100468 | 0.990193 |
| 2.0 | 97.3300% | 0.103643 | 0.993814 |

**Yorum:** Circuit activation arttıkça true Class 0 probability sistematik biçimde yükselmiştir. Scale 0'da circuit baskılandığında probability `0.7644` seviyesine düşmüş, scale 2'de `0.9938` seviyesine çıkmıştır. Bu, circuit-level causal evidence'i güçlendirmektedir; causality proved denmemiştir.

## 25. Graphs / Figures

Toplam **11 anlamlı figure** oluşturulmuştur:

1. MNIST sample visualization
2. Confusion matrix
3. Class mean activation heatmap
4. N47 intervention vs Class 0 probability
5. N17/N47 activation correlation scatter
6. Candidate circuit intervention vs Class 0 probability
7. Training loss
8. Neuron/circuit ablation accuracy
9. Candidate neuron activation distribution
10. Candidate circuit activation across classes
11. Progressive circuit ablation

## 26. Literature Review

Sekiz kaynak incelenmiş ve deneylerle ilişkilendirilmiştir:

1. *Interpretability in the Wild: a Circuit for IOI in GPT-2 Small*
2. *Towards Automated Circuit Discovery for Mechanistic Interpretability*
3. *Locating and Editing Factual Associations in GPT*
4. *Toy Models of Superposition*
5. *Sparse Autoencoders Find Highly Interpretable Features in Language Models*
6. *Causal Abstraction: A Theoretical Foundation for Mechanistic Interpretability*
7. *Tracr: Compiled Transformers as a Laboratory for Interpretability*
8. *Gemma Scope*

Deney ↔ literatür mapping: Activation Analysis, Neuron Ablation, Activation Intervention, Correlation vs Causality, Activation Patching, Circuit Discovery, Distributed Representation, Mechanistic Validation, Feature-Level Analysis ve Circuit-Level Intervention.

## 27. Limitations

1. Tek küçük MNIST MLP ve tek training seed kullanıldı.
2. Candidate selection activation/selectivity ve weight analizlerine bağlıdır.
3. Progressive ablation sırası order-dependent'dır.
4. `[47,17,57,53,28]` complete circuit olarak kanıtlanmamıştır.
5. Run-to-run statistical uncertainty sınırlı ölçülmüştür.
6. Candidate group Class 0-biased fakat exclusive değildir.
7. Activation patching kapsamı sınırlı source-target örnekleriyle yürütülmüştür.

## 28. Next Experiments

1. Multi-seed replication
2. Synthetic true-vs-spurious dataset
3. Distributed feature analysis
4. Expanded activation patching
5. Fashion-MNIST üzerinde ikinci dataset validation

## Genel Bilimsel Değerlendirme

Bu haftanın deneyleri modelin yalnızca doğru çıktı üretip üretmediğini değil, çıktının internal representation üzerinden hangi candidate feature ve circuit mekanizmalarıyla ilişkili olduğunu incelemiştir. Observation → hypothesis → intervention → output change → control → mechanistic validation zinciri kurulmuştur.

En önemli sonuç, Class 0 behavior ile güçlü biçimde ilişkili candidate group `[47,17,57,53,28]` bulunmasıdır. Circuit ablation `-12.0408 pp`, random control mean `-0.1122 pp` ve circuit activation intervention true Class 0 probability'sinde `0.7644 → 0.9938` değişimi göstermiştir. Bu sonuçlar güçlü causal evidence/support sağlar; ancak complete mechanism veya universal causality iddiası için yeterli değildir.
