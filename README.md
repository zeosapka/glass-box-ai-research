# Glass Box AI Araştırması

**Mekanistik Yorumlanabilirlik (Mechanistic Interpretability) ve Glass Box AI — 1. Hafta Araştırma Çalışması**

Bu repository (araştırma deposu), ilk hafta araştırma ödevindeki kontrollü MNIST MLP deneylerini, iç temsili (internal representation) analizlerini, müdahale (intervention) sonuçlarını ve aday devre (candidate circuit) doğrulama çalışmalarını kaydetmektedir.

## Araştırma Sorusu

> Model doğru sonucu üretiyor mu? sorusunun ötesinde: **Model bu sonucu hangi iç mekanizma (internal mechanism) üzerinden üretiyor?**

## Ana Metodoloji

`VERİ (DATA) → MODEL → İÇ TEMSİL (INTERNAL REPRESENTATION) → ÖZELLİK (FEATURE) → MÜDAHALE (INTERVENTION) → ÇIKTI (OUTPUT) → DOĞRULAMA (VALIDATION)`

1. **Modeli kur:** Kontrollü MNIST MLP temel modeli (baseline).
2. **İç temsili gözlemle:** Katman (layer), nöron (neuron), aktivasyon (activation) ve temsil öğrenme (representation learning) yapısını incele.
3. **Özellik adaylarını belirle:** Aktivasyon istatistikleri (activation statistics), sınıf davranışı (class behavior) ve seçicilik (selectivity) kullan.
4. **Hipotez oluştur:** Aday özellik/devre (candidate feature/circuit) → beklenen çıktı etkisi.
5. **Müdahale yap:** Ablasyon (ablation), aktivasyon yamalama (activation patching) ve kontrollü aktivasyon ölçekleme (controlled activation scaling).
6. **Çıktı değişimini ölç:** Olasılık (probability), logit ve sınıf doğruluğu (class accuracy) değişimlerini karşılaştır.
7. **Doğrulama yap:** Tekrarlı testler (repeated tests), rastgele kontroller (random controls), sınıf bazlı kontroller (class-wise controls), tekli çıkarma analizi (leave-one-out) ve aşamalı ablasyon (progressive ablation).
8. **Mekanizmayı çıkar:** Aday devre (candidate circuit) ve Glass Box hesaplama haritası (computational map).

## Dil Standardı

Repository'deki başlıklar, deney kayıtları, tablolar, rapor metinleri ve grafik yazıları Türkçe; anlamı korunması gereken teknik terimler ise İngilizce karşılıkları parantez içinde olacak şekilde yazılır. Kod sembolleri, dosya yolları, model/kütüphane adları ve makale başlıkları değiştirilmez. Ayrıntılı kural: `notes/language_standard.md`.

## Temel Model (Baseline)

- Veri seti (dataset): MNIST `60000 / 10000`
- Mimari (architecture): `784 → 128 → 64 → 10`
- Aktivasyon: ReLU
- Optimizasyon algoritması (optimizer): Adam
- Öğrenme oranı (learning rate): `0.001`
- Batch size: `64`
- Epoch: `5`
- Seed (rastgelelik tohumu): `42`
- CPU
- Test doğruluğu (test accuracy): **97.56%**

## Tamamlanan Deneyler

