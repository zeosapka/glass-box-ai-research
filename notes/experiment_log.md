# 1. Hafta Deney Günlüğü

Bu dosya, Colab üzerinde gerçekten çalıştırılmış Glass Box AI deneylerinin sonuçlarını kaydetmektedir. Deneyler küçük ve kontrollü bir MNIST MLP üzerinde yürütülmüştür.

## 1. Temel Model (Baseline Model)

- Veri seti (dataset): MNIST (`60000` eğitim / `10000` test)
- Mimari (architecture): `784 → 128 → 64 → 10`
- Aktivasyon (activation): ReLU
- Optimizasyon algoritması (optimizer): Adam
- Öğrenme oranı (learning rate): `0.001`
- Batch size: `64`
- Epoch: `5`
- Seed: `42`
- Cihaz (device): CPU
- Eğitim süresi (training time): `57.96 s`
- Test doğruluğu (test accuracy): **97.56%**

Epoch kaybı: `0.3328, 0.1354, 0.0945, 0.0717, 0.0558`.

Karmaşıklık matrisinin (confusion matrix) köşegeni güçlüydü. Sınıfa göre doğru tahminler: `0=967, 1=1128, 2=1003, 3=978, 4=970, 5=866, 6=927, 7=1010, 8=946, 9=961`.

**Yorum:** Temel model sonraki iç temsil (internal representation) ve müdahale (intervention) deneyleri için yeterli performansı sağlamıştır.

## 2. Aktivasyon Analizi (Activation Analysis)

ReLU2 aktivasyon çıktı şekli: `[64, 64]`; tam test aktivasyon matrisi: `[10000, 64]`.

Öne çıkan ortalama aktivasyonlar: N62 `4.661`, N61 `2.601`, N54 `2.559`, N47 `2.540`. N4, N19, N35 ve N58 çok düşük/ölü (dead) aktivasyon göstermiştir.

**Yorum:** Yüksek ortalama aktivasyon tek başına nedensel önem (causal importance) göstermez.

## 3. Sınıf Aktivasyonu ve Seçicilik (Class Activation / Selectivity)

Seçicilik = en yüksek sınıf ortalama aktivasyonu − ikinci en yüksek sınıf ortalama aktivasyonu.

| Nöron | En yüksek sınıf | Seçicilik |
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

**Yorum:** Seçicilik, aday nöron/özellik seçimi için gözlemsel (observational) bir ölçüttür; nedensel önem değildir.

## 4. Tek Nöron Ablasyonu (Single-Neuron Ablation)

### N54
- Genel: `97.5600% → 97.5300%` (`-0.0300 pp`)
- Sınıf 2: `97.1899% → 96.8023%` (`-0.3876 pp`)

### N47
- Genel: `97.5600% → 97.4600%` (`-0.1000 pp`)
- Sınıf 0: `98.6735% → 97.7551%` (`-0.9184 pp`)

### N62
- Genel: `97.5600% → 97.6400%` (`+0.0800 pp`)
- Sınıf 3: `96.8317% → 96.3366%` (`-0.4950 pp`)

**Yorum:** Ablasyon sonuçları seçilen nöronların sınıfa özgü model davranışına katkı verdiğine dair nedensel kanıtı (causal evidence/support) destekler. N62 kesin bir negatif kontrol (negative control) olarak değerlendirilmemiştir.

## 5. Aktivasyon Müdahalesi (Activation Intervention)

### N47 → Sınıf 0

| Ölçek | Doğruluk | Ortalama Sınıf 0 olasılığı | Gerçek Sınıf 0 olasılığı |
|---:|---:|---:|---:|
| 0.0 | 97.46% | 0.0956 | 0.9640 |
| 0.5 | 97.54% | 0.0968 | 0.9735 |
| 1.0 | 97.56% | 0.0977 | 0.9793 |
| 1.5 | 97.56% | 0.0984 | 0.9829 |
| 2.0 | 97.54% | 0.0990 | 0.9853 |

### N54 → Sınıf 2

| Ölçek | Doğruluk | Ortalama Sınıf 2 olasılığı | Gerçek Sınıf 2 olasılığı |
|---:|---:|---:|---:|
| 0.0 | 97.53% | 0.1026 | 0.9583 |
| 0.5 | 97.55% | 0.1034 | 0.9619 |
| 1.0 | 97.56% | 0.1041 | 0.9644 |
| 1.5 | 97.44% | 0.1048 | 0.9662 |
| 2.0 | 97.42% | 0.1056 | 0.9676 |

