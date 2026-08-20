# 1. Hafta Deney Günlüğü — Standardize Edilmiş Kayıt

Bu dosya, birinci haftada gerçekten yürütülmüş deneyleri hocanın istediği standart şablona göre yeniden düzenler. Sayısal sonuçlar mevcut `notes/experiment_log.md` kaydından korunmuştur. Tarih alanı için kaynak kayıtlarda kesin tarih bulunmadığından tarih uydurulmamıştır.

## Ortak deney koşulları
- Model: MNIST MLP — `784 → 128 → 64 → 10`
- Activation: ReLU
- Optimizer: Adam
- Learning rate: `0.001`
- Batch size: `64`
- Epoch: `5`
- Seed: `42`
- Device: CPU
- Dataset: MNIST (`60000` train / `10000` test)

---

## E01 — Baseline Model

**Deney ID:** E01  
**Tarih:** 1. hafta — kaynak kayıtta kesin tarih yok  
**Amaç:** Internal analiz ve müdahale deneylerinden önce güvenilir bir baseline model oluşturmak.  
**Hipotez:** Model MNIST üzerinde yeterli sınıflandırma başarımı gösterecek ve sonraki Glass Box deneyleri için kullanılabilir olacaktır.  
**Model:** `784 → 128 → 64 → 10`, ReLU, Adam  
**Dataset:** MNIST  
**Seed:** `42`  
**Değiştirilen parametre:** Yok; baseline koşulu  
**Kontrol grubu:** Müdahalesiz normal model  
**Müdahale grubu:** Yok  
**Sonuç:** Test accuracy `%97.56`; eğitim loss değerleri `0.3328, 0.1354, 0.0945, 0.0717, 0.0558`.  
**Accuracy değişimi:** Baseline olduğu için karşılaştırmalı değişim yok; referans accuracy `%97.56`.  
**Grafik:** Training/validation loss, training/validation accuracy ve confusion matrix kayıtları.  
**Yorum:** Baseline, sonraki internal representation ve intervention deneyleri için yeterli performansı sağlamıştır.  
**Beklenmeyen sonuç:** Kaynak kayıtta belirtilmemiştir.  
**Sonraki deney:** E02 — Activation Analysis.

---

## E02 — Activation Analysis

**Deney ID:** E02  
**Tarih:** 1. hafta — kaynak kayıtta kesin tarih yok  
**Amaç:** Hidden layer activation değerlerini gözlemlemek ve internal representation hakkında ilk ölçümleri elde etmek.  
**Hipotez:** Farklı nöronlar farklı aktivasyon seviyeleri gösterecek ve bazı nöronlar daha belirgin davranış sergileyecektir.  
**Model:** E01 baseline MLP  
**Dataset:** MNIST test seti  
**Seed:** `42`  
**Değiştirilen parametre:** Forward hook ile ReLU2 activation kaydı; model ağırlıkları değiştirilmedi.  
**Kontrol grubu:** Doğal/müdahalesiz model activation'ları  
**Müdahale grubu:** Yok  
**Sonuç:** Tek batch activation shape `[64,64]`; tam test activation matrix `[10000,64]`. Mean activation'ta N62=`4.661`, N61=`2.601`, N54=`2.559`, N47=`2.540` öne çıktı.  
**Accuracy değişimi:** Model değiştirilmedi; accuracy etkisi ölçülmedi.  
**Grafik:** Seçilen nöronların activation dağılımları ve internal activation karşılaştırmaları.  
**Yorum:** Yüksek mean activation tek başına causal importance göstermez.  
**Beklenmeyen sonuç:** N4, N19, N35 ve N58 çok düşük/dead activation gösterdi.  
**Sonraki deney:** E03 — Class Activation / Selectivity.

---

## E03 — Class Activation / Selectivity

