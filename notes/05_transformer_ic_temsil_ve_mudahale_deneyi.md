# Transformer İç Temsil ve Kontrollü Müdahale Deneyi

**Deney:** Hugging Face `distilgpt2` iç temsil analizi ve boyut müdahalesi  
**Notebook:** `notebooks/05_huggingface_model_inference.ipynb`  
**Durum:** Tamamlandı – aday boyut için nedensel rol araştırması yapıldı, rastgele kontrollerle sınandı.

---

## 1. Deneyin amacı

Bu çalışmada küçük bir sinir ağındaki Glass Box yaklaşımından açık kaynak bir Transformer modeline geçiş yapılmıştır. Amaç yalnızca modelin hangi tokenı tahmin ettiğine bakmak değil, **modelin iç temsilinde hangi yapıların çıktıyla ilişkili olduğunu ve kontrollü bir müdahalenin çıktıyı nasıl değiştirdiğini ölçmektir.**

Temel araştırma sorusu:

> **İç temsilinde farklı davranan belirli bir boyut, model çıktısında gerçekten özel bir nedensel role sahip mi?**

Deneyin temel mantığı:

```text
Girdi
  ↓
Transformer
  ↓
İç temsil
  ↓
Aday boyut / özellik
  ↓
Kontrollü müdahale
  ↓
Çıktı değişimi
  ↓
Rastgele kontrol karşılaştırması
  ↓
Nedensel kanıt değerlendirmesi
```

Buradaki temel metodolojik ilke:

> **Bir yapının gözlenmesi veya başka bir değişkenle ilişkili olması, onun nedensel olduğu anlamına gelmez.**

---

# 2. Kullanılan model ve ortam

| Özellik | Değer |
|---|---|
| Model | `distilgpt2` |
| Kütüphane | Hugging Face Transformers |
| Temel çatı | PyTorch |
| Model tipi | Causal Language Model |
| Görev | Sonraki token tahmini |
| Gizli temsil boyutu | 768 |
| Deney girdisi | 16 cümle |
| Temsil matrisi | `16 × 768` |
| Müdahale edilen bölüm | Son Transformer bloğu |
| Müdahale yöntemi | Seçilen boyutu sıfırlama |
| Ölçüm | Olasılık dağılımı değişimi |

### Önemli teknik ayrıntı

Müdahale şu katmanda yapılmıştır:

```python
model.transformer.h[-1]
```

Yani müdahale, **son Transformer bloğunun çıktısına** uygulanmıştır. Bu çıktı GPT-2'nin son katman normalizasyonundan (`ln_f`) ve dil modeli başlığından (language-model head) önce gelir.

Dolayısıyla bunu "son normalize edilmiş temsil üzerinde müdahale" olarak tanımlamak doğru değildir.

---

# 3. İlk aşama: İç temsilin çıkarılması

16 cümlelik keşif veri kümesi dört gruba ayrılmıştır:

| Grup | Örnek konu |
|---|---|
| Elektrik mühendisliği | Electrical engineering |
| Transformatör | Transformer |
| Motor | Motor |
| Bilgisayar | Computer |

Her cümlenin **son token konumundaki gizli temsili** alınmıştır.

Sonuç:

```text
16 cümle × 768 boyut
        ↓
   16 × 768 temsil matrisi
```

Bu matris üzerinden her boyutun gruplar arasında nasıl değiştiği incelenmiştir.

---

# 4. Boyut analizi: İlk gözlem

İlk olarak boyutların genel değişkenliği incelenmiştir. Daha sonra yalnızca ham standart sapmaya bakmak yerine **gruplar arası ayrımın grup içi değişime oranı** hesaplanmıştır.

Bu önemliydi çünkü:

```text
Yüksek toplam değişim
        ≠
Belirli grupları ayıran anlamlı yapı
```

Bu analiz sonucunda bazı boyutlar aday olarak öne çıkmıştır.

### Gruplar arası ayrım / grup içi değişim oranında öne çıkan boyutlar