**Yorum:** Kontrollü aktivasyon müdahalesi, ilgili nöron → çıktı yoluna daha güçlü nedensel kanıt sağlamıştır; sonuçlar “nedensellik kanıtlandı” şeklinde ifade edilmemiştir.

## 6. Korelasyon ve Nedensellik (Correlation vs Causality)

N17–N47 Pearson korelasyonu:
- Tüm test örnekleri: **0.4485**
- Yalnızca Sınıf 0: **0.7846**

**Yorum:** Korelasyon gözlemsel kanıt sağlar. Nedensel iddia için müdahale ve ablasyon gereklidir.

## 7. Aday Devre Keşfi (Candidate Circuit Discovery)

Sınıf 0 için aday grup:

`[47, 17, 57, 53, 28]`

N47 → Sınıf 0 çıktı ağırlığı: `+0.231610`.
Diğer aday Sınıf 0 ağırlıkları: N17 `+0.237246`, N28 `+0.233466`, N53 `+0.225550`, N57 `+0.186438`.

**Yorum:** Çıktı ağırlıkları aday yolu belirlemede kullanılmıştır; ağırlık büyüklüğü tek başına nedensel kanıt değildir.

## 8. N17 Aktivasyon Müdahalesi

| Ölçek | Doğruluk | Ortalama Sınıf 0 olasılığı | Gerçek Sınıf 0 olasılığı |
|---:|---:|---:|---:|
| 0.0 | 97.50% | 0.0954 | 0.9619 |
| 0.5 | 97.53% | 0.0967 | 0.9726 |
| 1.0 | 97.56% | 0.0977 | 0.9793 |
| 1.5 | 97.55% | 0.0984 | 0.9835 |
| 2.0 | 97.53% | 0.0991 | 0.9863 |

Ölçek `0→2` arasında gerçek Sınıf 0 olasılığı `+0.0244` artmıştır.

**Yorum:** N17 aktivasyon artışı Sınıf 0 olasılığını sistematik olarak artırmıştır; N17 → Sınıf 0 yolu için nedensel kanıtı destekler.

## 9. N17 + N47 Birleşik Ablasyonu

Genel doğruluk: `97.5600% → 97.1900%`, değişim `-0.3700 pp`.

Tekil etkiler: N17 `-0.0600 pp`, N47 `-0.1000 pp`; basit toplam `-0.1600 pp`.

Sınıf 0: N17 `-0.8163 pp`, N47 `-0.9184 pp`, birleşik `-2.7551 pp`; toplamsal beklenti `-1.7347 pp`; toplamsal olmayan fark `-1.0204 pp`.

**Yorum:** Toplamsal olmama, olası işlevsel etkileşim (functional interaction) veya paylaşılan temsil (shared representation) düşündürmektedir; doğrudan etkileşim kanıtlanmış değildir.

## 10. Aktivasyon Yamalama (Activation Patching)

Sınıf 0 kaynak → Sınıf 1 hedef tek örnek testinde N17, N47 ve N17+N47 yamaları Sınıf 0 olasılığını küçük miktarlarda artırmış, fakat tahmin Sınıf 1 olarak kalmıştır.

50 kaynak/hedef çifti testinde:

| Yamalama | Ortalama olasılık değişimi | Standart sapma |
|---|---:|---:|
| N17 | +0.00000119 | 0.00000396 |
| N47 | +0.00000024 | 0.00000072 |
| N17+N47 | +0.00000247 | 0.00000731 |

**Yorum:** Tek nöronlar Sınıf 0 davranış aktarımı için yeterli değildir; dağıtık temsil hipotezini destekleyen bir gözlemdir.

## 11. Dağıtık Özellik Yamalama (Distributed Feature Patching)

Top-5 aday: `[47,17,57,53,28]`.

50 Sınıf 0 kaynak → 50 Sınıf 1 hedef:

| Grup | Ortalama Sınıf 0 olasılık değişimi | Standart sapma |
|---|---:|---:|
| Top-1 | +0.00000024 | 0.00000072 |
| Top-3 | +0.00001863 | 0.00006229 |
| Top-5 | +0.00546138 | 0.02484783 |

**Yorum:** Top-5 etkisinin artması dağıtık temsil adayı oluşturur; yüksek standart sapma nedeniyle tek başına kesin devre değildir.