**Deney ID:** E03  
**Tarih:** 1. hafta — kaynak kayıtta kesin tarih yok  
**Amaç:** Hangi nöronların hangi sınıflarda daha seçici aktive olduğunu ölçmek ve candidate neuron seçimine observational temel oluşturmak.  
**Hipotez:** Bazı nöronlar belirli sınıflarda diğer sınıflara göre daha yüksek activation gösterecektir.  
**Model:** E01 baseline MLP  
**Dataset:** MNIST test seti  
**Seed:** `42`  
**Değiştirilen parametre:** Selectivity hesabı; model parametreleri değiştirilmedi.  
**Kontrol grubu:** Diğer sınıflardaki mean activation değerleri  
**Müdahale grubu:** Yok  
**Sonuç:** Selectivity = en yüksek class mean activation − ikinci en yüksek class mean activation. N54 class 2 için `3.561`, N47 class 0 için `3.163`, N22 class 1 için `2.881` ile öne çıktı.  
**Accuracy değişimi:** Model değiştirilmedi; accuracy etkisi ölçülmedi.  
**Grafik:** Sınıflara göre activation karşılaştırması.  
**Yorum:** Selectivity candidate seçimi için observational ölçüdür; causal importance değildir.  
**Beklenmeyen sonuç:** Kaynak kayıtta ayrıca belirtilmemiştir.  
**Sonraki deney:** E04 — Single-Neuron Ablation.

---

## E04 — Single-Neuron Ablation

**Deney ID:** E04  
**Tarih:** 1. hafta — kaynak kayıtta kesin tarih yok  
**Amaç:** Seçilen nöronların aktivasyonunu sıfırlayarak output üzerindeki etkilerini ölçmek.  
**Hipotez:** Selectivity ile seçilen bazı nöronların ablasyonu ilgili sınıf davranışını azaltacaktır.  
**Model:** E01 baseline MLP  
**Dataset:** MNIST test seti  
**Seed:** `42`  
**Değiştirilen parametre:** Seçilen nöron activation'ı `0` yapılmıştır.  
**Kontrol grubu:** Müdahalesiz baseline model  
**Müdahale grubu:** N54, N47 ve N62 ablation koşulları  
**Sonuç:** N54 overall `%97.5600 → %97.5300` (`-0.0300 pp`), Class 2 `%97.1899 → %96.8023` (`-0.3876 pp`). N47 overall `%97.5600 → %97.4600` (`-0.1000 pp`), Class 0 `%98.6735 → %97.7551` (`-0.9184 pp`). N62 overall `%97.5600 → %97.6400` (`+0.0800 pp`), Class 3 `%96.8317 → %96.3366` (`-0.4950 pp`).  
**Accuracy değişimi:** En belirgin candidate etkisi N47 için Class 0'da `-0.9184 percentage points`.  
**Grafik:** Ablation sonrası accuracy değişimi.  
**Yorum:** Ablation, seçilen nöronların sınıf davranışına katkısı için causal evidence sağlar; tek başına complete causal mechanism kanıtı değildir. N62 kesin negative control olarak değerlendirilmemiştir.  
**Beklenmeyen sonuç:** N62 overall accuracy'de küçük artış gösterirken Class 3 accuracy'sinde düşüş göstermiştir.  
**Sonraki deney:** E05 — Activation Intervention.

---

## E05 — Activation Intervention

**Deney ID:** E05  
**Tarih:** 1. hafta — kaynak kayıtta kesin tarih yok  
**Amaç:** Ablation'ın ötesinde activation seviyesini kontrollü olarak değiştirerek internal state ile output arasındaki ilişkiyi test etmek.  
**Hipotez:** İlgili nöronun activation seviyesi değiştirildiğinde hedef sınıfın output probability'si sistematik biçimde değişecektir.  
**Model:** E01 baseline MLP  
**Dataset:** MNIST test seti  
**Seed:** `42`  
**Değiştirilen parametre:** N47 veya N54 activation scale'i `0.0, 0.5, 1.0, 1.5, 2.0`.  
**Kontrol grubu:** Scale `1.0` doğal activation koşulu  
**Müdahale grubu:** N47 → Class 0 ve N54 → Class 2 scale koşulları  
**Sonuç:** N47'de true Class 0 probability `0.9640 → 0.9853`; N54'te true Class 2 probability `0.9583 → 0.9676`.  
**Accuracy değişimi:** N47 accuracy `%97.46 → %97.54` aralığında; N54 `%97.53 → %97.42` aralığında değişmiştir.  
**Grafik:** Intervention seviyesine karşı output probability.  
**Yorum:** Kontrollü intervention, ilgili neuron → output pathway için causal evidence'i destekler; “causality proved” denmemelidir.  
**Beklenmeyen sonuç:** Probability değişimi accuracy değişiminden daha belirgin olmuştur.  
**Sonraki deney:** E06 — Correlation vs Causality.

