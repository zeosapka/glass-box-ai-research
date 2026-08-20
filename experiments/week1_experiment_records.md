# Week 1 Experiment Records

Bu dosya, hocanın istediği standart deney kayıt formatını `experiments/` altında tutar. Ayrıntılı ham sayısal kayıt `notes/experiment_log.md` içindedir. Kaynakta bulunmayan tarih/değerler uydurulmaz.

## Ortak koşullar
- Model: MNIST MLP `784 → 128 → 64 → 10`
- Activation: ReLU
- Optimizer: Adam
- Learning rate: `0.001`
- Batch size: `64`
- Epoch: `5`
- Seed: `42`
- Dataset: MNIST (`60000` train / `10000` test)

---

## E01 — Baseline Model
- **Deney ID:** E01
- **Tarih:** 1. hafta; kesin tarih kaynakta yok
- **Amaç:** Sonraki internal analysis ve intervention deneyleri için baseline oluşturmak.
- **Hipotez:** Model MNIST'te yeterli accuracy sağlayacaktır.
- **Model/Dataset/Seed:** Ortak koşullar.
- **Değiştirilen parametre:** Yok; baseline.
- **Kontrol grubu:** Müdahalesiz model.
- **Müdahale grubu:** Yok.
- **Sonuç:** Test accuracy `%97.56`; epoch loss `0.3328, 0.1354, 0.0945, 0.0717, 0.0558`.
- **Accuracy değişimi:** Referans `%97.56`.
- **Grafik:** Baseline loss/accuracy/confusion kayıtları.
- **Yorum:** Sonraki Glass Box analizleri için yeterli baseline.
- **Beklenmeyen sonuç:** Kaynakta belirtilmemiş.
- **Sonraki deney:** E02.

## E02 — Activation Analysis
- **Deney ID:** E02
- **Tarih:** 1. hafta; kesin tarih kaynakta yok
- **Amaç:** Hidden-layer activation'larını gözlemlemek.
- **Hipotez:** Nöronlar farklı activation davranışları gösterecektir.
- **Model/Dataset/Seed:** Ortak koşullar; MNIST test seti; seed 42.
- **Değiştirilen parametre:** Forward hook ile ReLU2 activation kaydı; ağırlıklar değişmedi.
- **Kontrol grubu:** Doğal activation'lar.
- **Müdahale grubu:** Yok.
- **Sonuç:** Activation matrix `[10000,64]`; N62 `4.661`, N61 `2.601`, N54 `2.559`, N47 `2.540` mean activation ile öne çıktı.
- **Accuracy değişimi:** Model değiştirilmedi.
- **Grafik:** Activation dağılımları.
- **Yorum:** Yüksek activation tek başına causal importance değildir.
- **Beklenmeyen sonuç:** N4, N19, N35, N58 düşük/dead activation gösterdi.
- **Sonraki deney:** E03.

## E03 — Class Activation / Selectivity
- **Deney ID:** E03
- **Tarih:** 1. hafta; kesin tarih kaynakta yok
- **Amaç:** Class-selective candidate nöronları belirlemek.
- **Hipotez:** Bazı nöronlar belirli sınıflarda daha seçici olacaktır.
- **Model/Dataset/Seed:** Ortak koşullar; MNIST test; seed 42.
- **Değiştirilen parametre:** Selectivity hesabı; model değişmedi.
- **Kontrol grubu:** Diğer sınıfların mean activation'ları.
- **Müdahale grubu:** Yok.
- **Sonuç:** Selectivity: top class mean − second class mean. N54/Class2 `3.561`, N47/Class0 `3.163`, N22/Class1 `2.881`.
- **Accuracy değişimi:** Yok.
- **Grafik:** Selectivity/candidate ranking.
- **Yorum:** Observational candidate-selection ölçüsüdür; causal importance değildir.
- **Beklenmeyen sonuç:** Kaynakta ayrıca belirtilmemiş.
- **Sonraki deney:** E04.

