# Week 2 — Glass Box AI Araştırma Raporu

## 1. Amaç

Week 2, Week 1'deki aday özellik/devre bulgularını daha savunulabilir hale getirmek için multi-seed replikasyonu, eşleştirilmiş discovery/holdout tasarımı, graded intervention, geniş random controls, grup müdahalesi, sentetik true-vs-spurious testi ve local LLM toolbox tamamlamasını ekledi.

## 2. Week 1 → Week 2 geçişi

Week 1'de aday devre `[47,17,57,53,28]` için Class 0 ablasyon etkisi `−12.0408 pp`, random control ortalaması `−0.1122 pp` idi. Week 2'nin temel sorusu, bu tür bulguların seed, veri bölünmesi ve random-control tasarımına ne kadar dayanıklı olduğudur.

## 3. Deneyler

### E06 — Multi-Seed Circuit Replication
- Seed: `42, 0, 7, 123, 2024`.
- Ortalama aday etki: **−27.6735 pp**.
- Ortalama random control: **−0.3469 pp**.
- Aday/random oranı: **61.45×**.
- `5/5` seed kriteri geçti.
- Formal statistical significance bu deneyde hesaplanmadı.

### E07 — Matched Transformer Internal Representation
- Model: `distilgpt2`, hidden size `768`.
- 40 eşleştirilmiş cümle; Discovery `20`, Holdout `20`.
- Adaylar: `[430,496,36,374,314]`.
- Discovery oranı: **17.20×**; Holdout oranı: **15.71×**.
- Her iki sette de `0/20` random control aday ortalamasını geçti.
- Sonuç: **PASS**.
- Sınır: L1 ayrışması causal intervention değildir.

### E08 — Graded Transformer Intervention
- Aday: `496`; hedef layer `5`.
- 5 müdahale seviyesi kullanıldı.
- Aday ortalama L1: **0.023454**; kontroller: **0.003923**.
- Aday Spearman `ρ=0.9487`, `p=0.013847`.
- Aynı monoton ilişki kontrollerde de görüldü.
- Sonuç: **PARTIAL / SUPPORT**.

### E09 — Statistical Control Test
- `50` random control.
- Aday etki: **0.015057**.
- Kontrol ortalaması: **0.011293**, std `0.004407`.
- `z=0.854322`, percentile `%84`.
- Önceden tanımlı `|z|≥2` ve `%90` eşikleri karşılanmadı.
- Sonuç: **FAIL**; bu, deneyin çalışmadığı değil, adayın güçlü istatistiksel ayrışma göstermediği anlamına gelir.

### E10 — Group Intervention
- Aday grup: `[471,228,12,358,529]`.
- Joint effect: **0.033458**.
- Tekil toplam: **0.049894**.
- Non-additive difference: **−0.016436**.
- Joint/individual ratio: **0.670583**.
- Random group mean: **0.051979**; z `−0.789750`; percentile `%20`.
- Random-control üstünlüğü kriteri başarısız; non-additive kriteri **PASS / SUPPORT**.

### E11 — Synthetic True-vs-Spurious Feature
- Train `5000`, test `2000`.
- Train accuracy **96.04%**.
- Normal test **95.95%**.
- Spurious-broken test **80.40%**.
- Accuracy drop **15.55 pp**.
- Sonuç: **PASS / SUPPORT**.

### E12 — Local LLM / Ollama
- Model: **Llama 3.2 1B**.
- Local server ve model kurulumu başarıyla tamamlandı.
- `3` prompt çalıştırıldı: factual, reasoning, glass_box.
- Local execution: `True`.
- Internal intervention: `False`.
- Mechanistic evidence: `False`.
- Sonuç: Toolbox/local execution başarıyla tamamlandı; self-report açıklamalar mekanistik kanıt kabul edilmedi.

## 4. Genel sonuç

Week 2, Week 1'deki mekanistik araştırma zincirine tekrar üretilebilirlik ve istatistiksel kontrol katmanları ekledi. E06 güçlü replikasyon desteği verirken E09, aday Transformer boyutunun random-control dağılımından yeterince ayrışmadığını açıkça gösterdi. E10 non-additive grup davranışını destekledi; E11 kontrollü sentetik ortamda spurious bağımlılığı görünür hale getirdi; E12 ise local LLM toolbox'ını tamamladı.

## 5. Sınırlılıklar

1. E08 ve E10 kontrol sayıları sınırlıdır.
2. E09'un negatif sonucu güçlü mekanistik özgüllük iddiasını sınırlar.
3. E07 L1 ayrışması causal intervention değildir.
4. E12 davranışsal/toolbox deneyidir; mekanistik kanıt değildir.
5. Formal circuit verification uygulanmamıştır.

## 6. Sonraki araştırma

Daha geniş random-control dağılımları, bağımsız prompt/holdout setleri, çoklu Transformer katmanları, SAE/feature decomposition, formal circuit verification ve daha sonra Mechanism Provenance / AI Mechanism Lineage araştırılabilir.

## 7. Veri ve kod

Standart deney kayıtları: `experiments/week2_experiment_records.md`.
Ayrıntılı günlük: `notes/experiment_log_week2.md`.
Grafikler: `figures/week2/`.
