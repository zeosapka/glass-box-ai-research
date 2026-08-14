# Glass Box Computational Map

Bu harita 1. haftalık araştırma ödevindeki ana metodolojik akışı gösterir.

```mermaid
flowchart LR
A["① MODELİ AÇ — OBSERVE / GÖZLEM"] --> B["② İÇ TEMSİLİ İNCELE — FEATURE ANALYSIS"] --> C["③ TEST ET — HYPOTHESIS / INTERVENTION"] --> D["④ ETKİYİ ÖLÇ — CAUSAL EVIDENCE"] --> E["⑤ MEKANİZMASI ÇIKAR — VALIDATE"]
B --> B1["Internal Representation → Feature Analysis → Candidate Feature"]
C --> C1["Hypothesis → Intervention → Ablation / Patching / Steering / Attribution Patching"]
D --> D1["Output Change → Repeated Tests → Causal Evidence"]
E --> E1["Circuit Discovery → Circuit Map → Mechanism Hypothesis → Mechanistic Validation → Mechanistic Interpretability"]
```

## Core chain
`DATA → MODEL → INTERNAL REPRESENTATION → FEATURE → INTERVENTION → OUTPUT → VALIDATION`

Bu diyagram metodoloji haritasıdır; deney sonuçlarının yerine geçmez.
