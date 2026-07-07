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

Open the local companion notebook:

```powershell
marimo edit notebooks/first_token_sink_local.py
```

The competition notebook is `notebooks/first_token_sink.py`. It is tuned for molab with the attached RTX Pro 6000 and no longer includes local model choices. The local companion notebook is `notebooks/first_token_sink_local.py`; use it for CPU/small-GPU tinkering with `distilgpt2`, GPT-2 small, and GPT-2 medium.

Recommended cloud sequence:

1. Open `notebooks/first_token_sink.py` in molab after syncing from GitHub.
2. Attach the RTX Pro 6000 runtime.
3. For gated Hugging Face models, set `HF_TOKEN` / `HUGGING_FACE_HUB_TOKEN` in the cloud runtime or submit a read token through the notebook's masked Hugging Face token form. Public Qwen models should work without a token.
4. Select `Qwen2.5 7B open` with `fp16 on CUDA, fp32 on CPU`.
5. Click `Select probe configuration`, then `Load model and run attention probe`.
6. Run the anchor-ablation perturbation probe.
7. Run the streaming cache diagnostic.
8. Run the model-family sweep. Qwen should work without special access; Gemma and LLaMA may require Hugging Face authentication.
9. Run the long-context sweep from 128 to 2048 tokens.

Recommended local sequence:

1. Open `notebooks/first_token_sink_local.py`.
2. Start with `distilgpt2 local default`.
3. Run the anchor-ablation perturbation probe.
4. Run the streaming cache diagnostic.
5. Optionally compare `GPT-2 small` and `GPT-2 medium`.

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

The local companion keeps the same interactive mechanics but restricts model choices to smaller GPT-style models.

## Competition Checklist

- Meaningfully engage with the paper: explain attention sinks as anti-over-mixing mechanisms.
- Add an original angle: a small, interactive perturbation probe on user-chosen prompts.
- Use marimo UI for real exploration, not decorative controls.
- Use GPU when available through PyTorch model inference.
- Keep the notebook readable, deterministic, and self-contained.
- Keep expensive cloud experiments gated behind explicit run buttons.
- Publish to molab, record a video under 5 minutes, and submit before the competition deadline.