| Boyut | Ayrım / iç değişim oranı |
|---:|---:|
| 471 | 6.2639 |
| 228 | 4.0935 |
| 12 | 3.9387 |
| 358 | 3.7314 |
| 529 | 3.4448 |
| 347 | 3.3758 |
| 306 | 3.2213 |
| 470 | 2.9063 |
| 217 | 2.8268 |
| 125 | 2.8255 |

Bu tablo **nedensel özellik tablosu değildir.** Yalnızca hangi boyutların daha ayrışmış göründüğünü gösteren keşif aşamasıdır.

---

# 5. Aday boyut: 471

Boyut `471`, keşif analizinde en yüksek ayrım / grup içi değişim oranına sahip boyut olarak öne çıkmıştır.

Grup ortalamaları:

| Grup | Boyut 471 ortalaması | Grup içi std |
|---|---:|---:|
| Elektrik mühendisliği | -0.462 | 0.025 |
| Transformatör | -0.102 | 0.023 |
| Motor | -0.061 | 0.038 |
| Bilgisayar | 0.014 | 0.049 |

Bu sonuç şu hipotezi oluşturmuştur:

> **471 numaralı boyut belirli grup bilgilerini taşıyor olabilir.**

Fakat bu yalnızca bir **hipotezdir**.

```text
Temsil ayrışması
      ↓
Aday boyut 471
      ↓
HİPOTEZ
      ↓
Müdahale gerekli
```

---

# 6. Müdahale deneyi

471 numaralı boyut, son Transformer bloğunun çıktısında sıfırlanmıştır.

Normal durum:

```text
Transformer çıkışı
[ ... x470, x471, x472 ... ]
```

Müdahale durumu:

```text
Transformer çıkışı
[ ... x470,   0, x472 ... ]
```

Kod mantığı:

```python
modified_output[:, :, candidate_dimension] = 0.0
```

Ardından müdahale edilmiş model çıktısı, normal model çıktısıyla karşılaştırılmıştır.

Kullanılan ölçütler:

1. **L1 değişimi:** Tüm token olasılık dağılımının ne kadar değiştiği.
2. **Maksimum olasılık değişimi:** Her örnekte tek bir token olasılığındaki en büyük değişim.
3. **Top-1 token değişimi:** En yüksek olasılıklı tokenın değişip değişmediği.

---

# 7. 471 boyutu müdahale sonuçları

| # | Grup | Normal top-1 | Müdahale top-1 | Normal olasılık | Müdahale olasılık | L1 değişimi | Maks. değişim |
|---:|---|---|---|---:|---:|---:|---:|
| 1 | Elektrik müh. | `\\n` | `\\n` | 0.1199 | 0.1241 | 0.035408 | 0.004177 |
| 2 | Elektrik müh. | `\\n` | `\\n` | 0.2197 | 0.2263 | 0.036395 | 0.006676 |
| 3 | Elektrik müh. | `The` | `\\n` | 0.1424 | 0.1396 | 0.039406 | 0.005382 |
| 4 | Elektrik müh. | `\\n` | `\\n` | 0.2724 | 0.2800 | 0.038835 | 0.007606 |
| 5 | Transformatör | `The` | `The` | 0.1606 | 0.1597 | 0.006622 | 0.000922 |
| 6 | Transformatör | `\\n` | `\\n` | 0.1703 | 0.1722 | 0.011458 | 0.001917 |
| 7 | Transformatör | `The` | `The` | 0.2057 | 0.2042 | 0.009111 | 0.001504 |
| 8 | Transformatör | `The` | `The` | 0.1627 | 0.1614 | 0.009828 | 0.001397 |
| 9 | Motor | `The` | `The` | 0.1737 | 0.1727 | 0.007410 | 0.001079 |
| 10 | Motor | `�` | `�` | 0.1537 | 0.1531 | 0.004596 | 0.000670 |
| 11 | Motor | `\\n` | `\\n` | 0.1834 | 0.1850 | 0.008880 | 0.001599 |
| 12 | Motor | `The` | `The` | 0.1872 | 0.1867 | 0.003311 | 0.000467 |
| 13 | Bilgisayar | `The` | `The` | 0.1552 | 0.1555 | 0.003189 | 0.000434 |
| 14 | Bilgisayar | `\\n` | `\\n` | 0.1843 | 0.1850 | 0.003649 | 0.000638 |
| 15 | Bilgisayar | `\\n` | `\\n` | 0.2001 | 0.2002 | 0.000085 | 0.000016 |
| 16 | Bilgisayar | `The` | `The` | 0.1883 | 0.1876 | 0.004595 | 0.000742 |

