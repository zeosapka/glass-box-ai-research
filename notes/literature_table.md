# Literatür Tablosu — Glass Box / Mekanistik Yorumlanabilirlik

| # | Kaynak | Problem / Konu | Model / Bağlam | İç Bileşen | Yöntem | Nedensel Müdahale | Glass Box Katkısı | Bu araştırmadaki karşılığı | Sınırlılık / Not |
|---:|---|---|---|---|---|---|---|---|---|
| 1 | *Interpretability in the Wild: a Circuit for IOI in GPT-2 Small* | Devre keşfi | GPT-2 Small | Attention / MLP bileşenleri | Devre analizi | Bileşen düzeyi müdahaleler | Devre düzeyinde mekanizma yeniden kurma | Aday devre keşfi + ablasyon | Büyük dil modeli bağlamı; MNIST MLP'den farklı |
| 2 | *Towards Automated Circuit Discovery for Mechanistic Interpretability* | Devre keşfinin otomasyonu | Sinir ağı / Transformer bağlamı | Model bileşenleri | Otomatik devre araması | Bileşen müdahalesi | Aday devre keşfi metodolojisi | Aşamalı ablasyon + devre adayı | Otomatik keşif kapsamı bu çalışmada sınırlı |
| 3 | *Locating and Editing Factual Associations in GPT* | İçsel olgusal temsiller | GPT | MLP / iç temsiller | Yerelleştirme ve düzenleme | Aktivasyon/temsil düzenleme | İç temsil üzerinde kontrollü müdahale | Aktivasyon müdahalesi / yamalama | Dil modeli özelinde |
| 4 | *Toy Models of Superposition* | Özellikler ve süperpozisyon | Oyuncak sinir ağları | Dağıtık özellikler | Temsil analizi | Kontrollü özellik manipülasyonu | Özelliklerin tek nöron yerine dağıtık olabileceğini gösteren temel çerçeve | Dağıtık temsil / Top-5 yamalama | Oyuncak model sonuçlarının doğrudan MNIST'e genellenmesi sınırlı |
| 5 | *Sparse Autoencoders Find Highly Interpretable Features in Language Models* | Özellik ayrıştırma | Dil modelleri | Aktivasyon temsilleri | SAE | Özellik düzeyi manipülasyon / analiz | Karmaşık aktivasyon uzayından daha ayrışabilir özellik adayları çıkarma | Özellik analizi için ileri yöntem | SAE henüz bu haftanın deneylerine uygulanmadı |
| 6 | *Causal Abstraction: A Theoretical Foundation for Mechanistic Interpretability* | Nedensel doğrulama | Soyut hesaplama modelleri | Mekanistik değişkenler | Nedensel soyutlama | Müdahale | Mekanistik açıklamalar için nedensel çerçeve | Gözlem ve müdahale ayrımı + mekanistik doğrulama | Teorik çerçeve; deneysel uygulama ayrıca gerekir |
| 7 | *Tracr: Compiled Transformers as a Laboratory for Interpretability* | Kontrollü yorumlanabilirlik deneyleri | Derlenmiş Transformerlar | Bilinen hesaplama bileşenleri | Programdan Transformer derleme | Kontrollü müdahaleler | Bilinen hesaplamayı yorumlanabilirlik laboratuvarı olarak kullanma | Küçük ve kontrollü model kullanma yaklaşımı | Transformer odaklı |
| 8 | *Gemma Scope* | Büyük ölçekli özellik analizi | Gemma dil modelleri | Aktivasyon özellikleri | Seyrek otokodlayıcılar / özellik analizi | Özellik düzeyi müdahaleler ve analiz | Büyük ölçekli iç özellik incelemesi | Gelecekte SAE / özellik düzeyi genişleme | Bu haftanın MNIST modelinden çok daha büyük ölçek |
| 9 | *Efficient Automated Circuit Discovery in Transformers using Contextual Decomposition* | Verimli devre keşfi | Transformerlar | Attention / MLP düğümleri ve konumlar | Contextual Decomposition (CD-T) + pruning | Devre altgrafı çıkarımı ve faithfulness testi | Büyük Transformerlar için daha verimli devre keşfi ve faithfulness değerlendirmesi | E07 iç temsil ayrışması ve E10 grup müdahalesi için metodolojik karşılaştırma | Bizim deneyimiz CD-T uygulamıyor; yöntem karşılaştırmasıdır |
| 10 | *Scaling Monosemanticity: Extracting Interpretable Features from Claude 3 Sonnet* | Büyük modelde özellik ayrıştırma | Claude 3 Sonnet | Residual stream / SAE özellikleri | Sparse autoencoder / dictionary learning | Feature steering | Ölçeklenmiş özelliklerin yorumlanabilirliği ve davranışa nedensel etkisinin incelenmesi | E07–E08 aktivasyon müdahalesi ve gelecekte SAE genişlemesi | Büyük üretim modeli; bizim küçük distilgpt2 deneyimizle ölçek farkı vardır |
| 11 | *Formal Mechanistic Interpretability: Automated Circuit Discovery with Provable Guarantees* | Formal devre doğrulaması | Sinir ağları / vision modelleri | Devre altgrafları | Otomatik devre keşfi + neural verification | Robust patching / minimality / domain guarantees | Devre keşfine formel doğrulama ve robustness garantileri ekleme | E06–E10 kontrol ve doğrulama anlayışına ileri yöntem referansı | 2026 çalışması; bu araştırmada formel doğrulama uygulanmamıştır |

