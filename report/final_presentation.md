# Week 2 Glass Box AI Araştırması — 5–10 Dakikalık Sunum Planı

## Slayt 1 — Araştırma Problemi ve Week 1 → Week 2 Geçişi
- Black Box AI doğru çıktıyı üretir; Glass Box yaklaşımı bu çıktının iç hesaplama mekanizmasını araştırır.
- Ana soru: Model davranışını hangi iç temsil, özellik/boyut ve hesaplama yolu üretiyor?
- **Week 1:** MNIST MLP üzerinde iç temsil → nöron müdahalesi → aday devre → mekanistik doğrulama.
- **Week 2:** Aynı mantık Transformer/LLM bağlamına taşındı; multi-seed, holdout, random controls ve istatistiksel kontroller eklendi.

## Slayt 2 — Week 1 Baseline ve Mekanizma
- MNIST MLP: `784 → 128 → ReLU → 64 → ReLU → 10`
- Seed: 42, Adam, LR `0.001`, batch `64`, `5` epoch.
- Test doğruluğu: **97.56%**.
- Aday devre: **[47, 17, 57, 53, 28]**.
- Aday devre ablasyonu: Sınıf 0 doğruluğu **98.6735% → 86.6327%**, yani **−12.0408 pp**.
- Random kontrol ortalaması: **−0.1122 pp**.
- Sonuç: Week 1, kontrollü müdahale ile aday iç mekanizmanın davranışa katkısını destekledi.

## Slayt 3 — E06: Multi-Seed Replication
- Aynı devre hipotezi **5 farklı seed** üzerinde tekrarlandı.
- `5/5` seed'de aday devre etkisi önceden belirlenen **≤ −5 pp** eşiğini geçti.
- Ortalama aday devre etkisi: **−27.6735 pp**.
- Ortalama random control etkisi: **−0.3469 pp**.
- Ortalama aday/random etki oranı: **61.45×**.
- Başarı kriteri: **PASS**.
- Ancak formal istatistiksel anlamlılık henüz bu deneyde hesaplanmadı.

## Slayt 4 — E07: Discovery → Holdout İç Temsil
- Model: `distilgpt2`, hidden size `768`.
- Aday boyutlar: **[430, 496, 36, 374, 314]**.
- Discovery aday/random L1 oranı: **17.20×**.
- Holdout aday/random L1 oranı: **15.71×**.
- Discovery ve Holdout'ta `20` kontrol boyutunun hiçbiri aday ortalamasını geçmedi.
- Sonuç: **PASS**.
- Kritik sınırlama: L1 ayrışması gözlemsel/iç temsil kanıtıdır; tek başına causal intervention değildir.

## Slayt 5 — E08: Kademeli Müdahale ve E09: İstatistiksel Kontrol
### E08
- Aday boyut: `496`; hedef katman: `layer 5`.
- Aday ortalama L1 çıktı değişimi: **0.023454**.
- Kontrol ortalaması: **0.003923**.
- Aday Spearman: **ρ = 0.9487, p = 0.013847**.
- Sonuç: **PARTIAL / SUPPORT**; kontrollerde de monoton dose-response görüldüğü için özgüllük tek başına gösterilmedi.

### E09
- `50` random control dimension.
- Aday etki: **0.015057**; kontrol ortalaması **0.011293**.
- `z = 0.854322`, empirical percentile **84%**.
- Önceden belirlenen `|z| ≥ 2` ve `percentile ≥ 90%` kriterleri: **FAIL**.
- Bu negatif sonuç korunuyor: deney çalıştı, ancak aday `496` için güçlü istatistiksel ayrışma göstermedi.

## Slayt 6 — E10: Grup Müdahalesi ve E11: True-vs-Spurious
### E10 — Group Intervention
- Aday grup: **[471, 228, 12, 358, 529]**.
- Birlikte etki: **0.033458** L1.
- Tekil etkilerin toplamı: **0.049894**.
- Non-additive difference: **−0.016436**.
- Joint / individual-sum: **0.670583**.
- Random control karşılaştırması: `z = −0.789750`, percentile **20%**.
- Sonuç: Grup etkisinin additif olmadığı desteklendi; random kontrollere göre daha güçlü etki gösterilmedi.

### E11 — Sentetik True-vs-Spurious
- Kontrollü sentetik veri ile gerçek ve sahte ilişkinin ayrıştırılması test edildi.
- Ana ölçüm: **accuracy drop = 15.55 pp**.
- Sonuç: **PASS / SUPPORT**.
- Bu deney, mekanistik yöntemin bilinen gerçek/sahte özellikler arasında ayrım yapıp yapamadığını sınamak için kullanıldı.

## Slayt 7 — E12: Local LLM ve Negatif Kanıt Disiplini
- Yerel model: **Llama 3.2 1B**, Ollama.
- `3` prompt üzerinde davranışsal çıktı karşılaştırması yapıldı.
- E12'nin kaydı, yalnızca çıktı davranışından mekanistik iç yapı çıkarılmaması gerektiğini açıkça koruyor.
- **Mechanistic evidence = False**.
- Sonuç: Local LLM deneyi bir davranışsal/uygulamalı ek deneydir; mekanistik kanıt olarak sunulmamaktadır.

## Slayt 8 — Sonuç, Sınırlılıklar ve Sonraki Adım
- Metodolojik zincir: **İç Temsil → Özellik/Boyut → Müdahale → Tekrar → Random Control → İstatistiksel Doğrulama → Devre → Mekanistik Doğrulama**.
- Week 2, Week 1'deki mekanistik iddiayı daha geniş model bağlamında sınadı; sonuçlar deneyden deneye farklı güçte destek vermektedir.
- Sınırlılıklar:
  1. E08 tek discovery cümlesiyle sınırlı.
  2. E09 istatistiksel ayrışma kriterlerini karşılamadı.
  3. E10 random grup sayısı `5` ile sınırlı.
  4. E12 davranışsal; mekanistik kanıt değil.
  5. Formal doğrulama uygulanmadı.
- Sonraki deneyler:
  1. Daha büyük random-control dağılımları ve bağımsız prompt/holdout setleri.
  2. Çoklu Transformer katmanı ve farklı görevler.
  3. SAE / feature-level decomposition.
  4. Formal circuit verification ve robustness testleri.
  5. Mechanism Provenance / AI Mechanism Lineage: bir modelden diğerine aktarılan özelliklerin gerçek mekanizma mı, yoksa eğitim artifaktı mı olduğunu test etmek.

## Sunum için ana mesaj

> **Week 1'de küçük ve kontrollü bir modelde mekanistik müdahale zinciri kuruldu. Week 2'de bu zincir Transformer/LLM bağlamına taşındı; tekrar üretilebilirlik, holdout ve random-control katmanları eklendi. Sonuçlar bazı hipotezleri desteklerken E09 gibi negatif testler, mekanistik iddiaların sınırlarını açıkça gösterdi.**