### İlk gözlem

Elektrik mühendisliği grubunda L1 değişimleri belirgin biçimde daha yüksek örnekler içermektedir.

Örneğin:

- 1. örnek: `0.035408`
- 2. örnek: `0.036395`
- 3. örnek: `0.039406`
- 4. örnek: `0.038835`

Ayrıca 3. örnekte **top-1 token değişmiştir**.

Bu sonuç 471'in müdahaleye duyarlı olduğunu göstermektedir.

Ancak:

> **Müdahaleye duyarlı olmak, tek başına o boyutun özel bir nedensel özellik olduğunu kanıtlamaz.**

Bu nedenle kontrol deneyi yapılmıştır.

---

# 8. İlk rastgele kontrol: Boyut 655

471 dışından rastgele `655` numaralı boyut seçilmiş ve aynı şekilde sıfırlanmıştır.

| Ölçüt | 471 | 655 – rastgele kontrol |
|---|---:|---:|
| Ortalama L1 değişimi | **0.013924** | **0.014129** |
| Ortalama maksimum olasılık değişimi | 0.002202 | **0.002879** |

İlk kontrolün sonucu oldukça önemlidir:

**471, 655 numaralı rastgele boyuttan daha güçlü bir ortalama etki göstermemiştir.**

Tek bir kontrol boyutu kesin karar vermek için yeterli olmadığı için deney genişletilmiştir.

---

# 9. Yirmi rastgele kontrol deneyi

471 dışında 20 farklı boyut seçilmiştir.

Kullanılan boyutlar:

`53, 274, 89, 417, 272, 110, 39, 388, 550, 576, 340, 348, 163, 138, 345, 575, 341, 719, 251, 167`

Her boyut için aynı işlem uygulanmıştır:

```text
Boyutu seç
   ↓
Boyutu sıfırla
   ↓
Modeli tekrar çalıştır
   ↓
Normal çıktı ile karşılaştır
   ↓
Ortalama L1 değişimini hesapla
```

### Kontrol sonuçları

| Sıra | Kontrol boyutu | Ortalama L1 değişimi |
|---:|---:|---:|
| 1 | 53 | 0.022478 |
| 2 | 274 | 0.009072 |
| 3 | 89 | 0.018436 |
| 4 | 417 | 0.008736 |
| 5 | 272 | 0.008453 |
| 6 | 110 | 0.009402 |
| 7 | 39 | 0.007884 |
| 8 | 388 | 0.010355 |
| 9 | 550 | 0.024153 |
| 10 | 576 | 0.010553 |
| 11 | 340 | 0.015105 |
| 12 | 348 | 0.017517 |
| 13 | 163 | 0.012270 |
| 14 | 138 | 0.021835 |
| 15 | 345 | 0.015546 |
| 16 | 575 | 0.011092 |
| 17 | 341 | 0.008219 |
| 18 | 719 | 0.009677 |
| 19 | 251 | 0.024040 |
| 20 | 167 | **0.034599** |

### 471'in karşılaştırması

| Ölçüt | 471 | Rastgele kontroller |
|---|---:|---:|
| Ortalama L1 | **0.013924** | **0.014971** |
| Medyan L1 | — | **0.011681** |
| Sıralama | **10 / 21** | — |
| 471'den daha büyük etki | — | **9 kontrol** |
| Test edilen dağılımdaki konum | **%55** | — |