## E04 — Single-Neuron Ablation
- **Deney ID:** E04
- **Tarih:** 1. hafta; kesin tarih kaynakta yok
- **Amaç:** Seçilen nöronların activation'ını sıfırlayıp output etkisini ölçmek.
- **Hipotez:** Candidate nöron ablasyonu ilgili class behavior'ı azaltacaktır.
- **Model/Dataset/Seed:** Ortak koşullar; MNIST test; seed 42.
- **Değiştirilen parametre:** Seçilen activation `0`.
- **Kontrol grubu:** Baseline.
- **Müdahale grubu:** N54, N47, N62.
- **Sonuç:** N47 Class0 `%98.6735 → %97.7551` (`-0.9184 pp`); N54 Class2 `-0.3876 pp`; N62 Class3 `-0.4950 pp`.
- **Accuracy değişimi:** En belirgin candidate etkisi N47/Class0 `-0.9184 pp`.
- **Grafik:** Ablation accuracy.
- **Yorum:** Causal evidence/support sağlar; complete mechanism kanıtı değildir.
- **Beklenmeyen sonuç:** N62 overall accuracy küçük artarken Class3 düştü.
- **Sonraki deney:** E05.

## E05 — Activation Intervention
- **Deney ID:** E05
- **Tarih:** 1. hafta; kesin tarih kaynakta yok
- **Amaç:** Activation scaling ile output probability değişimini test etmek.
- **Hipotez:** Activation değişimi hedef class probability'sini sistematik değiştirecektir.
- **Model/Dataset/Seed:** Ortak koşullar; MNIST test; seed 42.
- **Değiştirilen parametre:** Scale `0.0, 0.5, 1.0, 1.5, 2.0`.
- **Kontrol grubu:** Scale 1.0.
- **Müdahale grubu:** N47→Class0, N54→Class2.
- **Sonuç:** N47 true Class0 probability `0.9640 → 0.9853`; N54 true Class2 `0.9583 → 0.9676`.
- **Accuracy değişimi:** N47 `%97.46–97.54`; N54 `%97.53–97.42`.
- **Grafik:** Scale vs probability.
- **Yorum:** Causal evidence'i destekler; “causality proved” değildir.
- **Beklenmeyen sonuç:** Probability etkisi accuracy etkisinden daha belirgin.
- **Sonraki deney:** E06.

## E06 — Correlation vs Causality
- **Deney ID:** E06
- **Tarih:** 1. hafta; kesin tarih kaynakta yok
- **Amaç:** Correlation'ı causal evidence'den ayırmak.
- **Hipotez:** Activation correlation gözlenebilir, fakat tek başına causal değildir.
- **Model/Dataset/Seed:** Ortak koşullar; MNIST test; seed 42.
- **Değiştirilen parametre:** Pearson correlation hesabı; model değişmedi.
- **Kontrol grubu:** Tüm test seti vs Class0 alt kümesi.
- **Müdahale grubu:** Yok.
- **Sonuç:** N17–N47 `r=0.4485` overall, `r=0.7846` Class0.
- **Accuracy değişimi:** Yok.
- **Grafik:** Correlation plot.
- **Yorum:** Correlation observational evidence; intervention/ablation causal evidence için gereklidir.
- **Beklenmeyen sonuç:** Class0 correlation daha yüksek.
- **Sonraki deney:** E07.

## E07 — Candidate Circuit Discovery
- **Deney ID:** E07
- **Tarih:** 1. hafta; kesin tarih kaynakta yok
- **Amaç:** Class0-biased candidate group belirlemek.
- **Hipotez:** Selectivity + output connections küçük bir candidate group ortaya çıkaracaktır.
- **Model/Dataset/Seed:** Ortak koşullar; MNIST; seed 42.
- **Değiştirilen parametre:** Candidate selection; model değişmedi.
- **Kontrol grubu:** Diğer nöronlar.
- **Müdahale grubu:** `[47,17,57,53,28]` candidate group.
- **Sonuç:** Class0 output weights N47 `+0.231610`, N17 `+0.237246`, N28 `+0.233466`, N53 `+0.225550`, N57 `+0.186438`.
- **Accuracy değişimi:** Selection aşamasında yok.
- **Grafik:** Candidate/selectivity comparison.
- **Yorum:** Weight magnitude tek başına causal evidence değildir.
- **Beklenmeyen sonuç:** Candidate tek nöron yerine beşli grup olarak öne çıktı.
- **Sonraki deney:** E08.

