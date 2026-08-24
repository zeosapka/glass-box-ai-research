# 1. Hafta Deney Kayıtları

Bu dosya Week 1'in **5 ana deneyini** standart kayıt şablonuyla tutar. Her ana deney aynı alanları kullanır; alt çalışmalar ana deney altında `x.1`, `x.2` biçiminde numaralandırılır. Alt çalışmalar ayrı deney ID'si değildir.

> **Standart deney şablonu:** Deney ID → Tarih → Amaç → Hipotez → Model → Dataset → Seed → Değiştirilen parametre → Kontrol grubu → Müdahale grubu → Sonuç → Accuracy / etki değişimi → Hedef başarım kriteri → Doğrulama sonucu → İstatistiksel anlamlılık (z / persentil, varsa) → Grafik → Yorum → Beklenmeyen sonuç → Commit hash → Sonraki deney.

---

## 1. Deney — E01: Temel Model (Baseline)

- **Deney ID:** E01
- **Tarih:** Kaynak kaydında belirtilmemiş.
- **Amaç:** Sonraki iç analiz ve müdahale deneyleri için temel model oluşturmak.
- **Hipotez:** Model MNIST'te sonraki Glass Box analizlerini mümkün kılacak yeterli doğruluğa ulaşacaktır.
- **Model:** MNIST MLP `784 → 128 → 64 → 10`; ReLU; Adam; learning rate `0.001`; batch size `64`; epoch `5`.
- **Dataset:** MNIST (`60000` eğitim / `10000` test).
- **Seed:** `42`.
- **Değiştirilen parametre:** Yok; baseline model eğitildi.
- **Kontrol grubu:** Yok.
- **Müdahale grubu:** Yok; baseline ölçümü.
- **Sonuç:** Test doğruluğu **%97.56**; epoch kayıpları `0.3328, 0.1354, 0.0945, 0.0717, 0.0558`.
- **Accuracy / etki değişimi:** Test accuracy **%97.56**.
- **Hedef başarım kriteri:** Kaynak kaydında açık eşik belirtilmemiştir; baseline'ın sonraki deneyler için yeterli performans vermesi hedeflenmiştir.
- **Doğrulama sonucu:** Baseline sonraki iç temsil ve müdahale deneylerini yürütmek için yeterli performansı sağlamıştır.
- **İstatistiksel anlamlılık (z / persentil, varsa):** Uygulanmadı; baseline ölçümüdür.
- **Grafik:** Week 1 grafik kayıtlarında baseline/karmaşıklık matrisi ve eğitim sonuçlarıyla ilişkilidir; ayrıntılı eşleme `figures/figure_index.md` içindedir.
- **Yorum:** Sonraki Glass Box analizleri için yeterli temel performans sağlandı.
- **Beklenmeyen sonuç:** Kaynak kaydında belirtilmemiştir.
- **Commit hash:** Deney kaydında belirtilmemiştir.
- **Sonraki deney:** **E02 — Aktivasyon Analizi.**

---

## 2. Deney — E02: Aktivasyon Analizi