Burada 21 = 1 aday + 20 rastgele kontroldür.

---

# 10. Kontrol deneyinin temel sonucu

471 numaralı boyut:

```text
471 ortalama L1 = 0.013924

Kontrol ortalaması = 0.014971
```

Yani 471'in etkisi, rastgele boyutların ortalama etkisinden **daha büyük değildir**.

Ayrıca 20 kontrolden **9 tanesi** 471'den daha büyük ortalama etki üretmiştir.

Sıralama:

```text
En yüksek etki
     ↓
167  = 0.034599
550  = 0.024153
251  = 0.024040
53   = 0.022478
...
471  = 0.013924   ← 10. sıra
...
```

Bu nedenle 471 için "özel" veya "benzersiz" bir nedensel etki iddiası yapılamaz.

---

# 11. Bilimsel değerlendirme

### Desteklenen bulgular

| Soru | Sonuç |
|---|---|
| 471 temsil analizinde ayrışıyor mu? | **Evet** |
| 471'e müdahale çıktıyı değiştiriyor mu? | **Evet** |
| Bazı örneklerde değişim belirgin mi? | **Evet** |
| Bir örnekte top-1 token değişiyor mu? | **Evet** |
| 471 tek rastgele kontrolden daha güçlü mü? | **Hayır** |
| 471, 20 rastgele kontrolden belirgin biçimde üstün mü? | **Hayır** |
| 471'in özel nedensel özellik olduğu gösterildi mi? | **Hayır** |

### Doğru bilimsel sonuç

> **471 numaralı boyut, temsil analizi sırasında güçlü grup ayrımı gösterdiği için aday olarak seçilmiştir. Boyutun sıfırlanması bazı girdilerde model çıktı dağılımını anlamlı ölçüde değiştirmiştir. Ancak aynı müdahale rastgele seçilen diğer boyutlarda da benzer veya daha büyük değişiklikler oluşturabilmiştir. Bu nedenle mevcut deney, 471 boyutunun belirli bir nedensel özellik olduğunu desteklemek için yeterli kanıt sağlamamaktadır.**

Bu sonuç başarısızlık değildir.

Tam tersine deney, Glass Box araştırmasının temel metodolojik ayrımını göstermektedir:

```text
Gözlem
  ↓
Korelasyon / aday ilişki
  ↓
Müdahale
  ↓
Çıktı değişimi
  ↓
Kontrol
  ↓
Gerçekten özel mi?
```

---

# 12. Neden 471 yine de önemli?

471'in özel bir nedensel özellik olduğu gösterilmemiş olsa da, aday seçim sürecinin tamamen anlamsız olduğu söylenemez.

471:

- Gruplar arasında belirgin ayrım göstermiştir.
- Müdahaleye duyarlı olmuştur.
- Bazı örneklerde diğerlerine göre daha büyük değişim üretmiştir.

Ancak aynı davranışın rastgele boyutlarda da ortaya çıkabilmesi, şu ihtimalleri gündeme getirmektedir:

1. Tek bir boyut semantik bilgiyi temsil etmiyor olabilir.
2. Bilgi birden fazla boyuta dağıtılmış olabilir.
3. Müdahale, modelin genel hesaplamasını bozduğu için yan etkiler oluşturuyor olabilir.
4. Veri kümesindeki cümle yapısı farkları sonucu etkiliyor olabilir.
5. Seçilen boyut doğal temsil dağılımının dışına taşınmış olabilir.

---

# 13. Veri kümesi problemi

Mevcut 16 cümle keşif açısından kullanışlı olsa da tam kontrollü değildir.

Örneğin başlangıç yapıları farklıdır:

```text
Electrical engineering is ...
The transformer is ...
The motor is ...
The computer ...
```

Dolayısıyla modelin gördüğü fark yalnızca kavram farkı değildir.