## E08 — Combined Ablation
- **Deney ID:** E08
- **Tarih:** 1. hafta; kesin tarih kaynakta yok
- **Amaç:** N17+N47 combined effect'in additive beklentiden sapmasını test etmek.
- **Hipotez:** Combined effect tekil etkilerin toplamından farklı olabilir.
- **Model/Dataset/Seed:** Ortak koşullar; MNIST; seed 42.
- **Değiştirilen parametre:** N17 ve N47 activation `0`.
- **Kontrol grubu:** Tekil ablation etkileri.
- **Müdahale grubu:** N17+N47.
- **Sonuç:** Overall `-0.3700 pp`; Class0 combined `-2.7551 pp`; additive expectation `-1.7347 pp`; non-additive difference `-1.0204 pp`.
- **Accuracy değişimi:** Overall `-0.3700 pp`; Class0 `-2.7551 pp`.
- **Grafik:** Group ablation.
- **Yorum:** Functional interaction/shared representation düşündürür; interaction kesin kanıtlanmış değildir.
- **Beklenmeyen sonuç:** Combined effect additive beklentiden büyüktü.
- **Sonraki deney:** E09.

## E09 — Activation Patching
- **Deney ID:** E09
- **Tarih:** 1. hafta; kesin tarih kaynakta yok
- **Amaç:** Source activation'ı target'a taşıyarak information transferini test etmek.
- **Hipotez:** Candidate patch target output'u Class0 yönünde değiştirebilir.
- **Model/Dataset/Seed:** MLP; Class0 source→Class1 target; seed42.
- **Değiştirilen parametre:** Target activation patch.
- **Kontrol grubu:** Unpatched target.
- **Müdahale grubu:** N17, N47, N17+N47.
- **Sonuç:** Mean probability change N17 `+0.00000119`, N47 `+0.00000024`, N17+N47 `+0.00000247`.
- **Accuracy değişimi:** Prediction Class1 olarak kaldı.
- **Grafik:** Patch effect.
- **Yorum:** Tek nöronlar davranış transferi için yeterli değildi; distributed representation hipotezini destekleyen gözlem.
- **Beklenmeyen sonuç:** Etkiler çok küçüktü.
- **Sonraki deney:** E10.

## E10 — Distributed Feature Patching
- **Deney ID:** E10
- **Tarih:** 1. hafta; kesin tarih kaynakta yok
- **Amaç:** Candidate group büyüklüğünün patch etkisine etkisini test etmek.
- **Hipotez:** Top-k group effect tek nörondan daha güçlü olabilir.
- **Model/Dataset/Seed:** MLP; Class0→Class1 patch pairs; seed42.
- **Değiştirilen parametre:** Patched group size Top1/Top3/Top5.
- **Kontrol grubu:** Unpatched target.
- **Müdahale grubu:** Top1/Top3/Top5 candidate groups.
- **Sonuç:** Mean C0 probability change Top1 `+0.00000024`, Top3 `+0.00001863`, Top5 `+0.00546138`.
- **Accuracy değişimi:** Kaynak kayıtta patch transferi için ayrı accuracy değişimi verilmedi.
- **Grafik:** Group size vs patch effect.
- **Yorum:** Distributed representation adayı; yüksek std nedeniyle definitive circuit değildir.
- **Beklenmeyen sonuç:** Top5 etkisi belirgin biçimde büyüdü.
- **Sonraki deney:** E11.

## E11 — Class-Specific Patching Control
- **Deney ID:** E11
- **Tarih:** 1. hafta; kesin tarih kaynakta yok
- **Amaç:** Candidate group'un Class0-exclusive olup olmadığını kontrol etmek.
- **Hipotez:** Candidate effect diğer target classes üzerinde de görülebilir.
- **Model/Dataset/Seed:** MLP; seed42.
- **Değiştirilen parametre:** Top5 candidate patch.
- **Kontrol grubu:** Class1/Class2 targets.
- **Müdahale grubu:** Top5 candidate patch.
- **Sonuç:** Class1 target `+0.00887395 ± 0.03161188`; Class2 target `+0.00536434 ± 0.02391533` C0 probability change.
- **Accuracy değişimi:** Kaynakta ayrı accuracy sonucu verilmedi.
- **Grafik:** Class-specific patch control.
- **Yorum:** Candidate Class0-exclusive değil; context-dependent.
- **Beklenmeyen sonuç:** Diğer class targets da etki aldı.
- **Sonraki deney:** E12.