- **Deney ID:** E02
- **Tarih:** Kaynak kaydında belirtilmemiş.
- **Amaç:** Gizli katman aktivasyonlarını gözlemlemek ve aday nöronların ilk gözlemsel sinyallerini belirlemek.
- **Hipotez:** Gizli katmandaki nöronlar farklı aktivasyon seviyeleri gösterecek ve bazıları sonraki aday seçiminde öne çıkacaktır.
- **Model:** MNIST MLP `784 → 128 → 64 → 10`; ReLU; Adam; learning rate `0.001`; batch size `64`; epoch `5`.
- **Dataset:** MNIST (`60000` eğitim / `10000` test).
- **Seed:** `42`.
- **Değiştirilen parametre:** Yok; ReLU2 aktivasyonları gözlemlendi.
- **Kontrol grubu:** Yok; gözlemsel analiz.
- **Müdahale grubu:** Yok.
- **Sonuç:** Tam ReLU2 aktivasyon matrisi `[10000,64]`. Öne çıkan ortalama aktivasyonlar N62 `4.661`, N61 `2.601`, N54 `2.559`, N47 `2.540`; N4, N19, N35 ve N58 düşük/ölü aktivasyon gösterdi.
- **Accuracy / etki değişimi:** Aktivasyon matrisi ve nöron düzeyi aktivasyon farkları ölçüldü; causal accuracy etkisi ölçülmedi.
- **Hedef başarım kriteri:** Kaynak kaydında açık eşik belirtilmemiştir; sonraki aday analizine yeterli iç temsil verisi elde edilmesi hedeflenmiştir.
- **Doğrulama sonucu:** Tam aktivasyon matrisi elde edildi ve aday analizine geçildi.
- **İstatistiksel anlamlılık (z / persentil, varsa):** Uygulanmadı.
- **Grafik:** Sınıf ortalama aktivasyon ısı haritası ve aday aktivasyon dağılımları; ayrıntılı eşleme `figures/figure_index.md` içindedir.
- **Yorum:** Yüksek aktivasyon tek başına nedensel önem değildir.
- **Beklenmeyen sonuç:** Bazı nöronlarda düşük/ölü aktivasyon gözlendi.
- **Commit hash:** Deney kaydında belirtilmemiştir.
- **Sonraki deney:** **E03 — Aday Özellik / Devre Keşfi.**

---

## 3. Deney — E03: Aday Özellik / Devre Keşfi

- **Deney ID:** E03
- **Tarih:** Kaynak kaydında belirtilmemiş.
- **Amaç:** Sınıf aktivasyonu, selectivity, çıktı ağırlıkları ve korelasyon kullanarak Class 0 ile ilişkili aday nöronları ve aday devreyi belirlemek.
- **Hipotez:** Class 0'a seçici aktivasyon gösteren ve çıktı yolunda güçlü katkıya sahip nöronlardan oluşan aday grup sonraki müdahalelerde Class 0 davranışını etkileyebilir.
- **Model:** MNIST MLP `784 → 128 → 64 → 10`; ReLU; Adam; learning rate `0.001`; batch size `64`; epoch `5`.
- **Dataset:** MNIST (`60000` eğitim / `10000` test).
- **Seed:** `42`.
- **Değiştirilen parametre:** Nöronlar değiştirilmedi; selectivity, aktivasyon, çıktı ağırlığı ve korelasyon ölçüldü.
- **Kontrol grubu:** Bu aşamada ayrı random-control müdahalesi yoktur.
- **Müdahale grubu:** Sonraki deneyler için aday grup `[47,17,57,53,28]`.
- **Sonuç:** N54/Sınıf2 selectivity `3.561`, N47/Sınıf0 `3.163`, N22/Sınıf1 `2.881`; aday grup `[47,17,57,53,28]`; N17–N47 korelasyonu tüm testte `0.4485`, yalnızca Sınıf0'da `0.7846`.
- **Accuracy / etki değişimi:** Bu deneyde causal accuracy değişimi ölçülmedi; aday grup belirlendi.
- **Hedef başarım kriteri:** Kaynak kaydında açık eşik belirtilmemiştir; sonraki müdahale deneyleri için test edilebilir aday mekanizma oluşturulması hedeflenmiştir.
- **Doğrulama sonucu:** Aday grup belirlendi; gözlemsel bulgular E04/E05 müdahalelerine taşındı.
- **İstatistiksel anlamlılık (z / persentil, varsa):** Uygulanmadı; korelasyon gözlemsel ölçümdür.
- **Grafik:** Sınıf ortalama aktivasyon/selectivity ve N17–N47 korelasyon grafikleri; ayrıntılı eşleme `figures/figure_index.md` içindedir.
- **Yorum:** Selectivity ve çıktı ağırlığı aday seçiminde kullanılmıştır; tek başına nedensel kanıt değildir.
- **Beklenmeyen sonuç:** Aday grup Class 0'a eğilimli olsa da yalnızca Class 0'a özgü değildir.
- **Commit hash:** Deney kaydında belirtilmemiştir.
- **Sonraki deney:** **E04 — Ablasyon ve Devre Müdahaleleri.**

