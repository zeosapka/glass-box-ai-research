# Hugging Face Transformer – İç Temsil ve Müdahale Deneyi

## 1. Deneyin amacı

Bu deneyin amacı, açık kaynak bir Transformer modelinin (distilgpt2) içindeki sayısal temsilleri incelemek ve gözlenen bir iç boyutun model çıktısı üzerinde özel bir etkisi olup olmadığını kontrollü müdahale ile araştırmaktır.

Temel araştırma sorusu:

> Modelin iç temsilinde farklılaşan bir boyut, çıktının oluşumunda gerçekten özel bir nedensel role sahip mi?

Buradaki temel ilke:

**Gözlem ≠ nedensellik.**

Bir boyutun farklı cümle gruplarında farklı değerler alması, tek başına o boyutun nedensel bir özellik olduğunu göstermez. Bunun için kontrollü müdahale (intervention) ve kontrol deneyleri gerekir.

---

## 2. Kullanılan model

- Model: `distilgpt2`
- Kütüphane: Hugging Face Transformers
- Gizli temsil boyutu: 768
- Kullanılan görev: Bir metin verildiğinde sonraki token için olasılık dağılımı üretme
- İç durum: Transformer bloklarının ürettiği gizli temsiller

Deneyde son Transformer bloğunun çıktısı incelenmiştir.

---

## 3. Temsil analizi

16 cümleden oluşan kontrollü bir veri kümesi kullanılmıştır:

- Elektrik mühendisliği
- Transformatör
- Motor
- Bilgisayar

Her cümlenin son token konumundaki son gizli temsili alınarak **16 × 768** boyutunda bir temsil matrisi oluşturulmuştur.

İlk aşamada boyutların gruplar arasında ne kadar değiştiği incelenmiştir.

Daha sonra grup içi değişim ile gruplar arası ayrımı birlikte değerlendiren bir oran kullanılmıştır. Bu analiz sonucunda bazı boyutlar aday özellik olarak seçilmiştir.

---

## 4. Aday boyut: 471

Boyut 471, dört grup arasındaki ayrımının grup içi değişimine göre yüksek olması nedeniyle deneysel aday olarak seçilmiştir.

Ancak bu seçim yalnızca **aday özellik** oluşturur. Henüz nedensel bir özellik olduğu kabul edilmemiştir.

Bu ayrım araştırma açısından önemlidir:

**Temsil içinde ayrışma → aday özellik**

**Kontrollü müdahale → nedensel kanıt arayışı**

---

## 5. Müdahale deneyi

Boyut 471'in son Transformer bloğundaki çıktısı sıfırlanmıştır.

Normal çalışmada:

`girdi → Transformer → iç temsil → çıktı olasılıkları`

Müdahalede:

`girdi → Transformer → boyut 471 = 0 → çıktı olasılıkları`

Normal ve müdahale edilmiş çıktı dağılımları karşılaştırılmıştır.

Karşılaştırmada özellikle:

- L1 dağılım değişimi
- En yüksek token olasılığındaki değişim
- En yüksek olasılıklı tokenın değişip değişmediği

incelenmiştir.

Elektrik mühendisliği grubunda bazı örneklerde daha belirgin değişimler görülmüş, bir örnekte en yüksek olasılıklı token da değişmiştir. Bu sonuç, 471 boyutunun araştırmaya değer olduğunu gösteren bir **müdahale etkisi** sağlamıştır; ancak tek başına nedenselliği kanıtlamamıştır.

---

## 6. Rastgele kontrol deneyi

Müdahalenin etkisinin gerçekten 471 boyutuna özgü olup olmadığını test etmek için 471 dışında rastgele boyutlar seçilmiştir.

Önce 655 numaralı rastgele kontrol boyutu kullanılmıştır. Daha sonra 471 dışındaki 20 farklı rastgele boyut ile aynı sıfırlama işlemi tekrarlanmıştır.

Amaç:

> 471 boyutunun etkisi, modelde rastgele seçilmiş başka boyutların etkisinden belirgin biçimde daha büyük mü?

---

## 7. Rastgele kontrollerin sonucu

471 boyutunun ortalama L1 değişimi:

**0.013924**

20 rastgele kontrolün ortalama L1 değişimi:

**0.014971**

Rastgele kontrollerin medyanı:

**0.011681**

471 boyutunun sıralaması:

**21 test edilmiş boyut arasında 10. sıra**

Bu sonuç 471 boyutunu rastgele kontrollerden açık biçimde ayırmamaktadır. 471, test edilen kontrol dağılımının yaklaşık **%55'lik dilimindedir**.

Dolayısıyla mevcut deney:

