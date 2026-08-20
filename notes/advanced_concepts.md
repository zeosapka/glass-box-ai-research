# İleri Glass Box AI Kavramları

Bu dosya, ödevde istenen ileri kavramları tanım + bu araştırmadaki işlevleri ile kaydeder. Bu haftada uygulanmayan yöntemler uygulanmış deney gibi sunulmaz.

| Kavram | Kısa anlam | Glass Box içindeki rol | Bu çalışmadaki durum |
|---|---|---|---|
| XAI (Açıklanabilir Yapay Zekâ) | İnsan tarafından anlaşılır açıklama üretme yaklaşımı | Model davranışını açıklamaya yardımcı olur; gerçek iç mekanizma (internal mechanism) ile aynı şey değildir | Kavramsal |
| Yorumlanabilirlik (Interpretability) | Modelin iç işlemlerini/temsilini inceleyebilme | İç temsilin (internal representation) incelenmesini sağlar | Uygulandı |
| Mekanistik Yorumlanabilirlik (Mechanistic Interpretability) | Belirli iç hesaplama/mekanizmayı yeniden kurup müdahale ile test etme | Bu araştırmanın ana hedefidir | Uygulandı |
| Özellik Görselleştirme (Feature Visualization) | Bir özelliğin hangi girdi örüntülerine tepki verdiğini inceleme | Aday özellik yorumunda kullanılır | Kavramsal + aktivasyon analizi |
| Aktivasyon Yamalama (Activation Patching) | Bir koşuldaki aktivasyonu başka koşula taşıyarak etkisini test etme | İç bilgi aktarımını test eder | Uygulandı |
| Katkı Yamalama (Attribution Patching) | İç bileşenlerin katkısını tahmin ederek adayları önceliklendirme | Büyük mekanizma aramasında aday sıralaması sağlar | Kavramsal; bu hafta ayrı yöntem olarak uygulanmadı |
| Nedensel İzleme (Causal Tracing) | Çıktı etkisinin iç yol boyunca izlenmesi | Aday devrenin hangi yol üzerinden etki ettiğini araştırır | Kavramsal; devre keşfi ile ilişkilendirildi |
| SAE (Sparse Autoencoder / Seyrek Otokodlayıcı) | Aktivasyon uzayını daha ayrışabilir/seyrek özelliklere dönüştürme | Dağıtık/örtüşen temsil analizini genişletir | Literatür düzeyi; uygulanmadı |
| Devre Keşfi (Circuit Discovery) | Birlikte çalışan özellik/nöron/bileşen gruplarını keşfetme | Aday mekanizmayı yeniden kurma | Uygulandı |
| Temsil Öğrenme (Representation Learning) | Modelin kullanışlı iç temsiller öğrenmesi | İç temsilin nasıl oluştuğunu anlamak için temel kavram | Uygulandı/analiz edildi |
| Aktivasyon Yönlendirme (Activation Steering) | Aktivasyonu kontrollü değiştirerek davranışı yönlendirme | Aday özellik/devrenin davranış katkısını test eder | Kontrollü aktivasyon ölçekleme ile uygulandı |
| Ablasyon (Ablation) | Bir bileşeni kapatıp çıktı değişimini ölçme | Nedensel kanıt üretmek için temel müdahale | Uygulandı |

## Metodolojik Ayrım

Gözlem (observation; aktivasyon/seçicilik) aday üretir. Müdahale (intervention; ablasyon, ölçekleme, yamalama) kontrollü kanıt üretir. Tekrarlı testler ve kontroller, nedensel yorumun gücünü artırır. Bu nedenle bu araştırmada “causality proved” yerine “causal evidence/support” kullanılır.

## Gemma / Gemma Scope / Tracr

- **Gemma:** Büyük dil modellerinin iç mekanizmalarının araştırılabileceği modern model ailesi bağlamıdır.
- **Gemma Scope:** Gemma aktivasyonlarını özellik düzeyinde incelemek için SAE tabanlı büyük ölçekli bir araştırma yaklaşımıdır.
- **Tracr:** Bilinen programları Transformer hesaplamasına derleyerek kontrollü yorumlanabilirlik laboratuvarı oluşturma yaklaşımıdır.

Bu üçü bu haftaki MNIST MLP deneyinde doğrudan çalıştırılmamış, literatür ve gelecek metodoloji bağlamında tutulmuştur.