### E03 alt çalışmalar

#### 3.1 — Sınıf Aktivasyonu ve Seçicilik
- Seçicilik = en yüksek sınıf ortalama aktivasyonu − ikinci en yüksek sınıf ortalama aktivasyonu.
- Öne çıkanlar: N54/Sınıf2 `3.561`, N47/Sınıf0 `3.163`, N22/Sınıf1 `2.881`.

#### 3.2 — Aday Devre Keşfi
- Aday grup: `[47,17,57,53,28]`.
- Sınıf0 çıktı ağırlıkları: N47 `+0.231610`, N17 `+0.237246`, N28 `+0.233466`, N53 `+0.225550`, N57 `+0.186438`.

#### 3.3 — Aday Grup Katkısı
- Sınıf0 ağırlık toplamı: `+1.114311`.
- Gerçek Sınıf0 ortalama grup katkısı: **+6.197485**.

#### 3.4 — Aday Grubun Tüm Logitlere Katkısı
- Gerçek Sınıf0 örneklerinde aday katkıları: C0 `+6.197485`, C1 `-2.253895`, C3 `-3.120183`, C4 `-3.548902`; diğerleri ham günlükte kayıtlı.

#### 3.5 — Korelasyon ve Nedensellik
- N17–N47 Pearson korelasyonu: tüm test `r=0.4485`; Sınıf0 `r=0.7846`.
- Korelasyon gözlemsel kanıttır; nedensel iddia için müdahale/ablasyon gerekir.

---

## 4. Deney — E04: Ablasyon ve Devre Müdahaleleri

- **Deney ID:** E04
- **Tarih:** Kaynak kaydında belirtilmemiş.
- **Amaç:** E03'te belirlenen aday nöron/devrenin Class 0 davranışına müdahale edildiğinde model çıktısının değişip değişmediğini ve etkinin random/class-specific kontrollerden ayrışıp ayrışmadığını test etmek.
- **Hipotez:** Aday nöron/devrenin ablasyonu Class 0 doğruluğunda belirgin düşüş oluşturmalı; random ve sınıfa özgü kontroller çok daha küçük etki göstermelidir.
- **Model:** MNIST MLP `784 → 128 → 64 → 10`; ReLU; Adam; learning rate `0.001`; batch size `64`; epoch `5`.
- **Dataset:** MNIST (`60000` eğitim / `10000` test).
- **Seed:** `42`.
- **Değiştirilen parametre:** Seçilen nöronların/aday devrenin aktivasyonları ablasyonla `0` yapıldı; birleşik ve aşamalı müdahaleler uygulandı.
- **Kontrol grubu:** Class 1/Class 2 kontrolleri ve random control grupları.
- **Müdahale grubu:** Aday `[47,17,57,53,28]` ve ilgili alt gruplar.
- **Sonuç:** Aday devre ablasyonu Class 0'da `%98.6735 → %86.6327`; etki **−12.0408 pp**. Random control ortalaması **−0.1122 pp**.
- **Accuracy / etki değişimi:** Tek nöron N47 `−0.9184 pp`; birleşik N17+N47 `−2.7551 pp`; aday devre `−12.0408 pp`.
- **Hedef başarım kriteri:** Aday devre etkisinin random controls'dan belirgin biçimde büyük olması ve sınıfa özgü kontrollerde aynı büyüklükte etki görülmemesi hedeflenmiştir; kaynak kaydında sayısal eşik ayrıca belirtilmemiştir.
- **Doğrulama sonucu:** Kriter yönü desteklendi; aday etki random kontrol ortalamasından çok daha büyüktür ve Class 1/Class 2 kontrollerinde benzer etki görülmemiştir.
- **İstatistiksel anlamlılık (z / persentil, varsa):** Formal z/persentil hesaplanmadı; random control karşılaştırması betimseldir.
- **Grafik:** Nöron/devre ablasyonu doğruluğu, aday aktivasyon dağılımı ve aşamalı devre ablasyonu; ayrıntılı eşleme `figures/figure_index.md` içindedir.
- **Yorum:** Bulgular aday devrenin Class 0 davranışıyla güçlü nedensel ilişkisini destekler; eksiksiz/tek devre iddiası yapılmaz.
- **Beklenmeyen sonuç:** Leave-one-out bağlamında N57 `−9.0816 pp` ile en güçlü tekli çıkarma etkisini gösterdi; bu sıralama tek nöron ablasyon sıralamasıyla aynı değildir.
- **Commit hash:** Deney kaydında belirtilmemiştir.
- **Sonraki deney:** **E05 — Aktivasyon Müdahalesi ve Yamalama.**

