# Mekanizma Kökeni / AI Mekanizma Soy Zinciri (Mechanism Provenance / AI Mechanism Lineage)

## Araştırma Hipotezi

Bir modelin doğru çıktı (output) üretmesi, kullandığı mekanizmanın doğru veya güvenilir olduğu anlamına gelmez. Uzun vadeli araştırma hedefi, bir AI modelinin öğrendiği iç özellik/devre (internal feature/circuit) bilgisinin başka bir AI modeline aktarılması durumunda **mekanizma kökeninin (mechanism provenance / lineage)** izlenebilmesidir.

## Önerilen Yapı

```text
AI-1
  ↓
Gerçek ilişki + olası sahte ilişkiyi öğrenir
  ↓
İç temsil / aday mekanizma
  ↓
Üretilmiş çıktılar veya sentetik eğitim verisi
  ↓
AI-2
  ↓
İlişkili bir davranışı öğrenir
  ↓
AI-1 mekanizması ↔ AI-2 mekanizması karşılaştırılır
```

## Araştırma Soruları

1. AI-2 aynı çıktı davranışını öğrenirken AI-1 ile aynı iç özellik/devreyi mi kullanıyor?
2. Davranış aktarılmış olsa bile mekanizma da aktarılmış oluyor mu?
3. AI-2'de görülen özellik, AI-1'deki özellikle aktivasyon/nedensel müdahale açısından eşleşiyor mu?
4. Sahte korelasyon (spurious correlation) AI-1'den AI-2'ye aktarılabilir mi?
5. Mekanizma kökeni, yalnızca çıktı/doğruluk karşılaştırmasından daha güvenilir bir aktarım analizi sağlayabilir mi?

## Önerilen Doğrulama Zinciri

`DAVRANIŞ EŞLEŞMESİ → TEMSİL EŞLEŞMESİ → ÖZELLİK EŞLEŞMESİ → MÜDAHALE EŞLEŞMESİ → DEVRE EŞLEŞMESİ → MEKANİZMA KÖKENİ`

Her aşama bir öncekinin ötesinde daha güçlü bir karşılaştırma sağlar. Çıktı eşleşmesi tek başına mekanizma eşleşmesi değildir.

## Kontrollü Gelecek Deneyi

Sentetik veri seti üzerinde iki ilişki oluşturulabilir:

- **Gerçek ilişki (true relation):** Hedef davranışı gerçekten açıklayan özellik.
- **Sahte ilişki (spurious relation):** Eğitim dağılımında hedefle korele fakat kontrollü testte geçersiz olan özellik.

AI-1 eğitildikten sonra AI-2, AI-1 çıktıları veya üretilmiş örnekler üzerinden eğitilir. Daha sonra iki modelde özellik/devre yerelleştirmesi (feature/circuit localization), ablasyon, aktivasyon müdahalesi ve yamalama karşılaştırılır.

## Bilimsel Sınır

Bu dosya bir gelecek araştırma hipotezidir; bu haftada AI-1 → AI-2 mekanizma aktarım deneyi yapılmamıştır. Sonuç gibi sunulmayacaktır.