## E12 — Logit-Level Patching
- **Deney ID:** E12
- **Tarih:** 1. hafta; kesin tarih kaynakta yok
- **Amaç:** Softmax saturation etkisini azaltmak için logit-level patch effect ölçmek.
- **Hipotez:** Probability'den daha büyük internal output effect görülebilir.
- **Model/Dataset/Seed:** MLP; seed42.
- **Değiştirilen parametre:** Top5 candidate patch.
- **Kontrol grubu:** Unpatched target.
- **Müdahale grubu:** Top5 patch.
- **Sonuç:** Class1 target C0 logit `+6.024506 ± 1.621096`; Class2 `+4.306821 ± 1.859204`.
- **Accuracy değişimi:** Kaynakta ayrı accuracy verilmedi.
- **Grafik:** Logit patch effect.
- **Yorum:** Candidate group C0 output'a güçlü fakat context-dependent katkı gösterdi.
- **Beklenmeyen sonuç:** Probability effectine göre logit effect çok daha görünür.
- **Sonraki deney:** E13.

## E13 — Candidate Group Contribution
- **Deney ID:** E13
- **Tarih:** 1. hafta; kesin tarih kaynakta yok
- **Amaç:** Candidate group'un output logits'e computational contribution'ını ölçmek.
- **Hipotez:** Candidate group C0 logitine pozitif katkı sağlayacaktır.
- **Model/Dataset/Seed:** MLP; seed42.
- **Değiştirilen parametre:** Contribution hesabı; model değişmedi.
- **Kontrol grubu:** Diğer neurons/bias.
- **Müdahale grubu:** `[47,17,57,53,28]`.
- **Sonuç:** C0 weight sum `+1.114311`; true C0 mean group contribution `+6.197485`.
- **Accuracy değişimi:** Yok.
- **Grafik:** Candidate group logit contribution.
- **Yorum:** Contribution decision yüzdesi değildir; diğer nöronlar ve bias da katkı verir.
- **Beklenmeyen sonuç:** Group C0-biased ama exclusive değil.
- **Sonraki deney:** E14.

## E14 — Candidate Group Contribution to All Logits
- **Deney ID:** E14
- **Tarih:** 1. hafta; kesin tarih kaynakta yok
- **Amaç:** Candidate contribution'ın yalnız C0 output node ile sınırlı olup olmadığını incelemek.
- **Hipotez:** Group bazı competitor logits'i de etkiler.
- **Model/Dataset/Seed:** MLP; seed42.
- **Değiştirilen parametre:** Contribution decomposition.
- **Kontrol grubu:** Diğer neurons/bias.
- **Müdahale grubu:** Candidate group.
- **Sonuç:** True C0 sample logits: C0 `+6.197485`; C1 `-2.253895`; C3 `-3.120183`; C4 `-3.548902`; diğerleri kaynak logda kayıtlı.
- **Accuracy değişimi:** Yok.
- **Grafik:** All-logit contribution.
- **Yorum:** Mekanizma tek output node'a indirgenemez.
- **Beklenmeyen sonuç:** Candidate bazı competitor logits'i bastırdı.
- **Sonraki deney:** E15.

## E15 — Candidate Circuit Ablation
- **Deney ID:** E15
- **Tarih:** 1. hafta; kesin tarih kaynakta yok
- **Amaç:** Candidate group'un birlikte çıkarılmasının Class0 davranışına etkisini ölçmek.
- **Hipotez:** Candidate group ablation Class0 accuracy'yi belirgin azaltacaktır.
- **Model/Dataset/Seed:** MLP; MNIST test; seed42.
- **Değiştirilen parametre:** `[47,17,57,53,28]` activation'ları sıfırlandı.
- **Kontrol grubu:** Normal candidate-group baseline.
- **Müdahale grubu:** Full candidate group ablation.
- **Sonuç:** Class0 `%98.6735 → %86.6327`, **`-12.0408 pp`**.
- **Accuracy değişimi:** `-12.0408 pp`.
- **Grafik:** Candidate circuit ablation.
- **Yorum:** Güçlü distributed circuit-level causal evidence; complete circuit ilan edilmez.
- **Beklenmeyen sonuç:** Group effect tekil nöron etkilerinden çok daha büyük.
- **Sonraki deney:** E16.

## E16 — Class-Specific Circuit Control
- **Deney ID:** E16
- **Tarih:** 1. hafta; kesin tarih kaynakta yok
- **Amaç:** Candidate circuit effect'in class-specific olup olmadığını kontrol etmek.
- **Hipotez:** Class0 effect kontrol class'larından belirgin büyük olacaktır.
- **Model/Dataset/Seed:** MLP; seed42.
- **Değiştirilen parametre:** Candidate group ablation.
- **Kontrol grubu:** Class1/Class2.
- **Müdahale grubu:** Candidate ablation.
- **Sonuç:** Class1 `%99.3833 → %99.4714` (`+0.0881 pp`); Class2 değişim `0.0000 pp`.
- **Accuracy değişimi:** Class0 etkisi kontrollere göre çok daha büyük.
- **Grafik:** Class-wise control.
- **Yorum:** Class0-biased effect için destek.
- **Beklenmeyen sonuç:** Class1'de küçük accuracy artışı.
- **Sonraki deney:** E17.

