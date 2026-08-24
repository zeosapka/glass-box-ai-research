# Literatür Tablosu — Glass Box / Mekanistik Yorumlanabilirlik

| # | Kaynak | Problem / Konu | Model / Bağlam | İç Bileşen | Yöntem | Nedensel Müdahale | Glass Box Katkısı | Bu araştırmadaki karşılığı | Sınırlılık / Not |
|---:|---|---|---|---|---|---|---|---|---|
| 1 | *Interpretability in the Wild: a Circuit for IOI in GPT-2 Small* | Devre keşfi | GPT-2 Small | Attention / MLP bileşenleri | Devre analizi | Bileşen düzeyi müdahaleler | Devre düzeyinde mekanizma yeniden kurma | Week 1 **E03–E04** aday devre, ablasyon ve kontrol mantığı | Büyük dil modeli bağlamı; MNIST MLP'den farklı |
| 2 | *Towards Automated Circuit Discovery for Mechanistic Interpretability* | Devre keşfinin otomasyonu | Sinir ağı / Transformer bağlamı | Model bileşenleri | Otomatik devre araması | Bileşen müdahalesi | Aday devre keşfi metodolojisi | Week 1 **E03–E04**; Week 2 **E06** devre tekrarı | Otomatik keşif kapsamı bu çalışmada sınırlı |
| 3 | *Locating and Editing Factual Associations in GPT* | İçsel olgusal temsiller | GPT | MLP / iç temsiller | Yerelleştirme ve düzenleme | Aktivasyon/temsil düzenleme | İç temsil üzerinde kontrollü müdahale | Week 1 **E05** aktivasyon müdahalesi ve yamalama | Dil modeli özelinde |
| 4 | *Toy Models of Superposition* | Özellikler ve süperpozisyon | Oyuncak sinir ağları | Dağıtık özellikler | Temsil analizi | Kontrollü özellik manipülasyonu | Özelliklerin tek nöron yerine dağıtık olabileceğini gösteren temel çerçeve | Week 1 **E04–E05**; grup etkisi, progressive ablation ve distributed patching | Oyuncak model sonuçlarının doğrudan MNIST'e genellenmesi sınırlı |
| 5 | *Sparse Autoencoders Find Highly Interpretable Features in Language Models* | Özellik ayrıştırma | Dil modelleri | Aktivasyon temsilleri | SAE | Özellik düzeyi manipülasyon / analiz | Karmaşık aktivasyon uzayından daha ayrışabilir özellik adayları çıkarma | Week 2 için ileri yöntem; mevcut **E07–E08** SAE uygulamıyor | SAE henüz bu haftanın deneylerine uygulanmadı |
| 6 | *Causal Abstraction: A Theoretical Foundation for Mechanistic Interpretability* | Nedensel doğrulama | Soyut hesaplama modelleri | Mekanistik değişkenler | Nedensel soyutlama | Müdahale | Mekanistik açıklamalar için nedensel çerçeve | Week 1 **E04–E05** ve Week 2 **E08/E10** müdahale-kontrol zinciri | Teorik çerçeve; deneysel uygulama ayrıca gerekir |
| 7 | *Tracr: Compiled Transformers as a Laboratory for Interpretability* | Kontrollü yorumlanabilirlik deneyleri | Derlenmiş Transformerlar | Bilinen hesaplama bileşenleri | Programdan Transformer derleme | Kontrollü müdahaleler | Bilinen hesaplamayı yorumlanabilirlik laboratuvarı olarak kullanma | Küçük/kontrollü model kullanımı için metodolojik referans | Transformer odaklı |
| 8 | *Gemma Scope* | Büyük ölçekli özellik analizi | Gemma dil modelleri | Aktivasyon özellikleri | Seyrek otokodlayıcılar / özellik analizi | Özellik düzeyi müdahaleler ve analiz | Büyük ölçekli iç özellik incelemesi | Week 2 **E07–E08** için gelecekte SAE genişlemesi | Bu haftanın distilgpt2 deneyinden çok daha büyük ölçek |
| 9 | *Efficient Automated Circuit Discovery in Transformers using Contextual Decomposition* | Verimli devre keşfi | Transformerlar | Attention / MLP düğümleri ve konumlar | Contextual Decomposition (CD-T) + pruning | Devre altgrafı çıkarımı ve faithfulness testi | Büyük Transformerlar için daha verimli devre keşfi ve faithfulness değerlendirmesi | Week 2 **E07/E10** için metodolojik karşılaştırma | Bizim deneyimiz CD-T uygulamıyor; yöntem karşılaştırmasıdır |
| 10 | *Scaling Monosemanticity: Extracting Interpretable Features from Claude 3 Sonnet* | Büyük modelde özellik ayrıştırma | Claude 3 Sonnet | Residual stream / SAE özellikleri | Sparse autoencoder / dictionary learning | Feature steering | Ölçeklenmiş özelliklerin yorumlanabilirliği ve davranışa nedensel etkisinin incelenmesi | Week 2 **E08** müdahale yaklaşımı ve gelecekte SAE/feature steering genişlemesi | Büyük üretim modeli; bizim distilgpt2 deneyimizle ölçek farkı vardır |
| 11 | *Formal Mechanistic Interpretability: Automated Circuit Discovery with Provable Guarantees* | Formal devre doğrulaması | Sinir ağları / vision modelleri | Devre altgrafları | Otomatik devre keşfi + neural verification | Robust patching / minimality / domain guarantees | Devre keşfine formel doğrulama ve robustness garantileri ekleme | Week 2 **E06–E10** kontrol/doğrulama mantığı için ileri yöntem referansı | Bu araştırmada formel doğrulama uygulanmamıştır |

