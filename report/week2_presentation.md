# Week 2 Glass Box AI Araştırması — 5–10 Dakikalık Sunum Planı

## Slayt 1 — Araştırma Problemi ve Week 1 → Week 2 Geçişi
- Glass Box yaklaşımı modelin iç hesaplama mekanizmasını araştırır.
- Week 1: MNIST MLP üzerinde iç temsil → nöron müdahalesi → aday devre.
- Week 2: Transformer/LLM bağlamına geçiş; multi-seed, holdout, random controls ve istatistiksel kontroller.

## Slayt 2 — Week 1 Baseline ve Mekanizma
- MNIST MLP: `784 → 128 → ReLU → 64 → ReLU → 10`.
- Seed 42; Adam; LR `0.001`; batch `64`; 5 epoch.
- Test accuracy: **97.56%**.
- Aday devre: `[47,17,57,53,28]`.
- Aday devre ablasyonu: **−12.0408 pp** Class 0.
- Random control ortalaması: **−0.1122 pp**.

## Slayt 3 — E06: Multi-Seed Replication
- 5 seed: `42, 0, 7, 123, 2024`.
- Ortalama aday: **−27.6735 pp**.
- Ortalama random: **−0.3469 pp**.
- Aday/random: **61.45×**.
- Kriter: **5/5 geçti**.
- Formal statistical significance: bu deneyde hesaplanmadı.

## Slayt 4 — E07: Discovery → Holdout
- Model: `distilgpt2`, hidden size `768`.
- Adaylar: `[430,496,36,374,314]`.
- Discovery oranı: **17.20×**.
- Holdout oranı: **15.71×**.
- `0/20` random control her iki sette de aday ortalamasını geçti.
- Sonuç: **PASS**.
- L1 ayrışması tek başına causal intervention değildir.

## Slayt 5 — E08 + E09
### E08
- Aday `496`; 5 graded intervention seviyesi.
- Aday L1: **0.023454**; kontrol ortalaması **0.003923**.
- Spearman `ρ=0.9487`, `p=0.013847`.
- Kontrollerde de monoton ilişki görüldü.
- **PARTIAL / SUPPORT**.

### E09
- `50` random control.
- Aday `0.015057`; kontrol ortalaması `0.011293`.
- `z=0.854322`; percentile `%84`.
- `|z|≥2` ve `%90` kriterleri: **FAIL**.

## Slayt 6 — E10 + E11
### E10
- Aday grup `[471,228,12,358,529]`.
- Joint `0.033458`; individual sum `0.049894`.
- Non-additive difference `−0.016436`.
- Ratio `0.670583`.
- Random z `−0.789750`, percentile `%20`.
- **PASS / SUPPORT** yalnızca non-additive kriteri için.

### E11
- Normal test: **95.95%**.
- Spurious-broken: **80.40%**.
- Drop: **15.55 pp**.
- **PASS / SUPPORT**.

## Slayt 7 — E12: Local LLM
- Ollama + **Llama 3.2 1B**.
- 3 prompt: factual, reasoning, glass_box.
- Local execution: **True**.
- Mechanistic evidence: **False**.
- Self-report açıklamalar mekanistik kanıt olarak kabul edilmedi.

## Slayt 8 — Sonuç, Sınırlılıklar ve Sonraki Adım
- Zincir: **İç Temsil → Özellik/Boyut → Müdahale → Tekrar → Random Control → İstatistiksel Doğrulama**.
- E09 gibi negatif sonuçlar iddiaların sınırlarını belirledi.
- Sınırlılıklar: sınırlı control sayıları, E07'nin causal olmaması, E12'nin davranışsal olması, formal verification uygulanmaması.
- Sonraki çalışmalar: daha geniş controls, bağımsız holdout/prompt setleri, çoklu Transformer katmanları, SAE, formal circuit verification, Mechanism Provenance.

## Ana mesaj

> Week 1'de küçük ve kontrollü bir modelde mekanistik müdahale zinciri kuruldu. Week 2'de bu zincir Transformer/LLM bağlamına taşındı; tekrar üretilebilirlik, holdout ve random-control katmanları eklendi. Pozitif ve negatif sonuçlar birlikte raporlanarak mekanistik iddiaların sınırları açıkça gösterildi.
