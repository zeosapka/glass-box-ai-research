# E12 — Local LLM / Ollama

- **Deney ID:** E12
- **Model:** `llama3.2:1b`
- **Çalıştırma ortamı:** Linux / Colab; Ollama local server (`127.0.0.1:11434`).
- **Amaç:** Küçük bir local LLM üzerinde farklı prompt türlerinin çalıştırılabildiğini göstermek ve modelin kendi açıklamalarının gerçek iç mekanizma kanıtı olarak değerlendirilmemesi gerektiğini belgelemek.
- **Prompt sayısı:** `3`.
- **Internal intervention:** Uygulanmadı.
- **Mechanistic evidence:** Elde edilmedi.

## Ortam ve Çalıştırma

- Ollama başlangıçta kurulu değildi.
- `zstd` bağımlılığı kurulduktan sonra Ollama başarıyla kuruldu.
- Ollama server başarıyla başlatıldı.
- `llama3.2:1b` modeli başarıyla indirildi ve çalıştırıldı.

## Promptlar

### P1 — factual

`What is a transformer model in artificial intelligence? Explain briefly.`

Model, Transformer mimarisini NLP görevlerinde kullanılan bir sinir ağı mimarisi olarak açıkladı. Yanıt süresi: **26.55 s**.

### P2 — reasoning

`Why might a language model give different answers to two very similar questions?`

Model; eğitim verisi sınırlılıkları, bağlam, belirsizlik, dilsel varyasyonlar ve sorgu niyeti gibi çeşitli nedenler sundu. Yanıt süresi: **80.12 s**.

### P3 — glass_box

`What kinds of internal information might a language model use when generating an answer?`

Model contextualized embeddings, tokenization, training data ve model parameters gibi çeşitli unsurlardan bahsetti. Yanıt süresi: **105.01 s**.

**Önemli metodolojik not:** P3'teki model öz-açıklaması gerçek iç mekanizmanın doğrudan kanıtı olarak kabul edilmemiştir. Modelin kendi üretmiş olduğu açıklamalar ile gerçek hesaplama mekanizması arasında ayrım yapılmalıdır.

## Glass Box Değerlendirmesi

- Local execution: **True**
- Prompt count: **3**
- Internal intervention: **False**
- Mechanistic evidence: **False**

### Sonuç

Local LLM başarıyla çalıştırılmış ve üç farklı prompt türüne cevap vermiştir. Çıktılar gözlenebilir davranış farklılıklarını göstermektedir; ancak cevapların kendisi modelin gerçek iç mekanizmalarına dair mekanistik kanıt oluşturmaz. Özellikle modelin kendi iç süreçleri hakkında verdiği açıklamalar mekanistik kanıt olarak kullanılmamalıdır.

**Genel E12 değerlendirmesi:** Local LLM demonstration **başarılı**; mekanistik/causal Glass Box kanıtı **elde edilmedi**.