## Literatür ↔ Deney Eşlemesi

| Literatür kavramı | Bizim deney | Sonuç / Kullanım |
|---|---|---|
| Aktivasyon Analizi | Deney 2 | `10000 × 64` aktivasyon matrisi, sınıf ortalamaları, seçicilik |
| Nöron Ablasyonu | Deney 3 | N47/N54/N62 sınıfa özgü etkiler |
| Aktivasyon Müdahalesi | Deney 4 | N47/N54 ölçekleme ve çıktı olasılığı değişimi |
| Korelasyon ve Nedensellik | Deney 5 | N17/N47 korelasyonu `0.4485` genel, `0.7846` Sınıf 0; müdahale ile ayrım |
| Aktivasyon Yamalama | Deneyler 10–13 | Aday bilgi aktarımı / logit düzeyi etkisi |
| Devre Keşfi | Deneyler 14–21 | `[47,17,57,53,28]` aday grubu |
| Dağıtık Temsil | Deneyler 9, 11, 18, 20 | Grup etkileri, aşamalı ablasyon ve tekli çıkarma |
| Mekanistik Doğrulama | Deneyler 22–23 | Rastgele kontroller + sınıf bazlı kontroller |
| Özellik Düzeyi Analiz | Deneyler 2–3, 24 | Sınıf 0'a eğilimli aday özellik karakterizasyonu |
| Devre Düzeyi Müdahale | Deney 24 | Gerçek Sınıf 0 olasılığı `0.7644 → 0.9938` |
| Transformer iç temsil ayrışması | E07 | Discovery/Holdout L1 ayrışması ve random kontroller |
| Kademeli müdahale / dose-response | E08 | Aday ve kontrol boyutlarında müdahale büyüklüğü–çıktı değişimi |
| İstatistiksel random-control değerlendirmesi | E09 | 50 kontrol boyutuyla z-score ve empirical percentile |
| Grup müdahalesi / non-additivity | E10 | Birlikte müdahale ile tekil etkilerin toplamının karşılaştırılması |
| Sentetik gerçek-sahte özellik ayrımı | E11 | True-vs-spurious mekanizma ayrımının kontrollü testi |
| Local LLM davranış incelemesi | E12 | Llama 3.2 1B çıktıları; mekanistik kanıt iddiası yok |

## Kaynak Kullanım İlkesi

Kaynaklar rapora aktarılırken orijinal makalelerin iddiaları ile bu çalışmada gerçekten ölçülen sonuçlar birbirinden ayrılacaktır. Literatür, deney sonuçlarını olduğundan daha güçlü göstermenin gerekçesi olarak kullanılmayacaktır.
