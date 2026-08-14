# Literature Table — Glass Box / Mechanistic Interpretability

| # | Kaynak | Problem / Konu | Model / Context | Internal Component | Method | Causal Intervention | Glass Box Contribution | Bu araştırmadaki karşılığı | Limitation / Not |
|---:|---|---|---|---|---|---|---|---|---|
| 1 | *Interpretability in the Wild: a Circuit for IOI in GPT-2 Small* | Circuit discovery | GPT-2 Small | Attention / MLP components | Circuit analysis | Component-level interventions | Circuit-level mechanism reconstruction | Candidate circuit discovery + ablation | Büyük language model bağlamı; MNIST MLP'den farklı |
| 2 | *Towards Automated Circuit Discovery for Mechanistic Interpretability* | Circuit discovery automation | Neural network / transformer setting | Model components | Automated circuit search | Component intervention | Candidate circuit discovery methodology | Progressive ablation + circuit candidate | Otomatik keşif kapsamı bu çalışmada sınırlı |
| 3 | *Locating and Editing Factual Associations in GPT* | Internal factual representations | GPT | MLP / internal representations | Localization and editing | Activation/representation editing | Internal representation üzerinde kontrollü müdahale | Activation intervention / patching | Language-model specific |
| 4 | *Toy Models of Superposition* | Features and superposition | Toy neural networks | Distributed features | Representation analysis | Controlled feature manipulation | Featurelerin tek neuron yerine distributed olabileceğini gösteren temel çerçeve | Distributed representation / Top-5 patching | Toy-model sonuçlarının doğrudan MNIST'e genellenmesi sınırlı |
| 5 | *Sparse Autoencoders Find Highly Interpretable Features in Language Models* | Feature decomposition | Language models | Activation representations | SAE | Feature-level manipulation / analysis | Complex activation space'den daha ayrışabilir feature adayları çıkarma | Feature analysis için ileri yöntem | SAE henüz bu haftanın deneylerine uygulanmadı |
| 6 | *Causal Abstraction: A Theoretical Foundation for Mechanistic Interpretability* | Causal validation | Abstract computational models | Mechanistic variables | Causal abstraction | Intervention | Mechanistic explanations için causal framework | Observation vs intervention ve mechanistic validation | Teorik çerçeve; deneysel implementation ayrıca gerekir |
| 7 | *Tracr: Compiled Transformers as a Laboratory for Interpretability* | Controlled interpretability experiments | Compiled transformers | Known computational components | Program-to-transformer compilation | Controlled interventions | Bilinen computation'ı interpretability laboratuvarı olarak kullanma | Küçük ve kontrollü model kullanma yaklaşımı | Transformer odaklı |
| 8 | *Gemma Scope* | Large-scale feature analysis | Gemma language models | Activation features | Sparse autoencoders / feature analysis | Feature-level interventions and analysis | Large-scale internal feature inspection | Gelecekte SAE / feature-level expansion | Bu haftanın MNIST modelinden çok daha büyük ölçek |

## Literature ↔ Our Experiments Mapping

| Literatür kavramı | Bizim deney | Sonuç / Kullanım |
|---|---|---|
| Activation Analysis | Experiment 2 | `10000 × 64` activation matrix, class means, selectivity |
| Neuron Ablation | Experiment 3 | N47/N54/N62 class-specific effects |
| Activation Intervention | Experiment 4 | N47/N54 scaling ve output probability değişimi |
| Correlation vs Causality | Experiment 5 | N17/N47 correlation `0.4485` overall, `0.7846` Class 0; intervention ile ayrım |
| Activation Patching | Experiments 10–13 | Candidate information transfer / logit-level effect |
| Circuit Discovery | Experiments 14–21 | `[47,17,57,53,28]` candidate group |
| Distributed Representation | Experiments 9, 11, 18, 20 | Group effects, progressive ablation ve Leave-One-Out |
| Mechanistic Validation | Experiments 22–23 | Random controls + class-wise controls |
| Feature-Level Analysis | Experiments 2–3, 24 | Class 0-biased candidate feature characterization |
| Circuit-Level Intervention | Experiment 24 | True Class 0 probability `0.7644 → 0.9938` |

## Kaynak Kullanım İlkesi

Kaynaklar rapora aktarılırken orijinal makalelerin iddiaları ile bu çalışmada gerçekten ölçülen sonuçlar birbirinden ayrılacaktır. Literatür, deney sonuçlarını olduğundan daha güçlü göstermenin gerekçesi olarak kullanılmayacaktır.