## E17 — Leave-One-Out Analysis
- **Deney ID:** E17
- **Tarih:** 1. hafta; kesin tarih kaynakta yok
- **Amaç:** Group içindeki her nöronun çıkarılmasıyla remaining-group importance'ı ölçmek.
- **Hipotez:** Nöronların group-context importance sıralaması single-neuron sıralamasıyla aynı olmayabilir.
- **Model/Dataset/Seed:** MLP; Class0 test; seed42.
- **Değiştirilen parametre:** Her seferinde bir candidate çıkarıldı.
- **Kontrol grubu:** Full candidate group.
- **Müdahale grubu:** N47/N17/N57/N53/N28 leave-one-out.
- **Sonuç:** N47 `-5.9184 pp`; N17 `-5.9184 pp`; N57 `-9.0816 pp`; N53 `-6.5306 pp`; N28 `-6.6327 pp`.
- **Accuracy değişimi:** En güçlü leave-one-out N57 `-9.0816 pp`.
- **Grafik:** Leave-one-out accuracy.
- **Yorum:** Single-neuron rank ile group-context rank farklıdır; non-additivity ile uyumludur.
- **Beklenmeyen sonuç:** N57 single ablation'da zayıfken leave-one-out'ta en güçlüydü.
- **Sonraki deney:** E18.

## E18 — Progressive Circuit Ablation
- **Deney ID:** E18
- **Tarih:** 1. hafta; kesin tarih kaynakta yok
- **Amaç:** Candidate group büyüklüğü arttıkça Class0 etkisinin nasıl değiştiğini görmek.
- **Hipotez:** Group büyüdükçe toplam etki artacaktır.
- **Model/Dataset/Seed:** MLP; Class0 test; seed42.
- **Değiştirilen parametre:** Group size 1→5.
- **Kontrol grubu:** Baseline.
- **Müdahale grubu:** `[47]`, `[47,17]`, `[47,17,57]`, `[47,17,57,53]`, full group.
- **Sonuç:** Change `-0.9184, -2.7551, -3.8776, -6.6327, -12.0408 pp`.
- **Accuracy değişimi:** 5-neuron group `-12.0408 pp`.
- **Grafik:** Progressive ablation.
- **Yorum:** Distributed/non-additive behavior ile uyumlu; sıra-dependent sonuçlar intrinsic importance olarak yorumlanmaz.
- **Beklenmeyen sonuç:** Group effect hızlı büyüdü.
- **Sonraki deney:** E19.

## E19 — Random Controls / Mechanistic Validation
- **Deney ID:** E19
- **Tarih:** 1. hafta; kesin tarih kaynakta yok
- **Amaç:** Candidate circuit effect'ini random control ve class control ile karşılaştırmak.
- **Hipotez:** Candidate effect random controls'tan belirgin büyük olmalıdır.
- **Model/Dataset/Seed:** MLP; MNIST test; seed42.
- **Değiştirilen parametre:** Random neuron groups ile aynı ablation/intervention ölçümü.
- **Kontrol grubu:** Random controls ve class-specific controls.
- **Müdahale grubu:** Candidate group.
- **Sonuç:** Random control mean Class0 effect `-0.1122 pp`; candidate circuit `-12.0408 pp`.
- **Accuracy değişimi:** Candidate vs random farkı çok büyüktür.
- **Grafik:** Candidate vs random control.
- **Yorum:** Candidate effect için güçlü karşılaştırmalı causal evidence; yine de tek seed nedeniyle genelleme iddiası yapılmaz.
- **Beklenmeyen sonuç:** Random control effect candidate effectinden yaklaşık iki mertebe küçüktür.
- **Sonraki deney:** Hafta 2 — multi-seed replication (E20).

## Kaynak ve tekrar üretilebilirlik
- Ayrıntılı ham sayısal kayıt: `notes/experiment_log.md`.
- Her deney için grafikler `figures/` altında tutulur.
- Bu dosya deney kayıtlarının standart formatıdır; yeni veri üretmez.
- Eksik tarih veya ölçüm uydurulmaz.
