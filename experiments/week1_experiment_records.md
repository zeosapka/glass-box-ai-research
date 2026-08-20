# 1. Hafta Deney Kayıtları

Bu dosya, hocanın istediği standart deney kayıt formatını `experiments/` altında tutar. Ayrıntılı ham sayısal kayıt `notes/experiment_log.md` içindedir. Kaynakta bulunmayan tarih/değerler uydurulmaz.

## Ortak Koşullar
- Model: MNIST MLP `784 → 128 → 64 → 10`
- Aktivasyon (activation): ReLU
- Optimizasyon algoritması (optimizer): Adam
- Öğrenme oranı (learning rate): `0.001`
- Batch size: `64`
- Epoch: `5`
- Seed (rastgelelik tohumu): `42`
- Veri seti (dataset): MNIST (`60000` eğitim / `10000` test)

---

## E01 — Temel Model (Baseline Model)
- **Deney ID:** E01
- **Tarih:** 1. hafta; kesin tarih kaynakta yok
- **Amaç:** Sonraki iç analiz (internal analysis) ve müdahale (intervention) deneyleri için temel model oluşturmak.
- **Hipotez:** Model MNIST'te yeterli doğruluk (accuracy) sağlayacaktır.
- **Model / Veri Seti / Seed:** Ortak koşullar.
- **Değiştirilen parametre:** Yok; temel model.
- **Kontrol grubu:** Müdahalesiz model.
- **Müdahale grubu:** Yok.
- **Sonuç:** Test doğruluğu `%97.56`; epoch kayıpları `0.3328, 0.1354, 0.0945, 0.0717, 0.0558`.
- **Accuracy değişimi:** Referans `%97.56`.
- **Grafik:** Temel model eğitim kaybı / doğruluk / karmaşıklık matrisi kayıtları.
- **Yorum:** Sonraki Glass Box analizleri için yeterli temel model oluşturuldu.
- **Beklenmeyen sonuç:** Kaynakta belirtilmemiş.
- **Sonraki deney:** E02.

## E02 — Aktivasyon Analizi (Activation Analysis)
- **Deney ID:** E02
- **Tarih:** 1. hafta; kesin tarih kaynakta yok
- **Amaç:** Gizli katman (hidden layer) aktivasyonlarını gözlemlemek.
- **Hipotez:** Nöronlar farklı aktivasyon davranışları gösterecektir.
- **Model / Veri Seti / Seed:** Ortak koşullar; MNIST test seti; seed 42.
- **Değiştirilen parametre:** Forward hook ile ReLU2 aktivasyon kaydı; ağırlıklar değişmedi.
- **Kontrol grubu:** Doğal aktivasyonlar.
- **Müdahale grubu:** Yok.
- **Sonuç:** Aktivasyon matrisi `[10000,64]`; N62 `4.661`, N61 `2.601`, N54 `2.559`, N47 `2.540` ortalama aktivasyon ile öne çıktı.
- **Accuracy değişimi:** Model değiştirilmedi.
- **Grafik:** Aktivasyon dağılımları.
- **Yorum:** Yüksek aktivasyon tek başına nedensel önem (causal importance) göstermez.
- **Beklenmeyen sonuç:** N4, N19, N35, N58 düşük/ölü (dead) aktivasyon gösterdi.
- **Sonraki deney:** E03.

## E03 — Sınıf Aktivasyonu / Seçicilik (Class Activation / Selectivity)
- **Deney ID:** E03
- **Tarih:** 1. hafta; kesin tarih kaynakta yok
- **Amaç:** Sınıf seçici (class-selective) aday nöronları belirlemek.
- **Hipotez:** Bazı nöronlar belirli sınıflarda daha seçici olacaktır.
- **Model / Veri Seti / Seed:** Ortak koşullar; MNIST test; seed 42.
- **Değiştirilen parametre:** Seçicilik hesabı; model değişmedi.
- **Kontrol grubu:** Diğer sınıfların ortalama aktivasyonları.
- **Müdahale grubu:** Yok.
- **Sonuç:** Seçicilik = en yüksek sınıf ortalama aktivasyonu − ikinci en yüksek sınıf ortalama aktivasyonu. N54/Sınıf2 `3.561`, N47/Sınıf0 `3.163`, N22/Sınıf1 `2.881`.
- **Accuracy değişimi:** Yok.
- **Grafik:** Seçicilik / aday sıralaması.
- **Yorum:** Gözlemsel (observational) aday-seçim ölçüsüdür; nedensel önem değildir.
- **Beklenmeyen sonuç:** Kaynakta ayrıca belirtilmemiş.
- **Sonraki deney:** E04.

