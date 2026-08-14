# Advanced Glass Box AI Concepts

Bu dosya, ödevde istenen ileri kavramları tanım + bu araştırmadaki işlevleri ile kaydeder. Bu haftada uygulanmayan yöntemler uygulanmış deney gibi sunulmaz.

| Kavram | Kısa anlam | Glass Box içindeki rol | Bu çalışmadaki durum |
|---|---|---|---|
| XAI | İnsan tarafından anlaşılır açıklama üretme yaklaşımı | Model davranışını açıklamaya yardımcı olur; gerçek internal mechanism ile aynı şey değildir | Kavramsal |
| Interpretability | Modelin iç işlemlerini/temsilini inceleyebilme | Internal representation'ın incelenmesini sağlar | Uygulandı |
| Mechanistic Interpretability | Belirli internal computation/mechanism'i yeniden kurup müdahale ile test etme | Bu araştırmanın ana hedefidir | Uygulandı |
| Feature Visualization | Bir feature'ın hangi input pattern'lerine tepki verdiğini inceleme | Candidate feature yorumu için kullanılır | Kavramsal + activation analysis |
| Activation Patching | Bir koşuldaki activation'ı başka koşula taşıyarak etkisini test etme | Internal information transferini test eder | Uygulandı |
| Attribution Patching | İç bileşenlerin katkısını tahmin ederek adayları önceliklendirme | Büyük mekanizma aramasında candidate ranking sağlar | Kavramsal; bu hafta ayrı yöntem olarak uygulanmadı |
| Causal Tracing | Output etkisinin internal pathway boyunca izlenmesi | Candidate circuit'in hangi yol üzerinden etki ettiğini araştırır | Kavramsal; circuit discovery ile ilişkilendirildi |
| SAE | Activation space'i daha ayrışabilir/sparse feature'lara dönüştürmek için sparse autoencoder | Distributed/overlapping representation analizini genişletir | Literatür düzeyi; uygulanmadı |
| Circuit Discovery | Birlikte çalışan feature/neuron/component gruplarını keşfetme | Candidate mechanism reconstruction | Uygulandı |
| Representation Learning | Modelin useful internal representations öğrenmesi | Internal representation'ın nasıl oluştuğunu anlamak için temel kavram | Uygulandı/analiz edildi |
| Activation Steering | Activation'ı kontrollü değiştirerek davranışı yönlendirme | Candidate feature/circuit davranış katkısını test eder | Controlled activation scaling ile uygulandı |
| Ablation | Component'i kapatıp output değişimini ölçme | Causal evidence üretmek için temel intervention | Uygulandı |

## Methodological distinction

Observation (activation/selectivity) candidate üretir. Intervention (ablation, scaling, patching) controlled evidence üretir. Repeated tests ve controls, causal interpretation'ın gücünü artırır. Bu nedenle bu araştırmada “causality proved” yerine “causal evidence/support” kullanılır.

## Gemma / Gemma Scope / Tracr

- **Gemma:** büyük language-model iç mekanizmalarının araştırılabileceği modern model ailesi bağlamıdır.
- **Gemma Scope:** Gemma activation'larını feature düzeyinde incelemek için SAE tabanlı büyük ölçekli bir araştırma yaklaşımıdır.
- **Tracr:** bilinen programları transformer hesaplamasına derleyerek kontrollü interpretability laboratuvarı oluşturma yaklaşımıdır.

Bu üçü bu haftaki MNIST MLP deneyinde doğrudan çalıştırılmamış, literatür ve gelecek metodoloji bağlamında tutulmuştur.
