# Figure Index

Bu klasördeki SVG grafikler deney günlüğünde kaydedilmiş gerçek ölçümlerin okunabilir, GitHub üzerinde doğrudan görüntülenebilir sürümleridir. Grafiklerde yeni deney sonucu uydurulmamıştır.

| # | Figure | İçerik | Kaynak |
|---:|---|---|---|
| 1 | `ablation_accuracy.svg` | Baseline + N47/N17/N57/N53/N28 single-neuron ablation + full candidate circuit ablation, Class 0 accuracy | E04, E13, E47 |
| 2 | `progressive_circuit_ablation.svg` | 1→5 candidate neuron progressive ablation | E20 |
| 3 | `circuit_intervention_probability.svg` | Circuit scale vs true Class 0 probability | E18 |
| 4 | `neuron_intervention_n47.svg` | N47 scale vs true Class 0 probability | E05 |
| 5 | `activation_correlation.svg` | N17–N47 Pearson correlation: all test samples vs Class 0 only | E06 |
| 6 | `baseline_training_loss.svg` | Epoch 1–5 training loss | Baseline |
| 7 | `candidate_circuit_activation_classes.svg` | Candidate neuron mean ReLU2 activations for Classes 0–2, with explicit class colors | E07 / E64 |
| 8 | `class_correct_predictions.svg` | MNIST class-wise correct prediction counts (confusion-matrix diagonal only) | Baseline |
| 9 | `selectivity_top10.svg` | Top-10 neuron selectivity values for candidate ranking | E03 |
| 10 | `leave_one_out.svg` | Candidate-group Leave-One-Out Class 0 accuracy | E46 |
| 11 | `candidate_group_logit_contribution.svg` | Candidate-neuron mean contributions to Class 0 logit on true Class 0 samples | E41 |

## Important Scope Notes

- `baseline_training_loss.svg` contains only the recorded training-loss series. Validation/test loss and epoch-wise accuracy values are not inserted unless their raw values are available.
- `class_correct_predictions.svg` intentionally shows only the confusion-matrix diagonal because the complete off-diagonal matrix values are not stored in the figure data.
- `candidate_circuit_activation_classes.svg` intentionally compares Classes 0–2, matching the recorded candidate-circuit analysis; it is not a full 10-class activation matrix.
- `selectivity_top10.svg` shows the top 10 candidates, not all 64 neurons.
- `candidate_group_logit_contribution.svg` shows computational contribution to the Class 0 logit for true Class 0 samples; it is not a percentage of the final decision.
- Selectivity, weight magnitude, and activation contribution are analysis signals; causal claims rely on intervention and ablation experiments.

## Reproducibility Rule

Eksik ham noktalar kafadan doldurulmaz. GitHub'a yalnızca deney günlüğünde veya mevcut deney kayıtlarında sayısal olarak doğrulanabilen değerler taşınır.
