# Glass Box AI Research

**Mechanistic Interpretability and Glass Box AI — 1. Hafta Araştırma Çalışması**

Bu repository, ilk hafta araştırma ödevindeki kontrollü MNIST MLP deneylerini, internal representation analizlerini, intervention sonuçlarını ve candidate circuit validation çalışmalarını kaydetmektedir.

## Araştırma Sorusu

> Model doğru sonucu üretiyor mu? sorusunun ötesinde: **Model bu sonucu hangi internal mechanism (iç mekanizma) üzerinden üretiyor?**

## Ana Metodoloji

`DATA → MODEL → INTERNAL REPRESENTATION → FEATURE → INTERVENTION → OUTPUT → VALIDATION`

1. **Modeli kur:** kontrollü MNIST MLP baseline.
2. **Internal representation'ı observe et:** Layer, Neuron, Activation ve Representation Learning yapısını incele.
3. **Feature adaylarını belirle:** activation statistics, class behavior ve selectivity kullan.
4. **Hypothesis oluştur:** candidate feature/circuit → expected output effect.
5. **Intervention yap:** Ablation, Activation Patching ve controlled activation scaling.
6. **Output change ölç:** probability, logit ve class accuracy değişimlerini karşılaştır.
7. **Validation yap:** repeated tests, random controls, class-wise controls, Leave-One-Out ve progressive ablation.
8. **Mechanism çıkar:** candidate circuit ve Glass Box computational map.

## Baseline

- MNIST: `60000 / 10000`
- Architecture: `784 → 128 → 64 → 10`
- ReLU
- Adam, learning rate `0.001`
- Batch size `64`
- 5 epochs
- Seed `42`
- CPU
- Test accuracy: **97.56%**

## Completed Experiments

| Çalışma | Durum | Ana sonuç |
|---|---|---|
| Environment | DONE | PyTorch environment çalıştı |
| Baseline model | DONE | 97.56% test accuracy |
| Activation analysis | DONE | `10000 × 64` activation matrix |
| Class activation / selectivity | DONE | Candidate neurons belirlendi |
| Single-neuron ablation | DONE | Class-specific effects ölçüldü |
| Activation intervention | DONE | Controlled probability changes |
| Correlation vs causality | DONE | Observation/intervention ayrımı |
| Activation patching | DONE | Multi-sample patching yapıldı |
| Distributed feature patching | DONE | Top-5 group etkisi incelendi |
| Candidate circuit discovery | DONE | `[47,17,57,53,28]` |
| Circuit ablation | DONE | Class 0 `-12.0408 pp` |
| Leave-One-Out | DONE | Context-dependent contributions |
| Progressive ablation | DONE | Distributed/non-additive effect |
| Random controls | DONE | Random mean `-0.1122 pp` |
| Class-wise validation | DONE | En büyük etki Class 0'da |
| Circuit activation intervention | DONE | True C0 probability `0.7644 → 0.9938` |
| Literature matrix | DONE | 8 kaynak + experiment mapping |
| Advanced concepts | DONE | `notes/advanced_concepts.md` |
| Mechanism provenance proposal | DONE | `notes/mechanism_provenance.md` |
| Figure index + GitHub SVGs | DONE | 11 verified/readable result figures |
| Glass Box map | DONE | Computational map tamamlandı |

## Candidate Circuit

`[47, 17, 57, 53, 28]`

Bu grup Class 0 behavior ile güçlü biçimde ilişkilidir.

### Mechanistic validation summary

- Candidate circuit ablation: **-12.0408 pp** Class 0 accuracy
- Random control mean: **-0.1122 pp**
- Candidate vs random mean: **-11.9286 pp**
- Class 1 control: **+0.0881 pp**
- Class 2 control: **0.0000 pp**
- Leave-One-Out strongest contextual effect: N57, **-9.0816 pp**
- Progressive ablation: **-0.9184 → -12.0408 pp**
- Logit-level patching: Class 1 target **+6.0245**, Class 2 target **+4.3068** Class 0 logit
- Circuit activation intervention: true Class 0 probability **0.7644 → 0.9938**

### Scientific interpretation

Bu sonuçlar candidate circuit'un Class 0 output behavior'a güçlü ve kontrollü bir katkısı olduğuna dair **causal evidence/support** sağlamaktadır. Ancak candidate group'un modeldeki complete circuit olduğu veya genel anlamda causality'nin tamamen ispatlandığı iddia edilmemektedir.