## E04 — Tek Nöron Ablasyonu (Single-Neuron Ablation)
- **Deney ID:** E04
- **Tarih:** 1. hafta; kesin tarih kaynakta yok
- **Amaç:** Seçilen nöronların aktivasyonunu sıfırlayıp çıktı etkisini ölçmek.
- **Hipotez:** Aday nöron ablasyonu ilgili sınıf davranışını azaltacaktır.
- **Model / Veri Seti / Seed:** Ortak koşullar; MNIST test; seed 42.
- **Değiştirilen parametre:** Seçilen aktivasyon `0`.
- **Kontrol grubu:** Temel model.
- **Müdahale grubu:** N54, N47, N62.
- **Sonuç:** N47 Sınıf0 `%98.6735 → %97.7551` (`-0.9184 pp`); N54 Sınıf2 `-0.3876 pp`; N62 Sınıf3 `-0.4950 pp`.
- **Accuracy değişimi:** En belirgin aday etkisi N47/Sınıf0 `-0.9184 pp`.
- **Grafik:** Ablasyon doğruluğu.
- **Yorum:** Nedensel kanıtı (causal evidence/support) destekler; eksiksiz mekanizma kanıtı değildir.
- **Beklenmeyen sonuç:** N62 genel doğruluğu küçük ölçüde artırırken Sınıf3 düştü.
- **Sonraki deney:** E05.

## E05 — Aktivasyon Müdahalesi (Activation Intervention)
- **Deney ID:** E05
- **Tarih:** 1. hafta; kesin tarih kaynakta yok
- **Amaç:** Aktivasyon ölçekleme ile çıktı olasılığındaki değişimi test etmek.
- **Hipotez:** Aktivasyon değişimi hedef sınıf olasılığını sistematik olarak değiştirecektir.
- **Model / Veri Seti / Seed:** Ortak koşullar; MNIST test; seed 42.
- **Değiştirilen parametre:** Ölçek `0.0, 0.5, 1.0, 1.5, 2.0`.
- **Kontrol grubu:** Ölçek 1.0.
- **Müdahale grubu:** N47→Sınıf0, N54→Sınıf2.
- **Sonuç:** N47 gerçek Sınıf0 olasılığı `0.9640 → 0.9853`; N54 gerçek Sınıf2 `0.9583 → 0.9676`.
- **Accuracy değişimi:** N47 `%97.46–97.54`; N54 `%97.53–97.42`.
- **Grafik:** Ölçek ve olasılık.
- **Yorum:** Nedensel kanıtı destekler; “nedensellik kanıtlandı” şeklinde ifade edilmez.
- **Beklenmeyen sonuç:** Olasılık etkisi doğruluk etkisinden daha belirgin.
- **Sonraki deney:** E06.

## E06 — Korelasyon ve Nedensellik (Correlation vs Causality)
- **Deney ID:** E06
- **Tarih:** 1. hafta; kesin tarih kaynakta yok
- **Amaç:** Korelasyonu nedensel kanıttan ayırmak.
- **Hipotez:** Aktivasyon korelasyonu gözlenebilir, fakat tek başına nedensel değildir.
- **Model / Veri Seti / Seed:** Ortak koşullar; MNIST test; seed 42.
- **Değiştirilen parametre:** Pearson korelasyon hesabı; model değişmedi.
- **Kontrol grubu:** Tüm test seti ve Sınıf0 alt kümesi.
- **Müdahale grubu:** Yok.
- **Sonuç:** N17–N47 `r=0.4485` genel, `r=0.7846` Sınıf0.
- **Accuracy değişimi:** Yok.
- **Grafik:** Korelasyon grafiği.
- **Yorum:** Korelasyon gözlemsel kanıt sağlar. Nedensel iddia için müdahale ve ablasyon gereklidir.
- **Beklenmeyen sonuç:** Sınıf0 korelasyonu daha yüksek.
- **Sonraki deney:** E07.

