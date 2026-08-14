# Mechanism Provenance / AI Mechanism Lineage

## Research hypothesis

Bir modelin doğru output üretmesi, kullandığı mechanism'in doğru veya güvenilir olduğu anlamına gelmez. Uzun vadeli araştırma hedefi, bir AI modelinin öğrendiği internal feature/circuit bilgisinin başka bir AI modeline aktarılması durumunda **mekanizma kökeninin (mechanism provenance / lineage)** izlenebilmesidir.

## Proposed setup

```text
AI-1
  ↓
Learns true relation + possible spurious relation
  ↓
Internal representation / candidate mechanism
  ↓
Generated outputs or synthetic training data
  ↓
AI-2
  ↓
Learns a related behavior
  ↓
Compare AI-1 mechanism ↔ AI-2 mechanism
```

## Research questions

1. AI-2 aynı output davranışını öğrenirken AI-1 ile aynı internal feature/circuit'i mi kullanıyor?
2. Davranış transfer edilmiş olsa bile mechanism transfer edilmiş oluyor mu?
3. AI-2'de görülen feature AI-1'deki feature ile activation/causal intervention açısından eşleşiyor mu?
4. Spurious correlation AI-1'den AI-2'ye aktarılabilir mi?
5. Mechanism provenance, yalnız output/accuracy karşılaştırmasından daha güvenilir bir transfer analizi sağlayabilir mi?

## Proposed validation chain

`BEHAVIOR MATCH → REPRESENTATION MATCH → FEATURE MATCH → INTERVENTION MATCH → CIRCUIT MATCH → MECHANISM PROVENANCE`

Her aşama bir öncekinin ötesinde daha güçlü bir karşılaştırma sağlar. Output eşleşmesi tek başına mechanism eşleşmesi değildir.

## Controlled future experiment

Synthetic dataset üzerinde iki ilişki oluşturulabilir:

- **True relation:** hedef davranışı gerçekten açıklayan feature.
- **Spurious relation:** eğitim dağılımında hedefle korele fakat kontrollü testte geçersiz olan feature.

AI-1 eğitildikten sonra AI-2, AI-1 çıktıları veya üretilmiş örnekler üzerinden eğitilir. Daha sonra iki modelde feature/circuit localization, ablation, activation intervention ve patching karşılaştırılır.

## Scientific limit

Bu dosya bir gelecek araştırma hipotezidir; bu haftada AI-1 → AI-2 mechanism transfer deneyi yapılmamıştır. Sonuç gibi sunulmayacaktır.