## 12. Sınıfa Özgü Yamalama Kontrolü (Class-Specific Patching Control)

Top-5 aday grubu için:
- Sınıf 1 hedefi → Sınıf 0 olasılığı: `+0.00887395 ± 0.03161188`
- Sınıf 2 hedefi → Sınıf 0 olasılığı: `+0.00536434 ± 0.02391533`

**Yorum:** Aday grup Sınıf 0'a özel değildir. Sınıf 0 logitine güçlü fakat bağlama bağlı katkı sağlayan dağıtık aday temsil olarak değerlendirilmiştir.

## 13. Logit Düzeyinde Yamalama (Logit-Level Patching)

Top-5 grup ile Sınıf 0 logit değişimi:
- Sınıf 1 hedefi: **+6.024506 ± 1.621096**
- Sınıf 2 hedefi: **+4.306821 ± 1.859204**

**Yorum:** Softmax doygunluğu olasılık etkisini küçük gösterebilir. Logit düzeyinde aday grubun Sınıf 0 çıktısına güçlü etkisi görülmüştür; etki bağlama bağlıdır.

## 14. Aday Grup Ağırlık / Katkı Analizi

Aday grubun Sınıf 0 çıktı ağırlıkları toplamı: **+1.114311**.

100 Sınıf 0 örneğinde ortalama aktivasyon × Sınıf 0 ağırlığı katkıları:

| Nöron | Ortalama aktivasyon | Ağırlık | Ortalama katkı |
|---:|---:|---:|---:|
| N47 | 7.1442 | +0.231610 | +1.654675 |
| N17 | 5.1893 | +0.237246 | +1.231128 |
| N57 | 4.3655 | +0.186438 | +0.813899 |
| N53 | 5.7294 | +0.225550 | +1.292274 |
| N28 | 5.1635 | +0.233466 | +1.205509 |
| **Toplam** | | | **+6.197485** |

Bu değer kararın yüzdesi olarak yorumlanmamıştır; diğer 59 nöron ve bias da katkı vermektedir.

Aday grubun Sınıf 0 logit katkısı:
- Gerçek Sınıf 0: `+6.197485`
- Gerçek Sınıf 1: `+0.736779`
- Gerçek Sınıf 2: `+2.432718`

**Yorum:** Grup Sınıf 0'a eğilimli fakat yalnızca Sınıf 0'a özgü değildir.

## 15. Aday Grubun Tüm Logitlere Katkısı

Gerçek Sınıf 0 örneklerinde aday grup katkıları:
`C0 +6.197485, C1 -2.253895, C2 +0.218861, C3 -3.120183, C4 -3.548902, C5 -1.585979, C6 +0.040571, C7 +0.004093, C8 -0.406147, C9 -0.499234`.

Gerçek Sınıf 1 örneklerinde C0 katkısı `+0.736779`; gerçek Sınıf 2 örneklerinde `+2.432718`.

**Yorum:** Grup Sınıf 0'ı güçlü biçimde desteklerken bazı rakip logitleri de bastırmaktadır; mekanizma tek bir çıktı düğümü ile sınırlı değildir.

## 16. Aday Devre Ablasyonu

Aday `[47,17,57,53,28]` birlikte ablate edildiğinde:

- Sınıf 0 temel durum: `98.6735%`
- Ablasyon sonrası: `86.6327%`
- Değişim: **-12.0408 pp**

**Yorum:** Aday grubun Sınıf 0 davranışına güçlü dağıtık devre düzeyi katkısı vardır. Bu grup eksiksiz devre olarak ilan edilmemiştir.

## 17. Sınıfa Özgü Devre Kontrolü

Aday devre ablasyonu:
- Sınıf 1: `99.3833% → 99.4714%`, `+0.0881 pp`
- Sınıf 2: `97.1899% → 97.1899%`, `0.0000 pp`

**Yorum:** Sınıf 0 etkisi diğer iki kontrol sınıfına göre belirgin biçimde daha büyüktür.

## 18. Tekli Çıkarma Analizi (Leave-One-Out Analysis)

Sınıf 0 temel durum: `98.6735%`.

| Çıkarılan nöron | Kalan grup doğruluğu | Değişim |
|---:|---:|---:|
| N47 | 92.7551% | -5.9184 pp |
| N17 | 92.7551% | -5.9184 pp |
| N57 | 89.5918% | -9.0816 pp |
| N53 | 92.1429% | -6.5306 pp |
| N28 | 92.0408% | -6.6327 pp |