Aynı zamanda:

- Tokenizasyon
- Cümle başlangıcı
- Sözdizimi
- Kelime uzunluğu
- Bağlam
- Token konumları

gibi faktörler de farklılaşmaktadır.

Bu nedenle mevcut sonuçları "471 boyutu elektrik mühendisliği özelliğidir" şeklinde yorumlamak doğru değildir.

---

# 14. Aday seçimi ve testin aynı veri üzerinde olması

471 boyutu aynı 16 örnek kullanılarak:

1. Aday olarak seçilmiş,
2. Müdahale edilerek test edilmiştir.

Bu durum **seçim yanlılığı (selection bias)** oluşturabilir.

Daha güçlü deney tasarımı:

```text
Keşif verisi
    ↓
Aday boyutları belirle
    ↓
----------------------
    ↓
Ayrı test verisi
    ↓
Müdahale
    ↓
Kontrol
    ↓
Doğrulama
```

Böylece aday seçiminden bağımsız bir doğrulama yapılabilir.

---

# 15. Müdahalenin büyüklüğü

Mevcut deneyde seçilen boyut doğrudan:

```text
x₄₇₁ → 0
```

yapılmıştır.

Bu güçlü bir müdahaledir.

Daha kontrollü bir sonraki deneyde örneğin:

```text
x → x - 0.25σ
x → x - 0.50σ
x → x - 1.00σ
x → x + 0.50σ
x → x + 1.00σ
```

gibi farklı müdahale büyüklükleri incelenebilir.

Amaç yalnızca "sıfırlayınca ne oldu?" sorusu değil:

> **İç temsildeki kontrollü değişimin büyüklüğü ile çıktı değişimi arasında sistematik bir ilişki var mı?**

sorusunu araştırmaktır.

---

# 16. Tek boyut yerine özellik grupları

Bir başka önemli ihtimal, modelin anlamlı bilgiyi tek bir boyutta değil, birçok boyutun birlikte oluşturduğu dağıtık bir temsil içinde taşımasıdır.

Bu durumda:

```text
Tek boyut
   ↓
471
```

yerine:

```text
Boyut 471 ─┐
Boyut 228 ─┤
Boyut 12  ─┼→ Ortak özellik / temsil
Boyut 358 ─┤
Boyut 529 ─┘
```

gibi bir yapı söz konusu olabilir.

Bu nedenle gelecekte **boyut grubu müdahalesi** ve daha sonra **özellik keşfi (feature discovery)** yöntemleri incelenebilir.

---

# 17. Deneyin Glass Box araştırmasındaki yeri

Bu deney, daha önce küçük MNIST ağı üzerinde uygulanan metodolojiyi açık kaynak bir Transformer'a taşımaktadır.

Genel araştırma zinciri:

```text
BLACK BOX
   ↓
Model çıktısını gözle
   ↓
GLASS BOX
   ↓
İç temsili çıkar
   ↓
Boyutları / özellikleri analiz et
   ↓
Aday mekanizma oluştur
   ↓
Müdahale et
   ↓
Çıktı değişimini ölç
   ↓
Rastgele / kontrollü karşılaştırma
   ↓
Nedensel kanıtı değerlendir
```

Bu deney henüz **devre keşfi (circuit discovery)** değildir. Fakat devre keşfine giden metodolojik zincirin önemli bir basamağıdır.

---

# 18. Deneyden çıkarılan ana ders

En önemli sonuç şudur:

> **Bir iç boyutun gruplar arasında ayrışması ve o boyuta müdahale edildiğinde çıktının değişmesi, tek başına o boyutun modelde özel bir nedensel rol taşıdığını göstermez.**

Özel bir mekanizma iddiası için:

```text
Aday özellik
     ↓
Kontrollü müdahale
     ↓
Uygun negatif / rastgele kontroller
     ↓
Tekrarlanabilir etki
     ↓
Eşleştirilmiş ve bağımsız test verisi
     ↓
Mekanizma hipotezi
     ↓
Mekanik doğrulama
```