| Çalışma | Durum | Ana sonuç |
|---|---|---|
| Ortam doğrulama (environment) | TAMAMLANDI | PyTorch ortamı çalıştı |
| Temel model (baseline model) | TAMAMLANDI | %97.56 test doğruluğu |
| Aktivasyon analizi (activation analysis) | TAMAMLANDI | `10000 × 64` aktivasyon matrisi |
| Sınıf aktivasyonu / seçicilik (selectivity) | TAMAMLANDI | Aday nöronlar belirlendi |
| Tek nöron ablasyonu (single-neuron ablation) | TAMAMLANDI | Sınıfa özgü etkiler ölçüldü |
| Aktivasyon müdahalesi (activation intervention) | TAMAMLANDI | Kontrollü olasılık değişimleri |
| Korelasyon ve nedensellik | TAMAMLANDI | Gözlem/müdahale ayrımı |
| Aktivasyon yamalama (activation patching) | TAMAMLANDI | Çoklu örnek yamalama yapıldı |
| Dağıtık özellik yamalama (distributed feature patching) | TAMAMLANDI | Top-5 grup etkisi incelendi |
| Aday devre keşfi (candidate circuit discovery) | TAMAMLANDI | `[47,17,57,53,28]` |
| Devre ablasyonu (circuit ablation) | TAMAMLANDI | Sınıf 0 `-12.0408 pp` |
| Tekli çıkarma (leave-one-out) | TAMAMLANDI | Bağlama bağlı katkılar |
| Aşamalı ablasyon (progressive ablation) | TAMAMLANDI | Dağıtık / toplamsal olmayan etki |
| Rastgele kontroller (random controls) | TAMAMLANDI | Rastgele ortalama `-0.1122 pp` |
| Sınıf bazlı doğrulama (class-wise validation) | TAMAMLANDI | En büyük etki Sınıf 0'da |
| Devre aktivasyon müdahalesi | TAMAMLANDI | Gerçek Sınıf 0 olasılığı `0.7644 → 0.9938` |
| Literatür matrisi | TAMAMLANDI | 8 kaynak + deney eşlemesi |
| İleri kavramlar (advanced concepts) | TAMAMLANDI | `notes/advanced_concepts.md` |
| Mekanizma kökeni önerisi (mechanism provenance) | TAMAMLANDI | `notes/mechanism_provenance.md` |
| Grafik indeksi + GitHub SVG'leri | TAMAMLANDI | 11 doğrulanabilir/okunabilir sonuç grafiği |
| Glass Box haritası | TAMAMLANDI | Hesaplama haritası tamamlandı |

## Aday Devre (Candidate Circuit)

`[47, 17, 57, 53, 28]`

Bu grup Sınıf 0 davranışı ile güçlü biçimde ilişkilidir.

### Mekanistik Doğrulama Özeti

- Aday devre ablasyonu: Sınıf 0 doğruluğunda **-12.0408 pp**
- Rastgele kontrol ortalaması: **-0.1122 pp**
- Aday − rastgele ortalama: **-11.9286 pp**
- Sınıf 1 kontrolü: **+0.0881 pp**
- Sınıf 2 kontrolü: **0.0000 pp**
- Tekli çıkarma analizinde en güçlü bağlamsal etki: N57, **-9.0816 pp**
- Aşamalı ablasyon: **-0.9184 → -12.0408 pp**
- Logit düzeyinde yamalama: Sınıf 1 hedefi **+6.0245**, Sınıf 2 hedefi **+4.3068** Sınıf 0 logiti
- Devre aktivasyon müdahalesi: gerçek Sınıf 0 olasılığı **0.7644 → 0.9938**

### Bilimsel Yorum

Bu sonuçlar aday devrenin Sınıf 0 çıktı davranışına güçlü ve kontrollü bir katkısı olduğuna dair **nedensel kanıtı (causal evidence/support)** desteklemektedir. Ancak aday grubun modeldeki eksiksiz devre (complete circuit) olduğu veya genel anlamda nedenselliğin tamamen kanıtlandığı iddia edilmemektedir.

## Bilimsel Sınırlar

- Korelasyon tek başına nedensellik değildir.
- Ağırlık büyüklüğü tek başına nedensel kanıt değildir.
- Seçicilik aday seçimi için kullanılır; nedensel önem değildir.
- Aday devre Sınıf 0'a eğilimlidir fakat yalnızca Sınıf 0'a özgü değildir.
- Aşamalı ablasyon sıralamaya bağlı olabilir.
- Tek eğitim seed'i kullanıldığı için çoklu seed tekrarı (multi-seed replication) gereklidir.
- Aday seçim yanlılığı (candidate selection bias) ve sınırlı yamalama kapsamı vardır.
- Sonuçlar küçük MNIST MLP üzerinde elde edilmiştir; daha büyük modellere doğrudan genellenemez.

## Repository Yapısı

