# Week 1 — Ayrıntılı Deney Günlüğü

> Bu dosya yalnızca **Week 1** Colab deneylerinin ayrıntılı ham/ara sonuç günlüğüdür. Week 2 günlük kayıtları `notes/experiment_log_week2.md` içindedir. Ana deney numaralandırması Week 1 için E01–E05'tir; alt çalışmalar `1.x–5.x` biçiminde değerlendirilir.

Bu dosyanın geri kalan içeriği Week 1'de gerçekten çalıştırılmış deneylerin ayrıntılı sayısal kaydıdır. Güncel ana deney özeti için `experiments/week1_experiment_records.md` kullanılmalıdır.

## Week 1 ayrıntılı kayıt özeti

### E01 — Temel Model
- MNIST `60000/10000`, MLP `784 → 128 → 64 → 10`, ReLU, Adam, LR `0.001`, batch `64`, epoch `5`, seed `42`, CPU.
- Test accuracy: **97.56%**.
- Epoch loss: `0.3328, 0.1354, 0.0945, 0.0717, 0.0558`.

### E02 — Aktivasyon Analizi
- ReLU2 tam test aktivasyon matrisi: `[10000,64]`.
- Öne çıkan ortalama aktivasyonlar: N62 `4.661`, N61 `2.601`, N54 `2.559`, N47 `2.540`.
- Düşük/ölü aktivasyon: N4, N19, N35, N58.

### E03 — Aday Özellik / Devre Keşfi
- Sınıf 0 aday grubu: `[47,17,57,53,28]`.
- Seçicilik örnekleri: N54/Sınıf2 `3.561`, N47/Sınıf0 `3.163`, N22/Sınıf1 `2.881`.
- N17–N47 Pearson korelasyonu: tüm test `0.4485`, Sınıf0 `0.7846`.
- Aday grup Sınıf0 logit katkısı: `+6.197485`.

### E04 — Ablasyon ve Devre Müdahaleleri
- N47 tek ablasyon: `-0.9184 pp` Sınıf0.
- N17+N47 birleşik ablasyon: `-2.7551 pp` Sınıf0; non-additive fark `-1.0204 pp`.
- Aday devre `[47,17,57,53,28]` ablasyonu: **-12.0408 pp** Sınıf0.
- Sınıf1 kontrolü: `+0.0881 pp`; Sınıf2: `0.0000 pp`.
- Leave-one-out en güçlü etki: N57 `-9.0816 pp`.
- Progressive ablation: `-0.9184 → -12.0408 pp`.
- Random control ortalaması: **-0.1122 pp**.

### E05 — Aktivasyon Müdahalesi ve Yamalama
- N47 gerçek Sınıf0 olasılığı: `0.9640 → 0.9853`.
- N17 gerçek Sınıf0 olasılığı: `0.9619 → 0.9863`.
- Top-5 patching etkisi: `+0.00546138` ortalama Sınıf0 olasılık değişimi.
- Logit-level patching: Sınıf1 hedefinde C0 logiti `+6.024506`; Sınıf2 hedefinde `+4.306821`.
- Devre aktivasyon ölçeği `0→2`: gerçek Sınıf0 olasılığı `0.764420 → 0.993814`.

## Week 1 genel bilimsel sonuç

Gözlem → aday → müdahale → çıktı değişimi → random/class controls zinciri kuruldu. `[47,17,57,53,28]` adayı için güçlü destek elde edildi; ancak tek seed ve sınırlı tasarım nedeniyle Week 2'de multi-seed, holdout ve geniş random-control doğrulaması gerekliydi.

> **Not:** Bu dosyada yer alan ayrıntılı tarihsel sayılar korunmuştur. Ana deney ID'leri E01–E05'tir; eski ara kayıtların E07/E08/E13/E15/E19 gibi numaraları artık bağımsız deney ID'si olarak kullanılmamalıdır.