---

## E06 — Correlation vs Causality

**Deney ID:** E06  
**Tarih:** 1. hafta — kaynak kayıtta kesin tarih yok  
**Amaç:** Activation ile output/class behavior arasındaki observational correlation'ı ölçmek ve causal evidence'den ayırmak.  
**Hipotez:** Candidate nöronların activation'ları hedef sınıf davranışıyla korelasyon gösterebilir; ancak correlation tek başına causal claim oluşturmaz.  
**Model:** E01 baseline MLP  
**Dataset:** MNIST test seti  
**Seed:** `42`  
**Değiştirilen parametre:** Pearson correlation hesabı; model değiştirilmedi.  
**Kontrol grubu:** Tüm test örnekleri vs. Class 0 alt kümesi karşılaştırması  
**Müdahale grubu:** Yok  
**Sonuç:** N17–N47 Pearson correlation tüm test örneklerinde `r=0.4485`, yalnız Class 0'da `r=0.7846`.  
**Accuracy değişimi:** Model değiştirilmedi; accuracy etkisi yok.  
**Grafik:** Activation karşılaştırması / correlation analizi.  
**Yorum:** Correlation observational evidence sağlar. Causal claim için ablation ve intervention gerekir.  
**Beklenmeyen sonuç:** Class 0 alt kümesindeki correlation tüm test setinden daha yüksek çıkmıştır.  
**Sonraki deney:** E07 — Candidate Circuit Discovery.

---

## E07 — Candidate Circuit Discovery

**Deney ID:** E07  
**Tarih:** 1. hafta — kaynak kayıtta kesin tarih yok  
**Amaç:** Class 0 davranışıyla ilişkili candidate neuron grubunu belirlemek.  
**Hipotez:** Selectivity ve output connection bilgileri birlikte kullanıldığında Class 0-biased küçük bir candidate group bulunabilir.  
**Model:** E01 baseline MLP  
**Dataset:** MNIST  
**Seed:** `42`  
**Değiştirilen parametre:** Candidate selection kriterleri; model değiştirilmedi.  
**Kontrol grubu:** Diğer neuron'lar  
**Müdahale grubu:** Candidate group `[47,17,57,53,28]`  
**Sonuç:** N47 → Class 0 weight `+0.231610`; N17 `+0.237246`; N28 `+0.233466`; N53 `+0.225550`; N57 `+0.186438`.  
**Accuracy değişimi:** Candidate selection aşamasında accuracy değişimi yok.  
**Grafik:** Candidate activation/selectivity karşılaştırmaları.  
**Yorum:** Output weights candidate pathway belirlemede kullanılabilir; weight magnitude tek başına causal evidence değildir.  
**Beklenmeyen sonuç:** Candidate group tek bir nörondan ziyade beşli bir grup olarak öne çıkmıştır.  
**Sonraki deney:** E08 — Combined Ablation.

---

## E08 — Combined Ablation