**Yorum:** N57 tekli çıkarma bağlamında en güçlü etkiyi göstermiştir. Bu, tek nöron önem sıralaması ile grup-bağlamı önem sıralamasının aynı olmadığını gösterir.

## 19. Tek Nöron Aday Karşılaştırması

Sınıf 0 temel durum `98.6735%`:

| Nöron | Ablasyon sonrası doğruluk | Değişim |
|---:|---:|---:|
| N47 | 97.7551% | -0.9184 pp |
| N17 | 97.8571% | -0.8164 pp |
| N57 | 98.4694% | -0.2041 pp |
| N53 | 98.1633% | -0.5102 pp |
| N28 | 98.0612% | -0.6123 pp |

**Yorum:** Tek nöron sıralaması N47 > N17 > N28 > N53 > N57 iken tekli çıkarma sıralaması farklıdır. Bu, bağlama bağlı/toplamsal olmayan katkı ile uyumludur.

## 20. Aşamalı Devre Ablasyonu (Progressive Circuit Ablation)

| Grup boyutu | Grup | Sınıf 0 doğruluğu | Değişim |
|---:|---|---:|---:|
| 1 | [47] | 97.7551% | -0.9184 pp |
| 2 | [47,17] | 95.9184% | -2.7551 pp |
| 3 | [47,17,57] | 94.7959% | -3.8776 pp |
| 4 | [47,17,57,53] | 92.0408% | -6.6327 pp |
| 5 | [47,17,57,53,28] | 86.6327% | -12.0408 pp |

**Yorum:** Grup büyüdükçe etki belirginleşmiştir. Sonuç dağıtık/toplamsal olmayan davranış ile uyumludur; sıra bağımlı olduğu için ara artışlar içsel nöron önemi olarak yorumlanmamıştır.

## 21. Devre Keşfi Özeti

Aday devre: `[47,17,57,53,28]`.

- Seçicilik: Sınıf 0'a eğilimli aday belirleme
- Tek ablasyon: N47 `-0.9184 pp`
- Devre ablasyonu: `-12.0408 pp`
- Sınıf 1 kontrolü: `+0.0881 pp`
- Sınıf 2 kontrolü: `0.0000 pp`
- Tekli çıkarma: N57 `-9.0816 pp`
- Aşamalı ablasyon: `-0.9184 → -12.0408 pp`
- Aktivasyon yamalama: Sınıf 1 hedeflerinde Sınıf 0 logiti `+6.0245`, Sınıf 2 hedeflerinde `+4.3068`

**Yorum:** Bulgular, Sınıf 0 davranışı ile ilişkili dağıtık aday devre için güçlü mekanistik kanıt sağlar; eksiksiz devre olduğu henüz kanıtlanmamıştır.

## 22. Mekanistik Doğrulama — Rastgele Kontrol

Aday grup `[47,17,57,53,28]` ile 10 rastgele kontrol grubu karşılaştırılmıştır.

- Aday Sınıf 0 değişimi: **-12.0408 pp**
- Rastgele grupların ortalama değişimi: **-0.1122 pp**
- Rastgele minimum: `-0.9184 pp`
- Rastgele maksimum: `+0.2041 pp`
- Aday − rastgele ortalama: **-11.9286 pp**

**Yorum:** Aday devre etkisinin rastgele nöron seçiminin doğal varyasyonundan kaynaklanma ihtimalini azaltan güçlü kontrol kanıtı elde edilmiştir.

## 23. Sınıf Bazlı Mekanistik Doğrulama

Aday devre `[47,17,57,53,28]` ablasyon sonuçları:

| Sınıf | Temel durum | Ablasyon sonrası | Değişim |
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

**Yorum:** En büyük negatif etki Sınıf 0'da görülmüştür. Grup Sınıf 0'a eğilimlidir fakat yalnızca Sınıf 0'a özgü değildir.

## 24. Devre Düzeyi Aktivasyon Müdahalesi

Aday devre `[47,17,57,53,28]` aktivasyonu ölçeklenmiştir.

| Ölçek | Doğruluk | Ortalama Sınıf 0 olasılığı | Gerçek Sınıf 0 olasılığı |
|---:|---:|---:|---:|
| 0.0 | 96.2700% | 0.075105 | 0.764420 |
| 0.5 | 97.3300% | 0.092623 | 0.938316 |
| 1.0 | 97.5600% | 0.097675 | 0.979257 |
| 1.5 | 97.5400% | 0.100468 | 0.990193 |
| 2.0 | 97.3300% | 0.103643 | 0.993814 |

