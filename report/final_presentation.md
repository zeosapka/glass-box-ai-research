# 1. Haftalık Glass Box AI Araştırması — Sunum Planı

## Slayt 1 — Araştırma Problemi
- Black Box AI yalnızca doğru çıktıyı ölçer.
- Glass Box yaklaşımı modelin internal mechanism'ini araştırır.
- Ana soru: Model doğru sonucu hangi internal computational mechanism üzerinden üretiyor?

## Slayt 2 — Baseline Model
- Dataset: MNIST
- Architecture: `784 → 128 → ReLU → 64 → ReLU → 10`
- Seed: 42
- Optimizer: Adam
- Learning rate: 0.001
- Batch size: 64
- Epoch: 5
- Test accuracy: **97.56%**

## Slayt 3 — Internal Representation
- ReLU2 activation matrix: **10000 × 64**
- Mean/max activation
- Zero activation ratio
- Class-wise activation analysis
- Selectivity candidate identification
- Selectivity = observation; causality değildir.

## Slayt 4 — Neuron-Level Intervention
- N47 Class 0 selectivity: **3.163**
- N47 ablation: **−0.9184 pp** Class 0 accuracy
- N47 activation scale 0→2: true Class 0 probability **0.9640→0.9853**
- N17 intervention de benzer sistematik etki göstermiştir.

## Slayt 5 — Circuit Discovery
- Candidate circuit: **[47, 17, 57, 53, 28]**
- Circuit ablation: Class 0 accuracy **98.6735%→86.6327%**
- Etki: **−12.0408 pp**
- Random controls mean: **−0.1122 pp**

## Slayt 6 — Distributed Representation
- Progressive ablation: 1→5 neuron etkisi **−0.9184→−12.0408 pp**
- Leave-One-Out: N57 context-dependent effect **−9.0816 pp**
- Activation Patching: Class 0 logit change
  - Class 1 target: **+6.0245**
  - Class 2 target: **+4.3068**
- Candidate circuit güçlü fakat context-dependent ve distributed.

## Slayt 7 — Mechanistic Validation
- Class-wise control: Class 0 **−12.0408 pp**
- Class 1: **+0.0881 pp**
- Class 2: **0.0000 pp**
- Circuit activation intervention: true Class 0 probability **0.7644→0.9938**
- Sonuç: causal evidence/support; causality proved denmemektedir.

## Slayt 8 — Sonuç ve Sonraki Araştırma
- Zincir: **Internal Representation → Feature → Intervention → Causal Evidence → Circuit Discovery → Mechanistic Validation**
- Sınırlılıklar: tek model, seed 42, candidate selection bias, sınırlı repetition.
- Sonraki deneyler:
  1. Multi-Seed Replication
  2. Synthetic True-vs-Spurious Dataset
  3. Distributed Feature Analysis
  4. Expanded Activation Patching
  5. Fashion-MNIST validation
- Uzun vadeli hipotez: **Mechanism Provenance / AI Mechanism Lineage**
  - AI-1 bir ilişki öğrenir.
  - AI-1 çıktıları/sentetik verileri AI-2 eğitiminde kullanılır.
  - AI-2 benzer internal feature öğrenir.
  - Öğrenilen feature gerçek mekanizmayı mı, yoksa aktarılan artefact'ı mı temsil ediyor?