**Deney ID:** E08  
**Tarih:** 1. hafta — kaynak kayıtta kesin tarih yok  
**Amaç:** N17 ve N47 birlikte ablate edildiğinde etkinin tekil etkilerin toplamından farklı olup olmadığını incelemek.  
**Hipotez:** Birlikte müdahale, basit additive beklentiden daha büyük bir etki gösterebilir.  
**Model:** E01 baseline MLP  
**Dataset:** MNIST  
**Seed:** `42`  
**Değiştirilen parametre:** N17 ve N47 activation'ları birlikte sıfırlandı.  
**Kontrol grubu:** Tekil N17 ve N47 ablation etkileri  
**Müdahale grubu:** N17 + N47 combined ablation  
**Sonuç:** Overall accuracy `%97.5600 → %97.1900` (`-0.3700 pp`). Class 0 combined `-2.7551 pp`; tekil etkilerin beklenen toplamı `-1.7347 pp`; non-additive fark `-1.0204 pp`.  
**Accuracy değişimi:** Overall `-0.3700 pp`; Class 0 `-2.7551 pp`.  
**Grafik:** Ablation group-size/accuracy karşılaştırması.  
**Yorum:** Non-additivity possible functional interaction veya shared representation düşündürür; interaction kesin olarak kanıtlanmış değildir.  
**Beklenmeyen sonuç:** Combined effect basit tekil toplamdan belirgin biçimde büyüktür.  
**Sonraki deney:** E09 — Activation Patching.

---

## E09 — Activation Patching

**Deney ID:** E09  
**Tarih:** 1. hafta — kaynak kayıtta kesin tarih yok  
**Amaç:** Source activation'larını target örneklerine patch ederek candidate feature'ın davranış transferindeki rolünü test etmek.  
**Hipotez:** Candidate activation'larının farklı sınıftaki target örneğe aktarılması target output'u Class 0 yönünde değiştirebilir.  
**Model:** E01 baseline MLP  
**Dataset:** MNIST, Class 0 source → Class 1 target  
**Seed:** `42`  
**Değiştirilen parametre:** Target activation'a source activation patch edilmiştir.  
**Kontrol grubu:** Patch yapılmayan target örnekler  
**Müdahale grubu:** N17, N47 ve N17+N47 patch'leri  
**Sonuç:** 50 source/target pair'de mean probability change: N17 `+0.00000119 ± 0.00000396`; N47 `+0.00000024 ± 0.00000072`; N17+N47 `+0.00000247 ± 0.00000731`. Tek örnekte prediction Class 1 olarak kalmıştır.  
**Accuracy değişimi:** Pair-level probability değişimi ölçülmüştür; kaynak kayıtta genel accuracy değişimi verilmemiştir.  
**Grafik:** Internal activation comparison / patch effect.  
**Yorum:** Tek nöronlar Class 0 behavior transferi için yeterli görünmemiştir; distributed representation hipotezi için gözlemsel destek sağlar.  
**Beklenmeyen sonuç:** Probability değişimleri çok küçüktür.  
**Sonraki deney:** E10 — Class-Specific Patching Control.

---

## E10 — Class-Specific Patching Control

**Deney ID:** E10  
**Tarih:** 1. hafta — kaynak kayıtta kesin tarih yok  
**Amaç:** Candidate patch etkisinin yalnızca Class 1 target üzerinde mi, yoksa farklı target context'lerinde de ortaya çıkıp çıkmadığını kontrol etmek.  
**Hipotez:** Candidate group Class 0-biased olabilir fakat etkisi target context'ine bağlı olarak farklı sınıflarda da görülebilir.  
**Model:** E01 baseline MLP  
**Dataset:** MNIST Class 0 source → Class 1 / Class 2 target  
**Seed:** `42`  
**Değiştirilen parametre:** Target context/class.  
**Kontrol grubu:** Farklı target sınıfları  
**Müdahale grubu:** Top-5 candidate group `[47,17,57,53,28]`  
**Sonuç:** Class 1 target → Class 0 probability `+0.00887395 ± 0.03161188`; Class 2 target → Class 0 probability `+0.00536434 ± 0.02391533`.  
**Accuracy değişimi:** Kaynak kayıtta genel accuracy değişimi verilmemiştir.  
**Grafik:** Class-specific patch comparison.  
**Yorum:** Candidate group Class 0-exclusive değildir; Class 0 logit'ine güçlü fakat context-dependent katkı sağlayan distributed candidate representation olarak değerlendirilmiştir.  
**Beklenmeyen sonuç:** Class 2 target'larında da pozitif Class 0 probability etkisi görülmüştür.  
**Sonraki deney:** E11 — Logit-Level Patching.

