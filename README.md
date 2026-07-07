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

The notebook defaults to a small Hugging Face causal language model. For the competition run, sync the repo into molab, attach the RTX Pro 6000 runtime, and use the cloud GPU sections with fp16 enabled.

Recommended cloud sequence:

1. Run the notebook once with `LOCAL · distilgpt2 interactive default` to verify the flow.
2. Switch to `CLOUD · Qwen2.5 7B open` with `fp16 on CUDA, fp32 on CPU`.
3. Run the anchor-ablation perturbation probe.
4. Run the streaming cache diagnostic.
5. Run the model-family sweep. Qwen should work without special access; Gemma and LLaMA may require Hugging Face authentication.
6. Run the long-context sweep from 128 to 2048 tokens.

## Interactivity

The notebook is interactive in the marimo sense: controls define values, and every downstream cell that depends on those values recomputes automatically.

The first version includes:

- model selector
- execution mode selector
- fp16/bf16/fp32 dtype selector
- prompt preset plus custom prompt
- first-token anchor mode
- max token budget
- sink threshold
- layer selector
- attention head selector
- selected-head attention heatmap
- whole-model sink-rate map
- streaming-cache diagnostic
- perturbation probe comparing hidden-state drift after a small prompt edit
- run-button-gated cloud GPU sweeps across Qwen, Gemma, and LLaMA-style models
- run-button-gated context-length sweep

## Competition Checklist

- Meaningfully engage with the paper: explain attention sinks as anti-over-mixing mechanisms.
- Add an original angle: a small, interactive perturbation probe on user-chosen prompts.
- Use marimo UI for real exploration, not decorative controls.
- Use GPU when available through PyTorch model inference.
- Keep the notebook readable, deterministic, and self-contained.
- Keep expensive cloud experiments gated behind explicit run buttons.
- Publish to molab, record a video under 5 minutes, and submit before the competition deadline.