### E04 alt çalışmalar

#### 4.1 — Tek Nöron Ablasyonu
- N47 Sınıf0: `%98.6735 → %97.7551` (`-0.9184 pp`).
- N54 Sınıf2: `-0.3876 pp`; N62 Sınıf3: `-0.4950 pp`.

#### 4.2 — Birleşik Ablasyon
- N17+N47 genel etki: `-0.3700 pp`.
- Sınıf0 birleşik etki: `-2.7551 pp`.
- Tekil toplam beklentisi: `-1.7347 pp`.
- Non-additive fark: `-1.0204 pp`.

#### 4.3 — Aday Devre Ablasyonu
- `[47,17,57,53,28]` birlikte ablate edildi.
- Sınıf0: `%98.6735 → %86.6327`.
- **Etki: `-12.0408 pp`.**

#### 4.4 — Sınıfa Özgü Devre Kontrolü
- Sınıf1: `+0.0881 pp`.
- Sınıf2: `0.0000 pp`.

#### 4.5 — Tekli Çıkarma / Leave-One-Out
- N47 `-5.9184 pp`; N17 `-5.9184 pp`; N57 `-9.0816 pp`; N53 `-6.5306 pp`; N28 `-6.6327 pp`.

#### 4.6 — Aşamalı Devre Ablasyonu
- Grup boyutu 1→5 etkileri: `-0.9184, -2.7551, -3.8776, -6.6327, -12.0408 pp`.

#### 4.7 — Rastgele Kontroller / Mekanistik Doğrulama
- Aday devre: `-12.0408 pp`.
- Rastgele kontrol ortalaması: `-0.1122 pp`.

---

## 5. Deney — E05: Aktivasyon Müdahalesi ve Yamalama