---

## E11 — Logit-Level Patching

**Deney ID:** E11  
**Tarih:** 1. hafta — kaynak kayıtta kesin tarih yok  
**Amaç:** Probability saturation etkisini azaltmak ve candidate patch'in output üzerindeki etkisini logit seviyesinde ölçmek.  
**Hipotez:** Probability değişimi küçük görünse bile candidate group logit üzerinde daha belirgin etki gösterebilir.  
**Model:** E01 baseline MLP  
**Dataset:** MNIST patching deneyleri  
**Seed:** `42`  
**Değiştirilen parametre:** Ölçüm metriği probability yerine Class 0 logit değişimi olarak ele alınmıştır.  
**Kontrol grubu:** Class 1 ve Class 2 target context'leri  
**Müdahale grubu:** Top-5 candidate group patch  
**Sonuç:** Class 1 target Class 0 logit değişimi `+6.024506 ± 1.621096`; Class 2 target `+4.306821 ± 1.859204`.  
**Accuracy değişimi:** Kaynak kayıtta genel accuracy değişimi verilmemiştir.  
**Grafik:** Logit-level patch comparison.  
**Yorum:** Softmax saturation probability etkisini küçük gösterebilir. Logit seviyesinde candidate group'un Class 0 output'una güçlü ve context-dependent etkisi görülmüştür.  
**Beklenmeyen sonuç:** Probability etkisine göre logit etkisi çok daha belirgin olmuştur.  
**Sonraki deney:** E12 — Candidate Group Contribution.

---

## E12 — Candidate Group Weight / Contribution Analysis

**Deney ID:** E12  
**Tarih:** 1. hafta — kaynak kayıtta kesin tarih yok  
**Amaç:** Candidate group'un output logits'e ağırlık ve activation üzerinden katkısını nicel olarak incelemek.  
**Hipotez:** Candidate group Class 0 logit'ine belirgin pozitif katkı sağlayacaktır ancak kararın tamamını tek başına açıklamayacaktır.  
**Model:** E01 baseline MLP  
**Dataset:** 100 Class 0 örneği ve karşılaştırmalı Class 1/Class 2 örnekleri  
**Seed:** `42`  
**Değiştirilen parametre:** Müdahale yok; contribution metriği hesaplandı.  
**Kontrol grubu:** Diğer 59 hidden neuron ve bias  
**Müdahale grubu:** Candidate group `[47,17,57,53,28]`  
**Sonuç:** Class 0 output weights toplamı `+1.114311`; True Class 0 mean candidate contribution `+6.197485`. N47 `+1.654675`, N17 `+1.231128`, N57 `+0.813899`, N53 `+1.292274`, N28 `+1.205509`.  
**Accuracy değişimi:** Model değiştirilmedi; accuracy etkisi ölçülmedi.  
**Grafik:** Candidate contribution comparison.  
**Yorum:** Contribution, kararın yüzdesi olarak yorumlanmamıştır; diğer 59 neuron ve bias da katkı verir. Candidate group Class 0-biased fakat Class 0-exclusive değildir.  
**Beklenmeyen sonuç:** Candidate group diğer class logits'lerine de pozitif/negatif katkılar sağlamıştır.  
**Sonraki deney:** E13 — Candidate Circuit Ablation.

---

## E13 — Candidate Circuit Ablation