gereklidir.

---

# 19. Bir sonraki deney için plan

Bir sonraki deneyde doğrudan daha fazla rastgele boyut denemek yerine deney tasarımının kalitesi artırılmalıdır.

### Öncelik 1 – Eşleştirilmiş veri

Aynı cümle kalıbı korunacak, yalnızca hedef kavram değiştirilecektir.

### Öncelik 2 – Ayrı keşif ve test kümeleri

Aday boyut keşif kümesinde seçilecek, doğrulama ayrı test kümesinde yapılacaktır.

### Öncelik 3 – Kontrollü müdahale büyüklüğü

Boyutun yalnızca sıfırlanması değil, farklı miktarlarda azaltılması/artırılması incelenecektir.

### Öncelik 4 – Kontrol dağılımı

Daha geniş rastgele kontrol kümesi kullanılacaktır.

### Öncelik 5 – Tekrar

Sonuçların tek bir cümle grubuna özgü olup olmadığı farklı örneklerde test edilecektir.

### Öncelik 6 – Gerekirse boyut grupları

Tek boyut yerine birlikte davranan boyut kümeleri araştırılacaktır.

---

# 20. Sonuç özeti

| Başlık | Sonuç |
|---|---|
| Model | `distilgpt2` |
| İç temsil | 768 boyut |
| Veri | 16 cümle |
| Aday boyut | **471** |
| Aday seçme nedeni | Yüksek grup ayrımı / grup içi değişim oranı |
| Müdahale | Boyut 471'i sıfırlama |
| Müdahale sonucu | Ölçülebilir çıktı değişimleri |
| Top-1 değişimi | 1 örnekte gözlendi |
| Tek rastgele kontrol | 655 |
| 471 ortalama L1 | **0.013924** |
| 655 ortalama L1 | **0.014129** |
| Rastgele kontrol sayısı | 20 |
| Kontrol ortalaması | **0.014971** |
| Kontrol medyanı | **0.011681** |
| 471 sıralaması | **10 / 21** |
| 471'den güçlü kontrol sayısı | **9** |
| 471'in test dağılımındaki konumu | **%55** |
| Özel nedensel özellik kanıtı | **Yetersiz** |
| Sonraki adım | Eşleştirilmiş veri + bağımsız doğrulama |

---

# 21. Nihai bilimsel ifade

> **Bu çalışmada distilgpt2 modelinin iç temsilleri incelenmiş ve 471 numaralı boyut, grup ayrımı açısından aday olarak belirlenmiştir. Bu boyuta uygulanan sıfırlama müdahalesi, bazı girdilerde modelin sonraki-token olasılık dağılımını değiştirmiş ve bir örnekte en yüksek olasılıklı tokenın değişmesine neden olmuştur. Ancak aynı müdahale farklı rastgele boyutlarda da benzer veya daha büyük değişiklikler oluşturmuştur. 471 numaralı boyutun ortalama L1 etkisi 0.013924 iken 20 rastgele kontrolün ortalaması 0.014971 olmuş ve 471 test edilen 21 boyut içinde 10. sırada kalmıştır. Bu nedenle mevcut deney, 471 boyutunun belirli ve benzersiz bir nedensel özellik olduğunu göstermemektedir. Sonuç, gözlenen temsil ayrışmasının nedensellik iddiasına dönüştürülebilmesi için uygun kontrol, bağımsız doğrulama ve tekrarlı müdahale deneylerinin gerekli olduğunu göstermektedir.**

---

## Araştırma notu

Bu deneyin amacı bir "özellik buldum" sonucu üretmekten çok, **Black Box'tan Glass Box'a geçerken nedensel iddianın nasıl test edilmesi gerektiğini uygulamalı olarak öğrenmektir.** Negatif sonuç da araştırma kaydının bir parçasıdır ve sonraki deney tasarımını doğrudan belirlemektedir.
