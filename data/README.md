# Veri (Data)

Bu klasör, araştırmada kullanılan veri setlerinin kapsamını ve veri kullanım politikasını açıklar.

## Kullanılan veri setleri

- **MNIST:** 1. hafta temel MLP ve aday devre deneylerinin ana veri setidir.
- **Eşleştirilmiş metin verisi:** 2. hafta E07–E10 Transformer iç temsil ve müdahale deneylerinde kullanılan kontrollü cümle kümeleridir.
- **Sentetik true-vs-spurious veri:** E11 deneyinde modelin gerçek özellik ile sahte (spurious) özellik arasındaki bağımlılığını test etmek için çalışma sırasında oluşturulmuştur.
- **Fashion-MNIST:** Bu çalışmada deneysel olarak kullanılmamıştır; gelecekteki doğrulama çalışması olarak planlanmıştır.
- **Local LLM verisi:** E12'de üç kontrollü prompt kullanılmış; harici bir eğitim veri seti repository'ye eklenmemiştir.

## Veri politikası

Ham veri dosyaları repository'ye commit edilmez. Notebooklar gerektiğinde veriyi indirir veya sentetik veriyi çalışma sırasında oluşturur.

Deneylerin tekrar üretilebilirliği için kullanılan veri boyutları, seed değerleri, promptlar ve veri oluşturma parametreleri ilgili deney kayıtlarında belirtilmiştir.

## Klasörün amacı

`data/` klasörü ham veri deposu değildir. Veri kaynaklarının kapsamını ve kullanım kurallarını belgelemek için tutulur. Bu nedenle klasörde yalnızca bu README dosyasının bulunması normaldir.
