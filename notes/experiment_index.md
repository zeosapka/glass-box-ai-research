# Experiment Index

Bu indeks, Colab'da gerçekleştirilen deneylerin GitHub kayıtlarını tek noktadan gösterir.

| ID | Deney | Ana ölçüm | Durum |
|---:|---|---|---|
| E01 | Baseline | Test accuracy 97.56%, loss history | Tamamlandı |
| E02 | Activation Analysis | 10000×64 ReLU2 matrix | Tamamlandı |
| E03 | Class Activation / Selectivity | Candidate neuron ranking | Tamamlandı |
| E04 | Single-Neuron Ablation | N47 Class0 −0.9184 pp | Tamamlandı |
| E05 | Activation Intervention | N47 C0 probability 0.9640→0.9853 | Tamamlandı |
| E06 | Correlation vs Causality | N17/N47 r=0.4485 overall, 0.7846 C0 | Tamamlandı |
| E07 | Circuit Candidate | [47,17,57,53,28] | Tamamlandı |
| E08 | Combined Ablation | N17+N47 non-additivity | Tamamlandı |
| E09 | Activation Patching | Top-1/3/5 transfer | Tamamlandı |
| E10 | Class-Specific Patching | Context-dependent control | Tamamlandı |
| E11 | Logit Patching | +6.0245 / +4.3068 C0 logit | Tamamlandı |
| E12 | Circuit Contribution | Candidate group logit contributions | Tamamlandı |
| E13 | Circuit Ablation | Class0 −12.0408 pp | Tamamlandı |
| E14 | Class-Wise Control | Class1 +0.0881 pp, Class2 0 | Tamamlandı |
| E15 | Leave-One-Out | N57 −9.0816 pp | Tamamlandı |
| E16 | Progressive Ablation | 1→5 neurons −0.9184→−12.0408 pp | Tamamlandı |
| E17 | Random Controls | Mean −0.1122 pp | Tamamlandı |
| E18 | Circuit Intervention | C0 probability 0.7644→0.9938 | Tamamlandı |
| E19 | Mechanistic Validation | Candidate vs random + class controls | Tamamlandı |

## Source of truth

Birinci haftanın sayısal sonuçlarının ham/detaylı kaydı `notes/experiment_log.md` dosyasında korunmaktadır.

Hocanın istediği standart deney günlüğü formatına göre yeniden düzenlenmiş kayıt ise:

`notes/experiment_log_week1_standardized.md`

İkinci haftadan itibaren her deney için hedef başarım kriteri, doğrulama sonucu, varsa istatistiksel anlamlılık ve commit hash alanları da deney kaydına eklenecektir.
