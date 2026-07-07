# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "accelerate>=0.33",
#     "marimo>=0.23",
#     "matplotlib>=3.8",
#     "numpy>=1.26",
#     "pandas>=2.2",
#     "plotly>=5.22",
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
            Built for the alphaXiv x marimo notebook competition and tuned for
            molab with an RTX Pro 6000. A separate local notebook keeps the
            small-model tinkering path out of this competition run.
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
            <circle cx="62" cy="74" r="16" fill="#16a34a"/>
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


@app.cell
def _(mo):
    mo.md(r"""
    **Reader's note.** For the best experience, run all cells once, turn **show code** off, and read vertically from top to bottom. This competition notebook is tuned for molab with the attached RTX Pro 6000. If you want to tinker locally with small models and CPU-friendly defaults, use `notebooks/first_token_sink_local.py` from the GitHub repo.
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## The strange thing we are trying to explain

    Open an attention map from a modern causal language model and you often see
    a vertical stripe at position zero. Many heads send probability mass to the
    first token even when that token has no obvious semantic role in the answer.

    The paper's claim is sharper than "attention is noisy": the first token can
    become a safe routing target. When a head does not need to mix in new
    information, it can attend to a low-information position and behave closer
    to an approximate no-op. That turns a visual oddity into infrastructure for
    depth, long context, and streaming inference.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    sink_playground = r"""
    <div id="sink-playground" class="sink-playground">
      <style>
        #sink-playground {
          border: 1px solid #d7dde8;
          border-radius: 8px;
          background: #fbfdff;
          padding: 16px;
          margin: 6px 0 24px;
          color: #172033;
        }
        #sink-playground * { box-sizing: border-box; }
        #sink-playground .sink-playground-grid {
          display: grid;
          grid-template-columns: minmax(0, 0.9fr) minmax(280px, 1.1fr);
          gap: 18px;
          align-items: start;
        }
        #sink-playground h3 {
          margin: 0 0 10px;
          font-size: 1.05rem;
          line-height: 1.25;
        }
        #sink-playground label {
          display: grid;
          gap: 5px;
          margin: 12px 0;
          font-weight: 700;
          color: #334155;
        }
        #sink-playground input[type="range"] { width: 100%; }
        #sink-playground .sink-track {
          position: relative;
          height: 34px;
          border-radius: 6px;
          background: #eef2f7;
          overflow: hidden;
          margin: 10px 0;
          border: 1px solid #dce3ee;
        }
        #sink-playground .sink-fill {
          height: 100%;
          width: 0%;
          display: flex;
          align-items: center;
          padding-left: 10px;
          color: #fff;
          font-weight: 850;
          font-size: 0.84rem;
          white-space: nowrap;
          transition: width 180ms ease;
        }
        #sink-playground .sink-zero { background: #16a34a; }
        #sink-playground .sink-recent { background: #2563eb; }
        #sink-playground .sink-semantic { background: #ca8a04; }
        #sink-playground .sink-meter {
          display: grid;
          grid-template-columns: repeat(3, minmax(0, 1fr));
          gap: 10px;
          margin-top: 12px;
        }
        #sink-playground .sink-metric {
          border: 1px solid #d7dde8;
          border-radius: 8px;
          background: #fff;
          padding: 10px;
        }
        #sink-playground .sink-metric span {
          display: block;
          color: #64748b;
          font-size: 0.74rem;
          font-weight: 850;
          text-transform: uppercase;
          letter-spacing: 0;
        }
        #sink-playground .sink-metric strong {
          display: block;
          margin-top: 4px;
          font-size: 1.25rem;
          color: #111827;
        }
        @media (max-width: 760px) {
          #sink-playground .sink-playground-grid { grid-template-columns: 1fr; }
          #sink-playground .sink-meter { grid-template-columns: 1fr; }
        }
      </style>
      <div class="sink-playground-grid">
        <section>
          <h3>Attention sink intuition</h3>
          <p style="margin:0;color:#475569;line-height:1.5;">
            Move the controls before running any model. The point is not to
            simulate a Transformer exactly; it is to make the mechanism visible.
            More no-op pressure and longer context make token 0 more attractive.
          </p>
          <label>No-op pressure <input data-role="noop" type="range" min="0" max="100" value="58"></label>
          <label>Semantic pressure <input data-role="semantic" type="range" min="0" max="100" value="42"></label>
          <label>Context length <input data-role="context" type="range" min="32" max="2048" step="32" value="512"></label>
        </section>
        <section>
          <div class="sink-track"><div class="sink-fill sink-zero" data-role="zero">token 0</div></div>
          <div class="sink-track"><div class="sink-fill sink-recent" data-role="recent">recent tokens</div></div>
          <div class="sink-track"><div class="sink-fill sink-semantic" data-role="semantic-bar">semantic tokens</div></div>
          <div class="sink-meter">
            <div class="sink-metric"><span>Sink mass</span><strong data-role="sink-mass">0%</strong></div>
            <div class="sink-metric"><span>Context</span><strong data-role="context-value">512</strong></div>
            <div class="sink-metric"><span>Interpretation</span><strong data-role="verdict">mixed</strong></div>
          </div>
        </section>
      </div>
      <script>
        (() => {
          const root = document.currentScript.closest("#sink-playground");
          const noop = root.querySelector("[data-role='noop']");
          const semantic = root.querySelector("[data-role='semantic']");
          const context = root.querySelector("[data-role='context']");
          const zero = root.querySelector("[data-role='zero']");
          const recent = root.querySelector("[data-role='recent']");
          const semanticBar = root.querySelector("[data-role='semantic-bar']");
          const sinkMass = root.querySelector("[data-role='sink-mass']");
          const contextValue = root.querySelector("[data-role='context-value']");
          const verdict = root.querySelector("[data-role='verdict']");

          function render() {
            const noopValue = Number(noop.value) / 100;
            const semanticValue = Number(semantic.value) / 100;
            const contextValueRaw = Number(context.value);
            const contextPressure = Math.log2(contextValueRaw / 32) / Math.log2(2048 / 32);
            const sink = Math.max(0.04, Math.min(0.88, 0.12 + 0.52 * noopValue + 0.28 * contextPressure - 0.34 * semanticValue));
            const semanticMass = Math.max(0.06, Math.min(0.78, 0.18 + 0.58 * semanticValue - 0.18 * noopValue));
            const recentMass = Math.max(0.05, 1 - sink - semanticMass);
            const total = sink + semanticMass + recentMass;
            const sinkPct = Math.round((sink / total) * 100);
            const recentPct = Math.round((recentMass / total) * 100);
            const semanticPct = Math.round((semanticMass / total) * 100);
            zero.style.width = `${sinkPct}%`;
            recent.style.width = `${recentPct}%`;
            semanticBar.style.width = `${semanticPct}%`;
            zero.textContent = `token 0 ${sinkPct}%`;
            recent.textContent = `recent tokens ${recentPct}%`;
            semanticBar.textContent = `semantic tokens ${semanticPct}%`;
            sinkMass.textContent = `${sinkPct}%`;
            contextValue.textContent = contextValueRaw.toLocaleString();
            verdict.textContent = sinkPct > 45 ? "sink-heavy" : sinkPct > 24 ? "mixed" : "semantic";
          }

          [noop, semantic, context].forEach((input) => input.addEventListener("input", render));
          render();
        })();
      </script>
    </div>
    """
    mo.Html(sink_playground)
    return


@app.cell(hide_code=True)
def _():
    dependency_error = None
    np = None
    pd = None
    plt = None
    go = None
    torch = None
    AutoModelForCausalLM = None
    AutoTokenizer = None
    from types import SimpleNamespace

    try:
        import gc
        import os
        import numpy as np
        import pandas as pd
        import matplotlib.pyplot as plt
        import plotly.graph_objects as go
        import torch
        from transformers import AutoModelForCausalLM, AutoTokenizer
    except Exception as exc:  # noqa: BLE001 - show import failures inside notebook.
        dependency_error = exc
    return (
        AutoModelForCausalLM,
        AutoTokenizer,
        SimpleNamespace,
        dependency_error,
        gc,
        go,
        np,
        os,
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
def _(mo):
    hf_token_input = mo.ui.text(
        kind="password",
        placeholder="Optional: paste a Hugging Face read token for gated models",
        label="Hugging Face token",
        full_width=True,
    )
    hf_token_form = hf_token_input.form(
        label="Use token for this session",
        clear_on_submit=True,
    )
    mo.vstack(
        [
            mo.md(
                """
                **Optional for gated models.** Public Qwen models do not need a
                Hugging Face token. Gemma and LLaMA-style gated models require
                either an `HF_TOKEN` / `HUGGING_FACE_HUB_TOKEN` environment
                variable in the cloud runtime, or a token submitted here for
                this session. The token is never displayed by the notebook.
                """
            ).callout(kind="info"),
            hf_token_form,
        ],
        gap=0.75,
    )
    return (hf_token_form,)


@app.cell(hide_code=True)
def _(hf_token_form, mo, os):
    env_hf_token = os.environ.get("HF_TOKEN") or os.environ.get("HUGGING_FACE_HUB_TOKEN")
    submitted_hf_token = (hf_token_form.value or "").strip()
    hf_token = env_hf_token or submitted_hf_token or None
    if env_hf_token:
        hf_token_source = "environment"
    elif submitted_hf_token:
        hf_token_source = "session input"
    else:
        hf_token_source = "none"

    hf_token_status = {
        "source": hf_token_source,
        "available": hf_token is not None,
    }
    mo.md(
        f"""
        Hugging Face auth: `{hf_token_source}`.
        """
    ).callout(kind="success" if hf_token is not None else "info")
    return hf_token, hf_token_status


@app.cell(hide_code=True)
def _():
    PAPER_URL = "https://arxiv.org/abs/2504.02732"
    ALPHAXIV_URL = "https://www.alphaxiv.org/abs/2504.02732"

    MODEL_OPTIONS = {
        "Qwen2.5 0.5B open": "Qwen/Qwen2.5-0.5B",
        "Qwen2.5 1.5B open": "Qwen/Qwen2.5-1.5B",
        "Qwen2.5 7B open": "Qwen/Qwen2.5-7B",
        "Qwen2.5 14B open": "Qwen/Qwen2.5-14B",
        "Gemma 2 2B auth may be required": "google/gemma-2-2b",
        "Gemma 2 9B auth may be required": "google/gemma-2-9b",
        "LLaMA 3.1 8B auth required": "meta-llama/Llama-3.1-8B",
    }

    DEFAULT_SWEEP_MODELS = [
        "Qwen2.5 1.5B open",
        "Qwen2.5 7B open",
        "Gemma 2 9B auth may be required",
        "LLaMA 3.1 8B auth required",
    ]

    EXECUTION_MODES = [
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
    TOKEN_BUDGET_OPTIONS = {
        "64 tokens": 64,
        "128 tokens": 128,
        "512 tokens": 512,
        "1024 tokens": 1024,
        "2048 tokens": 2048,
    }
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
        TOKEN_BUDGET_OPTIONS,
    )


@app.cell
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
def _(
    ANCHOR_MODES,
    EXECUTION_MODES,
    MODEL_OPTIONS,
    PRECISION_OPTIONS,
    PROMPT_PRESETS,
    TOKEN_BUDGET_OPTIONS,
    mo,
):
    execution_mode = mo.ui.dropdown(
        options=EXECUTION_MODES,
        value="Cloud GPU single model",
        label="Execution mode",
        full_width=True,
    )
    model_choice = mo.ui.dropdown(
        options=list(MODEL_OPTIONS.keys()),
        value="Qwen2.5 7B open",
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
    max_tokens = mo.ui.dropdown(
        options=list(TOKEN_BUDGET_OPTIONS.keys()),
        value="512 tokens",
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
def _(
    MODEL_OPTIONS,
    PRECISION_OPTIONS,
    SimpleNamespace,
    TOKEN_BUDGET_OPTIONS,
    anchor_mode,
    execution_mode,
    max_tokens,
    model_choice,
    precision_choice,
    selected_preset_name,
    selected_prompt,
    sink_threshold,
):
    current_probe_config = SimpleNamespace(
        execution_mode=execution_mode.value,
        model_label=model_choice.value,
        model_id=MODEL_OPTIONS[model_choice.value],
        precision_label=precision_choice.value,
        precision_key=PRECISION_OPTIONS[precision_choice.value],
        prompt_preset=selected_preset_name,
        prompt=selected_prompt,
        anchor_mode=anchor_mode.value,
        max_tokens=int(TOKEN_BUDGET_OPTIONS[max_tokens.value]),
        sink_threshold=float(sink_threshold.value),
    )
    return (current_probe_config,)


@app.cell(hide_code=True)
def _(mo):
    get_selected_probe_config, set_selected_probe_config = mo.state(None)
    return get_selected_probe_config, set_selected_probe_config


@app.cell(hide_code=True)
def _(get_selected_probe_config):
    probe_config = get_selected_probe_config()
    return (probe_config,)


@app.cell(hide_code=True)
def _(current_probe_config, mo, set_selected_probe_config):
    select_probe_config = mo.ui.button(
        label="Select probe configuration",
        kind="success",
        on_click=lambda _: set_selected_probe_config(current_probe_config),
    )
    mo.vstack(
        [
            mo.md(
                """
                Commit the setup before running it. This keeps the notebook from
                downloading a model every time a dropdown changes.
                """
            ).callout(kind="info"),
            select_probe_config,
        ],
        gap=0.6,
    )
    return (select_probe_config,)


@app.cell(hide_code=True)
def _(mo, probe_config):
    run_probe_button = mo.ui.run_button(
        label="Load model and run attention probe",
        kind="success",
        full_width=True,
    )
    if probe_config is None:
        probe_action_view = mo.md(
            "Select a probe configuration above. No model will load until a configuration is selected and the run button is clicked."
        ).callout(kind="info")
    else:
        probe_action_view = mo.vstack(
            [
                mo.md(
                    f"""
                    Selected probe:

                    - model: `{probe_config.model_id}`
                    - dtype policy: `{probe_config.precision_label}`
                    - prompt preset: `{probe_config.prompt_preset}`
                    - max inspected tokens: `{probe_config.max_tokens}`
                    - anchor mode: `{probe_config.anchor_mode}`
                    """
                ).callout(kind="info"),
                run_probe_button,
            ],
            gap=0.6,
        )
    probe_action_view
    return (run_probe_button,)


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
    def load_model_bundle(model_id, precision_key="fp16", hf_token=None):
        if dependency_error is not None:
            return None, None, None, None, dependency_error

        device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        try:
            gc.collect()
            if torch.cuda.is_available():
                torch.cuda.empty_cache()

            _auth_kwargs = {"token": hf_token} if hf_token else {}

            tokenizer = AutoTokenizer.from_pretrained(model_id, **_auth_kwargs)
            if tokenizer.pad_token is None:
                tokenizer.pad_token = tokenizer.eos_token or tokenizer.bos_token

            _model_kwargs = {"low_cpu_mem_usage": True, **_auth_kwargs}
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
def _(
    MODEL_OPTIONS,
    PRECISION_OPTIONS,
    hf_token,
    load_model_bundle,
    model_choice,
    precision_choice,
    probe_config,
    run_probe_button,
):
    selected_model_id = (
        probe_config.model_id if probe_config is not None else MODEL_OPTIONS[model_choice.value]
    )
    selected_precision_key = (
        probe_config.precision_key
        if probe_config is not None
        else PRECISION_OPTIONS[precision_choice.value]
    )
    probe_run_requested = bool(probe_config is not None and run_probe_button.value)
    if probe_run_requested:
        tokenizer, model, device, model_dtype, model_error = load_model_bundle(
            selected_model_id,
            selected_precision_key,
            hf_token,
        )
    else:
        tokenizer = None
        model = None
        device = None
        model_dtype = None
        model_error = None
    return (
        device,
        model,
        model_dtype,
        model_error,
        probe_run_requested,
        selected_model_id,
        selected_precision_key,
        tokenizer,
    )


@app.cell(hide_code=True)
def _(device, mo, model, model_dtype, model_error, probe_config, probe_run_requested, selected_model_id, torch):
    if probe_config is None:
        model_status_output = mo.md(
            """
            Model status: waiting for a selected probe configuration.
            """
        ).callout(kind="info")
    elif not probe_run_requested:
        model_status_output = mo.md(
            f"""
            Model status: ready to run `{selected_model_id}`.

            Click **Load model and run attention probe** when you want this cell
            to download/load weights and compute attentions.
            """
        ).callout(kind="info")
    elif model_error is not None:
        model_status_output = mo.md(
            f"""
            Model could not be loaded.

            ```text
            {model_error}
            ```
            """
        ).callout(kind="warn")
    elif model is None:
        model_status_output = mo.md("Model status: loading or waiting for the run button.").callout(kind="info")
    else:
        model_status_output = None
    model_status_output
    return


@app.cell(hide_code=True)
def _(mo, probe, sink_scores):
    selected_layer_index = 0
    selected_head_index = 0
    selected_head_score = None

    if probe is None or sink_scores is None:
        head_picker_view = mo.md(
            """
            ## 2. Pick a head to inspect

            The layer/head controls appear after the attention probe finishes.
            The notebook will preselect the strongest first-token sink head so
            the first heatmap is immediately meaningful.
            """
        ).callout(kind="info")
    else:
        layer_count, head_count = sink_scores.shape
        strongest_flat_index = int(sink_scores.flatten().argmax().item())
        strongest_layer = int(strongest_flat_index // head_count)
        strongest_head = int(strongest_flat_index % head_count)
        strongest_score = float(sink_scores[strongest_layer, strongest_head])

        layer_index_control = mo.ui.slider(
            start=0,
            stop=max(0, layer_count - 1),
            step=1,
            value=strongest_layer,
            show_value=True,
            label="Layer",
            full_width=True,
        )
        head_index_control = mo.ui.slider(
            start=0,
            stop=max(0, head_count - 1),
            step=1,
            value=strongest_head,
            show_value=True,
            label="Head",
            full_width=True,
        )
        selected_layer_index = min(int(layer_index_control.value), layer_count - 1)
        selected_head_index = min(int(head_index_control.value), head_count - 1)
        selected_head_score = float(sink_scores[selected_layer_index, selected_head_index])

        head_picker_view = mo.vstack(
            [
                mo.md(
                    f"""
                    ## 2. Pick a head to inspect

                    Preselected **L{strongest_layer} H{strongest_head}** because
                    it has the highest first-token sink score in this run
                    ({strongest_score:.3f}). Use the controls to audit any other
                    layer/head pair.
                    """
                ).callout(kind="info"),
                mo.hstack([layer_index_control, head_index_control], widths="equal", gap=1),
            ],
            gap=1,
        )

    head_picker_view
    return selected_head_index, selected_head_score, selected_layer_index


@app.cell(hide_code=True)
def _(anchored_prompt, probe_config, tokenizer):
    if probe_config is None:
        analysis_prompt = None
        anchor_note = "Select a probe configuration to build the prompt."
    elif (
        tokenizer is None
        and probe_config.anchor_mode == "Use model special token at first position"
    ):
        analysis_prompt = probe_config.prompt
        anchor_note = "The model special token will be prepended after the tokenizer loads."
    else:
        analysis_prompt, anchor_note = anchored_prompt(
            probe_config.prompt,
            probe_config.anchor_mode,
            tokenizer,
        )
    return analysis_prompt, anchor_note


@app.cell(hide_code=True)
def _(analysis_prompt, anchor_note, mo, probe_config):
    if probe_config is None:
        prompt_view = mo.md(
            """
            ## 3. Current prompt

            Waiting for a selected probe configuration.
            """
        ).callout(kind="info")
    else:
        prompt_view = mo.md(f"""
        ## 3. Current prompt

        Preset: `{probe_config.prompt_preset}`

        Anchor: {anchor_note}

        ```text
        {analysis_prompt}
        ```
        """)
    prompt_view
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
    model,
    model_error,
    probe_config,
    probe_run_requested,
    run_attention_probe,
    tokenizer,
    torch,
):
    if not probe_run_requested:
        probe_error = None
        probe = None
    elif model_error is not None or model is None or analysis_prompt is None:
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
                probe_config.max_tokens,
            )
            probe_error = None
        except Exception as exc:  # noqa: BLE001 - show probe failures in UI.
            probe = None
            probe_error = exc
    return probe, probe_error


@app.cell(hide_code=True)
def _(mo, probe, probe_error, probe_run_requested):
    if probe_error is not None:
        mo.md(
            f"""
            Probe failed.

            ```text
            {probe_error}
            ```
            """
        ).callout(kind="warn")
    elif probe is not None:
        mo.md(
            f"""
            Probe complete: `{len(probe["tokens"])}` tokens inspected.
            """
        ).callout(kind="success")
    elif probe_run_requested:
        mo.md("Probe is waiting for the model load to finish.").callout(kind="info")
    else:
        mo.md("Probe output is waiting for the run button.").callout(kind="info")
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
    mo,
    probe,
    selected_head_index,
    selected_layer_index,
    sink_rate,
    sink_scores,
    sink_threshold,
):
    if probe is None or sink_scores is None:
        _sink_metric_output = mo.md("Sink metrics are waiting for a successful model probe.")
    else:
        _layer = min(int(selected_layer_index), sink_scores.shape[0] - 1)
        _head = min(int(selected_head_index), sink_scores.shape[1] - 1)
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
def _(go, np):
    BLUE = "#2563eb"
    LIGHT_BLUE = "#eff6ff"
    SKY = "#38bdf8"
    GREEN = "#16a34a"
    YELLOW = "#facc15"
    SINK_COLORSCALE = [
        [0.0, LIGHT_BLUE],
        [0.35, SKY],
        [0.70, GREEN],
        [1.0, YELLOW],
    ]

    def _sampled_token_ticks(tokens, max_ticks=28):
        if not tokens:
            return [], []
        step = max(1, int(np.ceil(len(tokens) / max_ticks)))
        positions = list(range(0, len(tokens), step))
        labels = [f"{position}: {tokens[position][:14]}" for position in positions]
        return positions, labels

    def plot_attention_matrix(matrix, tokens, layer, head):
        data = np.asarray(matrix)
        token_count = len(tokens)
        tick_positions, tick_labels = _sampled_token_ticks(tokens)
        hover = [
            [
                (
                    f"query {row}: {tokens[row]}<br>"
                    f"key {col}: {tokens[col]}"
                )
                for col in range(token_count)
            ]
            for row in range(token_count)
        ]
        fig = go.Figure(
            data=go.Heatmap(
                z=data,
                x=list(range(token_count)),
                y=list(range(token_count)),
                customdata=hover,
                colorscale=SINK_COLORSCALE,
                zmin=0.0,
                zmax=max(0.05, float(np.nanmax(data))),
                colorbar={"title": "attention", "thickness": 12},
                hovertemplate="%{customdata}<br>attention=%{z:.4f}<extra></extra>",
            )
        )
        fig.update_layout(
            title=f"Attention weights: layer {layer}, head {head}",
            height=max(420, min(760, 20 * token_count)),
            margin={"l": 56, "r": 16, "t": 54, "b": 72},
            paper_bgcolor="#ffffff",
            plot_bgcolor="#ffffff",
            xaxis={
                "title": "Key token attended to",
                "tickmode": "array",
                "tickvals": tick_positions,
                "ticktext": tick_labels,
                "tickangle": -45,
            },
            yaxis={
                "title": "Query token receiving context",
                "tickmode": "array",
                "tickvals": tick_positions,
                "ticktext": tick_labels,
                "autorange": "reversed",
            },
        )
        return fig

    def plot_attention_flow(probe, layer, head, query_index, top_k=12):
        attention_row = probe["attention"][layer, head, query_index].numpy()
        visible_keys = np.arange(query_index + 1)
        top_count = min(int(top_k), len(visible_keys))
        top_positions = visible_keys[np.argsort(attention_row[: query_index + 1])[-top_count:]]
        top_positions = top_positions[np.argsort(attention_row[top_positions])]
        labels = [f"{position}: {probe['tokens'][position][:22]}" for position in top_positions]
        values = attention_row[top_positions]
        colors = [GREEN if int(position) == 0 else BLUE for position in top_positions]
        fig = go.Figure(
            data=go.Bar(
                x=values,
                y=labels,
                orientation="h",
                marker={"color": colors},
                customdata=[
                    f"key {int(position)}: {probe['tokens'][int(position)]}"
                    for position in top_positions
                ],
                hovertemplate="%{customdata}<br>attention=%{x:.4f}<extra></extra>",
            )
        )
        fig.update_layout(
            title=f"Where query token {query_index} sends attention",
            height=max(330, 32 * top_count),
            margin={"l": 126, "r": 16, "t": 52, "b": 48},
            paper_bgcolor="#ffffff",
            plot_bgcolor="#ffffff",
            xaxis={"title": "Attention weight", "range": [0, max(0.05, float(values.max()) * 1.12)]},
            yaxis={"title": ""},
            showlegend=False,
        )
        return fig

    def plot_sink_map(sink_scores, threshold):
        data = sink_scores.numpy()
        layer_count, head_count = data.shape
        hover = [
            [
                f"layer {layer}<br>head {head}<br>strong sink: {data[layer, head] > threshold}"
                for head in range(head_count)
            ]
            for layer in range(layer_count)
        ]
        fig = go.Figure(
            data=go.Heatmap(
                z=data,
                x=list(range(head_count)),
                y=list(range(layer_count)),
                customdata=hover,
                colorscale=SINK_COLORSCALE,
                zmin=0.0,
                zmax=max(0.75, float(np.nanmax(data))),
                colorbar={"title": "mean attention to token 0", "thickness": 12},
                hovertemplate="%{customdata}<br>score=%{z:.4f}<extra></extra>",
            )
        )
        strong_layers, strong_heads = np.where(data > threshold)
        if len(strong_layers) > 0:
            fig.add_trace(
                go.Scatter(
                    x=strong_heads,
                    y=strong_layers,
                    mode="markers",
                    marker={
                        "symbol": "circle-open",
                        "size": 14,
                        "color": "#ffffff",
                        "line": {"color": "#ffffff", "width": 2},
                    },
                    name="above threshold",
                    hoverinfo="skip",
                )
            )
        fig.update_layout(
            title="Mean attention to token 0 by layer and head",
            height=max(360, min(760, 26 * layer_count)),
            margin={"l": 56, "r": 16, "t": 52, "b": 50},
            paper_bgcolor="#ffffff",
            plot_bgcolor="#ffffff",
            xaxis={"title": "Head", "dtick": 1},
            yaxis={"title": "Layer", "dtick": 1, "autorange": "reversed"},
        )
        return fig

    def plot_hidden_delta(delta, tokens):
        data = delta.numpy()
        tick_positions, tick_labels = _sampled_token_ticks(tokens)
        layer_count, token_count = data.shape
        hover = [
            [
                f"layer {layer}<br>token {token}: {tokens[token]}"
                for token in range(token_count)
            ]
            for layer in range(layer_count)
        ]
        fig = go.Figure(
            data=go.Heatmap(
                z=data,
                x=list(range(token_count)),
                y=list(range(layer_count)),
                customdata=hover,
                colorscale=SINK_COLORSCALE,
                colorbar={"title": "L2 drift", "thickness": 12},
                hovertemplate="%{customdata}<br>drift=%{z:.4f}<extra></extra>",
            )
        )
        fig.update_layout(
            title="Hidden-state drift after perturbing the prompt",
            height=max(360, min(760, 24 * layer_count)),
            margin={"l": 56, "r": 16, "t": 52, "b": 72},
            paper_bgcolor="#ffffff",
            plot_bgcolor="#ffffff",
            xaxis={
                "title": "Token position",
                "tickmode": "array",
                "tickvals": tick_positions,
                "ticktext": tick_labels,
                "tickangle": -45,
            },
            yaxis={"title": "Layer, including embedding layer", "dtick": 1},
        )
        return fig

    def plot_streaming_cache_bars(streaming_cache_summary):
        labels = ["recent-only cache", "token 0 + recent cache"]
        values = [
            streaming_cache_summary["recent_only_attention_mass"],
            streaming_cache_summary["anchor_plus_recent_attention_mass"],
        ]
        fig = go.Figure(
            data=go.Bar(
                x=labels,
                y=values,
                marker={"color": [BLUE, GREEN]},
                hovertemplate="%{x}<br>attention mass=%{y:.4f}<extra></extra>",
            )
        )
        fig.update_layout(
            title="Attention mass preserved for the final token",
            height=330,
            margin={"l": 52, "r": 16, "t": 52, "b": 64},
            paper_bgcolor="#ffffff",
            plot_bgcolor="#ffffff",
            yaxis={"title": "Mean attention mass", "range": [0, max(1.0, max(values) * 1.12)]},
            xaxis={"title": ""},
            showlegend=False,
        )
        return fig

    def plot_next_token_distribution(next_tokens):
        labels = [item["token"] for item in reversed(next_tokens)]
        values = [item["probability"] for item in reversed(next_tokens)]
        fig = go.Figure(
            data=go.Bar(
                x=values,
                y=labels,
                orientation="h",
                marker={"color": BLUE},
                hovertemplate="token=%{y}<br>probability=%{x:.4f}<extra></extra>",
            )
        )
        fig.update_layout(
            title="Top next-token probabilities",
            height=max(320, 34 * len(labels)),
            margin={"l": 118, "r": 16, "t": 52, "b": 48},
            paper_bgcolor="#ffffff",
            plot_bgcolor="#ffffff",
            xaxis={"title": "Probability"},
            yaxis={"title": ""},
            showlegend=False,
        )
        return fig

    return (
        plot_attention_flow,
        plot_attention_matrix,
        plot_hidden_delta,
        plot_next_token_distribution,
        plot_sink_map,
        plot_streaming_cache_bars,
    )


@app.cell(hide_code=True)
def _(
    mo,
    plot_attention_matrix,
    probe,
    selected_head_index,
    selected_head_score,
    selected_layer_index,
):
    if probe is None:
        selected_attention_output = mo.md(
            """
            ## 5. Inspect one attention head

            Run a probe to reveal the token-by-token attention heatmap.
            """
        ).callout(kind="info")
    else:
        _layer = min(int(selected_layer_index), probe["attention"].shape[0] - 1)
        _head = min(int(selected_head_index), probe["attention"].shape[1] - 1)
        _score_line = (
            f"The selected head sends a mean {selected_head_score:.3f} of its attention to token 0."
            if selected_head_score is not None
            else "The selected head is ready for inspection."
        )
        _selected_matrix = probe["attention"][_layer, _head].numpy()
        selected_attention_fig = plot_attention_matrix(
            _selected_matrix,
            probe["tokens"],
            _layer,
            _head,
        )
        selected_attention_output = mo.vstack(
            [
                mo.md(
                    f"""
                    ## 5. Inspect one attention head

                    Hover any cell to see which query token attended to which key token.
                    A bright green-yellow vertical band at key position 0 is the
                    sink signature. {_score_line}
                    """
                ),
                selected_attention_fig,
            ],
            gap=0.75,
        )

    selected_attention_output
    return


@app.cell(hide_code=True)
def _(mo, probe):
    if probe is None:
        query_token_index = mo.ui.slider(
            start=0,
            stop=0,
            step=1,
            value=0,
            show_value=True,
            label="Query token",
            full_width=True,
        )
        query_token_view = mo.md(
            "The query-token selector appears after a successful probe."
        ).callout(kind="info")
    else:
        _last_token = max(0, len(probe["tokens"]) - 1)
        query_token_index = mo.ui.slider(
            start=0,
            stop=_last_token,
            step=1,
            value=_last_token,
            show_value=True,
            label="Query token",
            full_width=True,
        )
        query_token_view = mo.vstack(
            [
                mo.md(
                    """
                    ## 6. Follow one token's routing

                    Pick a query token and inspect which earlier tokens the
                    selected head attends to most strongly.
                    """
                ),
                query_token_index,
            ],
            gap=0.75,
        )
    query_token_view
    return (query_token_index,)


@app.cell(hide_code=True)
def _(plot_attention_flow, probe, query_token_index, selected_head_index, selected_layer_index):
    if probe is None:
        attention_flow_fig = None
    else:
        _layer = min(int(selected_layer_index), probe["attention"].shape[0] - 1)
        _head = min(int(selected_head_index), probe["attention"].shape[1] - 1)
        _query = min(int(query_token_index.value), len(probe["tokens"]) - 1)
        attention_flow_fig = plot_attention_flow(probe, _layer, _head, _query)

    attention_flow_fig
    return


@app.cell(hide_code=True)
def _(mo, plot_sink_map, sink_scores, sink_threshold):
    if sink_scores is None:
        sink_map_output = mo.md(
            "Sink atlas is waiting for a successful model probe."
        ).callout(kind="info")
    else:
        sink_map_fig = plot_sink_map(sink_scores, float(sink_threshold.value))
        sink_map_output = mo.vstack(
            [
                mo.md(
                    """
                    ## 7. Sink atlas

                    Each tile is one layer/head pair. White rings mark heads
                    above the selected strong-sink threshold.
                    """
                ),
                sink_map_fig,
            ],
            gap=0.75,
        )

    sink_map_output
    return


@app.cell(hide_code=True)
def _(mo, sink_table):
    strongest_sink_heads = sink_table.head(12) if sink_table is not None else None
    mo.vstack([mo.md("## 8. Strongest sink heads"), strongest_sink_heads])
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
                ## 9. Why streaming systems care

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
def _(
    mo,
    pd,
    plot_streaming_cache_bars,
    probe,
    streaming_cache_diagnostic,
    streaming_cache_window,
    torch,
):
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
        streaming_cache_fig = plot_streaming_cache_bars(streaming_cache_summary)
        _streaming_output = mo.vstack(
            [
                streaming_cache_fig,
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
    model,
    model_error,
    perturb_prompt,
    probe_config,
    probe_run_requested,
    run_attention_probe,
    tokenizer,
    torch,
):
    perturbed_prompt = perturb_prompt(analysis_prompt) if analysis_prompt else None

    if not probe_run_requested:
        perturbed_probe = None
        perturb_error = None
    elif model_error is not None or model is None or perturbed_prompt is None:
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
                probe_config.max_tokens,
            )
            perturb_error = None
        except Exception as exc:  # noqa: BLE001 - show perturb failures in UI.
            perturbed_probe = None
            perturb_error = exc
    return perturb_error, perturbed_probe, perturbed_prompt


@app.cell(hide_code=True)
def _(mo, perturbed_prompt):
    if perturbed_prompt is None:
        perturb_prompt_view = mo.md(
            """
            ## 10. Perturbation probe

            Waiting for a successful attention probe.
            """
        ).callout(kind="info")
    else:
        perturb_prompt_view = mo.md(f"""
        ## 10. Perturbation probe

        The paper uses perturbation experiments to argue that sinks can reduce
        how strongly information spreads across token positions. This miniature
        version changes one word and measures hidden-state drift by layer and
        token position.

        Perturbed prompt:

        ```text
        {perturbed_prompt}
        ```
        """)
    perturb_prompt_view
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
        layer_means = hidden_delta.mean(dim=1)
        impact_layer = int(layer_means.argmax().item())
        impact_mean = float(layer_means[impact_layer])
        impact_label = "embedding layer" if impact_layer == 0 else f"layer {impact_layer}"
        _perturb_summary_output = mo.md(
            f"""
            Perturbation drift summary:

            | Layer slice | Mean token drift |
            | --- | ---: |
            | Highest-impact slice ({impact_label}) | {impact_mean:.3f} |
            | Early layer | {first_layer_mean:.3f} |
            | Final layer | {final_layer_mean:.3f} |

            The heatmap above pre-shows the full perturbation pattern; the
            highest-impact row is where this one-word change spreads most
            strongly. Use the head inspector above to compare that effect against
            the strongest sink heads.

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
def _(CONTEXT_SWEEP_BUDGETS, DEFAULT_SWEEP_MODELS, MODEL_OPTIONS, TOKEN_BUDGET_OPTIONS, mo):
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
        value="Qwen2.5 7B open",
        label="Reference model",
        full_width=True,
    )
    comparison_model_b = mo.ui.dropdown(
        options=list(MODEL_OPTIONS.keys()),
        value="Qwen2.5 14B open",
        label="Comparison model",
        full_width=True,
    )
    comparison_token_budget = mo.ui.dropdown(
        options=list(TOKEN_BUDGET_OPTIONS.keys()),
        value="512 tokens",
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
        value="Qwen2.5 7B open",
        label="Long-context model",
        full_width=True,
    )
    context_sweep_button = mo.ui.run_button(
        label=f"Run context sweep: {CONTEXT_SWEEP_BUDGETS[0]}-{CONTEXT_SWEEP_BUDGETS[-1]} tokens",
        kind="success",
        full_width=True,
    )

    if comparison_run_mode.value == "Run selected pair":
        comparison_model_view = mo.hstack(
            [comparison_model_a, comparison_model_b],
            widths="equal",
            gap=1,
        )
    elif comparison_run_mode.value == "Run RTX family sweep":
        comparison_model_view = mo.md(
            "Planned RTX family sweep: "
            + ", ".join(f"`{label}`" for label in DEFAULT_SWEEP_MODELS)
            + "."
        ).callout(kind="info")
    else:
        comparison_model_view = mo.md(
            "Choose **Run selected pair** for a manual comparison, or **Run RTX family sweep** for the fixed cloud benchmark set."
        ).callout(kind="info")

    mo.vstack(
        [
            mo.md(
                """
                ## 11. Cloud GPU exploration

                The single-model probe proves the mechanics. The molab path is
                where we test the paper-shaped claim at a more serious scale:
                larger models, longer contexts, and model families beyond the
                first example.

                Qwen models are open defaults. Gemma and LLaMA entries are included
                because they match the paper's evidence more closely, but they may
                require Hugging Face access in the cloud runtime.
                """
            ),
            mo.hstack([comparison_run_mode, comparison_token_budget], widths="equal", gap=1),
            comparison_model_view,
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
        hf_token,
        torch,
        max_length,
        sink_threshold,
    ):
        _tokenizer, _model, _device, _model_dtype, _model_error = load_model_bundle(
            model_id,
            precision_key,
            hf_token,
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
        hf_token,
        torch,
        sink_threshold,
    ):
        _tokenizer, _model, _device, _model_dtype, _model_error = load_model_bundle(
            model_id,
            precision_key,
            hf_token,
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
    TOKEN_BUDGET_OPTIONS,
    comparison_model_a,
    comparison_model_b,
    comparison_run_button,
    comparison_run_mode,
    comparison_token_budget,
    hf_token,
    load_model_bundle,
    measure_anchor_effect,
    pd,
    probe_config,
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
        _sweep_prompt = probe_config.prompt if probe_config is not None else selected_prompt
        _comparison_token_budget = int(TOKEN_BUDGET_OPTIONS[comparison_token_budget.value])
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
                    _sweep_prompt,
                    load_model_bundle,
                    selected_precision_key,
                    hf_token,
                    torch,
                    _comparison_token_budget,
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
    hf_token,
    load_model_bundle,
    measure_context_sweep,
    pd,
    probe_config,
    selected_precision_key,
    selected_prompt,
    sink_threshold,
    torch,
):
    if not context_sweep_button.value or pd is None:
        context_sweep_table = None
    else:
        _context_model_id = MODEL_OPTIONS[context_sweep_model.value]
        _context_prompt = probe_config.prompt if probe_config is not None else selected_prompt
        context_sweep_table = pd.DataFrame(
            measure_context_sweep(
                _context_model_id,
                _context_prompt,
                CONTEXT_SWEEP_BUDGETS,
                load_model_bundle,
                selected_precision_key,
                hf_token,
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
def _(mo, plot_next_token_distribution, probe):
    if probe is None:
        next_token_output = mo.md(
            "Next-token distribution is waiting for a successful model probe."
        ).callout(kind="info")
    else:
        next_token_output = plot_next_token_distribution(probe["next_tokens"])
    mo.vstack([mo.md("## 12. Next-token distribution"), next_token_output])
    return


@app.cell
def _(mo):
    mo.md("""
    ## Why this weird token matters

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


@app.cell
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
