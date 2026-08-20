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