- **Deney ID:** E05
- **Tarih:** Kaynak kaydında belirtilmemiş.
- **Amaç:** Aday nöron/devre aktivasyonunun kontrollü olarak artırılması/azaltılması ve activation patching yoluyla çıktı davranışına etkisini test etmek.
- **Hipotez:** Aday nöron/devre aktivasyonunun kontrollü ölçeklenmesi Class 0 çıktısını sistematik olarak değiştirmeli; grup patching tek nöron patching'den daha belirgin olabilir.
- **Model:** MNIST MLP `784 → 128 → 64 → 10`; ReLU; Adam; learning rate `0.001`; batch size `64`; epoch `5`.
- **Dataset:** MNIST (`60000` eğitim / `10000` test).
- **Seed:** `42`.
- **Değiştirilen parametre:** N47/N54/N17 aktivasyon ölçekleri; aday grubun aktivasyonu; tekli ve grup patching.
- **Kontrol grubu:** Sınıf1/Sınıf2 hedefleri ve tekli/top-k patching karşılaştırmaları.
- **Müdahale grubu:** N47, N54, N17 ve aday Top-5 `[47,17,57,53,28]`.
- **Sonuç:** N47 gerçek Sınıf0 olasılığı `0.9640 → 0.9853`; N17 `0.9619 → 0.9863`; devre aktivasyonu `0.7644 → 0.9938`. Top-5 patching etkisi Top-1/Top-3'ten daha büyüktür.
- **Accuracy / etki değişimi:** Top-1 `+0.00000024`, Top-3 `+0.00001863`, Top-5 `+0.00546138` patching etkileri; devre ölçekleme gerçek Class 0 olasılığını `0.7644 → 0.9938` değiştirdi.
- **Hedef başarım kriteri:** Kontrollü aktivasyon müdahalesinin çıktı olasılığında sistematik değişim oluşturması ve grup patching'in dağıtık temsil hipotezini desteklemesi hedeflenmiştir; kaynak kaydında ayrı sayısal eşik belirtilmemiştir.
- **Doğrulama sonucu:** Müdahale sonucu sistematik değişim gözlendi; Top-5 patching etkisi arttı. Ancak yüksek standart sapma ve sınıfa özgü olmayan etkiler nedeniyle sonuçlar sınırlı destek olarak yorumlandı.
- **İstatistiksel anlamlılık (z / persentil, varsa):** Formal z/persentil raporlanmadı; patching sonuçlarında ortalama ve standart sapma verildi.
- **Grafik:** N47 müdahalesi/Sınıf0 olasılığı, aday devre müdahalesi/Sınıf0 olasılığı ve ilgili patching grafik kayıtları; ayrıntılı eşleme `figures/figure_index.md` içindedir.
- **Yorum:** Kontrollü activation intervention ve patching, aday grubun çıktı davranışına katkısını destekler; sonuçlar “nedensellik kanıtlandı” şeklinde yorumlanmaz.
- **Beklenmeyen sonuç:** Aday grup Sınıf1 ve Sınıf2 hedeflerinde de Sınıf0 logit/olasılık etkisi oluşturdu; aday mekanizma yalnızca Class 0'a özgü değildir.
- **Commit hash:** Deney kaydında belirtilmemiştir.
- **Sonraki deney:** **Week 2 — E06: Çoklu Seed Devre Tekrarı.**

### E05 alt çalışmalar

#### 5.1 — Aktivasyon Müdahalesi
- N47 gerçek Sınıf0 olasılığı `0.9640 → 0.9853` (ölçek `0→2`).
- N54 gerçek Sınıf2 olasılığı `0.9583 → 0.9676`.

#### 5.2 — Aktivasyon Yamalama
- N17: `+0.00000119 ± 0.00000396`.
- N47: `+0.00000024 ± 0.00000072`.
- N17+N47: `+0.00000247 ± 0.00000731`.

#### 5.3 — Dağıtık Özellik Yamalama
- Top-1: `+0.00000024`.
- Top-3: `+0.00001863`.
- Top-5: `+0.00546138`.

#### 5.4 — Sınıfa Özgü Yamalama Kontrolü
- Sınıf1 hedefi: `+0.00887395 ± 0.03161188`.
- Sınıf2 hedefi: `+0.00536434 ± 0.02391533`.

#### 5.5 — Logit Düzeyinde Yamalama
- Sınıf1 hedefinde Sınıf0 logiti: `+6.024506 ± 1.621096`.
- Sınıf2 hedefinde Sınıf0 logiti: `+4.306821 ± 1.859204`.

---

## Week 1 Sonuç Özeti

- Baseline test accuracy: **%97.56**.
- Aday grup: `[47,17,57,53,28]`.
- Aday devre ablasyonu: **−12.0408 pp** Class 0.
- Random control ortalaması: **−0.1122 pp**.
- Aktivasyon müdahalesi ve patching, aday iç temsilin çıktıyla ilişkisini müdahale yoluyla destekledi.
- Bilimsel sınır: sonuçlar tek seed ve sınırlı veri tasarımına dayandığından Week 2'de multi-seed, holdout ve geniş random-control doğrulaması gerekliydi.

## Kaynak ve Tekrar Üretilebilirlik

- Ayrıntılı ham sayısal kayıt: `notes/experiment_log_week1.md`.
- Grafikler: `figures/week1/`.
- Bu dosya **5 ana Week 1 deneyi** ve bunların `x.1`, `x.2` biçimindeki alt analizlerini kaydeder.
- Bölüm 17'deki güncellenmiş deney günlüğü standardı, Week 1 ve Week 2 kayıtlarının ortak şablonudur.
