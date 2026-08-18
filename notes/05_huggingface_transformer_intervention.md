# Hugging Face / Transformer Internal Representation — Experiment Note

## 1. Experiment purpose

This experiment extends the Glass Box AI workflow from a small supervised neural network to an open-source Transformer model. The goal is not only to observe the model output, but to inspect internal representations and test whether an observed internal dimension has a specific causal influence on the output.

Core research question:

> Does an observed internal representation dimension play a specifically causal role in the model's output, or can similar output changes be produced by arbitrary internal dimensions?

The experiment follows:

`MODEL → INTERNAL REPRESENTATION → OBSERVATION → CANDIDATE → INTERVENTION → OUTPUT CHANGE → RANDOM CONTROL → VALIDATION`

## 2. Model and setup

- Model: `distilgpt2`
- Framework: Hugging Face Transformers / PyTorch
- Hidden representation size: 768 dimensions
- Task: next-token prediction
- Main analysis uses the final Transformer block output through a forward hook.

Important implementation detail: the hook is registered on `model.transformer.h[-1]`. Therefore the intervention modifies the output of the final Transformer block before GPT-2's final layer normalization (`ln_f`) and language-model head. It should not be described as an intervention after the final normalization.

## 3. Initial representation analysis

A controlled 16-sentence exploratory dataset was constructed around four groups:

- Electrical engineering
- Transformer
- Motor
- Computer

For each sentence, the final-token representation was extracted. The representation matrix had shape `[16, 768]`.

Several dimensions were examined using variation and group-separation measures. Dimension `471` was selected as an exploratory candidate because it showed strong group separation relative to within-group variation.

This selection was exploratory. A separated representation dimension is not automatically a causal feature.

## 4. Candidate intervention: Dimension 471

The intervention set dimension 471 to zero at the output of the final Transformer block:

`modified_output[:, :, 471] = 0`

The baseline and intervention probability distributions were compared using:

- L1 probability change
- Maximum probability change
- Top-1 token change

The intervention produced larger effects for some Electrical Engineering examples and changed the top-1 prediction for one example. However, this alone was not treated as proof of causality.

## 5. Single random control

Dimension `655` was selected as a random control and subjected to the same zero intervention.

The mean L1 changes were:

- Dimension 471: `0.013924`
- Dimension 655: `0.014129`

Mean maximum probability change:

- Dimension 471: `0.002202`
- Dimension 655: `0.002879`

Thus the candidate did not outperform this single random control on the overall mean effect.

## 6. Multiple random controls

To avoid relying on one arbitrary control dimension, 20 random dimensions were selected with `random.seed(123)` while excluding dimension 471:

`53, 274, 89, 417, 272, 110, 39, 388, 550, 576, 340, 348, 163, 138, 345, 575, 341, 719, 251, 167`

Each dimension was zeroed independently using the same intervention procedure and evaluated on the same 16 sentences and baseline distributions.

Mean L1 changes:

| Dimension | Mean L1 change |
|---:|---:|
| 53 | 0.022478 |
| 274 | 0.009072 |
| 89 | 0.018436 |
| 417 | 0.008736 |
| 272 | 0.008453 |
| 110 | 0.009402 |
| 39 | 0.007884 |
| 388 | 0.010355 |
| 550 | 0.024153 |
| 576 | 0.010553 |
| 340 | 0.015105 |
| 348 | 0.017517 |
| 163 | 0.012270 |
| 138 | 0.021835 |
| 345 | 0.015546 |
| 575 | 0.011092 |
| 341 | 0.008219 |
| 719 | 0.009677 |
| 251 | 0.024040 |
| 167 | 0.034599 |

Candidate dimension 471:

- Mean L1 change: `0.013924`
- Rank including candidate: `10 / 21`
- Number of random controls with greater effect: `9`
- Random-control mean: `0.014971`
- Random-control median: `0.011681`
- Percentile relative to the tested random controls: `55.0%`

## 7. Scientific interpretation

The evidence does **not** support identifying dimension 471 as a uniquely causal feature.

The correct conclusion is:

> Dimension 471 showed exploratory group separation and produced context-dependent output changes under intervention, but its intervention effect was not exceptional relative to the tested random dimensions. Therefore, the experiment provides insufficient evidence to identify dimension 471 as a specific causal feature.

This is an informative negative result, not a failed experiment. It demonstrates the distinction between:

`OBSERVATION / CORRELATION → CANDIDATE HYPOTHESIS`

and

`CONTROLLED INTERVENTION → CAUSAL EVIDENCE`

## 8. Methodological limitations identified

### 8.1 Dataset confounding

The four groups use different sentence templates, for example:

- `Electrical engineering is ...`
- `The transformer is ...`
- `The motor is ...`
- `The computer ...`

Therefore the representation differences may reflect syntax, tokenization, sentence position, or general context rather than a clean semantic concept.

### 8.2 Candidate-selection bias

Dimension 471 was selected using the same 16 examples later used for intervention testing. This creates exploratory selection bias. A stronger future design should use a discovery set for candidate selection and a held-out set for validation.

### 8.3 Random-control sample size

Twenty random controls are useful as an initial control distribution, but they are not a definitive statistical test. More controls and repeated experiments can strengthen the comparison.

### 8.4 Intervention magnitude

Zeroing a dimension is a strong intervention and may move the representation outside its normal distribution. Future experiments should consider magnitude-matched interventions, such as controlled decrease/increase relative to the dimension's natural activation distribution.

## 9. Research conclusion

This experiment establishes the practical workflow for moving from Black Box observation toward Glass Box investigation on a Transformer:

`OUTPUT OBSERVATION → INTERNAL REPRESENTATION → CANDIDATE → INTERVENTION → RANDOM CONTROL → VALIDATION`

The main lesson is:

> A dimension can correlate with group behavior and its manipulation can change the output, while still failing to show a uniquely causal role when compared with appropriate controls.

The next experiment should use a more tightly matched dataset and held-out validation examples before making stronger claims about semantic features or causal mechanisms.