## Literatür ↔ Deney Eşlemesi

| Literatür kavramı | Bizim deney | Sonuç / Kullanım |
|---|---|---|
| Aktivasyon Analizi | **Week 1 E02–E03** | `10000 × 64` aktivasyon matrisi, sınıf ortalamaları, seçicilik |
| Nöron Ablasyonu | **Week 1 E04** | N47/N54/N62 sınıfa özgü etkiler |
| Aktivasyon Müdahalesi | **Week 1 E05** | N47/N54/N17 ölçekleme ve çıktı olasılığı değişimi |
| Korelasyon ve Nedensellik | **Week 1 E03** | N17/N47 korelasyonu `0.4485` genel, `0.7846` Sınıf 0; müdahale ile ayrım |
| Aktivasyon Yamalama | **Week 1 E05** | Tekli/grup yamalama ve logit düzeyi etkiler |
| Dağıtık Temsil | **Week 1 E04–E05** | Progressive ablation ve Top-1/3/5 patching |
| Devre Keşfi | **Week 1 E03–E04; Week 2 E06** | Aday devre, birlikte ablasyon, tekli çıkarma, random controls ve multi-seed tekrar |
| Mekanistik Doğrulama | **Week 1 E04; Week 2 E06/E09** | Sınıf bazlı kontroller, random controls, tekrar ve istatistiksel kontrol |
| Transformer iç temsil ayrışması | **Week 2 E07** | Discovery/Holdout L1 ayrışması ve 20 random control |
| Kademeli müdahale / dose-response | **Week 2 E08** | Aday ve kontrol boyutlarında müdahale büyüklüğü–çıktı değişimi |
| İstatistiksel random-control değerlendirmesi | **Week 2 E09** | 50 kontrol boyutuyla z-score ve empirical percentile |
| Grup müdahalesi / non-additivity | **Week 2 E10** | Birlikte müdahale ile tekil etkilerin toplamının karşılaştırılması |
| Sentetik gerçek-sahte özellik ayrımı | **Week 2 E11** | True-vs-spurious mekanizma ayrımının kontrollü testi |
| Local LLM davranış incelemesi | **Week 2 E12** | Llama 3.2 1B çıktıları; mekanistik kanıt iddiası yok |

## Kaynak Kullanım İlkesi

Kaynaklar rapora aktarılırken orijinal makalelerin iddiaları ile bu çalışmada gerçekten ölçülen sonuçlar birbirinden ayrılacaktır. Literatür, deney sonuçlarını olduğundan daha güçlü göstermenin gerekçesi olarak kullanılmayacaktır.