## E07 — Aday Devre Keşfi (Candidate Circuit Discovery)
- **Deney ID:** E07
- **Tarih:** 1. hafta; kesin tarih kaynakta yok
- **Amaç:** Sınıf0'a eğilimli aday grubu belirlemek.
- **Hipotez:** Seçicilik + çıktı bağlantıları küçük bir aday grubu ortaya çıkaracaktır.
- **Model / Veri Seti / Seed:** Ortak koşullar; MNIST; seed 42.
- **Değiştirilen parametre:** Aday seçimi; model değişmedi.
- **Kontrol grubu:** Diğer nöronlar.
- **Müdahale grubu:** `[47,17,57,53,28]` aday grubu.
- **Sonuç:** Sınıf0 çıktı ağırlıkları N47 `+0.231610`, N17 `+0.237246`, N28 `+0.233466`, N53 `+0.225550`, N57 `+0.186438`.
- **Accuracy değişimi:** Seçim aşamasında yok.
- **Grafik:** Aday / seçicilik karşılaştırması.
- **Yorum:** Çıktı ağırlığı büyüklüğü tek başına nedensel kanıt değildir.
- **Beklenmeyen sonuç:** Aday tek nöron yerine beşli grup olarak öne çıktı.
- **Sonraki deney:** E08.

## E08 — Birleşik Ablasyon (Combined Ablation)
- **Deney ID:** E08
- **Tarih:** 1. hafta; kesin tarih kaynakta yok
- **Amaç:** N17+N47 birleşik etkisinin toplamsal beklentiden sapmasını test etmek.
- **Hipotez:** Birleşik etki tekil etkilerin toplamından farklı olabilir.
- **Model / Veri Seti / Seed:** Ortak koşullar; MNIST; seed 42.
- **Değiştirilen parametre:** N17 ve N47 aktivasyonu `0`.
- **Kontrol grubu:** Tekil ablasyon etkileri.
- **Müdahale grubu:** N17+N47.
- **Sonuç:** Genel `-0.3700 pp`; Sınıf0 birleşik `-2.7551 pp`; toplamsal beklenti `-1.7347 pp`; toplamsal olmayan fark `-1.0204 pp`.
- **Accuracy değişimi:** Genel `-0.3700 pp`; Sınıf0 `-2.7551 pp`.
- **Grafik:** Grup ablasyonu.
- **Yorum:** İşlevsel etkileşim (functional interaction) / paylaşılan temsil (shared representation) düşündürür; etkileşim doğrudan kanıtlanmış değildir.
- **Beklenmeyen sonuç:** Birleşik etki toplamsal beklentiden büyüktü.
- **Sonraki deney:** E09.

## E09 — Aktivasyon Yamalama (Activation Patching)
- **Deney ID:** E09
- **Tarih:** 1. hafta; kesin tarih kaynakta yok
- **Amaç:** Kaynak aktivasyonu hedefe taşıyarak bilgi aktarımını test etmek.
- **Hipotez:** Aday yamalama hedef çıktıyı Sınıf0 yönünde değiştirebilir.
- **Model / Veri Seti / Seed:** MLP; Sınıf0 kaynak→Sınıf1 hedef; seed 42.
- **Değiştirilen parametre:** Hedef aktivasyon yamalama.
- **Kontrol grubu:** Yamalama yapılmamış hedef.
- **Müdahale grubu:** N17, N47, N17+N47.
- **Sonuç:** Ortalama olasılık değişimi N17 `+0.00000119`, N47 `+0.00000024`, N17+N47 `+0.00000247`.
- **Accuracy değişimi:** Tahmin Sınıf1 olarak kaldı.
- **Grafik:** Yamalama etkisi.
- **Yorum:** Tek nöronlar davranış aktarımı için yeterli değildi; dağıtık temsil (distributed representation) hipotezini destekleyen bir gözlemdir.
- **Beklenmeyen sonuç:** Etkiler çok küçüktü.
- **Sonraki deney:** E10.

