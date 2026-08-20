# Experiment Index

Bu indeks, araştırmadaki deney kayıtlarının tek noktadan navigasyonunu sağlar.

## Week 1

| ID | Deney | Ana ölçüm | Standart kayıt |
|---:|---|---|---|
| E01 | Baseline | Test accuracy 97.56% | `experiments/week1_experiment_records.md` |
| E02 | Activation Analysis | 10000×64 ReLU2 matrix | `experiments/week1_experiment_records.md` |
| E03 | Class Activation / Selectivity | Candidate ranking | `experiments/week1_experiment_records.md` |
| E04 | Single-Neuron Ablation | N47 Class0 −0.9184 pp | `experiments/week1_experiment_records.md` |
| E05 | Activation Intervention | N47 C0 probability 0.9640→0.9853 | `experiments/week1_experiment_records.md` |
| E06 | Correlation vs Causality | r=0.4485 overall, 0.7846 C0 | `experiments/week1_experiment_records.md` |
| E07 | Candidate Circuit Discovery | [47,17,57,53,28] | `experiments/week1_experiment_records.md` |
| E08 | Combined Ablation | Non-additivity | `experiments/week1_experiment_records.md` |
| E09 | Activation Patching | Top-1/2-neuron patch effects | `experiments/week1_experiment_records.md` |
| E10 | Distributed Feature Patching | Top-1/3/5 transfer | `experiments/week1_experiment_records.md` |
| E11 | Class-Specific Patching Control | Context-dependent control | `experiments/week1_experiment_records.md` |
| E12 | Logit-Level Patching | +6.0245 / +4.3068 C0 logit | `experiments/week1_experiment_records.md` |
| E13 | Candidate Group Contribution | C0 contribution +6.197485 | `experiments/week1_experiment_records.md` |
| E14 | All-Logit Contribution | Candidate effects across logits | `experiments/week1_experiment_records.md` |
| E15 | Candidate Circuit Ablation | Class0 −12.0408 pp | `experiments/week1_experiment_records.md` |
| E16 | Class-Specific Circuit Control | Class1 +0.0881 pp, Class2 0 | `experiments/week1_experiment_records.md` |
| E17 | Leave-One-Out | N57 −9.0816 pp | `experiments/week1_experiment_records.md` |
| E18 | Progressive Ablation | 1→5 neurons −0.9184→−12.0408 pp | `experiments/week1_experiment_records.md` |
| E19 | Random Controls / Mechanistic Validation | Random mean −0.1122 pp vs candidate −12.0408 pp | `experiments/week1_experiment_records.md` |

## Source of truth

- Ayrıntılı ham sayısal kayıt: `notes/experiment_log.md`
- Standart deney kayıtları: `experiments/week1_experiment_records.md`
- Grafik kayıtları: `figures/figure_index.md`

Week 2 deneylerinde aynı şablona ek olarak **Success Criterion**, **Verification Result**, **Statistical Significance** ve **Commit Hash** alanları kullanılacaktır.
