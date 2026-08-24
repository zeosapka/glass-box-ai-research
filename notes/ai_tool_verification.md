# Yapay Zekâ Aracı Doğrulama Günlüğü (AI Tool Verification Log)

Bu dosya, araştırma sırasında yapay zekâ araçlarından alınan teknik önerilerin doğrudan doğru kabul edilmemesi ve çalışmaya alınan sonuçların deneysel olarak doğrulanması için tutulur.

## Kural

Yapay zekâ tarafından verilen kod, kavramsal açıklama veya literatür iddiası doğrudan doğru kabul edilmez.

## Doğrulama Yöntemi

1. Kodun çalıştırılması ve hata kontrolü.
2. Kullanılan kütüphane/API davranışlarının ilgili dokümantasyonla kontrol edilmesi.
3. Literatür iddialarının orijinal kaynaklarla karşılaştırılması.
4. Deney çıktılarının notebook kayıtları ve standart deney kayıtlarıyla karşılaştırılması.
5. Sonuç ile yorumun birbirinden ayrılması; modelin kendi açıklamasının mekanistik kanıt sayılmaması.

## Araştırmada uygulanan doğrulama örnekleri

| Aşama | Yapay zekâ desteği | Doğrulama | Sonuç |
|---|---|---|---|
| Week 1 MNIST deneyleri | Kod ve analiz önerileri | Colab'da gerçek çalıştırma + çıktı kontrolü | Sonuçlar deney kayıtlarına işlendi |
| Week 2 Transformer deneyleri | Deney tasarımı ve analiz önerileri | Notebook çıktıları + random controls + discovery/holdout + multi-seed | Pozitif ve negatif sonuçlar ayrı raporlandı |
| E09 istatistiksel kontrol | İstatistiksel hesaplama/yorum önerileri | 50 random control dağılımı, z-score ve empirical percentile hesaplandı | Önceden tanımlanan kriterlere göre FAIL |
| E11 true-vs-spurious | Sentetik veri ve MLP deney tasarımı | Normal test ile spurious-broken test doğrudan karşılaştırıldı | 15.55 pp düşüş gözlendi; kriter PASS |
| E12 local LLM | Ollama kurulum ve test kodu | Colab Linux ortamında Ollama server + `llama3.2:1b` + 3 prompt gerçek çalıştırıldı | Local execution başarılı; mekanistik kanıt iddiası yapılmadı |

## Bilimsel sınır

Bu günlük, yapay zekâ desteğinin araştırma sürecindeki rolünü belgelemek içindir. Deney sonuçlarının kaynağı notebooklarda gerçekleştirilen gerçek çalıştırmalardır; yapay zekânın ürettiği açıklamalar tek başına deneysel kanıt olarak kabul edilmez.
