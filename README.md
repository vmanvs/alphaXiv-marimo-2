# Attention Sinks in marimo

Competition target: alphaXiv x marimo Notebook Competition #2

Notebook paper: "Why do LLMs attend to the first token?" by Federico Barbero, Alvaro Arroyo, Xiangming Gu, Christos Perivolaropoulos, Michael Bronstein, Petar Velickovic, and Razvan Pascanu.

Paper links:

- alphaXiv: https://www.alphaxiv.org/abs/2504.02732
- arXiv: https://arxiv.org/abs/2504.02732

## Notebook Thesis

First-token attention sinks are not just weird attention maps. The paper argues that they help deep causal Transformers avoid over-mixing: by sending attention to a low-information first position, some heads can behave closer to no-ops and reduce how strongly perturbations spread through the sequence.

This repo turns that idea into an interactive marimo notebook.

## Run Locally

Install dependencies in a Python environment:

```powershell
pip install -r requirements.txt
```

Open the notebook:

```powershell
marimo edit notebooks/first_token_sink.py
```

The notebook defaults to a small Hugging Face causal language model. For a competition run, use a GPU-backed molab environment and switch to a stronger model such as `gpt2` or `gpt2-medium`.

## Interactivity

The notebook is interactive in the marimo sense: controls define values, and every downstream cell that depends on those values recomputes automatically.

The first version includes:

- model selector
- prompt preset plus custom prompt
- first-token anchor mode
- max token budget
- sink threshold
- layer selector
- attention head selector
- selected-head attention heatmap
- whole-model sink-rate map
- perturbation probe comparing hidden-state drift after a small prompt edit

## Competition Checklist

- Meaningfully engage with the paper: explain attention sinks as anti-over-mixing mechanisms.
- Add an original angle: a small, interactive perturbation probe on user-chosen prompts.
- Use marimo UI for real exploration, not decorative controls.
- Use GPU when available through PyTorch model inference.
- Keep the notebook readable, deterministic, and self-contained.
- Publish to molab, record a video under 5 minutes, and submit before the competition deadline.