## Scientific Limits

- Correlation tek başına causality değildir.
- Weight magnitude tek başına causal evidence değildir.
- Selectivity candidate seçimi için kullanılır; causal importance değildir.
- Candidate circuit Class 0-biased'dır fakat Class 0-exclusive değildir.
- Progressive ablation order-dependent olabilir.
- Tek training seed kullanıldığı için multi-seed replication gereklidir.
- Candidate selection bias ve sınırlı patching kapsamı vardır.
- Sonuçlar küçük MNIST MLP üzerinde elde edilmiştir; daha büyük modellere genellenemez.

## Repository Structure

```text
glass-box-ai-research/
├── README.md
├── requirements.txt
├── notebooks/          # Deneylerin çalıştırıldığı Colab/Jupyter notebookları
├── src/                # Tekrar kullanılabilir Python model ve yardımcı fonksiyonları
├── experiments/        # Deneylere ait ek/gelecek deney dosyaları
├── results/            # Deney sonuçlarının özet kayıtları
├── figures/            # Deneylerden üretilen doğrulanabilir grafikler (11 SVG)
├── data/               # Veri seti ve veri kullanım açıklamaları
├── papers/             # Araştırmada kullanılacak/ kullanılan makale kaynakları
├── notes/              # Deney günlüğü, literatür, kavramlar ve araştırma notları
└── report/             # Glass Box computational map ve rapor/sunum materyalleri
```

### Klasörlerin rolü

- **`notebooks/`** — Baseline, activation analysis, ablation ve intervention deneylerinin Colab/Jupyter kayıtları.
- **`src/`** — Model, hook, evaluation ve intervention gibi tekrar kullanılabilir kodlar.
- **`figures/`** — Deney günlüğünde sayısal olarak doğrulanabilen 11 SVG grafik ve `figure_index.md`.
- **`notes/`** — Deney logu, literatür matrisi, advanced concepts, mechanism provenance ve deney planı.
- **`results/`** — Sonuçların kısa/özet kayıtları.
- **`report/`** — Glass Box computational map ve raporlama materyalleri.
- **`data/`** — MNIST gibi veri setlerinin repo içinde tutulmayan kullanım/açıklama bilgileri.
- **`papers/`** — Literatür dosyaları için ayrılmış alan.
- **`experiments/`** — Ayrı deney dosyaları için ayrılmış alan; mevcut deney sonuçları esas olarak `notebooks/`, `notes/` ve `figures/` içinde tutulmaktadır.

## Figure Set

`figures/` klasöründe 11 okunabilir SVG bulunmaktadır:

1. Ablation accuracy — tüm candidate neuronlar + candidate circuit
2. Progressive circuit ablation
3. Candidate circuit activation intervention
4. N47 activation intervention
5. N17–N47 correlation summary
6. Baseline training loss
7. Candidate circuit activation across Classes 0–2
8. Class-wise correct predictions (confusion-matrix diagonal)
9. Top-10 selectivity
10. Leave-One-Out
11. Candidate neuron contribution to Class 0 logit

Eksik ham veri noktaları uydurulmamıştır. Bu nedenle bazı grafikler orijinal Colab grafiklerinin doğrulanabilir, daha dar kapsamlı GitHub sürümleridir. Ayrıntılı kapsam `figures/figure_index.md` içinde belirtilmiştir.

## Baseline Learning Curves

`notebooks/01_baseline_model.ipynb` epoch bazında baseline eğitim sonuçlarını kaydetmektedir. GitHub'daki `baseline_training_loss.svg` yalnızca deney günlüğünde doğrulanmış training-loss serisini gösterir; doğrulanmamış validation/test noktaları grafiğe eklenmemiştir.

## Next Experiments

1. Multi-seed replication
2. Synthetic true-vs-spurious dataset
3. Distributed feature analysis
4. Expanded activation patching
5. Fashion-MNIST validation
6. AI-to-AI mechanism provenance / lineage

## Status

**Experimental phase: COMPLETED.**

Mevcut deney sonuçları, experiment log, literature mapping, advanced concept coverage, mechanism provenance proposal ve GitHub figure/result kayıtları tamamlanmıştır. Gelecek deneyler sonuç gibi sunulmamaktadır.
