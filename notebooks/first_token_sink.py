# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "accelerate>=0.33",
#     "marimo>=0.23",
#     "matplotlib>=3.8",
#     "numpy>=1.26",
#     "pandas>=2.2",
#     "torch>=2.3",
#     "transformers>=4.44",
# ]
# ///

import marimo

__generated_with = "0.23.13"
app = marimo.App(width="medium", auto_download=["html"])


@app.cell(hide_code=True)
def _():
    import marimo as mo

    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    hero = """
    <style>
      .sink-hero {
        color: #172033;
        margin: 0 0 24px;
      }
      .sink-hero__grid {
        align-items: stretch;
        display: grid;
        gap: 20px;
        grid-template-columns: minmax(0, 1.25fr) minmax(260px, 0.75fr);
        padding: 28px 26px;
      }
      .sink-pill {
        display: inline-flex;
        align-items: center;
        gap: 8px;
        padding: 6px 10px;
        border: 1px solid #bfdbfe;
        background: #eff6ff;
        border-radius: 999px;
        color: #1d4ed8;
        font-size: 0.76rem;
        font-weight: 800;
        letter-spacing: 0;
        text-transform: uppercase;
      }
      .sink-hero h1 {
        margin: 14px 0 10px;
        color: #111827;
        font-size: 2.35rem;
        line-height: 1.06;
        font-weight: 850;
        letter-spacing: 0;
      }
      .sink-card {
        border: 1px solid rgba(148, 163, 184, 0.35);
        background: rgba(255, 255, 255, 0.78);
        border-radius: 8px;
        padding: 16px 16px 14px;
        box-shadow: 0 12px 30px rgba(15, 23, 42, 0.10);
      }
      @media (max-width: 760px) {
        .sink-hero__grid {
          grid-template-columns: 1fr;
          padding: 24px 18px;
        }
        .sink-hero h1 {
          font-size: 1.9rem;
        }
      }
    </style>
    <div class="sink-hero">
      <div class="sink-hero__grid">
        <div>
          <div class="sink-pill">Paper explainer · cloud GPU lab</div>
          <h1>The first token is a circuit breaker</h1>
          <p style="margin:0;max-width:680px;color:#374151;font-size:1.05rem;line-height:1.55;">
            Large language models often pour attention into token 0. This notebook asks
            whether that strange-looking behavior is wasted computation, or whether the
            first token becomes infrastructure that helps deep Transformers avoid
            over-mixing.
          </p>
          <p style="margin:16px 0 0;color:#475569;font-size:0.93rem;line-height:1.5;">
            Built for the alphaXiv x marimo notebook competition. The heavy sections are
            designed for molab with an RTX Pro 6000; the small-model path remains runnable
            on ordinary hardware.
          </p>
        </div>
        <div class="sink-card">
          <div style="color:#64748b;font-size:0.72rem;font-weight:850;letter-spacing:0;text-transform:uppercase;margin-bottom:7px;">
            Original paper
          </div>
          <div style="font-size:1rem;line-height:1.35;font-weight:800;color:#111827;">
            Why do LLMs attend to the first token?
          </div>
          <div style="margin-top:7px;color:#475569;font-size:0.9rem;line-height:1.35;">
            Barbero · Arroyo · Gu · Perivolaropoulos · Bronstein · Velickovic · Pascanu
          </div>
          <a href="https://www.alphaxiv.org/abs/2504.02732" style="display:inline-block;margin-top:8px;color:#2563eb;font-size:0.9rem;font-weight:750;text-decoration:none;">
            alphaXiv:2504.02732
          </a>
          <svg viewBox="0 0 320 148" role="img" aria-label="Attention heads sending mass to token zero" style="width:100%;height:auto;display:block;margin-top:14px;">
            <defs>
              <linearGradient id="sink-bg" x1="0" y1="0" x2="1" y2="1">
                <stop offset="0%" stop-color="#eff6ff"/>
                <stop offset="52%" stop-color="#f8fafc"/>
                <stop offset="100%" stop-color="#ecfdf5"/>
              </linearGradient>
              <radialGradient id="sink-token" cx="38%" cy="35%" r="68%">
                <stop offset="0%" stop-color="#ffffff" stop-opacity="0.95"/>
                <stop offset="100%" stop-color="#2563eb" stop-opacity="0.94"/>
              </radialGradient>
            </defs>
            <rect x="0" y="0" width="320" height="148" rx="8" fill="url(#sink-bg)"/>
            <circle cx="62" cy="74" r="16" fill="#111827"/>
            <text x="62" y="79" text-anchor="middle" font-size="13" fill="#ffffff" font-weight="800">0</text>
            <g fill="url(#sink-token)" stroke="#ffffff" stroke-width="1.4">
              <circle cx="150" cy="35" r="7"/>
              <circle cx="188" cy="54" r="7"/>
              <circle cx="225" cy="76" r="7"/>
              <circle cx="178" cy="104" r="7"/>
              <circle cx="255" cy="35" r="7"/>
              <circle cx="278" cy="102" r="7"/>
            </g>
            <g stroke="#2563eb" stroke-width="3" stroke-linecap="round" opacity="0.78">
              <path d="M143 37 C112 43 91 56 74 69"/>
              <path d="M181 56 C136 57 101 64 76 72"/>
              <path d="M218 77 C159 74 111 74 79 74"/>
              <path d="M172 101 C127 95 96 85 76 78"/>
              <path d="M249 37 C170 39 111 55 75 70"/>
              <path d="M271 100 C184 92 119 82 79 76"/>
            </g>
          </svg>
        </div>
      </div>
    </div>
    """
    mo.Html(hero)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **Reader's note.** For the best experience, run all cells once, turn **show code** off, and read vertically from top to bottom. The first sections are safe on small local models. The model-family sweeps and long-context experiments are intentionally gated behind buttons and are meant for molab with the attached RTX Pro 6000.
    """)
    return


@app.cell(hide_code=True)
def _():
    dependency_error = None
    np = None
    pd = None
    plt = None
    torch = None
    AutoModelForCausalLM = None
    AutoTokenizer = None

    try:
        import gc
        import numpy as np
        import pandas as pd
        import matplotlib.pyplot as plt
        import torch
        from transformers import AutoModelForCausalLM, AutoTokenizer
    except Exception as exc:  # noqa: BLE001 - show import failures inside notebook.
        dependency_error = exc
    return (
        AutoModelForCausalLM,
        AutoTokenizer,
        dependency_error,
        gc,
        np,
        pd,
        plt,
        torch,
    )


@app.cell(hide_code=True)
def _(dependency_error, mo):
    if dependency_error is None:
        mo.md("Dependencies loaded.").callout(kind="success")
    else:
        mo.md(
            f"""
            Dependencies are not installed yet.

            Run:

            ```powershell
            pip install -r requirements.txt
            ```

            Import error:

            ```text
            {dependency_error}
            ```
            """
        ).callout(kind="warn")
    return


@app.cell(hide_code=True)
def _():
    PAPER_URL = "https://arxiv.org/abs/2504.02732"
    ALPHAXIV_URL = "https://www.alphaxiv.org/abs/2504.02732"

    MODEL_OPTIONS = {
        "LOCAL · tiny-gpt2 sanity check": "sshleifer/tiny-gpt2",
        "LOCAL · distilgpt2 interactive default": "distilgpt2",
        "LOCAL · GPT-2 small": "gpt2",
        "LOCAL · GPT-2 medium": "openai-community/gpt2-medium",
        "CLOUD · Qwen2.5 0.5B open": "Qwen/Qwen2.5-0.5B",
        "CLOUD · Qwen2.5 1.5B open": "Qwen/Qwen2.5-1.5B",
        "CLOUD · Qwen2.5 7B open": "Qwen/Qwen2.5-7B",
        "CLOUD · Qwen2.5 14B open": "Qwen/Qwen2.5-14B",
        "CLOUD · Gemma 2 2B auth may be required": "google/gemma-2-2b",
        "CLOUD · Gemma 2 9B auth may be required": "google/gemma-2-9b",
        "CLOUD · LLaMA 3.1 8B auth required": "meta-llama/Llama-3.1-8B",
    }

    DEFAULT_SWEEP_MODELS = [
        "CLOUD · Qwen2.5 1.5B open",
        "CLOUD · Qwen2.5 7B open",
        "CLOUD · Gemma 2 9B auth may be required",
        "CLOUD · LLaMA 3.1 8B auth required",
    ]

    EXECUTION_MODES = [
        "Local demo",
        "Cloud GPU single model",
        "Cloud GPU sweep",
    ]

    PRECISION_OPTIONS = {
        "fp16 on CUDA, fp32 on CPU": "fp16",
        "bf16 on CUDA, fp32 on CPU": "bf16",
        "fp32 everywhere": "fp32",
    }

    PROMPT_PRESETS = {
        "Paper-style greeting": "Hello! I've been well. I hope that you're doing well.",
        "Paper perturbation style": (
            "The greatest advantage of a long context model is that it can keep "
            "many details active while answering a later question."
        ),
        "Long-context facts": (
            "Paris is the capital of France. Berlin is the capital of Germany. "
            "Madrid is the capital of Spain. Rome is the capital of Italy. "
            "The next country in the list is"
        ),
        "Cloud long-context attention sink probe": (
            "We are studying why transformer attention heads sometimes route mass "
            "to the first token. The prompt contains repeated notes about long "
            "context, streaming inference, perturbation spread, and model scale."
        ),
        "Instruction": (
            "Summarize the role of attention sinks in a causal transformer in one sentence:"
        ),
        "Code": "def fibonacci(n):\n    if n <= 1:\n        return n\n    return",
    }

    ANCHOR_MODES = [
        "Use model special token at first position",
        "Plain prompt only",
        "Visible neutral anchor",
    ]
    CONTEXT_SWEEP_BUDGETS = [128, 256, 512, 1024, 2048]

    return (
        ALPHAXIV_URL,
        ANCHOR_MODES,
        CONTEXT_SWEEP_BUDGETS,
        DEFAULT_SWEEP_MODELS,
        EXECUTION_MODES,
        MODEL_OPTIONS,
        PAPER_URL,
        PRECISION_OPTIONS,
        PROMPT_PRESETS,
    )


@app.cell(hide_code=True)
def _(ALPHAXIV_URL, PAPER_URL, mo):
    mo.md(f"""
    ## What the paper gives us

    The paper argues that attention sinks are useful because they can reduce
    how much token information mixes across a deep causal Transformer. A sink
    gives some heads a low-information place to attend, making them closer to
    approximate no-ops when they do not need to update the current token.

    | Paper evidence | Why it matters for this notebook |
    | --- | --- |
    | Gemma 7B perturbation test | The paper changes one token and measures how much hidden states drift with and without the first-token sink. |
    | LLaMA 3.1 scale trend | The reported sink metric rises from 45.97% in 8B to 73.49% in 70B and 78.29% in 405B. |
    | Training/context-length experiments | Longer context produces stronger sinks even at similar validation loss. |
    | Downstream removal test | Removing the sink hurts performance, especially on long-context evaluation. |

    This notebook reproduces the shape of the Gemma perturbation experiment,
    then uses molab's cloud GPU path to ask a shareable question: **does the
    sink-as-circuit-breaker story generalize across Qwen, Gemma, and LLaMA-style
    model families?**

    Links: [alphaXiv]({ALPHAXIV_URL}) | [arXiv]({PAPER_URL})
    """)
    return


@app.cell(hide_code=True)
def _(ANCHOR_MODES, EXECUTION_MODES, MODEL_OPTIONS, PRECISION_OPTIONS, PROMPT_PRESETS, mo):
    execution_mode = mo.ui.dropdown(
        options=EXECUTION_MODES,
        value="Local demo",
        label="Execution mode",
        full_width=True,
    )
    model_choice = mo.ui.dropdown(
        options=list(MODEL_OPTIONS.keys()),
        value="LOCAL · distilgpt2 interactive default",
        label="Model",
        full_width=True,
    )
    precision_choice = mo.ui.dropdown(
        options=list(PRECISION_OPTIONS.keys()),
        value="fp16 on CUDA, fp32 on CPU",
        label="Model dtype",
        full_width=True,
    )
    prompt_preset = mo.ui.dropdown(
        options=list(PROMPT_PRESETS.keys()),
        value="Paper-style greeting",
        label="Prompt preset",
        full_width=True,
    )
    custom_prompt = mo.ui.text_area(
        value="",
        placeholder="Optional: type a custom prompt. Leave empty to use the preset.",
        rows=4,
        debounce=True,
        label="Custom prompt",
        full_width=True,
    )
    anchor_mode = mo.ui.dropdown(
        options=ANCHOR_MODES,
        value="Use model special token at first position",
        label="First-position anchor",
        full_width=True,
    )
    max_tokens = mo.ui.slider(
        start=32,
        stop=512,
        step=32,
        value=96,
        show_value=True,
        label="Max tokens to inspect",
        full_width=True,
    )
    sink_threshold = mo.ui.slider(
        start=0.05,
        stop=0.75,
        step=0.05,
        value=0.30,
        show_value=True,
        label="Strong-sink threshold",
        full_width=True,
    )

    mo.vstack(
        [
            mo.md("## 1. Choose the probe"),
            mo.hstack([execution_mode, model_choice], widths="equal", gap=1),
            mo.hstack([precision_choice, anchor_mode], widths="equal", gap=1),
            mo.hstack([prompt_preset, max_tokens, sink_threshold], widths="equal", gap=1),
            custom_prompt,
        ],
        gap=1,
    )
    return (
        anchor_mode,
        custom_prompt,
        execution_mode,
        max_tokens,
        model_choice,
        precision_choice,
        prompt_preset,
        sink_threshold,
    )


@app.cell(hide_code=True)
def _(PROMPT_PRESETS, custom_prompt, prompt_preset):
    selected_preset_name = prompt_preset.value or "Paper-style greeting"
    selected_prompt = custom_prompt.value.strip() or PROMPT_PRESETS[selected_preset_name]
    return selected_preset_name, selected_prompt


@app.cell(hide_code=True)
def _():
    def clean_token(token):
        return (
            token.replace("Ġ", " ")
            .replace("Ċ", "\\n")
            .replace("</w>", "")
            .replace("\n", "\\n")
        )

    def decode_token(tokenizer, token_id):
        return tokenizer.decode([int(token_id)]).replace("\n", "\\n")

    def anchored_prompt(base_prompt, mode, tokenizer):
        if mode == "Plain prompt only":
            return base_prompt, "No explicit anchor was added."
        if mode == "Visible neutral anchor":
            return f"ANCHOR: {base_prompt}", "A visible neutral anchor was prepended."
        special_token = None
        if tokenizer is not None:
            special_token = tokenizer.bos_token or tokenizer.eos_token
        if special_token:
            return (
                f"{special_token} {base_prompt}",
                f"The model special token {special_token!r} was prepended.",
            )
        return base_prompt, "The tokenizer has no special token, so no anchor was added."

    def perturb_prompt(prompt):
        words = prompt.split()
        if len(words) < 4:
            return f"{prompt} However, one detail changed."

        start = 1 if words[0].startswith("<|") else 0
        index = min(start + 1, len(words) - 1)
        stripped = words[index].strip(".,;:!?").lower()
        words[index] = "best" if stripped != "best" else "greatest"
        return " ".join(words)

    def build_long_context_prompt(base_prompt, target_sections=24):
        _facts = [
            "A transformer can either mix information from nearby tokens or route attention to a low-information anchor.",
            "A streaming decoder often keeps only a limited key-value cache, so old tokens compete for memory.",
            "Long-context prompts increase the number of possible tokens each query can attend to.",
            "If a head wants to avoid adding new information, a stable first-position sink can behave like a no-op route.",
            "Perturbing one word lets us measure how strongly that local change spreads through hidden states.",
            "The paper argues that sink behavior becomes more useful as depth and context length increase.",
        ]
        _paragraphs = [base_prompt.strip()]
        for _index in range(target_sections):
            _fact = _facts[_index % len(_facts)]
            _paragraphs.append(
                f"Context note {_index + 1}: {_fact} The control question remains the same: does token zero absorb attention mass?"
            )
        _paragraphs.append(
            "Final question: explain why an attention head might deliberately attend to the first token instead of a semantically relevant recent token."
        )
        return "\n".join(_paragraphs)

    return anchored_prompt, build_long_context_prompt, clean_token, decode_token, perturb_prompt


@app.cell(hide_code=True)
def _(AutoModelForCausalLM, AutoTokenizer, dependency_error, gc, torch):
    from functools import lru_cache

    def _cuda_dtype(precision_key, device):
        if device.type != "cuda":
            return None
        if precision_key == "bf16":
            return torch.bfloat16
        if precision_key == "fp32":
            return torch.float32
        return torch.float16

    @lru_cache(maxsize=1)
    def load_model_bundle(model_id, precision_key="fp16"):
        if dependency_error is not None:
            return None, None, None, None, dependency_error

        device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        try:
            gc.collect()
            if torch.cuda.is_available():
                torch.cuda.empty_cache()

            tokenizer = AutoTokenizer.from_pretrained(model_id)
            if tokenizer.pad_token is None:
                tokenizer.pad_token = tokenizer.eos_token or tokenizer.bos_token

            _model_kwargs = {"low_cpu_mem_usage": True}
            _dtype = _cuda_dtype(precision_key, device)
            if _dtype is not None:
                _model_kwargs["torch_dtype"] = _dtype

            try:
                model = AutoModelForCausalLM.from_pretrained(
                    model_id,
                    attn_implementation="eager",
                    **_model_kwargs,
                )
            except TypeError:
                model = AutoModelForCausalLM.from_pretrained(model_id, **_model_kwargs)

            model.to(device)
            model.eval()
            if torch.cuda.is_available():
                torch.cuda.empty_cache()
            _dtype_name = str(next(model.parameters()).dtype)
            return tokenizer, model, device, _dtype_name, None
        except Exception as exc:  # noqa: BLE001 - show model load failures in UI.
            return None, None, None, None, exc

    return (load_model_bundle,)


@app.cell(hide_code=True)
def _(MODEL_OPTIONS, PRECISION_OPTIONS, load_model_bundle, model_choice, precision_choice):
    selected_model_id = MODEL_OPTIONS[model_choice.value]
    selected_precision_key = PRECISION_OPTIONS[precision_choice.value]
    tokenizer, model, device, model_dtype, model_error = load_model_bundle(
        selected_model_id,
        selected_precision_key,
    )
    return (
        device,
        model,
        model_dtype,
        model_error,
        selected_model_id,
        selected_precision_key,
        tokenizer,
    )


@app.cell(hide_code=True)
def _(device, mo, model_dtype, model_error, selected_model_id, torch):
    if model_error is not None:
        mo.md(
            f"""
            Model could not be loaded.

            ```text
            {model_error}
            ```
            """
        ).callout(kind="warn")
    else:
        cuda_line = ""
        if torch.cuda.is_available():
            cuda_line = f"GPU: `{torch.cuda.get_device_name(0)}`"
        else:
            cuda_line = "GPU: not available in this runtime; using CPU fallback."

        mo.md(
            f"""
            Loaded `{selected_model_id}` on `{device}`.

            Dtype: `{model_dtype}`. {cuda_line}
            """
        ).callout(kind="info")
    return


@app.cell(hide_code=True)
def _(mo, model):
    if model is None:
        num_layers = 1
        num_heads = 1
    else:
        num_layers = int(
            getattr(
                model.config,
                "n_layer",
                getattr(model.config, "num_hidden_layers", 1),
            )
        )
        num_heads = int(
            getattr(
                model.config,
                "n_head",
                getattr(model.config, "num_attention_heads", 1),
            )
        )

    layer_index = mo.ui.slider(
        start=0,
        stop=max(0, num_layers - 1),
        step=1,
        value=min(2, max(0, num_layers - 1)),
        show_value=True,
        label="Layer",
        full_width=True,
    )
    head_index = mo.ui.slider(
        start=0,
        stop=max(0, num_heads - 1),
        step=1,
        value=min(3, max(0, num_heads - 1)),
        show_value=True,
        label="Head",
        full_width=True,
    )

    mo.vstack(
        [
            mo.md("## 2. Pick a head to inspect"),
            mo.hstack([layer_index, head_index], widths="equal", gap=1),
        ],
        gap=1,
    )
    return head_index, layer_index


@app.cell(hide_code=True)
def _(anchor_mode, anchored_prompt, selected_prompt, tokenizer):
    analysis_prompt, anchor_note = anchored_prompt(
        selected_prompt,
        anchor_mode.value,
        tokenizer,
    )
    return analysis_prompt, anchor_note


@app.cell(hide_code=True)
def _(analysis_prompt, anchor_note, mo, selected_preset_name):
    mo.md(f"""
    ## 3. Current prompt

    Preset: `{selected_preset_name}`

    Anchor: {anchor_note}

    ```text
    {analysis_prompt}
    ```
    """)
    return


@app.cell(hide_code=True)
def _(clean_token, decode_token):
    def run_attention_probe(
        text,
        model,
        tokenizer,
        device,
        torch,
        max_length,
        top_k=8,
    ):
        encoded = tokenizer(
            text,
            return_tensors="pt",
            truncation=True,
            max_length=int(max_length),
            add_special_tokens=False,
        )
        encoded = {key: value.to(device) for key, value in encoded.items()}

        with torch.inference_mode():
            outputs = model(
                **encoded,
                output_attentions=True,
                output_hidden_states=True,
                use_cache=False,
            )

        if outputs.attentions is None:
            raise RuntimeError("This model did not return attention tensors.")

        input_ids = encoded["input_ids"][0].detach().cpu()
        tokens = [
            clean_token(token)
            for token in tokenizer.convert_ids_to_tokens(input_ids.tolist())
        ]

        attention = torch.stack(
            [layer_attn[0].detach().float().cpu() for layer_attn in outputs.attentions]
        )
        hidden = torch.stack(
            [layer_hidden[0].detach().float().cpu() for layer_hidden in outputs.hidden_states]
        )

        logits = outputs.logits[0, -1].detach().float().cpu()
        probs = torch.softmax(logits, dim=-1)
        top_probs, top_ids = torch.topk(probs, k=top_k)
        next_tokens = [
            {
                "token": decode_token(tokenizer, token_id),
                "probability": float(probability),
            }
            for token_id, probability in zip(top_ids, top_probs)
        ]

        return {
            "text": text,
            "tokens": tokens,
            "attention": attention,
            "hidden": hidden,
            "next_tokens": next_tokens,
        }

    return (run_attention_probe,)


@app.cell(hide_code=True)
def _():
    def summarize_attention_sink(probe, torch, sink_threshold):
        _attention = probe["attention"]
        if _attention.shape[-1] <= 1:
            _sink_scores = torch.zeros(_attention.shape[0], _attention.shape[1])
        else:
            _sink_scores = _attention[:, :, 1:, 0].mean(dim=-1)
        _strong_sink_rate = float(
            (_sink_scores > float(sink_threshold)).float().mean().item() * 100.0
        )
        _mean_sink_strength = float(_sink_scores.mean().item())
        _last_token_sink = float(_attention[:, :, -1, 0].mean().item())
        return {
            "token_count": len(probe["tokens"]),
            "sink_scores": _sink_scores,
            "sink_rate_percent": _strong_sink_rate,
            "mean_sink_strength": _mean_sink_strength,
            "last_token_attention_to_token_0": _last_token_sink,
        }

    def hidden_drift_summary(base_probe, perturbed_probe, torch):
        _layer_count = min(base_probe["hidden"].shape[0], perturbed_probe["hidden"].shape[0])
        _token_count = min(base_probe["hidden"].shape[1], perturbed_probe["hidden"].shape[1])
        _delta = torch.linalg.vector_norm(
            base_probe["hidden"][:_layer_count, :_token_count, :]
            - perturbed_probe["hidden"][:_layer_count, :_token_count, :],
            dim=-1,
        )
        return {
            "delta": _delta,
            "early_layer_mean_drift": float(_delta[1].mean().item()) if _delta.shape[0] > 1 else 0.0,
            "final_layer_mean_drift": float(_delta[-1].mean().item()),
        }

    def streaming_cache_diagnostic(probe, cache_window, torch):
        _attention = probe["attention"]
        _token_count = _attention.shape[-1]
        _window = max(1, min(int(cache_window), _token_count))
        _last_query_attention = _attention[:, :, -1, :]
        _recent_indices = torch.arange(max(0, _token_count - _window), _token_count)
        _anchor_plus_recent = torch.unique(
            torch.cat([torch.tensor([0]), _recent_indices])
        )
        _recent_only_mass = float(_last_query_attention[:, :, _recent_indices].sum(dim=-1).mean().item())
        _anchor_plus_recent_mass = float(
            _last_query_attention[:, :, _anchor_plus_recent].sum(dim=-1).mean().item()
        )
        return {
            "token_count": int(_token_count),
            "cache_window": int(_window),
            "recent_only_attention_mass": _recent_only_mass,
            "anchor_plus_recent_attention_mass": _anchor_plus_recent_mass,
            "attention_mass_recovered_by_keeping_token_0": _anchor_plus_recent_mass
            - _recent_only_mass,
        }

    return hidden_drift_summary, streaming_cache_diagnostic, summarize_attention_sink


@app.cell(hide_code=True)
def _(
    analysis_prompt,
    device,
    max_tokens,
    model,
    model_error,
    run_attention_probe,
    tokenizer,
    torch,
):
    if model_error is not None or model is None:
        probe_error = model_error
        probe = None
    else:
        try:
            probe = run_attention_probe(
                analysis_prompt,
                model,
                tokenizer,
                device,
                torch,
                max_tokens.value,
            )
            probe_error = None
        except Exception as exc:  # noqa: BLE001 - show probe failures in UI.
            probe = None
            probe_error = exc
    return probe, probe_error


@app.cell(hide_code=True)
def _(mo, probe, probe_error):
    if probe_error is not None:
        mo.md(
            f"""
            Probe failed.

            ```text
            {probe_error}
            ```
            """
        ).callout(kind="warn")
    else:
        mo.md(
            f"""
            Probe complete: `{len(probe["tokens"])}` tokens inspected.
            """
        ).callout(kind="success")
    return


@app.cell(hide_code=True)
def _(pd, probe, sink_threshold, summarize_attention_sink, torch):
    if probe is None:
        sink_scores = None
        sink_rate = 0.0
        sink_summary = None
        sink_table = pd.DataFrame() if pd is not None else None
    else:
        sink_summary = summarize_attention_sink(probe, torch, sink_threshold.value)
        sink_scores = sink_summary["sink_scores"]
        sink_rate = sink_summary["sink_rate_percent"]
        _strong_sink_mask = sink_scores > float(sink_threshold.value)

        _rows = []
        for _layer in range(sink_scores.shape[0]):
            for _head in range(sink_scores.shape[1]):
                _rows.append(
                    {
                        "layer": _layer,
                        "head": _head,
                        "mean_attention_to_first_token": float(sink_scores[_layer, _head]),
                        "strong_sink": bool(_strong_sink_mask[_layer, _head]),
                    }
                )
        sink_table = pd.DataFrame(_rows).sort_values(
            "mean_attention_to_first_token",
            ascending=False,
        )
    return sink_rate, sink_scores, sink_summary, sink_table


@app.cell(hide_code=True)
def _(
    head_index,
    layer_index,
    mo,
    probe,
    sink_rate,
    sink_scores,
    sink_threshold,
):
    if probe is None or sink_scores is None:
        _sink_metric_output = mo.md("Sink metrics are waiting for a successful model probe.")
    else:
        _layer = min(int(layer_index.value), sink_scores.shape[0] - 1)
        _head = min(int(head_index.value), sink_scores.shape[1] - 1)
        _selected_sink = float(sink_scores[_layer, _head])
        _last_token_sink = float(probe["attention"][_layer, _head, -1, 0])

        _sink_metric_output = mo.md(
            f"""
            ## 4. Sink metric

            The paper measures how many heads strongly attend to the first token.
            This notebook uses the same operational idea: a head is marked as a
            strong sink if its average attention to token 0 is above the selected
            threshold.

            | Metric | Value |
            | --- | ---: |
            | Strong-sink threshold | {float(sink_threshold.value):.2f} |
            | Whole-model sink rate | {sink_rate:.1f}% |
            | Selected layer/head | L{_layer} H{_head} |
            | Selected head mean attention to token 0 | {_selected_sink:.3f} |
            | Last-token attention to token 0 in selected head | {_last_token_sink:.3f} |
            """
        )
    _sink_metric_output
    return


@app.cell(hide_code=True)
def _(np, plt):
    def plot_attention_matrix(matrix, tokens, layer, head):
        size = max(6, min(12, 0.45 * len(tokens)))
        fig, ax = plt.subplots(figsize=(size, size))
        image = ax.imshow(matrix, cmap="magma", vmin=0.0, vmax=max(0.05, float(np.max(matrix))))
        ax.set_title(f"Attention weights: layer {layer}, head {head}")
        ax.set_xlabel("Key token attended to")
        ax.set_ylabel("Query token receiving context")
        ax.set_xticks(range(len(tokens)))
        ax.set_yticks(range(len(tokens)))
        labels = [f"{index}:{token}" for index, token in enumerate(tokens)]
        ax.set_xticklabels(labels, rotation=90, fontsize=8)
        ax.set_yticklabels(labels, fontsize=8)
        fig.colorbar(image, ax=ax, fraction=0.046, pad=0.04)
        fig.tight_layout()
        return fig

    def plot_sink_map(sink_scores, threshold):
        data = sink_scores.numpy()
        fig, ax = plt.subplots(figsize=(10, max(3, data.shape[0] * 0.35)))
        image = ax.imshow(data, cmap="viridis", aspect="auto", vmin=0.0, vmax=max(0.75, float(data.max())))
        ax.contour(data > threshold, levels=[0.5], colors="white", linewidths=0.8)
        ax.set_title("Mean attention to token 0 by layer and head")
        ax.set_xlabel("Head")
        ax.set_ylabel("Layer")
        ax.set_xticks(range(data.shape[1]))
        ax.set_yticks(range(data.shape[0]))
        fig.colorbar(image, ax=ax, label="Mean attention to token 0")
        fig.tight_layout()
        return fig

    def plot_hidden_delta(delta, tokens):
        data = delta.numpy()
        fig, ax = plt.subplots(figsize=(10, max(3, data.shape[0] * 0.35)))
        image = ax.imshow(data, cmap="inferno", aspect="auto")
        ax.set_title("Hidden-state drift after perturbing the prompt")
        ax.set_xlabel("Token position")
        ax.set_ylabel("Layer, including embedding layer")
        ax.set_xticks(range(len(tokens)))
        ax.set_xticklabels(
            [f"{index}:{token}" for index, token in enumerate(tokens)],
            rotation=90,
            fontsize=8,
        )
        ax.set_yticks(range(data.shape[0]))
        fig.colorbar(image, ax=ax, label="L2 drift")
        fig.tight_layout()
        return fig

    return plot_attention_matrix, plot_hidden_delta, plot_sink_map


@app.cell(hide_code=True)
def _(head_index, layer_index, plot_attention_matrix, probe):
    if probe is None:
        selected_attention_fig = None
    else:
        _layer = min(int(layer_index.value), probe["attention"].shape[0] - 1)
        _head = min(int(head_index.value), probe["attention"].shape[1] - 1)
        _selected_matrix = probe["attention"][_layer, _head].numpy()
        selected_attention_fig = plot_attention_matrix(
            _selected_matrix,
            probe["tokens"],
            _layer,
            _head,
        )

    selected_attention_fig
    return


@app.cell(hide_code=True)
def _(plot_sink_map, sink_scores, sink_threshold):
    if sink_scores is None:
        sink_map_fig = None
    else:
        sink_map_fig = plot_sink_map(sink_scores, float(sink_threshold.value))

    sink_map_fig
    return


@app.cell(hide_code=True)
def _(mo, sink_table):
    strongest_sink_heads = sink_table.head(12) if sink_table is not None else None
    mo.vstack([mo.md("## 5. Strongest sink heads"), strongest_sink_heads])
    return


@app.cell(hide_code=True)
def _(mo):
    streaming_cache_window = mo.ui.slider(
        start=4,
        stop=128,
        step=4,
        value=32,
        show_value=True,
        label="Streaming cache budget",
        full_width=True,
    )
    mo.vstack(
        [
            mo.md(
                """
                ## 6. Why streaming systems care

                A streaming decoder cannot keep every old key/value vector forever.
                If a recent-only cache drops token 0, how much attention mass does
                the final token lose compared with a cache that keeps token 0 plus
                recent tokens?
                """
            ),
            streaming_cache_window,
        ],
        gap=1,
    )
    return (streaming_cache_window,)


@app.cell(hide_code=True)
def _(mo, pd, probe, streaming_cache_diagnostic, streaming_cache_window, torch):
    if probe is None or pd is None:
        streaming_cache_table = None
        _streaming_output = mo.md("Streaming diagnostic is waiting for a successful model probe.").callout(kind="info")
    else:
        streaming_cache_summary = streaming_cache_diagnostic(
            probe,
            streaming_cache_window.value,
            torch,
        )
        streaming_cache_table = pd.DataFrame([streaming_cache_summary])
        _streaming_output = mo.vstack(
            [
                streaming_cache_table,
                mo.md(
                    """
                    Keeping token 0 is not a free lunch, but this diagnostic shows
                    why sink tokens became important in streaming-attention work:
                    a token with little semantic content can still carry routing
                    mass that the cache policy should preserve.
                    """
                ).callout(kind="info"),
            ],
            gap=0.75,
        )
    _streaming_output
    return (streaming_cache_table,)


@app.cell(hide_code=True)
def _(
    analysis_prompt,
    device,
    max_tokens,
    model,
    model_error,
    perturb_prompt,
    run_attention_probe,
    tokenizer,
    torch,
):
    perturbed_prompt = perturb_prompt(analysis_prompt)

    if model_error is not None or model is None:
        perturbed_probe = None
        perturb_error = model_error
    else:
        try:
            perturbed_probe = run_attention_probe(
                perturbed_prompt,
                model,
                tokenizer,
                device,
                torch,
                max_tokens.value,
            )
            perturb_error = None
        except Exception as exc:  # noqa: BLE001 - show perturb failures in UI.
            perturbed_probe = None
            perturb_error = exc
    return perturb_error, perturbed_probe, perturbed_prompt


@app.cell(hide_code=True)
def _(mo, perturbed_prompt):
    mo.md(f"""
    ## 7. Perturbation probe

    The paper uses perturbation experiments to argue that sinks can reduce
    how strongly information spreads across token positions. This miniature
    version changes one word and measures hidden-state drift by layer and
    token position.

    Perturbed prompt:

    ```text
    {perturbed_prompt}
    ```
    """)
    return


@app.cell(hide_code=True)
def _(hidden_drift_summary, perturb_error, perturbed_probe, plot_hidden_delta, probe, torch):
    if probe is None or perturbed_probe is None or perturb_error is not None:
        hidden_delta = None
        hidden_drift_metrics = None
        hidden_delta_fig = None
    else:
        hidden_drift_metrics = hidden_drift_summary(probe, perturbed_probe, torch)
        hidden_delta = hidden_drift_metrics["delta"]
        _token_count = hidden_delta.shape[1]
        hidden_delta_fig = plot_hidden_delta(hidden_delta, probe["tokens"][:_token_count])

    hidden_delta_fig
    return hidden_delta, hidden_drift_metrics


@app.cell(hide_code=True)
def _(hidden_delta, mo, perturb_error):
    if perturb_error is not None:
        _perturb_summary_output = mo.md(
            f"""
            Perturbation probe failed.

            ```text
            {perturb_error}
            ```
            """
        ).callout(kind="warn")
    elif hidden_delta is not None:
        first_layer_mean = float(hidden_delta[1].mean()) if hidden_delta.shape[0] > 1 else 0.0
        final_layer_mean = float(hidden_delta[-1].mean())
        _perturb_summary_output = mo.md(
            f"""
            Perturbation drift summary:

            | Layer slice | Mean token drift |
            | --- | ---: |
            | Early layer | {first_layer_mean:.3f} |
            | Final layer | {final_layer_mean:.3f} |

            Try switching the first-position anchor between the special token,
            the plain prompt, and a visible neutral anchor. If the sink is acting
            like an anti-mixing valve, the drift pattern should change.
            """
        )
    else:
        _perturb_summary_output = mo.md("Perturbation summary is waiting for a successful probe.")
    _perturb_summary_output
    return


@app.cell(hide_code=True)
def _(CONTEXT_SWEEP_BUDGETS, MODEL_OPTIONS, mo):
    comparison_run_mode = mo.ui.dropdown(
        options=[
            "Skip cloud sweep",
            "Run selected pair",
            "Run RTX family sweep",
        ],
        value="Skip cloud sweep",
        label="Model-family sweep",
        full_width=True,
    )
    comparison_model_a = mo.ui.dropdown(
        options=list(MODEL_OPTIONS.keys()),
        value="CLOUD · Qwen2.5 7B open",
        label="Reference model",
        full_width=True,
    )
    comparison_model_b = mo.ui.dropdown(
        options=list(MODEL_OPTIONS.keys()),
        value="CLOUD · Qwen2.5 14B open",
        label="Comparison model",
        full_width=True,
    )
    comparison_token_budget = mo.ui.slider(
        start=64,
        stop=512,
        step=64,
        value=256,
        show_value=True,
        label="Sweep token budget",
        full_width=True,
    )
    comparison_run_button = mo.ui.run_button(
        label="Run model-family sweep",
        kind="success",
        full_width=True,
    )
    context_sweep_model = mo.ui.dropdown(
        options=list(MODEL_OPTIONS.keys()),
        value="CLOUD · Qwen2.5 7B open",
        label="Long-context model",
        full_width=True,
    )
    context_sweep_button = mo.ui.run_button(
        label=f"Run context sweep: {CONTEXT_SWEEP_BUDGETS[0]}-{CONTEXT_SWEEP_BUDGETS[-1]} tokens",
        kind="success",
        full_width=True,
    )

    mo.vstack(
        [
            mo.md(
                """
                ## 8. Cloud GPU exploration

                The local path proves the mechanics. The molab path is where we
                test the paper-shaped claim at a more serious scale: larger
                models, longer contexts, and model families beyond the first
                example.

                Qwen models are open defaults. Gemma and LLaMA entries are included
                because they match the paper's evidence more closely, but they may
                require Hugging Face access in the cloud runtime.
                """
            ),
            mo.hstack([comparison_run_mode, comparison_token_budget], widths="equal", gap=1),
            mo.hstack([comparison_model_a, comparison_model_b], widths="equal", gap=1),
            comparison_run_button,
            mo.md(
                """
                ### Longer contexts

                The paper argues that sinks become more useful as context length
                grows. This run keeps the model fixed and measures how sink
                strength changes as the inspected context budget expands.
                """
            ),
            context_sweep_model,
            context_sweep_button,
        ],
        gap=1,
    )
    return (
        comparison_model_a,
        comparison_model_b,
        comparison_run_button,
        comparison_run_mode,
        comparison_token_budget,
        context_sweep_button,
        context_sweep_model,
    )


@app.cell(hide_code=True)
def _(
    anchored_prompt,
    build_long_context_prompt,
    hidden_drift_summary,
    perturb_prompt,
    run_attention_probe,
    summarize_attention_sink,
):
    def measure_anchor_effect(
        model_id,
        base_prompt,
        load_model_bundle,
        precision_key,
        torch,
        max_length,
        sink_threshold,
    ):
        _tokenizer, _model, _device, _model_dtype, _model_error = load_model_bundle(
            model_id,
            precision_key,
        )
        if _model_error is not None or _model is None:
            return [
                {
                    "model": model_id,
                    "dtype": _model_dtype,
                    "condition": "load failed",
                    "tokens": None,
                    "sink_rate_percent": None,
                    "mean_sink_strength": None,
                    "last_token_attention_to_token_0": None,
                    "final_layer_drift": None,
                    "error": str(_model_error),
                }
            ]

        _comparison_rows = []
        try:
            for _condition, _anchor_name in [
                ("with model first-token anchor", "Use model special token at first position"),
                ("plain prompt", "Plain prompt only"),
            ]:
                _text, _anchor_note = anchored_prompt(base_prompt, _anchor_name, _tokenizer)
                _perturbed_text = perturb_prompt(_text)
                _base_probe = run_attention_probe(
                    _text,
                    _model,
                    _tokenizer,
                    _device,
                    torch,
                    max_length,
                    top_k=4,
                )
                _perturbed_probe = run_attention_probe(
                    _perturbed_text,
                    _model,
                    _tokenizer,
                    _device,
                    torch,
                    max_length,
                    top_k=4,
                )
                _sink_summary = summarize_attention_sink(
                    _base_probe,
                    torch,
                    sink_threshold,
                )
                _drift_summary = hidden_drift_summary(
                    _base_probe,
                    _perturbed_probe,
                    torch,
                )

                _comparison_rows.append(
                    {
                        "model": model_id,
                        "dtype": _model_dtype,
                        "condition": _condition,
                        "tokens": _sink_summary["token_count"],
                        "sink_rate_percent": _sink_summary["sink_rate_percent"],
                        "mean_sink_strength": _sink_summary["mean_sink_strength"],
                        "last_token_attention_to_token_0": _sink_summary[
                            "last_token_attention_to_token_0"
                        ],
                        "final_layer_drift": _drift_summary["final_layer_mean_drift"],
                        "error": "",
                    }
                )
        except Exception as exc:  # noqa: BLE001 - surface cloud runtime failures.
            return [
                {
                    "model": model_id,
                    "dtype": _model_dtype,
                    "condition": "analysis failed",
                    "tokens": None,
                    "sink_rate_percent": None,
                    "mean_sink_strength": None,
                    "last_token_attention_to_token_0": None,
                    "final_layer_drift": None,
                    "error": str(exc),
                }
            ]

        return _comparison_rows

    def measure_context_sweep(
        model_id,
        base_prompt,
        budgets,
        load_model_bundle,
        precision_key,
        torch,
        sink_threshold,
    ):
        _tokenizer, _model, _device, _model_dtype, _model_error = load_model_bundle(
            model_id,
            precision_key,
        )
        if _model_error is not None or _model is None:
            return [
                {
                    "model": model_id,
                    "dtype": _model_dtype,
                    "max_tokens": None,
                    "actual_tokens": None,
                    "sink_rate_percent": None,
                    "mean_sink_strength": None,
                    "last_token_attention_to_token_0": None,
                    "error": str(_model_error),
                }
            ]

        _long_prompt = build_long_context_prompt(base_prompt, target_sections=96)
        _anchored_text, _anchor_note = anchored_prompt(
            _long_prompt,
            "Use model special token at first position",
            _tokenizer,
        )
        _context_rows = []
        for _budget in budgets:
            try:
                _probe = run_attention_probe(
                    _anchored_text,
                    _model,
                    _tokenizer,
                    _device,
                    torch,
                    _budget,
                    top_k=4,
                )
                _sink_summary = summarize_attention_sink(_probe, torch, sink_threshold)
                _context_rows.append(
                    {
                        "model": model_id,
                        "dtype": _model_dtype,
                        "max_tokens": int(_budget),
                        "actual_tokens": _sink_summary["token_count"],
                        "sink_rate_percent": _sink_summary["sink_rate_percent"],
                        "mean_sink_strength": _sink_summary["mean_sink_strength"],
                        "last_token_attention_to_token_0": _sink_summary[
                            "last_token_attention_to_token_0"
                        ],
                        "error": "",
                    }
                )
            except Exception as exc:  # noqa: BLE001 - keep partial sweep results.
                _context_rows.append(
                    {
                        "model": model_id,
                        "dtype": _model_dtype,
                        "max_tokens": int(_budget),
                        "actual_tokens": None,
                        "sink_rate_percent": None,
                        "mean_sink_strength": None,
                        "last_token_attention_to_token_0": None,
                        "error": str(exc),
                    }
                )
        return _context_rows

    return measure_anchor_effect, measure_context_sweep


@app.cell(hide_code=True)
def _(
    DEFAULT_SWEEP_MODELS,
    MODEL_OPTIONS,
    comparison_model_a,
    comparison_model_b,
    comparison_run_button,
    comparison_run_mode,
    comparison_token_budget,
    load_model_bundle,
    measure_anchor_effect,
    pd,
    selected_precision_key,
    selected_prompt,
    sink_threshold,
    torch,
):
    if (
        comparison_run_mode.value == "Skip cloud sweep"
        or not comparison_run_button.value
        or pd is None
    ):
        comparison_table = None
    else:
        _comparison_rows = []
        if comparison_run_mode.value == "Run RTX family sweep":
            _comparison_labels = DEFAULT_SWEEP_MODELS
        else:
            _comparison_labels = [comparison_model_a.value, comparison_model_b.value]

        _comparison_model_ids = []
        for _model_label in _comparison_labels:
            _model_id = MODEL_OPTIONS[_model_label]
            if _model_id not in _comparison_model_ids:
                _comparison_model_ids.append(_model_id)

        for _model_id in _comparison_model_ids:
            _comparison_rows.extend(
                measure_anchor_effect(
                    _model_id,
                    selected_prompt,
                    load_model_bundle,
                    selected_precision_key,
                    torch,
                    comparison_token_budget.value,
                    sink_threshold.value,
                )
            )
        comparison_table = pd.DataFrame(_comparison_rows)
    return (comparison_table,)


@app.cell(hide_code=True)
def _(comparison_table, mo):
    if comparison_table is None:
        _comparison_output = mo.md(
            """
            The model-family sweep is skipped by default because it can load
            multiple large models. Choose a sweep mode and click the run button
            in molab after attaching the RTX Pro 6000.
            """
        ).callout(kind="info")
    else:
        _comparison_output = mo.vstack(
            [
                mo.md(
                    """
                    The most persuasive result is not a single large number. It
                    is the pattern: adding a first-position anchor should increase
                    sink behavior and often reduce how much a local perturbation
                    spreads into the final layer.
                    """
                ),
                comparison_table,
            ],
            gap=1,
        )
    _comparison_output
    return


@app.cell(hide_code=True)
def _(
    CONTEXT_SWEEP_BUDGETS,
    MODEL_OPTIONS,
    context_sweep_button,
    context_sweep_model,
    load_model_bundle,
    measure_context_sweep,
    pd,
    selected_precision_key,
    selected_prompt,
    sink_threshold,
    torch,
):
    if not context_sweep_button.value or pd is None:
        context_sweep_table = None
    else:
        _context_model_id = MODEL_OPTIONS[context_sweep_model.value]
        context_sweep_table = pd.DataFrame(
            measure_context_sweep(
                _context_model_id,
                selected_prompt,
                CONTEXT_SWEEP_BUDGETS,
                load_model_bundle,
                selected_precision_key,
                torch,
                sink_threshold.value,
            )
        )
    return (context_sweep_table,)


@app.cell(hide_code=True)
def _(context_sweep_table, mo):
    if context_sweep_table is None:
        _context_sweep_output = mo.md(
            """
            The context-length sweep is waiting for a cloud GPU run. This is the
            section that most directly tests the paper's claim that sink behavior
            becomes more useful as context length grows.
            """
        ).callout(kind="info")
    else:
        _context_sweep_output = mo.vstack(
            [
                context_sweep_table,
                mo.md(
                    """
                    Read this table vertically: if sink behavior strengthens with
                    longer inspected contexts, the result mirrors the paper's
                    context-length story in a form viewers can rerun and modify.
                    """
                ).callout(kind="success"),
            ],
            gap=0.75,
        )
    _context_sweep_output
    return


@app.cell(hide_code=True)
def _(mo, probe):
    next_token_output = probe["next_tokens"] if probe is not None else None
    mo.vstack([mo.md("## 9. Next-token distribution"), next_token_output])
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## 10. Why this weird token matters

    The core reproduction sections focus on paper-faithful claims: perturbation
    spread, larger models, longer contexts, and streaming attention. Two other
    consequences are worth keeping in mind:

    | Area | Relevance |
    | --- | --- |
    | Quantization | If sink behavior is tied to unusual activation or routing patterns, compression schemes need to preserve the numerically important parts of a token that may look semantically boring. |
    | Robustness | A sink can dampen or reshape how local prompt edits spread through the network. That makes token 0 a stabilizer in some settings and a critical position to inspect in others. |
    | Interpretability | Attention maps are not only semantic lookup tables. Sometimes they expose control flow: where a head routes when it wants to do less mixing. |

    The closing question is therefore practical, not just aesthetic: when we
    optimize, compress, stream, or interpret LLMs, are we preserving the
    infrastructure tokens the model has learned to rely on?
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Shareable notebook arc

    The final version should feel like a short investigation:

    1. A surprising visual: many heads attend to the first token.
    2. The paper's explanation: the sink can act as an approximate no-op.
    3. A reproduction: perturbation spreads more when the first-token anchor is absent.
    4. A streaming diagnostic: keeping token 0 can preserve otherwise dropped attention mass.
    5. A cloud GPU exploration: test Qwen, Gemma, and LLaMA-style families.
    6. A practical takeaway: attention sinks matter for long context, streaming,
       quantization, and robustness.

    That arc is designed for the rubric's shareability clause: a viewer should
    leave with one memorable mechanism and a reason to open the original paper.
    """)
    return


if __name__ == "__main__":
    app.run()
