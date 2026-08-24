# Transformer Ön Çalışma — İç Temsil ve Kontrollü Müdahale

> **Arşiv / ön çalışma kaydı.** Bu dosya Week 2'nin nihai E07–E10 kayıtlarının yerine geçmez. İlk Transformer keşif denemesini ve 471 numaralı boyut üzerindeki erken müdahale sonuçlarını tarihsel olarak korur.

## Neden ayrı tutuluyor?

Bu çalışma, Week 2'deki daha kontrollü Transformer deneylerinin öncesindeki keşif aşamasıdır. İlk denemede 16 cümlelik keşif verisi, `distilgpt2` ve 768 boyutlu son Transformer bloğu kullanılmış; 471 numaralı boyut aday olarak seçilmiş ve 20 rastgele boyutla karşılaştırılmıştır.

İlk sonuçta 471'in ortalama L1 etkisi `0.013924`, 20 rastgele kontrolün ortalaması `0.014971` olmuş; 471 test edilen 21 boyut içinde 10. sırada kalmış ve 9 kontrol 471'den daha büyük etki üretmiştir. Bu nedenle 471 için özel/benzersiz nedensel rol iddiası desteklenmemiştir.

## Metodolojik önemi

Bu ön çalışma şu problemi ortaya koymuştur:

`Temsil ayrışması → müdahale etkisi → rastgele kontrol → bağımsız doğrulama ihtiyacı`

Dolayısıyla sonraki Week 2 deneyleri daha kontrollü tasarlanmıştır:

- eşleştirilmiş veri,
- discovery/holdout ayrımı,
- çoklu seed,
- daha geniş random-control dağılımı,
- kademeli müdahale,
- grup müdahalesi ve non-additivity analizi.

## Nihai Week 2 kayıtları

Bu ön çalışmanın güncel ve standart sonuçları için:

- `experiments/week2_experiment_records.md`
- `notes/experiment_index.md`
- `results/results_summary.md`

dosyalarına bakılmalıdır.

**Not:** Eski notebook numarasıyla başlayan dosya adı bilinçli olarak kaldırılmıştır; böylece `notebooks/05_...` adlandırmasıyla karışıklık oluşmaz.