**Deney ID:** E13  
**Tarih:** 1. hafta — kaynak kayıtta kesin tarih yok  
**Amaç:** Top-5 candidate circuit'in Class 0 behavior üzerindeki birleşik etkisini ölçmek.  
**Hipotez:** Candidate circuit'in birlikte ablation'ı Class 0 accuracy'sinde belirgin bir düşüş oluşturacaktır.  
**Model:** E01 baseline MLP  
**Dataset:** MNIST test seti  
**Seed:** `42`  
**Değiştirilen parametre:** `[47,17,57,53,28]` activation'ları birlikte sıfırlandı.  
**Kontrol grubu:** Müdahalesiz baseline; ayrıca random circuit kontrolleri sonraki validasyon için kullanıldı.  
**Müdahale grubu:** Candidate circuit `[47,17,57,53,28]`  
**Sonuç:** Class 0 baseline `%98.6735`, ablated `%86.6327`. Etki `-12.0408 percentage points`.  
**Accuracy değişimi:** **`-12.0408 pp`**.  
**Grafik:** Ablation sonrası accuracy değişimi / circuit effect.  
**Yorum:** Candidate group'un Class 0 behavior'a güçlü distributed circuit-level katkısı vardır; complete/definitive circuit olarak ilan edilmemiştir.  
**Beklenmeyen sonuç:** Group etkisi tekil nöron etkilerinden çok daha büyük çıkmıştır.  
**Sonraki deney:** E14 — Class-Wise Circuit Control.

---

## E14 — Class-Wise Circuit Control

**Deney ID:** E14  
**Tarih:** 1. hafta — kaynak kayıtta kesin tarih yok  
**Amaç:** Candidate circuit ablation etkisinin Class 0'a özgü olup olmadığını kontrol etmek.  
**Hipotez:** Candidate circuit Class 0 üzerinde daha büyük etki gösterecek, kontrol sınıflarında etki küçük kalacaktır.  
**Model:** E01 baseline MLP  
**Dataset:** MNIST test seti  
**Seed:** `42`  
**Değiştirilen parametre:** Candidate circuit activation'ları sıfırlandı; değerlendirme sınıfa göre ayrıldı.  
**Kontrol grubu:** Class 1 ve Class 2  
**Müdahale grubu:** Candidate circuit `[47,17,57,53,28]`  
**Sonuç:** Class 1 `%99.3833 → %99.4714` (`+0.0881 pp`); Class 2 `%97.1899 → %97.1899` (`0.0000 pp`).  
**Accuracy değişimi:** Class 1 `+0.0881 pp`, Class 2 `0.0000 pp`; Class 0 `-12.0408 pp` ile çok daha büyük.  
**Grafik:** Class-specific ablation accuracy comparison.  
**Yorum:** Class 0 etkisi diğer iki kontrol sınıfına göre belirgin biçimde daha büyüktür.  
**Beklenmeyen sonuç:** Class 1 accuracy'sinde küçük bir artış görülmüştür.  
**Sonraki deney:** E15 — Leave-One-Out Analysis.

---

## E15 — Leave-One-Out Analysis

**Deney ID:** E15  
**Tarih:** 1. hafta — kaynak kayıtta kesin tarih yok  
**Amaç:** Candidate group içindeki her nöronun diğer candidate nöronlar mevcutken grup bağlamındaki katkısını ölçmek.  
**Hipotez:** Group içindeki nöronların bağlamsal katkıları birbirinden farklı olacaktır.  
**Model:** E01 baseline MLP  
**Dataset:** MNIST Class 0 test örnekleri  
**Seed:** `42`  
**Değiştirilen parametre:** Her koşulda candidate group'dan bir nöron çıkarıldı.  
**Kontrol grubu:** Full candidate group `[47,17,57,53,28]`  
**Müdahale grubu:** Her leave-one-out alt grubu  
**Sonuç:** Baseline `%98.6735`; N47 çıkarılınca `%92.7551` (`-5.9184 pp`), N17 `%92.7551` (`-5.9184 pp`), N57 `%89.5918` (`-9.0816 pp`), N53 `%92.1429` (`-6.5306 pp`), N28 `%92.0408` (`-6.6327 pp`).  
**Accuracy değişimi:** En büyük leave-one-out etkisi N57 için `-9.0816 pp`.  
**Grafik:** Leave-one-out accuracy comparison.  
**Yorum:** N57 group-context içinde en güçlü etkiyi göstermiştir. Single-neuron importance ile group-context importance aynı sıralamayı vermemektedir.  
**Beklenmeyen sonuç:** N57 tek başına ablation'da küçük etkiye sahipken leave-one-out koşulunda en büyük etkiyi göstermiştir.  
**Sonraki deney:** E16 — Single-Neuron Candidate Comparison / Progressive Ablation.