## E10 — Dağıtık Özellik Yamalama (Distributed Feature Patching)
- **Deney ID:** E10
- **Tarih:** 1. hafta; kesin tarih kaynakta yok
- **Amaç:** Aday grup büyüklüğünün yamalama etkisine etkisini test etmek.
- **Hipotez:** Top-k grup etkisi tek nörondan daha güçlü olabilir.
- **Model / Veri Seti / Seed:** MLP; Sınıf0→Sınıf1 yamalama çiftleri; seed 42.
- **Değiştirilen parametre:** Yamalı grup büyüklüğü Top1/Top3/Top5.
- **Kontrol grubu:** Yamalama yapılmamış hedef.
- **Müdahale grubu:** Top1/Top3/Top5 aday grupları.
- **Sonuç:** Ortalama Sınıf0 olasılık değişimi Top1 `+0.00000024`, Top3 `+0.00001863`, Top5 `+0.00546138`.
- **Accuracy değişimi:** Kaynak kayıtta yamalama aktarımı için ayrı doğruluk değişimi verilmedi.
- **Grafik:** Grup büyüklüğü ve yamalama etkisi.
- **Yorum:** Dağıtık temsil adayı; yüksek std nedeniyle tek başına kesin devre değildir.
- **Beklenmeyen sonuç:** Top5 etkisi belirgin biçimde büyüdü.
- **Sonraki deney:** E11.

## E11 — Sınıfa Özgü Yamalama Kontrolü (Class-Specific Patching Control)
- **Deney ID:** E11
- **Tarih:** 1. hafta; kesin tarih kaynakta yok
- **Amaç:** Aday grubun yalnızca Sınıf0'a özgü olup olmadığını kontrol etmek.
- **Hipotez:** Aday etki diğer hedef sınıflarda da görülebilir.
- **Model / Veri Seti / Seed:** MLP; seed 42.
- **Değiştirilen parametre:** Top5 aday yamalama.
- **Kontrol grubu:** Sınıf1/Sınıf2 hedefleri.
- **Müdahale grubu:** Top5 aday yamalama.
- **Sonuç:** Sınıf1 hedefi `+0.00887395 ± 0.03161188`; Sınıf2 hedefi `+0.00536434 ± 0.02391533` Sınıf0 olasılık değişimi.
- **Accuracy değişimi:** Kaynakta ayrı doğruluk sonucu verilmedi.
- **Grafik:** Sınıfa özgü yamalama kontrolü.
- **Yorum:** Aday Sınıf0'a özel değildir; bağlama bağlıdır (context-dependent).
- **Beklenmeyen sonuç:** Diğer hedef sınıflar da etki aldı.
- **Sonraki deney:** E12.

## E12 — Logit Düzeyinde Yamalama (Logit-Level Patching)
- **Deney ID:** E12
- **Tarih:** 1. hafta; kesin tarih kaynakta yok
- **Amaç:** Softmax doygunluğunun etkisini azaltmak için logit düzeyindeki yamalama etkisini ölçmek.
- **Hipotez:** Olasılıktan daha büyük bir iç çıktı etkisi görülebilir.
- **Model / Veri Seti / Seed:** MLP; seed 42.
- **Değiştirilen parametre:** Top5 aday yamalama.
- **Kontrol grubu:** Yamalama yapılmamış hedef.
- **Müdahale grubu:** Top5 yamalama.
- **Sonuç:** Sınıf1 hedefi Sınıf0 logiti `+6.024506 ± 1.621096`; Sınıf2 `+4.306821 ± 1.859204`.
- **Accuracy değişimi:** Kaynakta ayrı doğruluk verilmedi.
- **Grafik:** Logit yamalama etkisi.
- **Yorum:** Aday grup Sınıf0 çıktısına güçlü fakat bağlama bağlı katkı gösterdi.
- **Beklenmeyen sonuç:** Olasılık etkisine göre logit etkisi çok daha görünür.
- **Sonraki deney:** E13.

## E13 — Aday Grup Katkısı (Candidate Group Contribution)
- **Deney ID:** E13
- **Tarih:** 1. hafta; kesin tarih kaynakta yok
- **Amaç:** Aday grubun çıktı logitlerine hesaplamalı katkısını ölçmek.
- **Hipotez:** Aday grup Sınıf0 logitine pozitif katkı sağlayacaktır.
- **Model / Veri Seti / Seed:** MLP; seed 42.
- **Değiştirilen parametre:** Katkı hesabı; model değişmedi.
- **Kontrol grubu:** Diğer nöronlar / bias.
- **Müdahale grubu:** `[47,17,57,53,28]`.
- **Sonuç:** Sınıf0 ağırlık toplamı `+1.114311`; gerçek Sınıf0 ortalama grup katkısı `+6.197485`.
- **Accuracy değişimi:** Yok.
- **Grafik:** Aday grup logit katkısı.
- **Yorum:** Katkı, kararın yüzdesi değildir; diğer nöronlar ve bias da katkı verir.
- **Beklenmeyen sonuç:** Grup Sınıf0'a eğilimli fakat yalnızca Sınıf0'a özgü değil.
- **Sonraki deney:** E14.