```text
glass-box-ai-research/
├── README.md
├── requirements.txt
├── notebooks/          # Deneylerin çalıştırıldığı Colab/Jupyter notebookları
├── src/                # Tekrar kullanılabilir Python model ve yardımcı fonksiyonları
├── experiments/        # Standart deney kayıtları ve deneylere ait ek dosyalar
├── results/            # Deney sonuçlarının özet kayıtları
├── figures/            # Deneylerden üretilen doğrulanabilir grafikler (11 SVG)
├── data/               # Veri seti ve veri kullanım açıklamaları
├── papers/             # Araştırmada kullanılan/kullanılacak makale kaynakları
├── notes/              # Deney günlüğü, literatür, kavramlar ve araştırma notları
└── report/             # Glass Box hesaplama haritası ve rapor/sunum materyalleri
```

### Klasörlerin Rolü

- **`notebooks/`** — Temel model, aktivasyon analizi, ablasyon ve müdahale deneylerinin Colab/Jupyter kayıtları.
- **`src/`** — Model, hook, değerlendirme (evaluation) ve müdahale gibi tekrar kullanılabilir kodlar.
- **`figures/`** — Deney günlüğünde sayısal olarak doğrulanabilen 11 SVG grafik ve `figure_index.md`.
- **`notes/`** — Deney günlüğü, literatür matrisi, ileri kavramlar, mekanizma kökeni ve deney planı.
- **`results/`** — Sonuçların kısa/özet kayıtları.
- **`report/`** — Glass Box hesaplama haritası ve raporlama materyalleri.
- **`data/`** — MNIST gibi veri setlerinin repo içinde tutulmayan kullanım/açıklama bilgileri.
- **`papers/`** — Literatür dosyaları için ayrılmış alan.
- **`experiments/`** — Standart deney kayıtlarının tutulduğu ana klasördür.

## Grafik Seti

`figures/` klasöründe 11 okunabilir SVG bulunmaktadır. Grafik başlıkları ve eksen açıklamaları da aynı dil standardını kullanır.

1. Ablasyon doğruluğu — tüm aday nöronlar + aday devre
2. Aşamalı devre ablasyonu
3. Aday devre aktivasyon müdahalesi
4. N47 aktivasyon müdahalesi
5. N17–N47 aktivasyon korelasyonu
6. Temel model eğitim kaybı
7. Aday devre aktivasyonunun sınıflar arasındaki dağılımı
8. Sınıf bazlı doğru tahminler
9. En yüksek 10 nöron seçiciliği
10. Tekli çıkarma analizi
11. Aday nöronların Sınıf 0 logitine katkısı

Eksik ham veri noktaları uydurulmamıştır. Bu nedenle bazı grafikler orijinal Colab grafiklerinin doğrulanabilir, daha dar kapsamlı GitHub sürümleridir. Ayrıntılı kapsam `figures/figure_index.md` içinde belirtilmiştir.

## Temel Model Öğrenme Eğrileri

`notebooks/01_baseline_model.ipynb` epoch bazında temel model eğitim sonuçlarını kaydetmektedir. GitHub'daki `baseline_training_loss.svg` yalnızca deney günlüğünde doğrulanmış eğitim-kaybı serisini gösterir; doğrulanmamış doğrulama/test noktaları grafiğe eklenmemiştir.

## Sonraki Deneyler

1. Çoklu seed tekrarı (multi-seed replication)
2. Sentetik gerçek ve sahte ilişki (true-vs-spurious) veri seti
3. Dağıtık özellik analizi
4. Genişletilmiş aktivasyon yamalama
5. Fashion-MNIST doğrulaması
6. AI'dan AI'a mekanizma kökeni / soy zinciri (mechanism provenance / lineage)

## Durum

**Deneysel aşama: TAMAMLANDI.**

Mevcut deney sonuçları, deney günlüğü, literatür eşlemesi, ileri kavram kapsamı, mekanizma kökeni önerisi ve GitHub grafik/sonuç kayıtları tamamlanmıştır. Gelecek deneyler sonuç gibi sunulmamaktadır.
