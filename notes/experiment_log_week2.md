# Week 2 — Ayrıntılı Deney Günlüğü

Bu dosya yalnızca **Week 2 (E06–E12)** deneylerinin günlük/çalıştırma özetini tutar. Standart kayıtların tam yapısı `experiments/week2_experiment_records.md` içindedir.

## E06 — Multi-Seed Circuit Replication
- Seed'ler: `42, 0, 7, 123, 2024`.
- Ortalama aday devre etkisi: **−27.6735 pp**.
- Ortalama random control etkisi: **−0.3469 pp**.
- Aday/random oranı: **61.45×**.
- Kriter: **5/5 seed geçti**.
- Not: Seed 0 aday etkisi `−77.8571 pp` ile belirgin büyüktü; random control grubu adayla `46` ve `47` boyutlarında çakıştı. Bu nedenle bu kontrol bağımsızlık açısından sınırlıdır.
- Statistical significance: Bu deneyde formal z-score/percentile hesaplanmadı.

## E07 — Matched Transformer Internal Representation
- Model: `distilgpt2`, hidden size `768`.
- Veri: 40 eşleştirilmiş cümle; Discovery `20`, Holdout `20`.
- Discovery adaylar: `[430,496,36,374,314]`.
- Discovery aday/control oranı: **17.20×**.
- Holdout aday/control oranı: **15.71×**.
- Her iki sette de `0/20` random control aday ortalamasını geçti.
- Kriter: **PASS**.
- Sınır: L1 ayrışması causal intervention değildir.

## E08 — Graded Transformer Intervention
- Model: `distilgpt2`, hedef katman `5`, hidden size `768`.
- Aday: `496`; kontroller: `[434,161,541,219,408]`.
- Müdahale seviyeleri: `−0.25σ, −0.50σ, −1.00σ, +0.50σ, +1.00σ`.
- Aday ortalama L1: **0.023454**.
- Kontrol ortalama L1: **0.003923**.
- Aday Spearman: `ρ=0.9487`, `p=0.013847`.
- Kontrollerde de aynı monoton ilişki gözlendi.
- Sonuç: **PARTIAL / SUPPORT**.

## E09 — Statistical Control Test
- Aday: `496`.
- Random controls: **50**.
- Aday ortalama L1: **0.015057**.
- Kontrol ortalaması: **0.011293**.
- Kontrol std: **0.004407**.
- z-score: **0.854322**.
- Empirical percentile: **84%**.
- Kriter `|z|≥2` ve percentile `≥90%`: **FAIL**.
- Bilimsel yorum: Deney başarıyla çalıştı; adayın kontrol dağılımından yeterince ayrışmadığını gösterdi.

## E10 — Group Intervention
- Aday grup: `[471,228,12,358,529]`.
- Birlikte grup etkisi: **0.033458** L1.
- Tekil etkilerin toplamı: **0.049894**.
- Non-additive difference: **−0.016436**.
- Joint/individual ratio: **0.670583**.
- 5 random grup ortalaması: **0.051979**, std `0.023452`.
- Candidate vs random z: `−0.789750`, percentile `%20`.
- Sonuç: Random-control üstünlüğü desteklenmedi; **non-additive kriteri PASS / SUPPORT**.

## E11 — Synthetic True-vs-Spurious Feature Test
- Train: `5000`; test: `2000`.
- Temizlenmiş true feature → label accuracy: **100%**.
- Model: MLP `2→16→8→2`, Adam `0.001`, 50 epoch.
- Train accuracy: **96.04%**.
- Normal test accuracy: **95.95%**.
- Spurious-broken accuracy: **80.40%**.
- Accuracy drop: **15.55 pp**.
- Sonuç: **PASS / SUPPORT**.
- Yorum: Spurious feature bozulduğunda performans düşmesi modelin sahte korelasyondan yararlandığını destekliyor.

## E12 — Local LLM / Ollama
- Ortam: Linux, Python `3.13.15`.
- Local server: Ollama API `127.0.0.1:11434`.
- Model: `llama3.2:1b`.
- Prompt sayısı: `3` — factual, reasoning, glass_box.
- Local execution: **True**.
- Internal intervention: **False**.
- Mechanistic evidence: **False**.
- Sonuç: Local LLM çalıştırıldı ve üç promptta çıktı üretildi. Modelin kendi iç mekanizmasına dair self-report açıklamalar mekanistik kanıt olarak kabul edilmedi.

## Week 2 genel günlük sonucu

Week 2'de Week 1'in küçük MNIST devre çalışması; multi-seed, discovery/holdout, graded intervention, geniş random-control dağılımı, grup müdahalesi, sentetik true-vs-spurious testi ve local LLM çalıştırmasıyla genişletildi. Sonuçlar bilinçli olarak karışık raporlandı: E08 **PARTIAL / SUPPORT**, E09 **FAIL**, E10 **PASS / SUPPORT**, E11 **PASS / SUPPORT**, E12 davranışsal/toolbox sonucu.

Tam kriter, verification ve commit alanları: `experiments/week2_experiment_records.md`.
