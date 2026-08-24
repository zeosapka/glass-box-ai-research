# Glass Box AI Araştırması

**Mekanistik Yorumlanabilirlik (Mechanistic Interpretability) ve Glass Box AI — 2 Haftalık Araştırma Çalışması**

Bu repository, iki haftalık araştırma çalışmasının deneylerini, analizlerini, sonuçlarını ve raporlama materyallerini içerir. İlk hafta kontrollü bir MNIST MLP üzerinde aday nöron/devre mekanizmasının keşfi ve müdahale ile doğrulanması; ikinci hafta ise bu yaklaşımın çoklu seed, bağımsız holdout, geniş random-control, graded intervention, grup müdahalesi, sentetik true-vs-spurious test ve küçük bir local LLM üzerinde genişletilmesi ele alınmıştır.

## Araştırma sorusu

> Model doğru sonucu üretiyor mu? sorusunun ötesinde: **Model bu sonucu hangi iç mekanizma (internal mechanism) üzerinden üretiyor?**

## Ana metodoloji

`VERİ (DATA) → MODEL → İÇ TEMSİL (INTERNAL REPRESENTATION) → ÖZELLİK (FEATURE) → MÜDAHALE (INTERVENTION) → ÇIKTI (OUTPUT) → DOĞRULAMA (VALIDATION)`

1. **Modeli kur:** Kontrollü bir baseline model oluştur.
2. **İç temsili gözlemle:** Katman, nöron, aktivasyon ve temsil yapısını incele.
3. **Aday özellikleri belirle:** Aktivasyon istatistikleri, sınıf davranışı ve seçicilik kullan.
4. **Hipotez oluştur:** Aday özellik/devre ile beklenen çıktı etkisi arasında mekanistik hipotez kur.
5. **Müdahale yap:** Ablasyon, activation patching ve kontrollü aktivasyon ölçekleme uygula.
6. **Çıktı değişimini ölç:** Olasılık, logit, L1 etki ve sınıf doğruluğu değişimlerini ölç.
7. **Kontrol et:** Random controls, multi-seed tekrar, Discovery/Holdout ayrımı ve dağılım tabanlı istatistiksel ölçümler kullan.
8. **Sınırları belirt:** Korelasyon, temsil ayrışması ve modelin kendi açıklamalarını tek başına mekanistik kanıt olarak kabul etme.
9. **Mekanizma haritasını çıkar:** Desteklenen bulguları Glass Box computational map içinde ilişkilendir.

## Deney kimliği ve yapı

Araştırmada **12 ana deney** vardır:

- **Week 1:** E01–E05
- **Week 2:** E06–E12

Ana deneylerin alt analizleri `1.1`, `3.1`, `4.1`, `4.2`, `5.1` gibi bölüm numaralarıyla tutulur; bunlar yeni deney ID'si değildir.

## Hafta 1 — MNIST MLP

Baseline model:

- Veri seti: MNIST (`60000` eğitim / `10000` test)
- Mimari: `784 → 128 → 64 → 10`
- Aktivasyon: ReLU
- Optimizer: Adam
- Learning rate: `0.001`
- Batch size: `64`
- Epoch: `5`
- Baseline seed: `42`
- Test accuracy: **97.56%**

Hafta 1'in ana deneyleri E01 baseline, E02 aktivasyon analizi, E03 aday özellik/devre keşfi, E04 ablasyon/devre müdahaleleri ve E05 aktivasyon müdahalesi/yamalama olarak düzenlenmiştir.

### Hafta 1 aday devre

`[47, 17, 57, 53, 28]`

Bu aday grup Class 0 davranışıyla güçlü biçimde ilişkilendirildi ve kontrollü müdahalelerde belirgin çıktı etkileri gözlendi. Bulgular nedensel kanıtı desteklemektedir; ancak aday grubun eksiksiz devre olduğu veya genel nedenselliğin tamamen kanıtlandığı iddia edilmemektedir.

## Hafta 2 — Genelleme ve istatistiksel doğrulama

Hafta 2 deneyleri E06–E12 arasında kaydedilmiştir.

| Deney | Amaç | Sonuç |
|---|---|---|
| **E06** | Multi-seed devre tekrarı | 5/5 seed'de kriter karşılandı; aday etki random control'den çok daha büyük |
| **E07** | Matched Transformer Discovery/Holdout | Discovery ve Holdout'ta adaylar random controls'dan güçlü biçimde ayrıştı |
| **E08** | Graded intervention | Aday 496 için müdahale büyüklüğü–L1 ilişkisi test edildi; sonuç destekleyici ancak sınırlı |
| **E09** | 50 random-control istatistiği | `z=0.854`, `%84` percentile; önceden tanımlı kriter karşılanmadı (**FAIL**) |
| **E10** | Grup müdahalesi ve non-additivity | `joint/individual sum=0.6706`; non-additive kriter karşılandı (**PASS / SUPPORT**) |
| **E11** | True-vs-spurious sentetik test | Normal accuracy `%95.95`, broken accuracy `%80.40`, düşüş `15.55 pp` (**PASS**) |
| **E12** | Local LLM / Llama 3.2 1B | Ollama üzerinde 3 prompt başarıyla çalıştırıldı; davranışsal çıktı mekanistik kanıt olarak kabul edilmedi |