## E14 — Aday Grubun Tüm Logitlere Katkısı
- **Deney ID:** E14
- **Tarih:** 1. hafta; kesin tarih kaynakta yok
- **Amaç:** Aday katkısının yalnızca Sınıf0 çıktı düğümü ile sınırlı olup olmadığını incelemek.
- **Hipotez:** Grup bazı rakip logitleri de etkileyecektir.
- **Model / Veri Seti / Seed:** MLP; seed 42.
- **Değiştirilen parametre:** Katkı ayrıştırması (contribution decomposition).
- **Kontrol grubu:** Diğer nöronlar / bias.
- **Müdahale grubu:** Aday grup.
- **Sonuç:** Gerçek Sınıf0 örnek logitleri: C0 `+6.197485`; C1 `-2.253895`; C3 `-3.120183`; C4 `-3.548902`; diğerleri ham günlükte kayıtlı.
- **Accuracy değişimi:** Yok.
- **Grafik:** Tüm logitlere katkı.
- **Yorum:** Mekanizma tek bir çıktı düğümüne indirgenemez.
- **Beklenmeyen sonuç:** Aday grup bazı rakip logitleri bastırdı.
- **Sonraki deney:** E15.

## E15 — Aday Devre Ablasyonu (Candidate Circuit Ablation)
- **Deney ID:** E15
- **Tarih:** 1. hafta; kesin tarih kaynakta yok
- **Amaç:** Aday grubun birlikte çıkarılmasının Sınıf0 davranışına etkisini ölçmek.
- **Hipotez:** Aday grup ablasyonu Sınıf0 doğruluğunu belirgin azaltacaktır.
- **Model / Veri Seti / Seed:** MLP; MNIST test; seed 42.
- **Değiştirilen parametre:** `[47,17,57,53,28]` aktivasyonları sıfırlandı.
- **Kontrol grubu:** Normal aday-grup temel durumu.
- **Müdahale grubu:** Tam aday grup ablasyonu.
- **Sonuç:** Sınıf0 `%98.6735 → %86.6327`, **`-12.0408 pp`**.
- **Accuracy değişimi:** `-12.0408 pp`.
- **Grafik:** Aday devre ablasyonu.
- **Yorum:** Güçlü dağıtık devre düzeyi nedensel kanıtı; eksiksiz devre ilan edilmez.
- **Beklenmeyen sonuç:** Grup etkisi tekil nöron etkilerinden çok daha büyük.
- **Sonraki deney:** E16.

## E16 — Sınıfa Özgü Devre Kontrolü
- **Deney ID:** E16
- **Tarih:** 1. hafta; kesin tarih kaynakta yok
- **Amaç:** Aday devre etkisinin sınıfa özgü olup olmadığını kontrol etmek.
- **Hipotez:** Sınıf0 etkisi kontrol sınıflarından belirgin büyük olacaktır.
- **Model / Veri Seti / Seed:** MLP; seed 42.
- **Değiştirilen parametre:** Aday grup ablasyonu.
- **Kontrol grubu:** Sınıf1/Sınıf2.
- **Müdahale grubu:** Aday ablasyonu.
- **Sonuç:** Sınıf1 `%99.3833 → %99.4714` (`+0.0881 pp`); Sınıf2 değişim `0.0000 pp`.
- **Accuracy değişimi:** Sınıf0 etkisi kontrollere göre çok daha büyük.
- **Grafik:** Sınıf bazlı kontrol.
- **Yorum:** Sınıf0'a eğilimli etki için destek.
- **Beklenmeyen sonuç:** Sınıf1'de küçük doğruluk artışı.
- **Sonraki deney:** E17.

