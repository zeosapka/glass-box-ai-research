# Figure Index

Bu klasördeki SVG grafikler deney günlüğünde kaydedilmiş gerçek ölçümlerin okunabilir, GitHub üzerinde doğrudan görüntülenebilir sürümleridir. Grafiklerde yeni deney sonucu uydurulmamıştır.

| # | Figure | İçerik | Kaynak |
|---:|---|---|---|
| 1 | `ablation_accuracy.svg` | Baseline / N47 / N17 / candidate circuit Class 0 accuracy | E04, E13 |
| 2 | `progressive_circuit_ablation.svg` | 1→5 candidate neuron progressive ablation | E20 |
| 3 | `circuit_intervention_probability.svg` | Circuit scale vs true Class 0 probability | E18 |
| 4 | `neuron_intervention_n47.svg` | N47 scale vs true Class 0 probability | E05 |
| 5 | `activation_correlation.svg` | N17–N47 Pearson correlation | E06 |
| 6 | `baseline_training_loss.svg` | Epoch 1–5 training loss | Baseline |
| 7 | `candidate_circuit_activation_classes.svg` | Candidate neuron mean activations for Classes 0–2 | E07 / E64 |
| 8 | `class_correct_predictions.svg` | MNIST class-wise correct prediction counts (confusion-matrix diagonal) | Baseline |
| 9 | `selectivity_top10.svg` | Top-10 neuron selectivity values | E03 |
| 10 | `leave_one_out.svg` | Candidate-group Leave-One-Out Class 0 accuracy | E18 / E46 |
| 11 | `candidate_group_logit_contribution.svg` | Candidate neuron mean contribution to Class 0 logit | E41 |

## Not

Colab'daki bazı orijinal grafikler ham runtime verisine bağlıydı. GitHub'a yalnızca deney günlüğünde sayısal olarak doğrulanabilen veriler taşındı; eksik ham noktalar uydurulmadı. Bu nedenle `class_correct_predictions.svg`, tam confusion-matrix görselinin yerine yalnızca kaydedilmiş diagonal doğru tahmin sayılarını gösterir.