---

## E16 — Progressive Circuit Ablation

**Deney ID:** E16  
**Tarih:** 1. hafta — kaynak kayıtta kesin tarih yok  
**Amaç:** Candidate group büyüdükçe Class 0 accuracy etkisinin nasıl değiştiğini ölçmek.  
**Hipotez:** Birden fazla candidate nöron birlikte ablate edildiğinde etki artacak ve dağıtık/non-additive davranış görülebilecektir.  
**Model:** E01 baseline MLP  
**Dataset:** MNIST Class 0 test seti  
**Seed:** `42`  
**Değiştirilen parametre:** Ablate edilen group size: `1 → 5`.  
**Kontrol grubu:** Önceki group size / baseline koşulu  
**Müdahale grubu:** `[47]`, `[47,17]`, `[47,17,57]`, `[47,17,57,53]`, `[47,17,57,53,28]`  
**Sonuç:** Accuracy etkisi `-0.9184 → -2.7551 → -3.8776 → -6.6327 → -12.0408 pp`.  
**Accuracy değişimi:** 1 nöronda `-0.9184 pp`; 5 nöronda `-12.0408 pp`.  
**Grafik:** Group size vs Class 0 accuracy change.  
**Yorum:** Group büyüdükçe etki belirginleşmiştir. Sonuç distributed/non-additive behavior ile uyumludur; sıra-dependent olduğu için ara artışlar intrinsic neuron importance olarak yorumlanmamıştır.  
**Beklenmeyen sonuç:** Group effect tekil etkilerin basit toplamından daha hızlı büyümüştür.  
**Sonraki deney:** E17 — Random Controls.

---

## E17 — Random Controls

**Deney ID:** E17  
**Tarih:** 1. hafta — kaynak kayıtta kesin tarih yok  
**Amaç:** Candidate circuit etkisinin rastgele seçilen kontrol nöronlarına göre olağandışı olup olmadığını ölçmek.  
**Hipotez:** Candidate circuit effect random control effects'den belirgin biçimde büyük olacaktır.  
**Model:** E01 baseline MLP  
**Dataset:** MNIST Class 0 test seti  
**Seed:** `42`  
**Değiştirilen parametre:** Random control neuron/circuit selection  
**Kontrol grubu:** Randomly selected neuron groups  
**Müdahale grubu:** Candidate circuit `[47,17,57,53,28]`  
**Sonuç:** Candidate Class 0 effect `-12.0408 pp`; random control mean `-0.1122 pp`; candidate effect magnitude yaklaşık `107×` büyüktür.  
**Accuracy değişimi:** Candidate `-12.0408 pp`; random control mean `-0.1122 pp`.  
**Grafik:** Candidate vs random-control effect comparison.  
**Yorum:** Candidate effect random control ortalamasından çok daha büyüktür. Ancak bu ilk hafta kontrolü tek başına çoklu-seed veya geniş istatistiksel doğrulama yerine geçmez.  
**Beklenmeyen sonuç:** Candidate/control ayrımı çok büyük çıkmıştır.  
**Sonraki deney:** E18 — Circuit Intervention.

---

## E18 — Circuit Activation Intervention

