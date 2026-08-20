# Araştırma Deposu Dil Standardı

Bu repository'de araştırma metinleri ve görsel açıklamaları için tek bir dil standardı kullanılır.

## 1. Ana dil

- Başlıklar, açıklamalar, tablolar, deney kayıtları, raporlar ve grafik metinleri **Türkçe** yazılır.
- İngilizce bırakılması gereken özel adlar, model adları, kütüphane adları, standart yöntem adları ve kod sembolleri korunur.

## 2. Teknik terim kuralı

Yerleşik bir teknik terim Türkçede anlam kaybına uğrayacaksa ilk kullanımda:

`Türkçe karşılık (English technical term)`

biçimi kullanılır.

Örnekler:

- iç temsil (internal representation)
- aktivasyon (activation)
- müdahale (intervention)
- nedensel kanıt (causal evidence)
- mekanistik yorumlanabilirlik (mechanistic interpretability)
- aday devre (candidate circuit)
- aktivasyon yamalama (activation patching)
- ileri geçiş kancası (forward hook)

Sonraki kullanımlarda cümle akışını bozmayacak şekilde Türkçe terim kullanılabilir; gerekli olduğunda İngilizce teknik terim parantez içinde korunur.

## 3. Değiştirilmeyecek öğeler

Aşağıdaki öğeler teknik doğruluk ve tekrar üretilebilirlik için çevrilmez:

- Python değişken, fonksiyon ve sınıf adları
- Dosya ve klasör yolları
- Notebook dosya adları
- Model adları (`distilgpt2`, `Gemma` vb.)
- Kütüphane adları (`PyTorch`, `Transformers`, `Hugging Face` vb.)
- API/metot adları (`forward`, `register_forward_hook` vb.)
- Sayısal değerler, tensor şekilleri ve deney ID'leri
- Makale başlıkları ve özel isimler

## 4. Grafik standardı

Grafik başlığı, eksen adı, lejant, açıklama ve dipnotlar Türkçe yazılır. Teknik terim gerektiğinde parantez içinde İngilizce karşılığı verilir.

Örnek:

`Aday Devre Aktivasyon Müdahalesi (Candidate Circuit Activation Intervention)`

`Gerçek Sınıf 0 olasılığı`

`Aktivasyon ölçeği (activation scale)`

## 5. Bilimsel ifade standardı

Aşırı iddialı İngilizce ifadeler doğrudan kullanılmaz.

- `causality proved` → **nedensellik kanıtlandı** ifadesi ancak gerçekten destekleniyorsa kullanılabilir; mevcut çalışmada kullanılmaz.
- `causal evidence/support` → **nedensel kanıtı destekleyen bulgu** / **nedensel kanıt**
- `candidate` → **aday**
- `complete circuit` → **eksiksiz devre**
- `Class-0-biased` → **Sınıf 0'a eğilimli**
- `context-dependent` → **bağlama bağlı**
- `distributed representation` → **dağıtık temsil**

## 6. Kod yorumları

Kodun çalışmasını etkileyen Python sembolleri İngilizce kalır. Açıklama amaçlı yorumlar ve docstring'ler Türkçe yazılır; gerektiğinde teknik İngilizce terim parantez içinde eklenir.

Bu standardın amacı repository'nin ne tamamen İngilizce ne de zoraki biçimde tamamen Türkçe olmasını sağlamak; bilimsel anlamı koruyan, okunabilir ve tutarlı bir Türkçe araştırma dili oluşturmaktır.