> **471 boyutunun özel bir nedensel özellik olduğunu desteklemek için yeterli kanıt sağlamamıştır.**

Bu, deneyin başarısız olduğu anlamına gelmez. Tam tersine, araştırma açısından önemli bir sonuçtur: İlk gözlemden hareketle nedensel yorum yapmanın güvenilir olmadığını göstermiştir.

---

## 8. Bilimsel yorum

Bu deneyin en önemli sonucu şudur:

**Bir iç boyutun gruplar arasında farklı davranması, o boyutun model mekanizmasında özel bir nedensel role sahip olduğunu göstermez.**

Araştırma akışı şu şekilde korunmalıdır:

`İç temsil → Gözlem → Aday özellik → Müdahale → Kontrol → Çıktı değişimi → Tekrarlı doğrulama`

Bu nedenle 471 boyutu şu aşamada:

- Nedensel özellik: **Hayır, gösterilmedi**
- Araştırmaya değer aday: **Evet**
- Müdahale etkisi gözlendi mi?: **Evet**
- Rastgele kontrollerden belirgin biçimde ayrıldı mı?: **Hayır**

---

## 9. Deneyin sınırlılıkları

### 9.1 Veri kümesi eşleşmesi

Kullanılan 16 cümle tam anlamıyla eşleştirilmiş değildir. Örneğin farklı gruplar farklı başlangıç kalıpları kullanmaktadır. Bu durum sözdizimi, tokenizasyon ve bağlam farklarının iç temsile yansımasına neden olabilir.

### 9.2 Aday seçimi ve test aynı veri üzerinde

471 boyutu aynı 16 örnek üzerinden hem aday olarak seçilmiş hem de müdahale edilerek test edilmiştir. Bu durum seçim yanlılığı oluşturabilir.

### 9.3 Müdahale büyüklüğü

Bir boyutu doğrudan sıfırlamak güçlü bir müdahaledir. Daha doğal değerlerden kontrollü miktarlarda azaltma/artırma deneyleri daha güçlü bir test sağlayabilir.

### 9.4 Kontrol sayısı

20 rastgele kontrol yararlı bir ilk kontrol oluşturmaktadır; ancak daha güçlü istatistiksel değerlendirme için daha geniş ve sistematik kontrol dağılımları kullanılabilir.

### 9.5 Boyut tek başına özellik olmayabilir

Bir anlamın tek bir boyutta değil, birden fazla boyutun birlikte oluşturduğu dağıtık bir temsil içinde bulunması mümkündür. Bu nedenle tek boyut analizi gerçek mekanizmayı kaçırabilir.

---

## 10. Sonraki deney için metodolojik gereklilik

Bir sonraki aşamada daha iyi eşleştirilmiş cümleler kullanılmalıdır.

Örneğin aynı cümle kalıbı korunarak yalnızca hedef kavram değiştirilmelidir. Böylece sözdizimi ve genel cümle yapısından kaynaklanan farklar azaltılabilir.

Ayrıca:

1. Aday boyut eğitim/keşif verisinde seçilmeli.
2. Müdahale ayrı bir test kümesinde uygulanmalı.
3. Birden fazla müdahale büyüklüğü denenmeli.
4. Çok sayıda rastgele kontrol kullanılmalı.
5. Sonuçlar tekrarlanmalı.
6. Gerekirse tek boyut yerine boyut grupları incelenmeli.

---

## 11. Deneyin Glass Box araştırmasındaki yeri

Bu deney, Black Box modelin iç kısmını açarak şu zinciri uygulamaktadır:

**Model → İç Temsil → Aday Özellik → Müdahale → Çıktı Değişimi → Kontrol → Nedensel Kanıt Arayışı**

Henüz bir mekanizmanın veya devrenin (circuit) keşfedildiği söylenemez.

Ancak deney, gelecekteki **özellik keşfi (feature discovery)**, **devre keşfi (circuit discovery)** ve **nedensel doğrulama (causal validation)** çalışmalarının temel metodolojisini uygulamaktadır.

---

## 12. Sonuç

Bu deneyin sonucu “471 boyutu modelin özelliğidir” değildir.

Daha doğru bilimsel sonuç:

> 471 boyutu temsil analizi sonucunda aday olarak belirlenmiş, sıfırlama müdahalesiyle çıktı üzerinde ölçülebilir değişiklik oluşturmuştur. Ancak 20 rastgele kontrol boyutuyla yapılan karşılaştırmada etkisi belirgin biçimde özel değildir. Bu nedenle 471 boyutunun belirli bir nedensel özellik olduğu sonucuna varmak için yeterli kanıt bulunmamaktadır.

Bu sonuç, **korelasyon ile nedenselliğin ayrılması** açısından deneyin temel kazanımıdır.