**Deney ID:** E18  
**Tarih:** 1. hafta — kaynak kayıtta kesin tarih yok  
**Amaç:** Candidate circuit activation'ını kontrollü biçimde değiştirerek Class 0 output probability'sindeki değişimi ölçmek.  
**Hipotez:** Candidate circuit activation müdahalesi Class 0 probability'sini sistematik biçimde değiştirecektir.  
**Model:** E01 baseline MLP  
**Dataset:** MNIST Class 0 örnekleri  
**Seed:** `42`  
**Değiştirilen parametre:** Candidate circuit activation seviyesi  
**Kontrol grubu:** Doğal activation koşulu  
**Müdahale grubu:** Candidate circuit activation intervention  
**Sonuç:** Gerçek Class 0 probability `0.7644 → 0.9938`.  
**Accuracy değişimi:** Kaynak kayıtta bu deney için accuracy değişimi verilmemiştir; output probability değişimi temel ölçümdür.  
**Grafik:** Intervention seviyesine karşı output probability.  
**Yorum:** Candidate circuit → Class 0 output pathway için güçlü causal evidence desteği vardır; “causality proved” denmemiştir.  
**Beklenmeyen sonuç:** Probability değişimi çok büyük olurken genel accuracy aynı ölçüde değişmemiş olabilir; bu iki metriğin farklı olduğuna dikkat edilmelidir.  
**Sonraki deney:** E19 — Mechanistic Validation.

---

## E19 — Mechanistic Validation / Candidate vs Controls

**Deney ID:** E19  
**Tarih:** 1. hafta — kaynak kayıtta kesin tarih yok  
**Amaç:** Candidate circuit'in Class 0 davranışındaki etkisini selectivity, ablation, intervention, class controls ve random controls birlikte değerlendirerek mekanistik kanıt zincirini özetlemek.  
**Hipotez:** Candidate circuit'in etkisi yalnızca observational correlation'a değil, kontrollü müdahale ve karşılaştırma gruplarına da dayanmalıdır.  
**Model:** E01 baseline MLP  
**Dataset:** MNIST  
**Seed:** `42`  
**Değiştirilen parametre:** Yeni model parametresi yok; önceki deneylerin sonuçları birlikte değerlendirilmiştir.  
**Kontrol grubu:** Class 1/Class 2 controls + random circuit controls  
**Müdahale grubu:** Candidate circuit `[47,17,57,53,28]`  
**Sonuç:** Candidate circuit Class 0 ablation effect `-12.0408 pp`; random control mean `-0.1122 pp`; Class 1 `+0.0881 pp`; Class 2 `0.0000 pp`; intervention true Class 0 probability `0.7644 → 0.9938`.  
**Accuracy değişimi:** Candidate circuit Class 0 `-12.0408 pp`; random control mean `-0.1122 pp`.  
**Grafik:** Candidate vs random controls ve class-specific validation grafikleri.  
**Yorum:** Birinci hafta sonunda candidate circuit için causal evidence/support elde edilmiştir; ancak sonuç tek seed ve tek modelle sınırlıdır. “Causality proved” veya “complete circuit” iddiası yapılmamalıdır.  
**Beklenmeyen sonuç:** Transformer tarafındaki sonraki analizde benzer candidate-feature yaklaşımının tek boyutta istatistiksel olarak özel olmadığı görüldü; bu durum metodolojinin kontrol ihtiyacını güçlendirdi.  
**Sonraki deney:** 2. hafta E06 Multi-seed Circuit Replication.

---

## 1. Hafta Standardizasyon Notu

Bu kayıt, birinci haftada elde edilen sonuçları geriye dönük olarak hocanın deney günlüğü şablonuna eşleştirir. Kaynaklarda bulunmayan tarih, grafik dosya adı, tekrar sayısı veya başka deney ayrıntıları uydurulmamıştır. İkinci haftadan itibaren her deneyin **Hedef başarım kriteri**, **Doğrulama sonucu**, **İstatistiksel anlamlılık** ve **Commit hash** alanları da ayrıca zorunlu tutulacaktır; bu alanlar ikinci hafta ödevinde açıkça istenmiştir.
