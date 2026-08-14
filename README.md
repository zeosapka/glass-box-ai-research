# Glass Box AI Research

**Mechanistic Interpretability and Glass Box AI — 1. Hafta Araştırma Çalışması**

Bu repository, `@Ahmet_Gullek_1_Haftalik_Glass_Box_AI_Arastirma_Odevi.pdf` içindeki ilk hafta metodolojisini ve deney kayıtlarını takip eder.

## Araştırma sorusu
> Model doğru sonucu üretiyor mu? sorusunun ötesinde: **Model bu sonucu hangi internal mechanism (iç mekanizma) üzerinden üretiyor?**

## Ana metodoloji
`DATA → MODEL → INTERNAL REPRESENTATION → FEATURE → INTERVENTION → OUTPUT → VALIDATION`

1. **Modeli aç / observe:** Input → AI Model → Output ve internal representation
2. **İç temsili incele:** layer, neuron, activation; feature visualization, feature analysis, SAE
3. **Hipotez + müdahale:** candidate feature → hypothesis → ablation / activation patching / activation steering / attribution patching
4. **Etkiyi ölç:** output change → repeated tests → causal evidence
5. **Mekanizmayı çıkar:** circuit discovery → circuit map → mechanism hypothesis → mechanistic validation → mechanistic interpretability

## Repository yapısı
```text
glass-box-ai-research/
├── README.md
├── requirements.txt
├── notebooks/
│   ├── 01_baseline_model.ipynb
│   ├── 02_activation_analysis.ipynb
│   ├── 03_ablation_experiment.ipynb
│   └── 04_intervention_experiment.ipynb
├── src/
│   ├── model.py
│   ├── hooks.py
│   ├── evaluation.py
│   └── interventions.py
├── experiments/
├── results/
├── figures/
├── data/
├── papers/
├── notes/
└── report/
    └── glass_box_map.md
```

## Deney sırası
| Deney | Amaç |
|---|---|
| Baseline | Küçük, kontrol edilebilir MNIST modeli kurmak |
| Activation analysis | İç aktivasyonları gözlemek ve aday feature bulmak |
| Ablation | Seçili iç bileşenin çıkarılmasıyla output etkisini ölçmek |
| Intervention | Aktivasyonu kontrollü değiştirerek output etkisini test etmek |

## Deneysel sınırlar
- Korelasyon tek başına nedensellik değildir.
- Müdahale etkisi tekrarlı kontrollü deneylerle güçlendirilmelidir.
- “Causality proved” yerine **causal evidence/support** dili kullanılacaktır.
- Deneyler çalıştırılmadan sonuç uydurulmayacaktır.

## Durum
- [x] Repository iskeleti
- [x] Glass Box computational map
- [x] Dört deney notebook iskeleti
- [x] Deney günlüğü ve literatür tablosu
- [ ] Baseline gerçek sonuçları
- [ ] Activation istatistikleri ve sınıf analizi
- [ ] Ablation sonuçları
- [ ] Controlled intervention sonuçları
- [ ] Tekrarlı testler ve nihai causal evidence değerlendirmesi
