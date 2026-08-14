# Experimental Results Summary

## Baseline

- MNIST: 60000 train / 10000 test
- Architecture: `784 → 128 → ReLU → 64 → ReLU → 10`
- Seed: 42
- Adam, LR 0.001, batch 64, 5 epochs
- Test accuracy: **97.56%**
- Recorded epoch training loss: `0.3328, 0.1354, 0.0945, 0.0717, 0.0558`

## Internal representation

- ReLU2 test activation matrix: `10000 × 64`
- Candidate Class-0 group: `[47,17,57,53,28]`
- N47 selectivity: `3.1630`
- N17 selectivity: `2.1927`

## Neuron-level evidence

| Intervention | Result |
|---|---:|
| N47 ablation — Class 0 | −0.9184 pp |
| N17 ablation — Class 0 | −0.8164 pp |
| N47 activation scale 0→2 — true C0 probability | 0.9640 → 0.9853 |
| N17 activation scale 0→2 — true C0 probability | 0.9619 → 0.9863 |

## Circuit-level evidence

| Test | Result |
|---|---:|
| Candidate circuit ablation — Class 0 | **−12.0408 pp** |
| Random controls mean | −0.1122 pp |
| Candidate vs random mean | −11.9286 pp |
| Class 1 control | +0.0881 pp |
| Class 2 control | 0.0000 pp |
| Leave-One-Out strongest context effect | N57, −9.0816 pp |
| Progressive ablation | −0.9184 → −12.0408 pp |
| Class 1 target logit patch | +6.0245 C0 logit |
| Class 2 target logit patch | +4.3068 C0 logit |
| Circuit intervention scale 0→2 | 0.7644 → 0.9938 true C0 probability |

## Interpretation

The candidate group `[47,17,57,53,28]` provides strong causal evidence/support for a distributed, Class-0-biased internal mechanism. It is not Class-0-exclusive and is not claimed to be the complete or unique circuit. Observation, intervention and control results are kept conceptually separate.

## Reproducibility note

The original numerical results above were recorded from the completed Colab experiments. The updated baseline notebook now also records epoch-level train/test loss and accuracy to generate the missing learning-curve figures. Those new curves must be run in Colab before being treated as experimental results.