**Yorum:** Devre aktivasyonu arttıkça gerçek Sınıf 0 olasılığı sistematik biçimde yükselmiştir. Ölçek 0'da devre baskılandığında olasılık `0.7644` seviyesine düşmüş, ölçek 2'de `0.9938` seviyesine çıkmıştır. Bu, devre düzeyi nedensel kanıtı güçlendirmektedir; “nedensellik kanıtlandı” denmemiştir.

## 25. Grafikler

Toplam **11 anlamlı grafik** oluşturulmuştur:

1. MNIST örnek görselleştirmesi
2. Karmaşıklık matrisi
3. Sınıf ortalama aktivasyon ısı haritası
4. N47 müdahalesi ve Sınıf 0 olasılığı
5. N17/N47 aktivasyon korelasyonu saçılım grafiği
6. Aday devre müdahalesi ve Sınıf 0 olasılığı
7. Eğitim kaybı
8. Nöron/devre ablasyonu doğruluğu
9. Aday nöron aktivasyon dağılımı
10. Aday devre aktivasyonunun sınıflar arasındaki dağılımı
11. Aşamalı devre ablasyonu

## 26. Literatür İncelemesi

Sekiz kaynak incelenmiş ve deneylerle ilişkilendirilmiştir:

1. *Interpretability in the Wild: a Circuit for IOI in GPT-2 Small*
2. *Towards Automated Circuit Discovery for Mechanistic Interpretability*
3. *Locating and Editing Factual Associations in GPT*
4. *Toy Models of Superposition*
5. *Sparse Autoencoders Find Highly Interpretable Features in Language Models*
6. *Causal Abstraction: A Theoretical Foundation for Mechanistic Interpretability*
7. *Tracr: Compiled Transformers as a Laboratory for Interpretability*
8. *Gemma Scope*

Deney ↔ literatür eşlemesi: Aktivasyon Analizi, Nöron Ablasyonu, Aktivasyon Müdahalesi, Korelasyon ve Nedensellik, Aktivasyon Yamalama, Devre Keşfi, Dağıtık Temsil, Mekanistik Doğrulama, Özellik Düzeyi Analiz ve Devre Düzeyi Müdahale.

## 27. Sınırlılıklar

1. Tek küçük MNIST MLP ve tek eğitim seed'i kullanıldı.
2. Aday seçimi aktivasyon/seçicilik ve ağırlık analizlerine bağlıdır.
3. Aşamalı ablasyon sırası sıralamaya bağlıdır (order-dependent).
4. `[47,17,57,53,28]` eksiksiz devre olarak kanıtlanmamıştır.
5. Çalıştırmalar arası istatistiksel belirsizlik sınırlı ölçülmüştür.
6. Aday grup Sınıf 0'a eğilimlidir fakat yalnızca Sınıf 0'a özgü değildir.
7. Aktivasyon yamalama kapsamı sınırlı kaynak-hedef örnekleriyle yürütülmüştür.

## 28. Sonraki Deneyler

1. Çoklu seed tekrarı
2. Sentetik gerçek-sahte ilişki veri seti
3. Dağıtık özellik analizi
4. Genişletilmiş aktivasyon yamalama
5. Fashion-MNIST üzerinde ikinci veri seti doğrulaması

## Genel Bilimsel Değerlendirme

Bu haftanın deneyleri modelin yalnızca doğru çıktı üretip üretmediğini değil, çıktının iç temsil üzerinden hangi aday özellik ve devre mekanizmalarıyla ilişkili olduğunu incelemiştir. Gözlem → hipotez → müdahale → çıktı değişimi → kontrol → mekanistik doğrulama zinciri kurulmuştur.

En önemli sonuç, Sınıf 0 davranışı ile güçlü biçimde ilişkili aday grubun `[47,17,57,53,28]` bulunmasıdır. Devre ablasyonu `-12.0408 pp`, rastgele kontrol ortalaması `-0.1122 pp` ve devre aktivasyon müdahalesi gerçek Sınıf 0 olasılığında `0.7644 → 0.9938` değişimi göstermiştir. Bu sonuçlar güçlü nedensel kanıtı destekler; ancak eksiksiz mekanizma veya evrensel nedensellik iddiası için yeterli değildir.