### Bilimsel yorum

Hafta 2'nin amacı her deneyi zorla pozitif sonuca dönüştürmek değildir. Önceden belirlenen kriterlerin uygulanması esas alınmıştır. Bu nedenle E09'un başarısız olması sonuçların gizlenmesi yerine açıkça raporlanmıştır. E10'da non-additive davranış desteklenmiş, E11'de spurious feature kırıldığında performans düşüşü gözlenmiş ve E12'de local LLM çalıştırmasının modelin gerçek iç mekanizmasını tek başına açıklamadığı özellikle belirtilmiştir.

## İstatistiksel ve metodolojik sınırlar

- Korelasyon tek başına nedensellik değildir.
- L1 temsil ayrışması tek başına nedensel kanıt değildir.
- Aday seçiminde Discovery verisi kullanıldığı için Holdout doğrulaması önemlidir.
- Random-control sonuçları kullanılan kontrol sayısı ve örnekleme tasarımına bağlıdır.
- E09'da aday değer önceden tanımlı `|z| >= 2` ve `percentile >= 90` kriterlerini karşılamamıştır.
- E10'daki non-additive etki grup etkileşimini destekler; tek başına belirli bir mekanizmanın eksiksiz olduğunu göstermez.
- E11 sentetik deney davranışsal bir testtir; doğrudan gerçek bir model içi devre keşfi değildir.
- E12'de local LLM'in kendi ürettiği iç-mekanizma açıklamaları mechanistic evidence olarak kabul edilmemiştir.
- Sonuçlar kullanılan küçük/kontrollü modeller ve deney tasarımlarıyla sınırlıdır; daha büyük modellere doğrudan genellenemez.

## Grafikler

`figures/` altında Hafta 1 ve Hafta 2 sonuçlarına ait doğrulanabilir SVG grafikler bulunur. Hafta 2 grafiklerinde E06–E11 ve Week 1 vs Week 2 özeti yer alır. Ayrıntılı deney bağlantıları ve grafik kapsamı `figures/figure_index.md` içinde tutulur.

## Literatür

Literatür matrisi ve deney eşlemesi `notes/literature_table.md` dosyasındadır. Hafta 2 kapsamında yeni kaynaklar eklenmiş ve toplam literatür kapsamı genişletilmiştir.

## Repository yapısı

```text
glass-box-ai-research/
├── README.md
├── requirements.txt
├── notebooks/          # Deneylerin çalıştırıldığı Colab/Jupyter notebookları
├── src/                # Tekrar kullanılabilir model ve yardımcı fonksiyonlar
├── experiments/        # Week 1 ve Week 2 standart deney kayıtları
├── results/            # Sonuç özetleri
├── figures/            # Hafta 1 ve Hafta 2 SVG grafikleri
├── data/               # Veri kullanım politikası; ham veriler commit edilmez
├── papers/             # Literatür dosyaları için ayrılan alan
├── notes/              # Deney günlükleri, literatür ve metodolojik notlar
└── report/             # Week 1/Week 2 raporları, sunumları ve Glass Box map
```

## Tekrar üretilebilirlik

- Deney ID'leri, model ayarları, seed değerleri ve deneysel ölçümler ilgili deney kayıtlarında tutulur.
- Python bağımlılıkları `requirements.txt` içinde tanımlıdır.
- Hugging Face tabanlı deneyler gerekli model/tokenizer dosyalarını çalışma sırasında indirir.
- E12 local LLM deneyi Colab Linux ortamında Ollama ile gerçekleştirilmiştir; Ollama kurulumu için sistem bağımlılıkları notebook içinde belgelenmiştir.
- Ham veri dosyaları repository'ye eklenmez.

## Raporlama materyalleri

- `report/week1_report.md` — Week 1 kısa araştırma raporu
- `report/week2_report.md` — Week 2 kısa araştırma raporu
- `report/week1_presentation.md` — Week 1 sunum planı
- `report/week2_presentation.md` — Week 2 sunum planı
- `report/glass_box_map.md` — güncellenmiş Glass Box computational map
- `results/results_summary.md` — sayısal sonuç özeti
- `figures/figure_index.md` — grafik indeksi
- `notes/literature_table.md` — literatür matrisi
- `notes/mechanism_provenance.md` — gelecek Mechanism Provenance araştırma notu

## Sonraki çalışmalar

Bu repository'deki deneysel aşama tamamlanmıştır. Gelecekteki çalışmalar; daha geniş model ve veri setlerinde doğrulama, daha güçlü random-control tasarımları, distributed feature analysis, genişletilmiş activation patching ve mechanism provenance/lineage çalışmalarını içerebilir. Bu maddeler mevcut sonuç olarak sunulmamaktadır.

## Durum

**Deneysel aşama: TAMAMLANDI.**

Hafta 1 ve Hafta 2 deneyleri, sonuç kayıtları, grafikler, literatür eşlemesi, Glass Box map ve raporlama materyalleri repository içinde belgelenmiştir. Negatif veya kriteri karşılamayan sonuçlar da açıkça raporlanmıştır.
