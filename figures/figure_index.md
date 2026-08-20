# Figure Index

Bu klasördeki grafikler deney günlüğünde kayıtlı gerçek ölçümlerin GitHub üzerinde görüntülenebilir sürümleridir.

| # | Figure | İçerik | Kaynak deney |
|---:|---|---|---|
| 1 | `ablation_accuracy.svg` | Single-neuron ve candidate-circuit Class0 ablation | E04, E15 |
| 2 | `progressive_circuit_ablation.svg` | 1→5 candidate neuron progressive ablation | E18 |
| 3 | `circuit_intervention_probability.svg` | Circuit scale vs true Class0 probability | E19 / intervention record |
| 4 | `neuron_intervention_n47.svg` | N47 scale vs true Class0 probability | E05 |
| 5 | `activation_correlation.svg` | N17–N47 Pearson correlation | E06 |
| 6 | `baseline_training_loss.svg` | Epoch 1–5 training loss | E01 |
| 7 | `candidate_circuit_activation_classes.svg` | Candidate neuron activations for Classes 0–2 | E07 |
| 8 | `class_correct_predictions.svg` | MNIST class-wise correct prediction counts | E01 |
| 9 | `selectivity_top10.svg` | Top-10 selectivity ranking | E03 |
| 10 | `leave_one_out.svg` | Candidate-group Leave-One-Out Class0 accuracy | E17 |
| 11 | `candidate_group_logit_contribution.svg` | Candidate contribution to Class0 logit | E13 |

## Scope rules

- Grafiklerde ham kayıtta bulunmayan değerler uydurulmaz.
- Selectivity, weight magnitude ve activation contribution observational/analysis signals'dir.
- Causal interpretation intervention, ablation ve controls üzerinden yapılır.
- Eksik ham noktalar doldurulmaz.