## E17 — Tekli Çıkarma Analizi (Leave-One-Out Analysis)
- **Deney ID:** E17
- **Tarih:** 1. hafta; kesin tarih kaynakta yok
- **Amaç:** Grup içindeki her nöronun çıkarılmasıyla kalan-grup önemini ölçmek.
- **Hipotez:** Nöronların grup-bağlamındaki önem sıralaması tek nöron sıralamasıyla aynı olmayabilir.
- **Model / Veri Seti / Seed:** MLP; Sınıf0 test; seed 42.
- **Değiştirilen parametre:** Her seferinde bir aday çıkarıldı.
- **Kontrol grubu:** Tam aday grubu.
- **Müdahale grubu:** N47/N17/N57/N53/N28 tekli çıkarma.
- **Sonuç:** N47 `-5.9184 pp`; N17 `-5.9184 pp`; N57 `-9.0816 pp`; N53 `-6.5306 pp`; N28 `-6.6327 pp`.
- **Accuracy değişimi:** En güçlü tekli çıkarma N57 `-9.0816 pp`.
- **Grafik:** Tekli çıkarma doğruluğu.
- **Yorum:** Tek nöron sıralaması ile grup-bağlamı sıralaması farklıdır; toplamsal olmayan katkıyla uyumludur.
- **Beklenmeyen sonuç:** N57 tek nöron ablasyonunda zayıfken tekli çıkarma bağlamında en güçlüydü.
- **Sonraki deney:** E18.

## E18 — Aşamalı Devre Ablasyonu (Progressive Circuit Ablation)
- **Deney ID:** E18
- **Tarih:** 1. hafta; kesin tarih kaynakta yok
- **Amaç:** Aday grup büyüklüğü arttıkça Sınıf0 etkisinin nasıl değiştiğini görmek.
- **Hipotez:** Grup büyüdükçe toplam etki artacaktır.
- **Model / Veri Seti / Seed:** MLP; Sınıf0 test; seed 42.
- **Değiştirilen parametre:** Grup boyutu 1→5.
- **Kontrol grubu:** Temel model.
- **Müdahale grubu:** `[47]`, `[47,17]`, `[47,17,57]`, `[47,17,57,53]`, tam grup.
- **Sonuç:** Değişim `-0.9184, -2.7551, -3.8776, -6.6327, -12.0408 pp`.
- **Accuracy değişimi:** 5 nöronlu grup `-12.0408 pp`.
- **Grafik:** Aşamalı ablasyon.
- **Yorum:** Dağıtık/toplamsal olmayan davranışla uyumlu; sıralamaya bağlı sonuçlar içsel önem olarak yorumlanmaz.
- **Beklenmeyen sonuç:** Grup etkisi hızlı büyüdü.
- **Sonraki deney:** E19.

## E19 — Rastgele Kontroller / Mekanistik Doğrulama
- **Deney ID:** E19
- **Tarih:** 1. hafta; kesin tarih kaynakta yok
- **Amaç:** Aday devre etkisini rastgele kontrol ve sınıf kontrolü ile karşılaştırmak.
- **Hipotez:** Aday etkisi rastgele kontrollerden belirgin büyük olmalıdır.
- **Model / Veri Seti / Seed:** MLP; MNIST test; seed 42.
- **Değiştirilen parametre:** Rastgele nöron grupları ile aynı ablasyon/müdahale ölçümü.
- **Kontrol grubu:** Rastgele kontroller ve sınıfa özgü kontroller.
- **Müdahale grubu:** Aday grup.
- **Sonuç:** Rastgele kontrol ortalama Sınıf0 etkisi `-0.1122 pp`; aday devre `-12.0408 pp`.
- **Accuracy değişimi:** Aday ve rastgele kontrol arasındaki fark çok büyüktür.
- **Grafik:** Aday ve rastgele kontrol.
- **Yorum:** Aday etki için güçlü karşılaştırmalı nedensel kanıt; yine de tek seed nedeniyle genelleme iddiası yapılmaz.
- **Beklenmeyen sonuç:** Rastgele kontrol etkisi aday etkisinden yaklaşık iki mertebe küçüktür.
- **Sonraki deney:** 2. hafta — çoklu seed tekrarı (multi-seed replication, E20).

## Kaynak ve Tekrar Üretilebilirlik
- Ayrıntılı ham sayısal kayıt: `notes/experiment_log.md`.
- Her deney için grafikler `figures/` altında tutulur.
- Bu dosya deney kayıtlarının standart formatıdır; yeni veri üretmez.
- Eksik tarih veya ölçüm uydurulmaz.
