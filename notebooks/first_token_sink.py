# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "accelerate>=0.33",
#     "marimo>=0.23.11",
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
      .sink-hero svg g[stroke="#2563eb"] path {
        animation: sink-path-arrival 1.35s ease-out 1 both;
        stroke-dasharray: 120;
        stroke-dashoffset: 120;
      }
      .sink-hero svg g[stroke="#2563eb"] path:nth-child(2) { animation-delay: 70ms; }
      .sink-hero svg g[stroke="#2563eb"] path:nth-child(3) { animation-delay: 140ms; }
      .sink-hero svg g[stroke="#2563eb"] path:nth-child(4) { animation-delay: 210ms; }
      .sink-hero svg g[stroke="#2563eb"] path:nth-child(5) { animation-delay: 280ms; }
      .sink-hero svg g[stroke="#2563eb"] path:nth-child(6) { animation-delay: 350ms; }
      @keyframes sink-path-arrival { to { stroke-dashoffset: 0; } }
      @media (max-width: 760px) {
        .sink-hero__grid {
          grid-template-columns: 1fr;
          padding: 24px 18px;
        }
        .sink-hero h1 {
          font-size: 1.9rem;
        }
      }
      @media (prefers-reduced-motion: reduce) {
        .sink-hero svg g[stroke="#2563eb"] path { animation: none; stroke-dashoffset: 0; }
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
    **Reader's note.** Read vertically with **show code** off. The notebook opens
    as an explainer, then lets you reproduce the live probes on molab's
    RTX Pro 6000 GPU. Gemma and LLaMA runs require a Hugging Face read token; Qwen remains
    an open control. If you want to tinker locally with small models and
    CPU-friendly defaults, use `notebooks/first_token_sink_local.py` from the
    GitHub repo.
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
def _():
    dependency_error = None
    np = None
    pd = None
    plt = None
    go = None
    torch = None
    AutoModelForCausalLM = None
    AutoProcessor = None
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
        from transformers import AutoModelForCausalLM, AutoProcessor, AutoTokenizer
    except Exception as exc:  # noqa: BLE001 - show import failures inside notebook.
        dependency_error = exc
    return (
        AutoModelForCausalLM,
        AutoProcessor,
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
        dependency_status_output = None
    else:
        dependency_status_output = mo.md(
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
        ).callout(kind="danger")
    dependency_status_output
    return


@app.cell(hide_code=True)
def _(mo, pd):
    def format_result_table(
        table,
        *,
        columns=None,
        labels=None,
        decimals=None,
        page_size=10,
        label="",
        wrapped_columns=None,
    ):
        if table is None or pd is None:
            return None
        _display = table.copy()
        if columns is not None:
            _visible = [column for column in columns if column in _display.columns]
            _display = _display.loc[:, _visible]
        _condition_map = {
            "plain prompt": "Plain prompt",
            "with model first-token anchor": "First-token anchor",
            "load failed": "Load failed",
            "analysis failed": "Analysis failed",
        }
        if "condition" in _display.columns:
            _display["condition"] = _display["condition"].replace(_condition_map)
        if "architecture" in _display.columns:
            _display["architecture"] = _display["architecture"].replace(
                {"dense": "Dense", "moe": "MoE"}
            )
        for _column, _places in (decimals or {}).items():
            if _column in _display.columns and pd.api.types.is_numeric_dtype(
                _display[_column]
            ):
                _display[_column] = _display[_column].round(int(_places))
        _labels = labels or {}
        _display = _display.rename(columns=_labels)
        _wrapped = [
            _labels.get(column, column)
            for column in (wrapped_columns or [])
            if _labels.get(column, column) in _display.columns
        ]
        return mo.ui.table(
            _display,
            selection=None,
            pagination=len(_display) > int(page_size),
            page_size=int(page_size),
            show_column_summaries=False,
            show_data_types=False,
            show_download=True,
            wrapped_columns=_wrapped,
            label=label,
        )

    return (format_result_table,)


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
                **Required for live paper-model runs.** Public Qwen models work
                without authentication. Gemma and LLaMA runs require either an
                `HF_TOKEN` / `HUGGING_FACE_HUB_TOKEN` environment variable in
                the cloud runtime, or a token submitted here for this session.
                The token is never displayed by the notebook.
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
    mo.md(f"Hugging Face auth: `{hf_token_source}`.")
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
        "Gemma 2 2B (Hugging Face token required)": "google/gemma-2-2b",
        "Gemma 2 9B (Hugging Face token required)": "google/gemma-2-9b",
        "Gemma 4 31B Dense (Hugging Face token required)": "google/gemma-4-31B-it",
        "Gemma 4 26B-A4B MoE (Hugging Face token required)": "google/gemma-4-26B-A4B-it",
        "LLaMA 3.1 8B (Hugging Face token required)": "meta-llama/Llama-3.1-8B",
    }

    GEMMA4_DENSE_MOE_MODELS = [
        {
            "label": "Gemma 4 31B Dense",
            "model": "google/gemma-4-31B-it",
            "architecture": "dense",
            "total_parameters_b": 30.7,
            "active_parameters_b": 30.7,
            "reported_layers": 60,
            "notes": "Dense decoder; Gemma 4 hybrid local/global attention.",
        },
        {
            "label": "Gemma 4 26B-A4B MoE",
            "model": "google/gemma-4-26B-A4B-it",
            "architecture": "moe",
            "total_parameters_b": 25.2,
            "active_parameters_b": 3.8,
            "reported_layers": 30,
            "notes": "128 routed experts plus 1 shared expert; about 4B active parameters.",
        },
    ]

    DEFAULT_SWEEP_MODELS = [
        "Qwen2.5 1.5B open",
        "Qwen2.5 7B open",
        "Gemma 2 9B (Hugging Face token required)",
        "LLaMA 3.1 8B (Hugging Face token required)",
    ]

    NEUTRAL_BENCHMARK_PROMPTS = [
        (
            "Cardiac tissue repair after myocardial infarction depends on a carefully timed immune response. "
            "Early inflammatory cells clear damaged tissue and release signals that attract additional repair pathways. "
            "If that response lasts too long, oxidative stress and fibrosis can weaken ventricular function."
        ),
        (
            "Soil samples collected near a non-ferrous metal smelter contained elevated concentrations of cadmium, "
            "lead, and zinc. Isotope ratios suggested that ore processing, road transport, and local background geology "
            "all contributed to the observed contamination pattern."
        ),
        (
            "A pilot hospital ward introduced alcohol hand rub dispensers beside patient beds to encourage hand hygiene. "
            "Staff training, product placement, and infection-rate monitoring were used to evaluate whether bedside access "
            "changed daily disinfection behavior."
        ),
        (
            "Visual recognition remains stable even when objects change position, lighting, or scale. Neuroscience studies "
            "suggest that invariant recognition is supported by hierarchical representations that preserve category-relevant "
            "structure while discarding many accidental image details."
        ),
        (
            "The court reviewed whether an eyewitness identification should have been excluded after the witness recognized "
            "the defendant in the courtroom. The opinion distinguished reliability concerns from admissibility and emphasized "
            "the role of cross-examination and fact-finder judgment."
        ),
        (
            "A synthesis route produced several ruthenium polypyridyl complexes with measurable anticancer activity in cell culture. "
            "Follow-up assays examined DNA binding, mitochondrial membrane potential, reactive oxygen species, and apoptosis markers "
            "to characterize the mechanism."
        ),
        (
            "Pharmacokinetic measurements after oral omeprazole administration showed low systemic exposure in llamas. Plasma samples "
            "were collected across multiple time points, and the estimated absorption profile suggested that higher doses did not "
            "substantially improve bioavailability."
        ),
        (
            "Studies of host genetic susceptibility to bacterial carriage combine epidemiological sampling with variant-level analysis. "
            "Because colonization depends on immune response, microbial strain differences, and environment, association signals are often "
            "modest and require careful interpretation."
        ),
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
        GEMMA4_DENSE_MOE_MODELS,
        MODEL_OPTIONS,
        NEUTRAL_BENCHMARK_PROMPTS,
        PAPER_URL,
        PRECISION_OPTIONS,
        PROMPT_PRESETS,
        TOKEN_BUDGET_OPTIONS,
    )


@app.cell
def _(ALPHAXIV_URL, PAPER_URL, mo):
    mo.md(f"""
    ## The investigation

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

    We use three complementary roles. LLaMA 3.1 is the direct-reproduction
    family; Gemma 2 9B is a replication-style extension using the same protocol;
    and Qwen is an open scale control. The final Dense-vs-MoE experiment asks a
    new architecture question that goes beyond the paper.

    Links: [alphaXiv]({ALPHAXIV_URL}) | [arXiv]({PAPER_URL})
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### A decoder-only attention block in one minute

    For query token $i$, head $h$ in layer $\ell$ assigns a causal
    probability to every earlier key token $j \leq i$:

    $$
    \alpha_{ij}^{(\ell,h)} =
    \operatorname{softmax}_{j \leq i}
    \left(\frac{{q_i^{(\ell,h)}}^{\top}k_j^{(\ell,h)}}{\sqrt{d_h}}\right),
    \qquad
    z_i^{(\ell,h)} =
    \sum_{j \leq i}\alpha_{ij}^{(\ell,h)}W_V^{(\ell,h)}v_j^{(\ell)}.
    $$

    The first equation produces the attention map; the second says why it is
    a **mixing operator**. Every output is a weighted combination of earlier
    token values. The causal mask makes the matrix lower triangular, so later
    tokens can read earlier ones but not vice versa.

    High attention therefore need not mean "this token is semantically
    important." It can also mean "this is where the head routes when it wants
    to avoid mixing useful content." That is the control-flow interpretation
    tested throughout this notebook.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    collapse_guess = mo.ui.dropdown(
        options=["Collapse", "Survives"],
        value="Survives",
        label="Your prediction",
        full_width=True,
    )
    escape_valve = mo.ui.slider(
        start=0.0,
        stop=0.95,
        step=0.05,
        value=0.35,
        show_value=True,
        label="Escape valve: no-op / sink fraction",
        full_width=True,
    )
    chamber_depth = mo.ui.slider(
        start=4,
        stop=48,
        step=2,
        value=24,
        show_value=True,
        label="Network depth",
        full_width=True,
    )
    reveal_collapse_button = mo.ui.run_button(
        label="Reveal chamber outcome",
        kind="success",
        full_width=True,
    )
    mixing_chamber_controls = mo.vstack(
        [
            mo.md(
                """
                ### NumPy verification: why depth needs an escape valve

                Over-mixing, rank collapse, and representational collapse are
                best read as a causal chain. Repeated attention mixing makes
                token states less distinguishable; in the strongest linear case
                this becomes rank collapse, and rank collapse implies
                representational collapse. The reverse does not have to hold.

                This toy chamber is a faithful simulation of that mechanism, not
                a decorative animation. Each token starts as a random vector. At
                each layer it either mixes with the others or keeps part of its
                current identity through a no-op route, which is the role the
                paper assigns to sink-like heads.
                """
            ),
            mo.md(
                """
                **Tiny prediction game.** Before revealing the curves, choose
                whether this setup will collapse token identities or keep them
                distinguishable.
                """
            ),
            mo.hstack(
                [collapse_guess, escape_valve, chamber_depth],
                widths="equal",
                wrap=True,
                gap=1,
            ),
            reveal_collapse_button,
        ],
        gap=1,
    )
    return (
        chamber_depth,
        collapse_guess,
        escape_valve,
        mixing_chamber_controls,
        reveal_collapse_button,
    )


@app.cell(hide_code=True)
def _(apply_plot_theme, go, np):
    def simulate_mixing_chamber(
        n_tokens=8,
        dim=16,
        depth=24,
        noop_fraction=0.0,
        temperature=1.0,
        seed=7,
    ):
        _rng = np.random.default_rng(seed)
        _representations = _rng.normal(size=(n_tokens, dim))
        _states = [_representations.copy()]
        _effective_ranks = []
        _similarities = []

        def _measure(_matrix):
            _singular_values = np.linalg.svd(_matrix, compute_uv=False)
            _total = max(float(_singular_values.sum()), 1e-12)
            _probabilities = _singular_values / _total
            _effective_rank = float(
                np.exp(-(_probabilities * np.log(_probabilities + 1e-12)).sum())
            )
            _normed = _matrix / np.clip(
                np.linalg.norm(_matrix, axis=1, keepdims=True),
                1e-12,
                None,
            )
            _sim_matrix = _normed @ _normed.T
            _off_diag = _sim_matrix[~np.eye(n_tokens, dtype=bool)]
            return _effective_rank, float(_off_diag.mean())

        _rank, _similarity = _measure(_representations)
        _effective_ranks.append(_rank)
        _similarities.append(_similarity)

        for _ in range(depth):
            _logits = _rng.normal(size=(n_tokens, n_tokens)) / temperature
            _attention = np.exp(_logits - _logits.max(axis=1, keepdims=True))
            _attention /= _attention.sum(axis=1, keepdims=True)
            _mixed = _attention @ _representations
            _representations = (
                (1.0 - noop_fraction) * _mixed
                + noop_fraction * _representations
            )
            _states.append(_representations.copy())
            _rank, _similarity = _measure(_representations)
            _effective_ranks.append(_rank)
            _similarities.append(_similarity)

        _rank_ratio = np.asarray(_effective_ranks) / float(min(n_tokens, dim))
        return {
            "states": np.asarray(_states),
            "rank_ratio": _rank_ratio,
            "similarity": np.asarray(_similarities),
            "final_rank_ratio": float(_rank_ratio[-1]),
            "final_similarity": float(_similarities[-1]),
        }

    def plot_mixing_chamber_curves(mixing_chamber_result):
        _layers = np.arange(len(mixing_chamber_result["rank_ratio"]))
        _fig = go.Figure()
        _fig.add_trace(
            go.Scatter(
                x=_layers,
                y=mixing_chamber_result["rank_ratio"],
                mode="lines+markers",
                name="normalized effective rank",
                line={"color": "#2563eb", "width": 3},
                marker={"size": 5},
                hovertemplate="layer=%{x}<br>rank=%{y:.3f}<extra></extra>",
            )
        )
        _fig.add_trace(
            go.Scatter(
                x=_layers,
                y=mixing_chamber_result["similarity"],
                mode="lines+markers",
                name="mean token similarity",
                line={"color": "#16a34a", "width": 3},
                marker={"size": 5},
                hovertemplate="layer=%{x}<br>similarity=%{y:.3f}<extra></extra>",
            )
        )
        _fig.add_hrect(
            y0=0.80,
            y1=1.05,
            fillcolor="#fef3c7",
            opacity=0.28,
            line_width=0,
            annotation_text="collapse zone",
            annotation_position="top left",
        )
        _fig.update_layout(
            title="Repeated mixing makes tokens less distinguishable",
            height=390,
            margin={"l": 54, "r": 20, "t": 58, "b": 54},
            hovermode="x unified",
            legend={"orientation": "h", "y": -0.22},
            xaxis={"title": "Layer"},
            yaxis={
                "title": "Score",
                "range": [-0.05, 1.05],
                "gridcolor": "#e5edf7",
            },
        )
        return apply_plot_theme(_fig)

    def token_identity_strip(mixing_chamber_result):
        _states = mixing_chamber_result["states"]
        _indices = [0, max(0, len(_states) // 2), len(_states) - 1]
        _selected = _states[_indices]
        _flat = _selected.reshape(-1, _selected.shape[-1])
        _centered = _flat - _flat.mean(axis=0, keepdims=True)
        _, _, _vh = np.linalg.svd(_centered, full_matrices=False)
        _components = _vh[:3].T
        if _components.shape[1] < 3:
            _components = np.pad(_components, ((0, 0), (0, 3 - _components.shape[1])))
        _projected = _centered @ _components[:, :3]
        _mins = _projected.min(axis=0, keepdims=True)
        _ranges = np.clip(_projected.max(axis=0, keepdims=True) - _mins, 1e-9, None)
        _rgb = 45 + 180 * ((_projected - _mins) / _ranges)
        _rgb = _rgb.reshape(_selected.shape[0], _selected.shape[1], 3).astype(int)

        _rows = []
        for _row_index, _layer_index in enumerate(_indices):
            _beads = []
            for _token_index, _color in enumerate(_rgb[_row_index]):
                _border = "#16a34a" if _token_index == 0 else "#ffffff"
                _beads.append(
                    f"""
                    <span class="mixing-bead"
                          style="background: rgb({_color[0]}, {_color[1]}, {_color[2]});
                                 border-color: {_border};">
                      {_token_index}
                    </span>
                    """
                )
            _label = "initial layer" if _layer_index == 0 else f"layer {_layer_index}"
            _rows.append(
                f"""
                <div class="mixing-row">
                  <div class="mixing-row-label">{_label}</div>
                  <div class="mixing-beads">{''.join(_beads)}</div>
                </div>
                """
            )

        return f"""
        <style>
          .mixing-chamber {{
            border: 1px solid #d7dde8;
            border-radius: 8px;
            background: #fbfdff;
            padding: 14px;
          }}
          .mixing-row {{
            align-items: center;
            display: grid;
            grid-template-columns: 108px minmax(0, 1fr);
            gap: 12px;
            margin: 9px 0;
          }}
          .mixing-row-label {{
            color: #475569;
            font-size: 0.82rem;
            font-weight: 800;
          }}
          .mixing-beads {{
            display: flex;
            flex-wrap: wrap;
            gap: 8px;
          }}
          .mixing-bead {{
            align-items: center;
            border: 3px solid #ffffff;
            border-radius: 999px;
            box-shadow: 0 4px 12px rgba(15, 23, 42, 0.14);
            color: #0f172a;
            display: inline-flex;
            font-size: 0.75rem;
            font-weight: 850;
            height: 34px;
            justify-content: center;
            width: 34px;
          }}
        </style>
        <div class="mixing-chamber">
          <div style="color:#0f172a;font-weight:850;margin-bottom:8px;">
            Token identity strip
          </div>
          <div style="color:#475569;font-size:0.9rem;line-height:1.45;margin-bottom:10px;">
            Each bead color is computed from the simulated token vectors. When
            the chamber over-mixes, the final row loses color diversity.
          </div>
          {''.join(_rows)}
        </div>
        """

    return simulate_mixing_chamber, plot_mixing_chamber_curves, token_identity_strip


@app.cell(hide_code=True)
def _(
    chamber_depth,
    collapse_guess,
    escape_valve,
    go,
    mo,
    np,
    plot_mixing_chamber_curves,
    reveal_collapse_button,
    simulate_mixing_chamber,
    token_identity_strip,
):
    if np is None or go is None:
        mixing_chamber_output = mo.md(
            "The mixing chamber needs NumPy and Plotly to render."
        ).callout(kind="danger")
    elif not reveal_collapse_button.value:
        mixing_chamber_output = mo.md(
            """
            The chamber is sealed. Make a prediction above, then click
            **Reveal chamber outcome** to see whether repeated mixing collapses
            token identities.
            """
        ).callout(kind="info")
    else:
        _mixing_chamber_result = simulate_mixing_chamber(
            depth=int(chamber_depth.value),
            noop_fraction=float(escape_valve.value),
        )
        _final_rank = _mixing_chamber_result["final_rank_ratio"]
        _final_similarity = _mixing_chamber_result["final_similarity"]
        if _final_rank < 0.25 and _final_similarity > 0.80:
            _verdict = "rank collapse"
            _kind = "warn"
        elif _final_similarity > 0.55:
            _verdict = "over-mixing"
            _kind = "info"
        else:
            _verdict = "identities preserved"
            _kind = "success"
        _prediction = "rank collapse" if collapse_guess.value == "Collapse" else "identities preserved"
        _prediction_hit = (
            (_prediction == "rank collapse" and _verdict == "rank collapse")
            or (_prediction == "identities preserved" and _verdict != "rank collapse")
        )
        _prediction_line = (
            "Your prediction held up."
            if _prediction_hit
            else "The chamber disagreed with your prediction."
        )
        mixing_chamber_output = mo.vstack(
            [
                mo.hstack(
                    [
                        mo.Html(token_identity_strip(_mixing_chamber_result)),
                        mo.md(
                            f"""
                            **Chamber readout**

                            | Signal | Value |
                            | --- | ---: |
                            | Escape valve | {float(escape_valve.value):.2f} |
                            | Simulated depth | {int(chamber_depth.value)} |
                            | Final normalized effective rank | {_final_rank:.3f} |
                            | Final mean token similarity | {_final_similarity:.3f} |
                            | State | **{_verdict}** |
                            | Prediction | {collapse_guess.value} |

                            {_prediction_line} Low escape-valve settings force
                            tokens to keep mixing, so rank falls and pairwise
                            similarity rises. Opening the valve slows the
                            collapse by letting some layers behave closer to the
                            paper's approximate no-op.
                            """
                        ).callout(kind=_kind),
                    ],
                    widths=[1.15, 0.85],
                    wrap=True,
                    gap=1,
                ),
                plot_mixing_chamber_curves(_mixing_chamber_result),
            ],
            gap=1,
        )
    return (mixing_chamber_output,)


@app.cell(hide_code=True)
def _(mo):
    import html as html_lib

    circuit_breaker_html = r"""
    <!doctype html>
    <html lang="en">
    <head>
      <meta charset="utf-8">
      <meta name="viewport" content="width=device-width, initial-scale=1">
    </head>
    <body>
      <div id="circuit-breaker-challenge">
        <style>
          :root {
            color: #172033;
            font-family: Inter, ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
          }
          * { box-sizing: border-box; }
          body { margin: 0; }
          #circuit-breaker-challenge {
            background: linear-gradient(145deg, #f8fbff 0%, #ffffff 56%, #f3fbf7 100%);
            border: 1px solid #d8e2ee;
            border-radius: 12px;
            color: #172033;
            overflow: hidden;
          }
          #circuit-breaker-challenge.cb-win-pulse {
            animation: cb-win-pulse 760ms ease-out;
          }
          @keyframes cb-win-pulse {
            0% { border-color: #d8e2ee; box-shadow: 0 0 0 0 rgba(22,163,74,0); }
            38% { border-color: #22a06b; box-shadow: 0 0 0 5px rgba(34,160,107,0.16); }
            100% { border-color: #b7dfca; box-shadow: 0 0 0 0 rgba(34,160,107,0); }
          }
          .cb-challenge {
            align-items: center;
            background: #eef6ff;
            border-bottom: 1px solid #cfe0f3;
            display: grid;
            gap: 11px;
            grid-template-columns: 34px minmax(0, 1fr);
            padding: 13px 18px;
            transition: background-color 220ms ease, border-color 220ms ease;
          }
          .cb-challenge[data-state="safe"] {
            background: #ecfdf3;
            border-color: #b7dfca;
          }
          .cb-challenge__icon {
            align-items: center;
            background: #dbeafe;
            border-radius: 50%;
            color: #1d4ed8;
            display: inline-flex;
            font-size: 1.02rem;
            font-weight: 850;
            height: 32px;
            justify-content: center;
            transition: background-color 220ms ease, color 220ms ease, transform 220ms ease;
            width: 32px;
          }
          .cb-challenge[data-state="safe"] .cb-challenge__icon {
            background: #bbf7d0;
            color: #15803d;
            transform: scale(1.06);
          }
          .cb-challenge__kicker {
            color: #64748b;
            display: block;
            font-size: 0.68rem;
            font-weight: 850;
            letter-spacing: .06em;
            margin-bottom: 2px;
            text-transform: uppercase;
          }
          .cb-challenge__message { color: #1e3a5f; font-size: 0.9rem; line-height: 1.4; }
          .cb-challenge[data-state="safe"] .cb-challenge__message { color: #14532d; }
          .cb-top {
            align-items: start;
            display: grid;
            gap: 18px;
            grid-template-columns: minmax(220px, 0.78fr) minmax(0, 1.22fr);
            padding: 18px 18px 12px;
          }
          .cb-controls { display: grid; gap: 16px; }
          .cb-field { display: grid; gap: 7px; }
          .cb-field label { color: #334155; font-size: 0.86rem; font-weight: 750; }
          .cb-value { color: #0f766e; font-variant-numeric: tabular-nums; }
          .cb-range {
            --fill: 0%;
            appearance: none;
            background: linear-gradient(to right, #0f766e 0 var(--fill), #dbe5ee var(--fill) 100%);
            border-radius: 999px;
            cursor: pointer;
            height: 8px;
            margin: 3px 0;
            outline: none;
            width: 100%;
          }
          .cb-range::-webkit-slider-runnable-track { background: transparent; border: 0; height: 8px; }
          .cb-range::-webkit-slider-thumb {
            appearance: none;
            background: #ffffff;
            border: 3px solid #0f766e;
            border-radius: 50%;
            box-shadow: 0 2px 8px rgba(15,118,110,0.24);
            height: 20px;
            margin-top: -6px;
            width: 20px;
          }
          .cb-range::-moz-range-track { background: #dbe5ee; border: 0; border-radius: 999px; height: 8px; }
          .cb-range::-moz-range-progress { background: #0f766e; border-radius: 999px; height: 8px; }
          .cb-range::-moz-range-thumb {
            background: #ffffff;
            border: 3px solid #0f766e;
            border-radius: 50%;
            box-shadow: 0 2px 8px rgba(15,118,110,0.24);
            height: 16px;
            width: 16px;
          }
          .cb-range:focus-visible { outline: 3px solid rgba(37,99,235,0.28); outline-offset: 4px; }
          .cb-ticks {
            color: #8190a3;
            display: flex;
            font-size: 0.66rem;
            font-variant-numeric: tabular-nums;
            justify-content: space-between;
            line-height: 1;
          }
          .cb-metrics { display: grid; gap: 10px; grid-template-columns: repeat(auto-fit, minmax(146px, 1fr)); }
          .cb-metric {
            align-items: center;
            background: rgba(255,255,255,0.88);
            border: 1px solid #dce6f1;
            border-radius: 9px;
            display: grid;
            gap: 8px;
            grid-template-columns: minmax(0, 1fr) 54px;
            min-height: 84px;
            padding: 11px;
            transition: border-color 200ms ease, box-shadow 200ms ease;
          }
          .cb-metric[data-health="good"] { border-color: #a7d8bb; }
          .cb-metric[data-health="caution"] { border-color: #e9ca82; }
          .cb-metric[data-health="bad"] { border-color: #efb0aa; }
          .cb-metric__label { color: #64748b; font-size: 0.69rem; font-weight: 800; letter-spacing: .02em; text-transform: uppercase; }
          .cb-metric__note { color: #475569; font-size: 0.72rem; line-height: 1.3; margin-top: 4px; }
          .cb-gauge { color: #64748b; height: 52px; position: relative; width: 52px; }
          .cb-metric[data-health="good"] .cb-gauge { color: #15803d; }
          .cb-metric[data-health="caution"] .cb-gauge { color: #b7791f; }
          .cb-metric[data-health="bad"] .cb-gauge { color: #c2413b; }
          .cb-gauge svg { display: block; height: 52px; overflow: visible; transform: rotate(-90deg); width: 52px; }
          .cb-gauge__track { fill: none; stroke: #e7edf3; stroke-width: 5; }
          .cb-gauge__progress {
            fill: none;
            stroke: currentColor;
            stroke-dasharray: 100;
            stroke-dashoffset: 100;
            stroke-linecap: round;
            stroke-width: 5;
            transition: stroke-dashoffset 220ms ease, stroke 220ms ease;
          }
          .cb-metric__value {
            color: currentColor;
            font-size: 0.91rem;
            font-variant-numeric: tabular-nums;
            font-weight: 850;
            left: 50%;
            position: absolute;
            top: 50%;
            transform: translate(-50%, -50%);
          }
          .cb-status {
            background: #f8fafc;
            border-left: 4px solid #94a3b8;
            color: #334155;
            font-size: 0.86rem;
            line-height: 1.45;
            margin: 0 18px 13px;
            padding: 10px 12px;
            transition: background-color 200ms ease, border-color 200ms ease;
          }
          .cb-status[data-state="safe"] { background: #ecfdf3; border-color: #22a06b; }
          .cb-status[data-state="sealed"] { background: #fff8e8; border-color: #d39a2c; }
          .cb-status[data-state="mixing"] { background: #fff1f0; border-color: #e45555; }
          .cb-status strong { color: #0f172a; }
          .cb-grid-wrap { overflow-x: auto; padding: 1px 18px 16px; }
          .cb-grid-stage { min-width: 610px; position: relative; }
          .cb-flow {
            height: 100%;
            left: 0;
            overflow: visible;
            pointer-events: none;
            position: absolute;
            top: 0;
            width: 100%;
            z-index: 3;
          }
          .cb-flow__signal, .cb-flow__noise {
            fill: none;
            stroke-linecap: round;
            stroke-width: 2.2;
            transition: opacity 220ms ease, stroke-width 220ms ease;
          }
          .cb-flow__signal { stroke: #158a5c; stroke-dasharray: 7 7; }
          .cb-flow__noise { stroke: #dc4c4c; stroke-dasharray: 4 7; }
          .cb-grid { display: grid; gap: 5px; min-width: 610px; position: relative; z-index: 2; }
          .cb-grid__head { align-items: center; color: #64748b; display: grid; font-size: 0.72rem; font-weight: 800; grid-template-columns: 116px repeat(7, minmax(48px, 1fr)); text-align: center; }
          .cb-grid__head span:first-child { text-align: left; }
          .cb-row { align-items: center; display: grid; gap: 5px; grid-template-columns: 116px repeat(7, minmax(48px, 1fr)); }
          .cb-token { color: #334155; font-size: 0.77rem; font-weight: 750; line-height: 1.2; }
          .cb-row--anchor .cb-token { color: #596579; }
          .cb-cell {
            background: rgba(255,255,255,0.88);
            border: 1px solid rgba(148,163,184,0.42);
            border-radius: 7px;
            height: 38px;
            overflow: hidden;
            position: relative;
          }
          .cb-cell__signal, .cb-cell__noise {
            inset: 0;
            opacity: 0;
            position: absolute;
            transition: opacity 220ms ease;
          }
          .cb-cell__signal { background: #22a06b; }
          .cb-cell__noise { background: #e45555; }
          .cb-cell[data-mark="mixed"] .cb-cell__signal { clip-path: polygon(0 0, 0 100%, 100% 100%); }
          .cb-cell[data-mark="mixed"] .cb-cell__noise { clip-path: polygon(0 0, 100% 0, 100% 100%); }
          .cb-cell[data-mark="signal"] { box-shadow: inset 0 0 12px rgba(22,163,74,0.24); }
          .cb-cell[data-mark="spill"] { box-shadow: inset 0 0 12px rgba(220,76,76,0.20); }
          .cb-cell.is-anchor {
            background: repeating-linear-gradient(135deg, #eef2f6 0 7px, #e5eaf0 7px 14px);
            border: 1px dashed #8794a6;
          }
          .cb-cell.is-anchor::after {
            color: #64748b;
            content: "·";
            font-size: 1.05rem;
            left: 50%;
            position: absolute;
            top: 50%;
            transform: translate(-50%, -56%);
          }
          .cb-legend { color: #64748b; display: flex; flex-wrap: wrap; font-size: 0.76rem; gap: 14px; padding: 0 18px 18px; }
          .cb-legend span { align-items: center; display: inline-flex; gap: 6px; }
          .cb-dot { border-radius: 50%; display: inline-block; height: 9px; width: 9px; }
          .cb-dot--signal { background: #22a06b; }
          .cb-dot--noise { background: #e45555; }
          .cb-dot--anchor { background: #94a3b8; border: 1px dashed #596579; }
          @media (max-width: 700px) {
            .cb-top { grid-template-columns: 1fr; }
          }
          @media (max-width: 420px) {
            .cb-challenge, .cb-top { padding-left: 13px; padding-right: 13px; }
            .cb-status { margin-left: 13px; margin-right: 13px; }
            .cb-grid-wrap { padding-left: 13px; padding-right: 13px; }
            .cb-legend { padding-left: 13px; padding-right: 13px; }
          }
          @media (prefers-reduced-motion: reduce) {
            #circuit-breaker-challenge *, #circuit-breaker-challenge *::before, #circuit-breaker-challenge *::after {
              animation-duration: 0.01ms !important;
              transition-duration: 0.01ms !important;
            }
          }
        </style>
        <section aria-label="Circuit Breaker Challenge">
          <div class="cb-challenge" data-role="challenge" data-state="active" aria-live="polite">
            <div class="cb-challenge__icon" data-role="challenge-icon" aria-hidden="true">◎</div>
            <div>
              <span class="cb-challenge__kicker" data-role="challenge-kicker">Challenge</span>
              <div class="cb-challenge__message" data-role="challenge-message">Find a setting where identity survives, the fact reaches the query, and perturbation spill stays contained.</div>
            </div>
          </div>
          <div class="cb-top">
            <div class="cb-controls">
              <div class="cb-field">
                <label for="cb-sink">Heads routed to the anchor <span class="cb-value" data-role="sink-value"></span></label>
                <input class="cb-range" id="cb-sink" data-role="sink" type="range" min="0" max="100" step="5" value="10">
                <div class="cb-ticks" aria-hidden="true"><span>0%</span><span>25%</span><span>50%</span><span>75%</span><span>100%</span></div>
              </div>
              <div class="cb-field">
                <label for="cb-depth">Transformer depth <span class="cb-value" data-role="depth-value"></span></label>
                <input class="cb-range" id="cb-depth" data-role="depth" type="range" min="4" max="24" step="2" value="18">
                <div class="cb-ticks" aria-hidden="true"><span>4</span><span>8</span><span>12</span><span>16</span><span>20</span><span>24</span></div>
              </div>
            </div>
            <div class="cb-metrics">
              <div class="cb-metric" data-role="identity-card">
                <div><div class="cb-metric__label">Identity separation</div><div class="cb-metric__note">higher resists collapse</div></div>
                <div class="cb-gauge"><svg viewBox="0 0 48 48" aria-hidden="true"><circle class="cb-gauge__track" cx="24" cy="24" r="18"></circle><circle class="cb-gauge__progress" data-role="identity-ring" pathLength="100" cx="24" cy="24" r="18"></circle></svg><div class="cb-metric__value" data-role="identity"></div></div>
              </div>
              <div class="cb-metric" data-role="fact-card">
                <div><div class="cb-metric__label">Fact at query</div><div class="cb-metric__note">enough mixing is required</div></div>
                <div class="cb-gauge"><svg viewBox="0 0 48 48" aria-hidden="true"><circle class="cb-gauge__track" cx="24" cy="24" r="18"></circle><circle class="cb-gauge__progress" data-role="fact-ring" pathLength="100" cx="24" cy="24" r="18"></circle></svg><div class="cb-metric__value" data-role="fact"></div></div>
              </div>
              <div class="cb-metric" data-role="noise-card">
                <div><div class="cb-metric__label">Perturbation spill</div><div class="cb-metric__note">lower is safer</div></div>
                <div class="cb-gauge"><svg viewBox="0 0 48 48" aria-hidden="true"><circle class="cb-gauge__track" cx="24" cy="24" r="18"></circle><circle class="cb-gauge__progress" data-role="noise-ring" pathLength="100" cx="24" cy="24" r="18"></circle></svg><div class="cb-metric__value" data-role="noise"></div></div>
              </div>
            </div>
          </div>
          <div class="cb-status" data-role="status" data-state="mixing" aria-live="polite"></div>
          <div class="cb-grid-wrap">
            <div class="cb-grid-stage" data-role="grid-stage">
              <svg class="cb-flow" data-role="flow" aria-hidden="true">
                <defs>
                  <marker id="cb-arrow-signal" markerWidth="7" markerHeight="7" refX="6" refY="3.5" orient="auto"><path d="M0,0 L7,3.5 L0,7 Z" fill="#158a5c"></path></marker>
                  <marker id="cb-arrow-noise" markerWidth="7" markerHeight="7" refX="6" refY="3.5" orient="auto"><path d="M0,0 L7,3.5 L0,7 Z" fill="#dc4c4c"></path></marker>
                </defs>
                <path class="cb-flow__signal" data-role="signal-path" marker-end="url(#cb-arrow-signal)"></path>
                <path class="cb-flow__noise" data-role="noise-path-a" marker-end="url(#cb-arrow-noise)"></path>
                <path class="cb-flow__noise" data-role="noise-path-b" marker-end="url(#cb-arrow-noise)"></path>
                <path class="cb-flow__noise" data-role="noise-path-query" marker-end="url(#cb-arrow-noise)"></path>
              </svg>
              <div class="cb-grid" data-role="grid" role="img" aria-label="Token states sampled across Transformer depth"></div>
            </div>
          </div>
          <div class="cb-legend"><span><i class="cb-dot cb-dot--signal"></i>useful signal</span><span><i class="cb-dot cb-dot--noise"></i>perturbation</span><span><i class="cb-dot cb-dot--anchor"></i>low-information anchor</span></div>
        </section>
        <script>
          (() => {
            const root = document.getElementById("circuit-breaker-challenge");
            if (!root) return;
            const els = {
              challenge: root.querySelector('[data-role="challenge"]'),
              challengeIcon: root.querySelector('[data-role="challenge-icon"]'),
              challengeKicker: root.querySelector('[data-role="challenge-kicker"]'),
              challengeMessage: root.querySelector('[data-role="challenge-message"]'),
              sink: root.querySelector('[data-role="sink"]'),
              depth: root.querySelector('[data-role="depth"]'),
              sinkValue: root.querySelector('[data-role="sink-value"]'),
              depthValue: root.querySelector('[data-role="depth-value"]'),
              identity: root.querySelector('[data-role="identity"]'),
              fact: root.querySelector('[data-role="fact"]'),
              noise: root.querySelector('[data-role="noise"]'),
              identityCard: root.querySelector('[data-role="identity-card"]'),
              factCard: root.querySelector('[data-role="fact-card"]'),
              noiseCard: root.querySelector('[data-role="noise-card"]'),
              identityRing: root.querySelector('[data-role="identity-ring"]'),
              factRing: root.querySelector('[data-role="fact-ring"]'),
              noiseRing: root.querySelector('[data-role="noise-ring"]'),
              status: root.querySelector('[data-role="status"]'),
              grid: root.querySelector('[data-role="grid"]'),
              gridStage: root.querySelector('[data-role="grid-stage"]'),
              flow: root.querySelector('[data-role="flow"]'),
              signalPath: root.querySelector('[data-role="signal-path"]'),
              noisePaths: [
                root.querySelector('[data-role="noise-path-a"]'),
                root.querySelector('[data-role="noise-path-b"]'),
                root.querySelector('[data-role="noise-path-query"]'),
              ],
            };
            const thresholds = { identity: 0.62, fact: 0.50, noise: 0.52 };
            const tokens = [
              { label: "⌂  anchor", kind: "anchor" },
              { label: "✓  useful fact", kind: "fact" },
              { label: "✦  edited word", kind: "perturb" },
              { label: "·  distractor A", kind: "distractor" },
              { label: "·  distractor B", kind: "distractor" },
              { label: "?  final query", kind: "query" },
            ];
            const clamp = (value) => Math.max(0, Math.min(1, value));
            const pct = (value) => `${Math.round(value * 100)}%`;
            const layerLabels = [];
            const cellRefs = [];
            let initialized = false;
            let wasSafe = false;
            let renderFrame = null;
            let resizeFrame = null;

            function model() {
              const sink = Number(els.sink.value) / 100;
              const depth = Number(els.depth.value);
              const mix = 1 - sink;
              const pressure = clamp(mix * depth / 18);
              const identity = clamp(1 - 0.78 * pressure + 0.12 * sink);
              const rawFact = 1 - Math.exp(-0.31 * mix * depth);
              const noise = clamp(0.9 * pressure);
              const fact = clamp(rawFact * (1 - 0.54 * noise));
              const safe = identity >= thresholds.identity && fact >= thresholds.fact && noise <= thresholds.noise;
              const sealed = fact < thresholds.fact;
              return { sink, depth, mix, identity, fact, noise, safe, sealed };
            }
            function tokenState(kind, progress, values) {
              if (kind === "anchor") return { signal: 0.02, noise: 0.02 };
              if (kind === "fact") return { signal: clamp(1 - 0.24 * values.noise * progress), noise: 0.14 * values.noise * progress };
              if (kind === "perturb") return { signal: 0.08 * progress, noise: clamp(0.95 - 0.35 * values.sink * progress) };
              if (kind === "query") return { signal: values.fact * Math.pow(progress, 1.45), noise: values.noise * Math.pow(progress, 1.18) };
              return { signal: 0.23 * values.fact * progress, noise: 0.64 * values.noise * progress };
            }
            function mark(state) {
              const signalVisible = state.signal > 0.16;
              const noiseVisible = state.noise > 0.16;
              if (signalVisible && noiseVisible) return "mixed";
              if (signalVisible) return "signal";
              if (noiseVisible) return "spill";
              return "quiet";
            }
            function health(metric, value) {
              if (metric === "identity") return value >= thresholds.identity ? "good" : value >= 0.40 ? "caution" : "bad";
              if (metric === "fact") return value >= thresholds.fact ? "good" : value >= 0.30 ? "caution" : "bad";
              return value <= thresholds.noise ? "good" : value <= 0.75 ? "caution" : "bad";
            }
            function buildGrid() {
              const head = document.createElement("div");
              head.className = "cb-grid__head";
              const headTitle = document.createElement("span");
              headTitle.textContent = "token state";
              head.appendChild(headTitle);
              for (let index = 0; index < 7; index += 1) {
                const label = document.createElement("span");
                layerLabels.push(label);
                head.appendChild(label);
              }
              els.grid.appendChild(head);

              tokens.forEach((token) => {
                const row = document.createElement("div");
                row.className = `cb-row${token.kind === "anchor" ? " cb-row--anchor" : ""}`;
                const tokenLabel = document.createElement("div");
                tokenLabel.className = "cb-token";
                tokenLabel.textContent = token.label;
                row.appendChild(tokenLabel);
                const rowCells = [];
                for (let index = 0; index < 7; index += 1) {
                  const cell = document.createElement("div");
                  cell.className = `cb-cell${token.kind === "anchor" ? " is-anchor" : ""}`;
                  cell.dataset.mark = token.kind === "anchor" ? "quiet" : "quiet";
                  cell.setAttribute("role", "img");
                  const signalLayer = document.createElement("span");
                  signalLayer.className = "cb-cell__signal";
                  const noiseLayer = document.createElement("span");
                  noiseLayer.className = "cb-cell__noise";
                  cell.append(signalLayer, noiseLayer);
                  row.appendChild(cell);
                  rowCells.push({ cell, signalLayer, noiseLayer });
                }
                els.grid.appendChild(row);
                cellRefs.push(rowCells);
              });
            }
            function updateRangeFill(input) {
              const value = (Number(input.value) - Number(input.min)) / (Number(input.max) - Number(input.min));
              input.style.setProperty("--fill", `${value * 100}%`);
            }
            function updateMetric(metric, value, valueElement, ringElement, cardElement) {
              valueElement.textContent = pct(value);
              ringElement.style.strokeDashoffset = String(100 - value * 100);
              cardElement.dataset.health = health(metric, value);
              cardElement.setAttribute("aria-label", `${metric}: ${pct(value)}, ${health(metric, value)}`);
            }
            function renderGrid(values) {
              const marks = Array.from({ length: 7 }, (_, index) => Math.round(index * values.depth / 6));
              layerLabels.forEach((label, index) => { label.textContent = `L${marks[index]}`; });
              tokens.forEach((token, rowIndex) => {
                marks.forEach((layer, columnIndex) => {
                  const state = tokenState(token.kind, layer / values.depth, values);
                  const ref = cellRefs[rowIndex][columnIndex];
                  const stateMark = token.kind === "anchor" ? "quiet" : mark(state);
                  ref.cell.dataset.mark = stateMark;
                  if (token.kind !== "anchor") {
                    const signalOpacity = stateMark === "signal" || stateMark === "mixed" ? 0.18 + 0.76 * state.signal : 0;
                    const noiseOpacity = stateMark === "spill" || stateMark === "mixed" ? 0.16 + 0.76 * state.noise : 0;
                    ref.signalLayer.style.opacity = String(signalOpacity);
                    ref.noiseLayer.style.opacity = String(noiseOpacity);
                  }
                  const label = `${token.label}, layer ${layer}: useful signal ${pct(state.signal)}, perturbation ${pct(state.noise)}`;
                  ref.cell.setAttribute("aria-label", label);
                  ref.cell.title = label;
                });
              });
            }
            function pointFor(ref) {
              const stageRect = els.gridStage.getBoundingClientRect();
              const rect = ref.cell.getBoundingClientRect();
              return {
                x: rect.left - stageRect.left + rect.width / 2,
                y: rect.top - stageRect.top + rect.height / 2,
              };
            }
            function curve(start, end, bend = 0) {
              const distance = Math.max(42, (end.x - start.x) * 0.42);
              return `M ${start.x} ${start.y} C ${start.x + distance} ${start.y + bend}, ${end.x - distance} ${end.y - bend}, ${end.x} ${end.y}`;
            }
            function updateFlowGeometry(values) {
              const width = els.gridStage.scrollWidth;
              const height = els.gridStage.scrollHeight;
              if (!width || !height || cellRefs.length !== tokens.length) return;
              els.flow.setAttribute("viewBox", `0 0 ${width} ${height}`);
              els.flow.setAttribute("width", String(width));
              els.flow.setAttribute("height", String(height));
              const factStart = pointFor(cellRefs[1][0]);
              const perturbStart = pointFor(cellRefs[2][0]);
              const distractorAEnd = pointFor(cellRefs[3][6]);
              const distractorBEnd = pointFor(cellRefs[4][6]);
              const queryEnd = pointFor(cellRefs[5][6]);
              els.signalPath.setAttribute("d", curve(factStart, queryEnd, -10));
              els.noisePaths[0].setAttribute("d", curve(perturbStart, distractorAEnd, 6));
              els.noisePaths[1].setAttribute("d", curve(perturbStart, distractorBEnd, 12));
              els.noisePaths[2].setAttribute("d", curve(perturbStart, queryEnd, 18));
              els.signalPath.style.opacity = String(0.14 + 0.62 * values.fact);
              els.signalPath.style.strokeWidth = String(1.6 + 1.6 * values.fact);
              els.noisePaths.forEach((path, index) => {
                const scale = index === 2 ? 1 : 0.78;
                path.style.opacity = String((0.10 + 0.58 * values.noise) * scale);
                path.style.strokeWidth = String(1.4 + 1.5 * values.noise * scale);
              });
            }
            function syncFrameHeight() {
              if (resizeFrame !== null) cancelAnimationFrame(resizeFrame);
              resizeFrame = requestAnimationFrame(() => {
                resizeFrame = null;
                const frame = window.frameElement;
                if (!frame) return;
                const height = Math.ceil(document.documentElement.scrollHeight);
                const current = Number.parseFloat(frame.style.height || "0");
                if (Math.abs(current - height) > 2) frame.style.height = `${height}px`;
              });
            }
            function celebrate() {
              root.classList.remove("cb-win-pulse");
              void root.offsetWidth;
              root.classList.add("cb-win-pulse");
            }
            function render() {
              const values = model();
              els.sinkValue.textContent = pct(values.sink);
              els.depthValue.textContent = `${values.depth} layers`;
              updateRangeFill(els.sink);
              updateRangeFill(els.depth);
              updateMetric("identity", values.identity, els.identity, els.identityRing, els.identityCard);
              updateMetric("fact", values.fact, els.fact, els.factRing, els.factCard);
              updateMetric("noise", values.noise, els.noise, els.noiseRing, els.noiseCard);
              if (values.safe) {
                els.challenge.dataset.state = "safe";
                els.challengeIcon.textContent = "✓";
                els.challengeKicker.textContent = "Balanced circuit";
                els.challengeMessage.textContent = "You found a regime where identity survives, the fact arrives, and perturbation spill stays contained.";
                els.status.dataset.state = "safe";
                els.status.innerHTML = "<strong>Balanced circuit.</strong> Some heads can park attention at the anchor, reducing spill while leaving enough content routing for the fact to reach the query.";
              } else if (values.sealed) {
                els.challenge.dataset.state = "active";
                els.challengeIcon.textContent = "◎";
                els.challengeKicker.textContent = "Challenge";
                els.challengeMessage.textContent = "The fact is not reaching the query. Restore some content routing or add enough depth for it to travel.";
                els.status.dataset.state = "sealed";
                els.status.innerHTML = "<strong>Too little content routing.</strong> The perturbation is contained, but so is the useful fact: the final query receives too little information.";
              } else {
                els.challenge.dataset.state = "active";
                els.challengeIcon.textContent = "◎";
                els.challengeKicker.textContent = "Challenge";
                els.challengeMessage.textContent = "Identity or noise is outside the safe range. Route more heads to the anchor or reduce depth.";
                els.status.dataset.state = "mixing";
                els.status.innerHTML = "<strong>Over-mixing.</strong> Too much content routing lets the red perturbation spread through the sequence and erodes token identity.";
              }
              renderGrid(values);
              updateFlowGeometry(values);
              if (initialized && values.safe && !wasSafe) celebrate();
              wasSafe = values.safe;
              initialized = true;
              syncFrameHeight();
            }
            function scheduleRender() {
              if (renderFrame !== null) return;
              renderFrame = requestAnimationFrame(() => {
                renderFrame = null;
                render();
              });
            }
            buildGrid();
            els.sink.addEventListener("input", scheduleRender);
            els.depth.addEventListener("input", scheduleRender);
            root.addEventListener("animationend", () => root.classList.remove("cb-win-pulse"));
            const observer = new ResizeObserver(() => {
              updateFlowGeometry(model());
              syncFrameHeight();
            });
            observer.observe(root);
            window.addEventListener("resize", () => {
              updateFlowGeometry(model());
              syncFrameHeight();
            });
            render();
          })();
        </script>
      </div>
    </body>
    </html>
    """

    mo.vstack(
        [
            mo.md(
                """
                ## 1. The Circuit Breaker Challenge

                A useful early fact must reach the final query, while a local
                perturbation should not flood every token. Choose how many heads
                take the low-information anchor route and find the regime that
                preserves both signal and separation.

                This is a deterministic mechanism game, not a live-model result.
                It makes the paper's trade-off concrete before we inspect actual
                attention heads below.
                """
            ),
            mo.Html(
                f"""
                <iframe
                  title="Circuit Breaker Challenge"
                  srcdoc="{html_lib.escape(circuit_breaker_html, quote=True)}"
                  style="border:0;display:block;height:660px;width:100%;"
                ></iframe>
                """
            ),
        ],
        gap=0.7,
    )
    return


@app.cell(hide_code=True)
def _(mixing_chamber_controls, mixing_chamber_output, mo):
    mo.vstack(
        [
            mo.md(
                """
                The challenge gives the intuition. Open the verification below
                to measure the same over-mixing story with actual token vectors,
                effective rank, and pairwise similarity.
                """
            ),
            mo.accordion(
                {
                    "Verify the intuition with a NumPy simulation": mo.vstack(
                        [mixing_chamber_controls, mixing_chamber_output],
                        gap=1,
                    )
                }
            ),
        ],
        gap=0.65,
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### What the game is standing in for

    Let $V^{(L)} \in \mathbb{R}^{T \times d}$ collect all token
    representations after $L$ layers. A standard measure of **rank collapse**
    asks whether every row of $V^{(L)}$ is becoming close to the sequence
    average:

    $$
    \left\|V^{(L)} - \frac{1}{T}\mathbf{1}\mathbf{1}^{\top}V^{(L)}\right\|_F
    < \Delta.
    $$

    The paper proves that this strong condition implies a related
    representational-collapse condition,
    $\left\|v_T^{(L)}-v_{T-1}^{(L)}\right\|_2 < \Delta$, although the
    converse need not hold. Depth and long context create different routes to
    the same practical danger: token states become harder to distinguish.

    To study how a local edit spreads, define the sensitivity

    $$
    J_{i\rightarrow j}^{(L)} =
    \frac{\partial v_j^{(L)}}{\partial v_i^{(0)}}.
    $$

    In readable form, the paper's multi-head bound says this sensitivity is at
    most a sum over all causal paths from $i$ to $j$, with each path weighted
    by a product of attention coefficients across layers:

    $$
    \left\|J_{i\rightarrow j}^{(L)}\right\|
    \le C_{\max}^{L}
    \sum_{\pi:i\rightsquigarrow j}
    \prod_{\ell=1}^{L}\bar{\alpha}_{\pi_\ell}^{(\ell)}.
    $$

    A sink removes weight from many content-to-content paths. Appendix B adds
    the crucial mechanical detail: the beginning token has an unusually
    low-norm value vector. If a head concentrates on it,

    $$
    z_i^{(\ell,h)} \approx W_V^{(\ell,h)}v_{\mathrm{bos}}^{(\ell)} \approx 0,
    \qquad
    v_i^{(\ell+1)} \approx v_i^{(\ell)}
    $$

    through the residual pathway. That is the paper's approximate no-op. The
    game models this mechanism; it does not claim that its scores are measured
    from LLaMA or Gemma.

    _Paper trail: Section 3, Theorem 3.2, and Appendix B._
    """)
    return


@app.cell(hide_code=True)
def _(
    ANCHOR_MODES,
    MODEL_OPTIONS,
    PRECISION_OPTIONS,
    PROMPT_PRESETS,
    TOKEN_BUDGET_OPTIONS,
    mo,
):
    model_choice = mo.ui.dropdown(
        options=list(MODEL_OPTIONS.keys()),
        value="LLaMA 3.1 8B (Hugging Face token required)",
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
        label="Attention-sink threshold",
        full_width=True,
    )

    mo.vstack(
        [
            mo.md("## 2. Configure the live probe"),
            mo.md(
                """
                Start with one model so the circuit is easy to inspect. The
                broader RTX family and long-context sweeps come later, after the
                sink behavior is visible in a single prompt.
                """
            ),
            model_choice,
            mo.hstack(
                [precision_choice, anchor_mode], widths="equal", wrap=True, gap=1
            ),
            mo.hstack(
                [prompt_preset, max_tokens, sink_threshold],
                widths="equal",
                wrap=True,
                gap=1,
            ),
            custom_prompt,
        ],
        gap=1,
    )
    return (
        anchor_mode,
        custom_prompt,
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
    max_tokens,
    model_choice,
    precision_choice,
    selected_preset_name,
    selected_prompt,
    sink_threshold,
):
    current_probe_config = SimpleNamespace(
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
            ),
            select_probe_config,
        ],
        gap=0.6,
    )
    return (select_probe_config,)


@app.cell(hide_code=True)
def _(hf_token, mo, probe_config):
    run_probe_button = mo.ui.run_button(
        label="Load model and run attention probe",
        kind="success",
        full_width=True,
    )
    if probe_config is None:
        probe_action_view = mo.md(
            "_Select and commit a probe configuration. No model loads until the run button is clicked._"
        )
    else:
        _requires_hf_token = probe_config.model_id.startswith(("google/", "meta-llama/"))
        _auth_note = (
            "Hugging Face authentication: required and available."
            if _requires_hf_token and hf_token
            else "Hugging Face authentication: required before this live run."
            if _requires_hf_token
            else "Hugging Face authentication: not required for this open control."
        )
        _probe_ready = not _requires_hf_token or bool(hf_token)
        probe_action_view = mo.vstack(
            [
                mo.md(
                    f"""
                    **Experiment status — {'ready to run' if _probe_ready else 'action required'}**

                    - model: `{probe_config.model_id}`
                    - dtype policy: `{probe_config.precision_label}`
                    - prompt preset: `{probe_config.prompt_preset}`
                    - max inspected tokens: `{probe_config.max_tokens}`
                    - anchor mode: `{probe_config.anchor_mode}`
                    - {_auth_note}
                    """
                ).callout(kind="success" if _probe_ready else "warn"),
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
def _(AutoModelForCausalLM, AutoProcessor, AutoTokenizer, dependency_error, gc, torch):
    from functools import lru_cache

    def _cuda_dtype(precision_key, device):
        if device.type != "cuda":
            return None
        if precision_key == "bf16":
            return torch.bfloat16
        if precision_key == "fp32":
            return torch.float32
        return torch.float16

    def release_model_memory():
        gc.collect()
        if torch.cuda.is_available():
            torch.cuda.empty_cache()
            try:
                torch.cuda.ipc_collect()
            except (AttributeError, RuntimeError):
                pass

    def _load_model_bundle_uncached(model_id, precision_key="fp16", hf_token=None):
        if dependency_error is not None:
            return None, None, None, None, dependency_error

        if model_id.startswith(("google/", "meta-llama/")) and not hf_token:
            return (
                None,
                None,
                None,
                None,
                RuntimeError(
                    "This Gemma/LLaMA probe requires a Hugging Face read token. "
                    "Submit one above, or use an open Qwen control."
                ),
            )

        device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        try:
            release_model_memory()

            _auth_kwargs = {"token": hf_token} if hf_token else {}

            try:
                tokenizer = AutoTokenizer.from_pretrained(model_id, **_auth_kwargs)
            except Exception as tokenizer_exc:
                try:
                    processor = AutoProcessor.from_pretrained(model_id, **_auth_kwargs)
                    tokenizer = getattr(processor, "tokenizer", processor)
                    if not hasattr(tokenizer, "convert_ids_to_tokens"):
                        raise tokenizer_exc
                except Exception:
                    raise tokenizer_exc
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
            release_model_memory()
            _dtype_name = str(next(model.parameters()).dtype)
            return tokenizer, model, device, _dtype_name, None
        except Exception as exc:  # noqa: BLE001 - show model load failures in UI.
            return None, None, None, None, exc

    @lru_cache(maxsize=1)
    def load_model_bundle(model_id, precision_key="fp16", hf_token=None):
        return _load_model_bundle_uncached(model_id, precision_key, hf_token)

    def load_ephemeral_model_bundle(model_id, precision_key="fp16", hf_token=None):
        return _load_model_bundle_uncached(model_id, precision_key, hf_token)

    def clear_cached_model_bundle():
        load_model_bundle.cache_clear()
        release_model_memory()

    return clear_cached_model_bundle, load_ephemeral_model_bundle, load_model_bundle, release_model_memory


@app.cell(hide_code=True)
def _(
    MODEL_OPTIONS,
    PRECISION_OPTIONS,
    hf_token,
    load_model_bundle,
    mo,
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
        with mo.status.spinner(
            title="Loading model",
            subtitle=f"Preparing {selected_model_id} on the selected device.",
        ):
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
def _(device, hf_token, mo, model, model_dtype, model_error, probe_config, probe_run_requested, selected_model_id, torch):
    if model_error is not None:
        model_status_output = mo.md(
            f"""
            Model could not be loaded.

            ```text
            {model_error}
            ```
            """
        ).callout(kind="danger")
    else:
        model_status_output = None
    model_status_output
    return


@app.cell(hide_code=True)
def _(mo, probe, sink_scores, torch):
    layer_index_control = None
    head_index_control = None
    strongest_layer = None
    strongest_head = None
    strongest_score = None

    if probe is None or sink_scores is None:
        head_picker_view = mo.md(
            """
            ## 3. Attention anatomy

            The layer/head controls appear after the attention probe finishes.
            The notebook will preselect the strongest first-token sink head so
            the first heatmap is immediately meaningful.
            """
        )
    else:
        _layer_count, _head_count = sink_scores.shape
        _finite_sink_mask = torch.isfinite(sink_scores)
        if bool(_finite_sink_mask.any()):
            _safe_sink_scores = sink_scores.clone()
            _safe_sink_scores[~_finite_sink_mask] = -float("inf")
            strongest_flat_index = int(_safe_sink_scores.flatten().argmax().item())
        else:
            strongest_flat_index = 0
        strongest_layer = int(strongest_flat_index // _head_count)
        strongest_head = int(strongest_flat_index % _head_count)
        strongest_score = float(sink_scores[strongest_layer, strongest_head])

        layer_index_control = mo.ui.slider(
            start=0,
            stop=max(0, _layer_count - 1),
            step=1,
            value=strongest_layer,
            show_value=True,
            label="Layer",
            full_width=True,
        )
        head_index_control = mo.ui.slider(
            start=0,
            stop=max(0, _head_count - 1),
            step=1,
            value=strongest_head,
            show_value=True,
            label="Head",
            full_width=True,
        )

        head_picker_view = mo.vstack(
            [
                mo.md("## 3. Attention anatomy"),
                mo.md(
                    f"""
                    ### Select a head

                    Preselected **L{strongest_layer} H{strongest_head}** because
                    it has the highest finite first-token sink score in this run
                    ({strongest_score:.3f}). Use the controls to audit any other
                    layer/head pair.
                    """
                ).callout(kind="info"),
                mo.hstack(
                    [layer_index_control, head_index_control],
                    widths="equal",
                    wrap=True,
                    gap=1,
                ),
            ],
            gap=1,
        )

    head_picker_view
    return (
        head_index_control,
        layer_index_control,
        strongest_head,
        strongest_layer,
        strongest_score,
    )


@app.cell(hide_code=True)
def _(head_index_control, layer_index_control, sink_scores, torch):
    if sink_scores is None or layer_index_control is None or head_index_control is None:
        selected_layer_index = 0
        selected_head_index = 0
        selected_head_score = None
    else:
        _layer_count, _head_count = sink_scores.shape
        selected_layer_index = min(int(layer_index_control.value), _layer_count - 1)
        selected_head_index = min(int(head_index_control.value), _head_count - 1)
        _score = sink_scores[selected_layer_index, selected_head_index]
        selected_head_score = float(_score) if bool(torch.isfinite(_score)) else None

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
            ### Prompt under inspection

            Waiting for a selected probe configuration.
            """
        )
    else:
        prompt_view = mo.md(f"""
        ### Prompt under inspection

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
        collect_hidden=True,
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
                output_hidden_states=bool(collect_hidden),
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
        if collect_hidden and outputs.hidden_states is not None:
            hidden = torch.stack(
                [
                    layer_hidden[0].detach().float().cpu()
                    for layer_hidden in outputs.hidden_states
                ]
            )
        else:
            hidden = None

        logits = outputs.logits[0, -1].detach().float().cpu()
        diagnostics = {
            "attention_nonfinite": int((~torch.isfinite(attention)).sum().item()),
            "hidden_nonfinite": int((~torch.isfinite(hidden)).sum().item()) if hidden is not None else 0,
            "logits_nonfinite": int((~torch.isfinite(logits)).sum().item()),
            "attention_values": int(attention.numel()),
            "hidden_values": int(hidden.numel()) if hidden is not None else 0,
            "logits_values": int(logits.numel()),
        }

        finite_logits = torch.isfinite(logits)
        if finite_logits.any():
            safe_logits = logits.clone()
            replacement = logits[finite_logits].min() - 50.0
            safe_logits = torch.where(finite_logits, safe_logits, replacement)
            probs = torch.softmax(safe_logits, dim=-1)
            probs = torch.nan_to_num(probs, nan=0.0, posinf=0.0, neginf=0.0)
            top_probs, top_ids = torch.topk(probs, k=min(int(top_k), probs.numel()))
            next_tokens = [
                {
                    "token": decode_token(tokenizer, token_id),
                    "probability": float(probability),
                }
                for token_id, probability in zip(top_ids, top_probs)
            ]
        else:
            next_tokens = []

        return {
            "text": text,
            "tokens": tokens,
            "attention": attention,
            "hidden": hidden,
            "next_tokens": next_tokens,
            "diagnostics": diagnostics,
        }

    return (run_attention_probe,)


@app.cell(hide_code=True)
def _():
    def _finite_mean(tensor, torch, fallback=0.0):
        finite_values = tensor[torch.isfinite(tensor)]
        if finite_values.numel() == 0:
            return float(fallback)
        return float(finite_values.mean().item())

    def summarize_attention_sink(probe, torch, sink_threshold):
        _raw_attention = probe["attention"]
        _attention = torch.nan_to_num(
            _raw_attention,
            nan=0.0,
            posinf=0.0,
            neginf=0.0,
        )
        _nonfinite_attention = int((~torch.isfinite(_raw_attention)).sum().item())
        _token_count = _attention.shape[-1]
        _opportunities = torch.arange(
            _token_count,
            0,
            -1,
            dtype=_attention.dtype,
            device=_attention.device,
        )
        _position_scores = (_attention / _opportunities.view(1, 1, 1, _token_count)).sum(
            dim=-2
        )
        _sink_scores = _position_scores[:, :, 0]
        _position_sink_rates = (
            (_position_scores > float(sink_threshold)).float().mean(dim=(0, 1)) * 100.0
        )
        _strong_sink_rate = float(
            (_sink_scores > float(sink_threshold)).float().mean().item() * 100.0
        )
        _mean_sink_strength = _finite_mean(_sink_scores, torch)
        _last_token_sink = _finite_mean(_attention[:, :, -1, 0], torch)
        _position_rank = int(
            (torch.argsort(_position_sink_rates, descending=True) == 0)
            .nonzero(as_tuple=False)[0]
            .item()
            + 1
        )
        if _token_count > 1:
            _other_rates = _position_sink_rates[1:]
            _next_position = int(torch.argmax(_other_rates).item() + 1)
            _next_rate = float(_position_sink_rates[_next_position].item())
        else:
            _next_position = 0
            _next_rate = float(_position_sink_rates[0].item())
        return {
            "token_count": len(probe["tokens"]),
            "sink_scores": _sink_scores,
            "position_scores": _position_scores,
            "position_sink_rates": _position_sink_rates,
            "nonfinite_attention_count": _nonfinite_attention,
            "sink_rate_percent": _strong_sink_rate,
            "mean_sink_strength": _mean_sink_strength,
            "last_token_attention_to_token_0": _last_token_sink,
            "token0_position_rank": _position_rank,
            "next_strongest_position": _next_position,
            "next_strongest_position_rate_percent": _next_rate,
        }

    def hidden_drift_summary(base_probe, perturbed_probe, torch):
        _layer_count = min(base_probe["hidden"].shape[0], perturbed_probe["hidden"].shape[0])
        _token_count = min(base_probe["hidden"].shape[1], perturbed_probe["hidden"].shape[1])
        _delta = torch.linalg.vector_norm(
            base_probe["hidden"][:_layer_count, :_token_count, :]
            - perturbed_probe["hidden"][:_layer_count, :_token_count, :],
            dim=-1,
        )
        _nonfinite_drift = int((~torch.isfinite(_delta)).sum().item())
        _delta = torch.nan_to_num(_delta, nan=0.0, posinf=0.0, neginf=0.0)
        return {
            "delta": _delta,
            "early_layer_mean_drift": _finite_mean(_delta[1], torch) if _delta.shape[0] > 1 else 0.0,
            "final_layer_mean_drift": _finite_mean(_delta[-1], torch),
            "nonfinite_drift_count": _nonfinite_drift,
        }

    def streaming_cache_diagnostic(probe, cache_window, torch):
        _raw_attention = probe["attention"]
        _attention = torch.nan_to_num(
            _raw_attention,
            nan=0.0,
            posinf=0.0,
            neginf=0.0,
        )
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
            "nonfinite_attention_count": int((~torch.isfinite(_raw_attention)).sum().item()),
        }

    return hidden_drift_summary, streaming_cache_diagnostic, summarize_attention_sink


@app.cell(hide_code=True)
def _(
    analysis_prompt,
    device,
    model,
    model_error,
    mo,
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
            with mo.status.spinner(
                title="Running attention probe",
                subtitle=f"Collecting attentions and hidden states for up to {probe_config.max_tokens} tokens.",
            ):
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
        _probe_status_output = mo.md(
            f"""
            Probe failed.

            ```text
            {probe_error}
            ```
            """
        ).callout(kind="danger")
    elif probe is not None:
        _probe_status_output = mo.md(
            f"""
            Probe complete: `{len(probe["tokens"])}` tokens inspected.
            """
        ).callout(kind="success")
    else:
        _probe_status_output = None
    _probe_status_output
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
                        "token0_sink_score": float(sink_scores[_layer, _head]),
                        "strong_sink": bool(_strong_sink_mask[_layer, _head]),
                    }
                )
        sink_table = pd.DataFrame(_rows).sort_values(
            "token0_sink_score",
            ascending=False,
        )
    return sink_rate, sink_scores, sink_summary, sink_table


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### How this notebook measures a sink

    For key position $p$, layer $\ell$, and head $h$, we average the
    attention received over exactly the causal queries that had an opportunity
    to attend to that position:

    $$
    s_{\ell,h}(p) =
    \frac{1}{T-p}
    \sum_{i=p}^{T-1}\alpha_{i,p}^{(\ell,h)}.
    $$

    A head is counted as a token-0 sink when $s_{\ell,h}(0) > \varepsilon$.
    The whole-model rate is

    $$
    R_{\varepsilon} =
    \frac{1}{LH}
    \sum_{\ell=1}^{L}\sum_{h=1}^{H}
    \mathbf{1}\!\left[s_{\ell,h}(0)>\varepsilon\right].
    $$

    This is the notebook's opportunity-normalized operationalization of the
    sink metric used in the paper and the Attention-Sink work. The threshold
    controls classification, not the underlying attention values; use the
    continuous score and the atlas alongside the headline rate.
    """)
    return


@app.cell(hide_code=True)
def _(
    mo,
    plot_position_sink_profile,
    probe,
    selected_head_index,
    selected_layer_index,
    sink_rate,
    sink_scores,
    sink_summary,
    sink_threshold,
    torch,
):
    if probe is None or sink_scores is None or sink_summary is None:
        _sink_metric_output = mo.md("Sink metrics are waiting for a successful model probe.")
    else:
        _layer = min(int(selected_layer_index), sink_scores.shape[0] - 1)
        _head = min(int(selected_head_index), sink_scores.shape[1] - 1)
        _selected_sink = float(sink_scores[_layer, _head])
        _raw_last_token_sink = probe["attention"][_layer, _head, -1, 0]
        _last_token_sink = (
            f"{float(_raw_last_token_sink):.3f}"
            if bool(torch.isfinite(_raw_last_token_sink))
            else "non-finite"
        )
        _next_position = int(sink_summary["next_strongest_position"])
        _next_token = probe["tokens"][_next_position][:22]
        _position_profile_fig = plot_position_sink_profile(sink_summary, probe["tokens"])
        _diagnostics = probe.get("diagnostics", {})
        _attention_nonfinite = int(_diagnostics.get("attention_nonfinite", 0))
        _hidden_nonfinite = int(_diagnostics.get("hidden_nonfinite", 0))
        _logits_nonfinite = int(_diagnostics.get("logits_nonfinite", 0))
        _total_nonfinite = _attention_nonfinite + _hidden_nonfinite + _logits_nonfinite

        _metric_items = [
            mo.md(
                f"""
                    ### Whole-model sink summary

                    The equations above define the score used here. The table
                    reports both the aggregate classification rate and the
                    continuous evidence needed to audit that classification.

                    | Metric | Value |
                    | --- | ---: |
                    | Attention-sink threshold | {float(sink_threshold.value):.2f} |
                    | Token-0 sink rate across layer/head pairs | {sink_rate:.1f}% |
                    | Token-0 rank among positions | {sink_summary["token0_position_rank"]} |
                    | Next strongest position | {_next_position}: `{_next_token}` |
                    | Next strongest position sink rate | {sink_summary["next_strongest_position_rate_percent"]:.1f}% |
                    | Selected layer/head | L{_layer} H{_head} |
                    | Selected head token-0 sink score | {_selected_sink:.3f} |
                    | Last-token raw attention to token 0 in selected head | {_last_token_sink} |
                    """
            )
        ]
        if _total_nonfinite > 0:
            _metric_items.append(
                mo.md(
                    f"""
                    Numerical note: this forward pass emitted non-finite values
                    (`attention={_attention_nonfinite}`, `hidden={_hidden_nonfinite}`,
                    `logits={_logits_nonfinite}`). Aggregate sink metrics and plots
                    replace non-finite attention entries with zero so one unstable
                    head cannot corrupt the full notebook.
                    """
                ).callout(kind="warn")
            )
        _metric_items.append(_position_profile_fig)

        _sink_metric_output = mo.vstack(
            _metric_items,
            gap=0.75,
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

    def apply_plot_theme(fig):
        fig.update_layout(
            template="plotly_white",
            font={
                "family": 'Inter, ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif',
                "size": 13,
                "color": "#253247",
            },
            title={
                "x": 0.02,
                "xanchor": "left",
                "font": {"size": 18, "color": "#172033"},
            },
            hoverlabel={
                "bgcolor": "#ffffff",
                "bordercolor": "#cbd5e1",
                "font": {"color": "#172033", "size": 12},
            },
            colorway=[BLUE, GREEN, YELLOW, SKY, "#8b5cf6", "#e45555"],
        )
        fig.update_xaxes(
            gridcolor="#e7edf4",
            linecolor="#cbd5e1",
            zerolinecolor="#cbd5e1",
            tickfont={"color": "#526174"},
            title_font={"color": "#334155"},
        )
        fig.update_yaxes(
            gridcolor="#e7edf4",
            linecolor="#cbd5e1",
            zerolinecolor="#cbd5e1",
            tickfont={"color": "#526174"},
            title_font={"color": "#334155"},
        )
        return fig

    def _sampled_token_ticks(tokens, max_ticks=28):
        if not tokens:
            return [], []
        step = max(1, int(np.ceil(len(tokens) / max_ticks)))
        positions = list(range(0, len(tokens), step))
        labels = [f"{position}: {tokens[position][:14]}" for position in positions]
        return positions, labels

    def _sampled_indices(count, max_points, always_include=()):
        if count <= max_points:
            return list(range(count))
        _sampled = np.linspace(0, count - 1, max_points, dtype=int).tolist()
        return sorted(set(_sampled).union(int(value) for value in always_include))

    def plot_attention_matrix(
        matrix,
        tokens,
        layer,
        head,
        view_mode="Overview",
        window_center=None,
        window_size=64,
    ):
        _full_data = np.nan_to_num(
            np.asarray(matrix, dtype=float),
            nan=0.0,
            posinf=0.0,
            neginf=0.0,
        )
        token_count = len(tokens)
        if view_mode == "Token window" and token_count > 0:
            _center = token_count - 1 if window_center is None else int(window_center)
            _center = max(0, min(token_count - 1, _center))
            _size = max(8, min(int(window_size), token_count))
            _start = max(0, min(token_count - _size, _center - _size // 2))
            _query_indices = list(range(_start, _start + _size))
            _key_indices = sorted(set([0] + _query_indices))
            _view_label = f"token window {_query_indices[0]}–{_query_indices[-1]}"
        elif token_count > 128:
            _query_indices = _sampled_indices(token_count, 96, always_include=(token_count - 1,))
            _key_indices = _sampled_indices(token_count, 96, always_include=(0, token_count - 1))
            _view_label = f"overview · {len(_query_indices)}×{len(_key_indices)} sampled positions"
        else:
            _query_indices = list(range(token_count))
            _key_indices = list(range(token_count))
            _view_label = "full matrix"

        data = _full_data[np.ix_(_query_indices, _key_indices)]
        _x_tick_step = max(1, int(np.ceil(len(_key_indices) / 18)))
        _y_tick_step = max(1, int(np.ceil(len(_query_indices) / 18)))
        _x_ticks = _key_indices[::_x_tick_step]
        _y_ticks = _query_indices[::_y_tick_step]
        hover = [
            [
                (
                    f"query {row}: {tokens[row]}<br>"
                    f"key {col}: {tokens[col]}"
                )
                for col in _key_indices
            ]
            for row in _query_indices
        ]
        fig = go.Figure(
            data=go.Heatmap(
                z=data,
                x=_key_indices,
                y=_query_indices,
                customdata=hover,
                colorscale=SINK_COLORSCALE,
                zmin=0.0,
                zmax=max(0.05, float(np.nanmax(_full_data))),
                colorbar={"title": "attention", "thickness": 12},
                hovertemplate="%{customdata}<br>attention=%{z:.4f}<extra></extra>",
            )
        )
        fig.update_layout(
            title=f"Attention weights: layer {layer}, head {head} · {_view_label}",
            height=max(420, min(720, 8 * len(_query_indices))),
            margin={"l": 56, "r": 16, "t": 54, "b": 72},
            xaxis={
                "title": "Key token attended to",
                "tickmode": "array",
                "tickvals": _x_ticks,
                "ticktext": [f"{position}: {tokens[position][:14]}" for position in _x_ticks],
                "tickangle": -45,
            },
            yaxis={
                "title": "Query token receiving context",
                "tickmode": "array",
                "tickvals": _y_ticks,
                "ticktext": [f"{position}: {tokens[position][:14]}" for position in _y_ticks],
                "autorange": "reversed",
            },
        )
        return apply_plot_theme(fig)

    def build_sink_switch_counterfactual(matrix, tokens):
        _original = np.nan_to_num(
            np.asarray(matrix, dtype=float),
            nan=0.0,
            posinf=0.0,
            neginf=0.0,
        )
        _counterfactual = _original.copy()
        if _counterfactual.shape[1] == 0:
            _counterfactual = _original
            _token0_mass = np.zeros(_original.shape[0])
        else:
            _token0_mass = _counterfactual[:, 0].copy()
            _counterfactual[:, 0] = 0.0
            _row_sums = _counterfactual.sum(axis=1, keepdims=True)
            _counterfactual = np.divide(
                _counterfactual,
                _row_sums,
                out=np.zeros_like(_counterfactual),
                where=_row_sums > 1e-12,
            )

        def _routing_entropy(_matrix):
            _scores = []
            for _row_index, _row in enumerate(_matrix):
                _visible = np.clip(_row[: _row_index + 1], 0.0, None)
                _total = float(_visible.sum())
                if _total <= 1e-12 or len(_visible) <= 1:
                    continue
                _probabilities = _visible / _total
                _entropy = -float(
                    (_probabilities * np.log(_probabilities + 1e-12)).sum()
                )
                _scores.append(_entropy / max(float(np.log(len(_visible))), 1e-12))
            return float(np.mean(_scores)) if _scores else 0.0

        _gain = _counterfactual - _original
        _mean_gain = _gain.mean(axis=0) if _gain.size else np.asarray([])
        if len(_mean_gain) > 1:
            _recipient = int(np.argmax(_mean_gain[1:]) + 1)
        else:
            _recipient = 0
        _recipient_token = tokens[_recipient] if tokens and _recipient < len(tokens) else ""
        return {
            "original": _original,
            "counterfactual": _counterfactual,
            "mean_gain": _mean_gain,
            "mean_token0_mass": float(_token0_mass[1:].mean()) if len(_token0_mass) > 1 else float(_token0_mass.mean()) if len(_token0_mass) else 0.0,
            "original_mixing_score": _routing_entropy(_original),
            "counterfactual_mixing_score": _routing_entropy(_counterfactual),
            "top_recipient_position": _recipient,
            "top_recipient_token": _recipient_token,
        }

    def plot_sink_switch_lens(switch_result, tokens, layer, head):
        from plotly.subplots import make_subplots

        _original = switch_result["original"]
        _counterfactual = switch_result["counterfactual"]
        _token_count = len(tokens)
        _tick_positions, _tick_labels = _sampled_token_ticks(tokens)
        _zmax = max(
            0.05,
            float(np.nanmax(_original)) if _original.size else 0.0,
            float(np.nanmax(_counterfactual)) if _counterfactual.size else 0.0,
        )
        _fig = make_subplots(
            rows=1,
            cols=2,
            subplot_titles=[
                "Actual selected head",
                "Counterfactual: token 0 unavailable",
            ],
            horizontal_spacing=0.10,
        )
        _fig.add_trace(
            go.Heatmap(
                z=_original,
                x=list(range(_token_count)),
                y=list(range(_token_count)),
                colorscale=SINK_COLORSCALE,
                zmin=0.0,
                zmax=_zmax,
                colorbar={"title": "attention", "thickness": 12},
                hovertemplate="query=%{y}<br>key=%{x}<br>attention=%{z:.4f}<extra></extra>",
            ),
            row=1,
            col=1,
        )
        _fig.add_trace(
            go.Heatmap(
                z=_counterfactual,
                x=list(range(_token_count)),
                y=list(range(_token_count)),
                colorscale=SINK_COLORSCALE,
                zmin=0.0,
                zmax=_zmax,
                showscale=False,
                hovertemplate="query=%{y}<br>key=%{x}<br>counterfactual=%{z:.4f}<extra></extra>",
            ),
            row=1,
            col=2,
        )
        _fig.update_layout(
            title=f"Sink Switch lens: layer {layer}, head {head}",
            height=max(430, min(680, 18 * _token_count)),
            margin={"l": 54, "r": 18, "t": 74, "b": 86},
        )
        _fig.update_xaxes(
            title="Key token",
            tickmode="array",
            tickvals=_tick_positions,
            ticktext=_tick_labels,
            tickangle=-45,
        )
        _fig.update_yaxes(
            title="Query token",
            tickmode="array",
            tickvals=_tick_positions,
            ticktext=_tick_labels,
            autorange="reversed",
        )
        return apply_plot_theme(_fig)

    def plot_sink_switch_gain(switch_result, tokens, top_k=10):
        _gain = np.nan_to_num(
            np.asarray(switch_result["mean_gain"], dtype=float),
            nan=0.0,
            posinf=0.0,
            neginf=0.0,
        )
        if len(_gain) <= 1:
            _positions = np.asarray([0])
        else:
            _candidate_positions = np.arange(1, len(_gain))
            _top_count = min(int(top_k), len(_candidate_positions))
            _positions = _candidate_positions[
                np.argsort(_gain[1:])[-_top_count:]
            ]
            _positions = _positions[np.argsort(_gain[_positions])]
        _labels = [f"{int(_position)}: {tokens[int(_position)][:22]}" for _position in _positions]
        _values = _gain[_positions] if len(_gain) else np.asarray([0.0])
        _fig = go.Figure(
            data=go.Bar(
                x=_values,
                y=_labels,
                orientation="h",
                marker={"color": GREEN},
                hovertemplate="key=%{y}<br>mean gained attention=%{x:.4f}<extra></extra>",
            )
        )
        _fig.update_layout(
            title="Where token-0 attention is forced to go",
            height=max(300, 30 * len(_labels)),
            margin={"l": 136, "r": 16, "t": 52, "b": 46},
            xaxis={"title": "Mean gained attention"},
            yaxis={"title": ""},
            showlegend=False,
        )
        return apply_plot_theme(_fig)

    def plot_attention_flow(probe, layer, head, query_index, top_k=12):
        attention_row = np.nan_to_num(
            probe["attention"][layer, head, query_index].numpy(),
            nan=0.0,
            posinf=0.0,
            neginf=0.0,
        )
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
            xaxis={"title": "Attention weight", "range": [0, max(0.05, float(values.max()) * 1.12)]},
            yaxis={"title": ""},
            showlegend=False,
        )
        return apply_plot_theme(fig)

    def plot_sink_map(sink_scores, threshold):
        data = np.nan_to_num(
            sink_scores.numpy(),
            nan=0.0,
            posinf=0.0,
            neginf=0.0,
        )
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
                colorbar={"title": "token-0 sink score", "thickness": 12},
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
            title="Opportunity-normalized token-0 sink score by layer and head",
            height=max(360, min(760, 26 * layer_count)),
            margin={"l": 56, "r": 16, "t": 52, "b": 50},
            xaxis={"title": "Head", "dtick": 1},
            yaxis={"title": "Layer", "dtick": 1, "autorange": "reversed"},
        )
        return apply_plot_theme(fig)

    def plot_position_sink_profile(sink_summary, tokens):
        rates = np.nan_to_num(
            sink_summary["position_sink_rates"].numpy(),
            nan=0.0,
            posinf=0.0,
            neginf=0.0,
        )
        token_count = len(tokens)
        positions = np.arange(token_count)
        labels = [f"{position}: {tokens[position][:18]}" for position in positions]
        _runner = int(sink_summary.get("next_strongest_position", 0))
        _runner = max(0, min(token_count - 1, _runner))
        _lead = float(rates[0] - rates[_runner]) if token_count > 1 else 0.0
        colors = [
            YELLOW if position == 0 else BLUE if position == _runner else "#cbd5e1"
            for position in positions
        ]
        _text = ["" for _ in positions]
        if token_count > 0:
            _text[0] = f"token 0<br>{rates[0]:.1f}%"
        if token_count > 1 and _runner != 0:
            _text[_runner] = f"runner-up<br>{rates[_runner]:.1f}%"
        hover = [
            f"position {position}<br>token: {tokens[position]}<br>sink rate: {rates[position]:.2f}%"
            for position in positions
        ]
        fig = go.Figure(
            data=go.Bar(
                x=positions,
                y=rates,
                marker={"color": colors},
                text=_text,
                textposition="outside",
                cliponaxis=False,
                customdata=hover,
                hovertemplate="%{customdata}<extra></extra>",
            )
        )
        fig.update_layout(
            title=(
                "Is position 0 exceptional?"
                + (
                    f"<br><sup>token 0 minus the strongest nonzero position: {_lead:+.1f} percentage points</sup>"
                    if token_count > 1
                    else ""
                )
            ),
            height=360,
            margin={"l": 56, "r": 16, "t": 76, "b": 92},
            xaxis={
                "title": "Key position",
                "tickmode": "array",
                "tickvals": positions[:: max(1, int(np.ceil(token_count / 28)))],
                "ticktext": labels[:: max(1, int(np.ceil(token_count / 28)))],
                "tickangle": -45,
            },
            yaxis={"title": "Layer/head pairs above threshold (%)", "range": [0, 108]},
            showlegend=False,
        )
        return apply_plot_theme(fig)

    def plot_hidden_delta(delta, tokens):
        data = np.nan_to_num(
            delta.numpy(),
            nan=0.0,
            posinf=0.0,
            neginf=0.0,
        )
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
            xaxis={
                "title": "Token position",
                "tickmode": "array",
                "tickvals": tick_positions,
                "ticktext": tick_labels,
                "tickangle": -45,
            },
            yaxis={"title": "Layer, including embedding layer", "dtick": 1},
        )
        return apply_plot_theme(fig)

    def plot_streaming_cache_waterfall(streaming_cache_summary):
        _recent = float(
            np.nan_to_num(
                streaming_cache_summary["recent_only_attention_mass"],
                nan=0.0,
                posinf=0.0,
                neginf=0.0,
            )
        )
        _retained = float(
            np.nan_to_num(
                streaming_cache_summary["anchor_plus_recent_attention_mass"],
                nan=0.0,
                posinf=0.0,
                neginf=0.0,
            )
        )
        _recovered = max(0.0, _retained - _recent)
        fig = go.Figure(
            data=go.Waterfall(
                x=["recent-only", "+ token 0", "retained mass"],
                y=[_recent, _recovered, _retained],
                measure=["absolute", "relative", "total"],
                text=[f"{_recent:.3f}", f"+{_recovered:.3f}", f"{_retained:.3f}"],
                textposition="outside",
                connector={"line": {"color": "#94a3b8", "width": 1.5}},
                increasing={"marker": {"color": GREEN}},
                totals={"marker": {"color": BLUE}},
                decreasing={"marker": {"color": "#e45555"}},
                hovertemplate="%{x}<br>attention mass=%{y:.4f}<extra></extra>",
            )
        )
        fig.add_hline(
            y=1.0,
            line={"color": "#94a3b8", "dash": "dot", "width": 1.5},
            annotation_text="all attention mass = 1.0",
            annotation_position="top left",
        )
        fig.update_layout(
            title="How much routing mass token 0 restores",
            height=360,
            margin={"l": 52, "r": 16, "t": 64, "b": 64},
            yaxis={"title": "Mean retained attention mass", "range": [0, 1.12]},
            xaxis={"title": ""},
            showlegend=False,
        )
        return apply_plot_theme(fig)

    def _dense_moe_valid_rows(table):
        if table is None or len(table) == 0:
            return None
        _table = table.copy()
        if "valid_prompt_count" in _table.columns:
            _table = _table[_table["valid_prompt_count"].fillna(0) > 0]
        elif "error" in _table.columns:
            _table = _table[_table["error"].fillna("") == ""]
        _table = _table.dropna(subset=["sink_rate_percent"])
        return _table if len(_table) > 0 else None

    def plot_dense_moe_sink_bars(dense_moe_table):
        _table = _dense_moe_valid_rows(dense_moe_table)
        if _table is None:
            return None

        _plain = "plain prompt"
        _anchor = "with model first-token anchor"
        _model_order = list(dict.fromkeys(_table["model_label"].tolist()))
        _line_x = []
        _line_y = []
        _plain_x, _plain_y, _plain_err, _plain_hover = [], [], [], []
        _anchor_x, _anchor_y, _anchor_err, _anchor_hover = [], [], [], []
        _annotations = []

        for _model_label in _model_order:
            _model_rows = _table[_table["model_label"] == _model_label]
            _plain_rows = _model_rows[_model_rows["condition"] == _plain]
            _anchor_rows = _model_rows[_model_rows["condition"] == _anchor]
            if len(_plain_rows) == 0 or len(_anchor_rows) == 0:
                continue
            _plain_row = _plain_rows.iloc[0]
            _anchor_row = _anchor_rows.iloc[0]
            _plain_value = float(_plain_row["sink_rate_percent"])
            _anchor_value = float(_anchor_row["sink_rate_percent"])
            _plain_std = float(_plain_row.get("sink_rate_std", 0.0) or 0.0)
            _anchor_std = float(_anchor_row.get("sink_rate_std", 0.0) or 0.0)
            _line_x.extend([_plain_value, _anchor_value, None])
            _line_y.extend([_model_label, _model_label, None])
            _plain_x.append(_plain_value)
            _plain_y.append(_model_label)
            _plain_err.append(_plain_std)
            _anchor_x.append(_anchor_value)
            _anchor_y.append(_model_label)
            _anchor_err.append(_anchor_std)
            _plain_hover.append(
                f"{_model_label}<br>plain prompt<br>sink rate={_plain_value:.2f}%<br>"
                f"prompt std={_plain_std:.2f} pp<br>"
                f"valid prompts={int(_plain_row['valid_prompt_count'])}/{int(_plain_row['prompt_count'])}"
            )
            _anchor_hover.append(
                f"{_model_label}<br>first-token anchor<br>sink rate={_anchor_value:.2f}%<br>"
                f"prompt std={_anchor_std:.2f} pp<br>"
                f"valid prompts={int(_anchor_row['valid_prompt_count'])}/{int(_anchor_row['prompt_count'])}"
            )
            _annotations.append(
                {
                    "x": (_plain_value + _anchor_value) / 2.0,
                    "y": _model_label,
                    "text": f"Δ {_anchor_value - _plain_value:+.1f} pp",
                    "showarrow": False,
                    "yshift": 18,
                    "font": {"size": 11, "color": "#475569"},
                }
            )

        if not _plain_x:
            return None

        _fig = go.Figure()
        _fig.add_trace(
            go.Scatter(
                x=_line_x,
                y=_line_y,
                mode="lines",
                line={"color": "#94a3b8", "width": 4},
                hoverinfo="skip",
                showlegend=False,
            )
        )
        _fig.add_trace(
            go.Scatter(
                name="plain prompt",
                x=_plain_x,
                y=_plain_y,
                mode="markers+text",
                text=[f"{_value:.1f}%" for _value in _plain_x],
                textposition="bottom center",
                marker={"color": BLUE, "size": 13, "symbol": "circle"},
                error_x={"type": "data", "array": _plain_err, "visible": True, "color": BLUE},
                customdata=_plain_hover,
                hovertemplate="%{customdata}<extra></extra>",
            )
        )
        _fig.add_trace(
            go.Scatter(
                name="first-token anchor",
                x=_anchor_x,
                y=_anchor_y,
                mode="markers+text",
                text=[f"{_value:.1f}%" for _value in _anchor_x],
                textposition="top center",
                marker={"color": GREEN, "size": 13, "symbol": "diamond"},
                error_x={"type": "data", "array": _anchor_err, "visible": True, "color": GREEN},
                customdata=_anchor_hover,
                hovertemplate="%{customdata}<extra></extra>",
            )
        )
        _fig.update_layout(
            title="Anchor effect on token-0 sink rate",
            height=max(310, 120 + 92 * len(_plain_y)),
            margin={"l": 190, "r": 24, "t": 64, "b": 72},
            xaxis={
                "title": "Layer/head pairs above threshold (%)",
                "range": [0, 100],
                "gridcolor": "#e5e7eb",
            },
            yaxis={"title": "", "categoryorder": "array", "categoryarray": _model_order[::-1]},
            legend={"orientation": "h", "y": -0.25},
            annotations=_annotations,
        )
        return apply_plot_theme(_fig)

    def plot_dense_moe_depth_profile(dense_moe_layer_table):
        _table = _dense_moe_valid_rows(dense_moe_layer_table)
        if _table is None:
            return None
        _depth_rows = _table[
            _table["layer_group"].isin(["early third", "middle third", "late third"])
        ].copy()
        if len(_depth_rows) == 0:
            return None

        from plotly.subplots import make_subplots

        _bucket_order = ["early third", "middle third", "late third"]
        _condition_order = ["plain prompt", "with model first-token anchor"]
        _condition_titles = ["Plain prompt", "First-token anchor"]
        _model_order = list(dict.fromkeys(_depth_rows["model_label"].tolist()))
        _model_colors = {label: [BLUE, GREEN, YELLOW][index % 3] for index, label in enumerate(_model_order)}
        _model_symbols = {label: ["circle", "diamond", "square"][index % 3] for index, label in enumerate(_model_order)}
        _fig = make_subplots(rows=1, cols=2, shared_yaxes=True, subplot_titles=_condition_titles)

        for _column, _condition in enumerate(_condition_order, start=1):
            for _model_label in _model_order:
                _series = _depth_rows[
                    (_depth_rows["model_label"] == _model_label)
                    & (_depth_rows["condition"] == _condition)
                ]
                _values, _errors, _hover = [], [], []
                for _bucket in _bucket_order:
                    _match = _series[_series["layer_group"] == _bucket]
                    if len(_match) == 0:
                        _values.append(None)
                        _errors.append(0.0)
                        _hover.append("")
                        continue
                    _row = _match.iloc[0]
                    _value = float(_row["sink_rate_percent"])
                    _std = float(_row.get("sink_rate_std", 0.0) or 0.0)
                    _values.append(_value)
                    _errors.append(_std)
                    _hover.append(
                        f"{_model_label}<br>{_condition}<br>{_bucket}<br>"
                        f"layers={int(_row['layer_count'])}<br>sink rate={_value:.2f}%<br>"
                        f"prompt std={_std:.2f} pp<br>"
                        f"valid prompts={int(_row['valid_prompt_count'])}/{int(_row['prompt_count'])}"
                    )
                _fig.add_trace(
                    go.Scatter(
                        name=_model_label,
                        x=_bucket_order,
                        y=_values,
                        mode="lines+markers",
                        line={"width": 3, "color": _model_colors[_model_label]},
                        marker={"size": 9, "symbol": _model_symbols[_model_label]},
                        error_y={"type": "data", "array": _errors, "visible": True},
                        customdata=_hover,
                        hovertemplate="%{customdata}<extra></extra>",
                        showlegend=_column == 1,
                    ),
                    row=1,
                    col=_column,
                )
        _fig.update_yaxes(title_text="Layer/head pairs above threshold (%)", range=[0, 100], row=1, col=1)
        _fig.update_yaxes(range=[0, 100], row=1, col=2)
        _fig.update_xaxes(title_text="Normalized depth bucket", categoryorder="array", categoryarray=_bucket_order)
        _fig.update_layout(
            title="Where sink heads appear across depth",
            height=420,
            margin={"l": 62, "r": 18, "t": 78, "b": 92},
            legend={"orientation": "h", "y": -0.24},
        )
        return apply_plot_theme(_fig)

    def plot_dense_moe_attention_type(dense_moe_layer_table):
        _table = _dense_moe_valid_rows(dense_moe_layer_table)
        if _table is None:
            return None
        _type_order = ["local sliding-window attention", "global attention"]
        _type_rows = _table[_table["layer_group"].isin(_type_order)].copy()
        if len(_type_rows) == 0:
            return None

        _condition_order = ["plain prompt", "with model first-token anchor"]
        _model_order = list(dict.fromkeys(_type_rows["model_label"].tolist()))
        _row_keys = [
            (_model_label, _condition)
            for _model_label in _model_order
            for _condition in _condition_order
            if len(
                _type_rows[
                    (_type_rows["model_label"] == _model_label)
                    & (_type_rows["condition"] == _condition)
                ]
            )
            > 0
        ]
        _labels, _z, _text, _hover = [], [], [], []
        for _model_label, _condition in _row_keys:
            _short_model = "Dense" if "Dense" in _model_label else "MoE" if "MoE" in _model_label else _model_label
            _short_condition = "anchor" if _condition != "plain prompt" else "plain"
            _labels.append(f"{_short_model} · {_short_condition}")
            _values, _texts, _hovers = [], [], []
            for _layer_type in _type_order:
                _match = _type_rows[
                    (_type_rows["model_label"] == _model_label)
                    & (_type_rows["condition"] == _condition)
                    & (_type_rows["layer_group"] == _layer_type)
                ]
                if len(_match) == 0:
                    _values.append(None)
                    _texts.append("")
                    _hovers.append("")
                    continue
                _row = _match.iloc[0]
                _value = float(_row["sink_rate_percent"])
                _values.append(_value)
                _texts.append(f"{_value:.1f}%")
                _hovers.append(
                    f"{_model_label}<br>{_condition}<br>{_layer_type}<br>"
                    f"layers={int(_row['layer_count'])}<br>sink rate={_value:.2f}%<br>"
                    f"valid prompts={int(_row['valid_prompt_count'])}/{int(_row['prompt_count'])}"
                )
            _z.append(_values)
            _text.append(_texts)
            _hover.append(_hovers)

        _fig = go.Figure(
            data=go.Heatmap(
                z=_z,
                x=["Local sliding-window", "Global"],
                y=_labels,
                text=_text,
                customdata=_hover,
                texttemplate="%{text}",
                colorscale=SINK_COLORSCALE,
                zmin=0,
                zmax=100,
                colorbar={"title": "sink rate (%)", "thickness": 12},
                hovertemplate="%{customdata}<extra></extra>",
            )
        )
        _fig.update_layout(
            title="Sink rate by Gemma 4 attention layer type",
            height=max(330, 145 + 52 * len(_labels)),
            margin={"l": 120, "r": 24, "t": 62, "b": 58},
            xaxis={"title": "Attention layer type"},
            yaxis={"title": "", "autorange": "reversed"},
        )
        return apply_plot_theme(_fig)

    return (
        apply_plot_theme,
        build_sink_switch_counterfactual,
        plot_attention_flow,
        plot_attention_matrix,
        plot_dense_moe_attention_type,
        plot_dense_moe_depth_profile,
        plot_dense_moe_sink_bars,
        plot_hidden_delta,
        plot_position_sink_profile,
        plot_sink_switch_gain,
        plot_sink_switch_lens,
        plot_sink_map,
        plot_streaming_cache_waterfall,
    )


@app.cell(hide_code=True)
def _(mo, probe):
    if probe is None:
        attention_view_mode = None
        attention_window_center = None
        attention_window_size = None
        attention_view_controls = None
    else:
        _token_count = len(probe["tokens"])
        attention_view_mode = mo.ui.dropdown(
            options=["Overview", "Token window"],
            value="Overview",
            label="Attention-map view",
            full_width=True,
        )
        attention_window_center = mo.ui.slider(
            start=0,
            stop=max(1, _token_count - 1),
            step=1,
            value=max(0, _token_count - 1),
            show_value=True,
            label="Window center query token",
            full_width=True,
        )
        attention_window_size = mo.ui.dropdown(
            options=["32", "64", "96", "128"],
            value="64",
            label="Window size",
            full_width=True,
        )
        attention_view_controls = mo.vstack(
            [
                mo.hstack(
                    [attention_view_mode, attention_window_center, attention_window_size],
                    widths="equal",
                    wrap=True,
                    gap=1,
                ),
                mo.md(
                    "Overview mode downsamples long matrices before plotting. Token-window mode always retains key position 0 alongside the selected local range."
                ),
            ],
            gap=0.5,
        )
    return (
        attention_view_mode,
        attention_window_center,
        attention_window_size,
        attention_view_controls,
    )


@app.cell(hide_code=True)
def _(
    attention_view_controls,
    attention_view_mode,
    attention_window_center,
    attention_window_size,
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
            ### 3a. Inspect the strongest head

            Run a probe to reveal the token-by-token attention heatmap.
            """
        )
    else:
        _layer = min(int(selected_layer_index), probe["attention"].shape[0] - 1)
        _head = min(int(selected_head_index), probe["attention"].shape[1] - 1)
        _score_line = (
            f"The selected head has a normalized token-0 sink score of {selected_head_score:.3f}."
            if selected_head_score is not None
            else "The selected head is ready for inspection."
        )
        _selected_matrix = probe["attention"][_layer, _head].numpy()
        selected_attention_fig = plot_attention_matrix(
            _selected_matrix,
            probe["tokens"],
            _layer,
            _head,
            view_mode=attention_view_mode.value,
            window_center=int(attention_window_center.value),
            window_size=int(attention_window_size.value),
        )
        selected_attention_output = mo.vstack(
            [
                mo.md(
                    f"""
                    ### 3a. Inspect the strongest head

                    Hover any cell to see which query token attended to which key token.
                    A bright green-yellow vertical band at key position 0 is the
                    sink signature. {_score_line}
                    """
                ),
                attention_view_controls,
                selected_attention_fig,
            ],
            gap=0.75,
        )

    selected_attention_output
    return


@app.cell(hide_code=True)
def _(mo, probe):
    if probe is None:
        sink_switch_control = None
        _sink_switch_control_view = mo.md(
            """
            ### 3b. The Sink Switch

            The Sink Switch appears after a successful attention probe. It is a
            truthful counterfactual lens over the selected head, not a modified
            model forward pass.
            """
        )
    else:
        sink_switch_control = mo.ui.checkbox(
            value=False,
            label="Flip the Sink Switch: make token 0 unavailable in this selected head",
        )
        _sink_switch_control_view = mo.vstack(
            [
                mo.md(
                    """
                    ### 3b. The Sink Switch

                    Flip the switch to ask a narrow counterfactual question:
                    **if this one head could not route attention to token 0,
                    where would that attention mass go?**

                    This does not rerun or patch the model. It suppresses key
                    position 0 in the selected head's returned attention matrix
                    and renormalizes each query row over the remaining visible
                    keys. That makes it fast, portable, and honest.
                    """
                ),
                sink_switch_control,
            ],
            gap=0.75,
        )
    _sink_switch_control_view
    return (sink_switch_control,)


@app.cell(hide_code=True)
def _(
    build_sink_switch_counterfactual,
    mo,
    plot_sink_switch_gain,
    plot_sink_switch_lens,
    probe,
    selected_head_index,
    selected_layer_index,
    sink_switch_control,
):
    if probe is None or sink_switch_control is None:
        sink_switch_output = None
    else:
        _layer = min(int(selected_layer_index), probe["attention"].shape[0] - 1)
        _head = min(int(selected_head_index), probe["attention"].shape[1] - 1)
        _selected_matrix = probe["attention"][_layer, _head].numpy()
        _switch_result = build_sink_switch_counterfactual(
            _selected_matrix,
            probe["tokens"],
        )
        if not sink_switch_control.value:
            sink_switch_output = mo.md(
                f"""
                Switch off. In the actual selected head, query tokens send an
                average of **{_switch_result["mean_token0_mass"]:.3f}**
                attention mass to token 0. Flip the switch to see the
                counterfactual redistribution.
                """
            ).callout(kind="info")
        else:
            _recipient_position = int(_switch_result["top_recipient_position"])
            _recipient_token = _switch_result["top_recipient_token"][:24]
            sink_switch_output = mo.vstack(
                [
                    plot_sink_switch_lens(_switch_result, probe["tokens"], _layer, _head),
                    mo.md(
                        f"""
                        **Counterfactual readout**

                        | Signal | Value |
                        | --- | ---: |
                        | Actual mean attention to token 0 | {_switch_result["mean_token0_mass"]:.3f} |
                        | Actual mixing score | {_switch_result["original_mixing_score"]:.3f} |
                        | Counterfactual mixing score | {_switch_result["counterfactual_mixing_score"]:.3f} |
                        | Largest recipient after switch | {_recipient_position}: `{_recipient_token}` |

                        The right panel is not a new model run. It is a lens
                        over one selected head: token 0 is made unavailable,
                        and each query row is renormalized over the remaining
                        keys. If token 0 was absorbing no-op routing mass, the
                        switch forces that mass onto content tokens.
                        """
                    ).callout(kind="success"),
                    plot_sink_switch_gain(_switch_result, probe["tokens"]),
                ],
                gap=0.75,
            )
    sink_switch_output
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
        )
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
                    ### Follow one query token

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
        )
    else:
        sink_map_fig = plot_sink_map(sink_scores, float(sink_threshold.value))
        sink_map_output = mo.vstack(
            [
                mo.md(
                    """
                    ### Sink atlas

                    Each tile is one layer/head pair. The color is the
                    opportunity-normalized token-0 sink score, and white rings
                    mark heads above the selected threshold.
                    """
                ),
                sink_map_fig,
            ],
            gap=0.75,
        )

    sink_map_output
    return


@app.cell(hide_code=True)
def _(format_result_table, mo, sink_table):
    strongest_sink_heads = sink_table.head(12) if sink_table is not None else None
    _strongest_view = format_result_table(
        strongest_sink_heads,
        columns=["layer", "head", "token0_sink_score", "strong_sink"],
        labels={
            "layer": "Layer",
            "head": "Head",
            "token0_sink_score": "Token-0 sink strength",
            "strong_sink": "Above threshold",
        },
        decimals={"token0_sink_score": 3},
        page_size=12,
        label="Highest-scoring sink heads",
    )
    _strongest_output = (
        mo.vstack([mo.md("### Highest-scoring sink heads"), _strongest_view])
        if _strongest_view is not None
        else None
    )
    _strongest_output
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
                r"""
                ### 3c. Practical implication: streaming caches

                A streaming decoder cannot keep every old key/value vector forever.
                If a recent-only cache drops token 0, how much attention mass does
                the final token lose compared with a cache that keeps token 0 plus
                recent tokens?

                For the final query $T-1$, the diagnostic reports

$$
\Delta_{\mathrm{cache}} =
\frac{1}{LH}\sum_{\ell,h}
\left(
\sum_{j\in\{0\}\cup\mathcal{R}}\alpha_{T-1,j}^{(\ell,h)}
- \sum_{j\in\mathcal{R}}\alpha_{T-1,j}^{(\ell,h)}
\right),
$$

                where $\mathcal{R}$ is the recent-token window. This measures
                recovered routing mass, not perplexity or task accuracy; it is a
                mechanism diagnostic motivated by streaming-attention results.
                """
            ),
            streaming_cache_window,
        ],
        gap=1,
    )
    return (streaming_cache_window,)


@app.cell(hide_code=True)
def _(
    format_result_table,
    mo,
    pd,
    plot_streaming_cache_waterfall,
    probe,
    streaming_cache_diagnostic,
    streaming_cache_window,
    torch,
):
    if probe is None or pd is None:
        streaming_cache_table = None
        _streaming_output = mo.md("_Run the live probe to unlock the streaming-cache diagnostic._")
    else:
        streaming_cache_summary = streaming_cache_diagnostic(
            probe,
            streaming_cache_window.value,
            torch,
        )
        streaming_cache_table = pd.DataFrame([streaming_cache_summary])
        _streaming_table_view = format_result_table(
            streaming_cache_table,
            columns=[
                "token_count",
                "cache_window",
                "recent_only_attention_mass",
                "attention_mass_recovered_by_keeping_token_0",
                "anchor_plus_recent_attention_mass",
            ],
            labels={
                "token_count": "Tokens",
                "cache_window": "Recent-token budget",
                "recent_only_attention_mass": "Recent-only mass",
                "attention_mass_recovered_by_keeping_token_0": "Recovered by token 0",
                "anchor_plus_recent_attention_mass": "Retained mass",
            },
            decimals={
                "recent_only_attention_mass": 3,
                "attention_mass_recovered_by_keeping_token_0": 3,
                "anchor_plus_recent_attention_mass": 3,
            },
            page_size=5,
            label="Streaming-cache measurements",
        )
        streaming_cache_fig = plot_streaming_cache_waterfall(streaming_cache_summary)
        _streaming_output = mo.vstack(
            [
                streaming_cache_fig,
                _streaming_table_view,
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
def _(mo):
    mo.md(r"""
    ## 4. Does the sink limit perturbation spread?

    Take an original prompt $x$ and a controlled variant $x'$ that differs
    by one lexical edit. At token $i$ and layer $\ell$, the notebook measures

    $$
    D_i^{(\ell)} =
    \left\|v_i^{(\ell)}(x)-v_i^{(\ell)}(x')\right\|_2.
    $$

    A bright cell in the heatmap means that the local edit substantially changed
    that token representation at that depth. The paper interprets this as an
    empirical estimate of the Jacobian sensitivity introduced earlier. If a
    first-position sink removes weight from content-to-content paths, we expect
    less off-diagonal and late-layer spread—not necessarily zero drift.

    The within-condition heatmap below explains *where* the edit travels. The
    paired benchmark that follows asks the stronger question: how do sink rate
    and final-layer drift change with the model's special first-position token
    versus a plain prompt?
    """)
    return


@app.cell(hide_code=True)
def _(mo, perturbed_prompt):
    if perturbed_prompt is None:
        perturb_prompt_view = mo.md(
            """
            ### Current perturbation

            Waiting for a successful attention probe.
            """
        )
    else:
        perturb_prompt_view = mo.md(f"""
        ### Current perturbation

        This run changes one word and measures hidden-state drift for the
        selected condition.

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
        ).callout(kind="danger")
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

            This is the within-condition view. The paired benchmark below makes
            the stronger comparison: special first-position token versus plain
            prompt, across a fixed prompt set and model family.
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
    comparison_prompt_set = mo.ui.dropdown(
        options=[
            "Neutral document mini-benchmark",
            "Current selected prompt",
        ],
        value="Neutral document mini-benchmark",
        label="Prompt evaluation set",
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

    return (
        comparison_model_a,
        comparison_model_b,
        comparison_prompt_set,
        comparison_run_button,
        comparison_run_mode,
        comparison_token_budget,
        context_sweep_button,
        context_sweep_model,
    )


@app.cell(hide_code=True)
def _(
    DEFAULT_SWEEP_MODELS,
    comparison_model_a,
    comparison_model_b,
    comparison_prompt_set,
    comparison_run_button,
    comparison_run_mode,
    comparison_token_budget,
    context_sweep_button,
    context_sweep_model,
    mo,
):
    if comparison_run_mode.value == "Run selected pair":
        comparison_model_view = mo.hstack(
            [comparison_model_a, comparison_model_b],
            widths="equal",
            wrap=True,
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

    if comparison_run_mode.value == "Skip cloud sweep":
        _comparison_run_view = mo.md(
            "Select a sweep mode above to enable the model-family run button."
        ).callout(kind="info")
    else:
        _comparison_run_view = comparison_run_button

    mo.vstack(
        [
            mo.md(
                """
                ## 5. Cross-model evidence and a boundary test

                The single-model probe establishes the mechanism. This benchmark
                separates three roles: LLaMA 3.1 is the direct-reproduction
                family, Gemma 2 9B is a replication-style extension, and Qwen is
                an open control for testing model- and scale-dependence.

                The paper's within-family reference is:

                | LLaMA 3.1 | Total attention heads | Reported sink rate |
                | --- | ---: | ---: |
                | 8B | 1,024 | 45.97% |
                | 70B | 5,120 | 73.49% |
                | 405B | 16,128 | 78.29% |

                Our 8B run can reproduce the model-family phenomenon, but it
                cannot by itself reproduce this three-size scaling curve.

                By default this section evaluates a neutral mini-benchmark of
                document prefixes instead of the reader-facing prompt above. That
                makes the scale check less dependent on hand-authored wording.

                **Important training/inference distinction.** The paper shows
                that packing strategy determines whether a model learns to use
                the explicit beginning token or simply the first available
                position as its sink. Our anchor control changes the inference
                input only; it does not recreate those pre-training conditions.
                """
            ),
            mo.md(
                """
                The sweep path loads models ephemerally: after a model's rows are
                computed, it is moved off GPU, local references are deleted, and
                CUDA cache is cleared before the next model. For the cleanest
                memory profile, attach the GPU and run this section from a fresh
                cloud runtime.
                """
            ).callout(kind="info"),
            mo.hstack(
                [comparison_run_mode, comparison_token_budget, comparison_prompt_set],
                widths="equal",
                wrap=True,
                gap=1,
            ),
            comparison_model_view,
            _comparison_run_view,
            mo.md(
                """
                ### Boundary test: inference context length

                The paper's training result concerns models trained with different
                context lengths. This deliberately different test holds one model
                fixed and varies only inference length. It is a boundary test, not
                a reproduction: either direction is informative.
                """
            ),
            context_sweep_model,
            context_sweep_button,
        ],
        gap=1,
    )
    return


@app.cell(hide_code=True)
def _(
    anchored_prompt,
    build_long_context_prompt,
    hidden_drift_summary,
    mo,
    perturb_prompt,
    run_attention_probe,
    summarize_attention_sink,
):
    def measure_anchor_effect(
        model_id,
        base_prompt,
        load_ephemeral_model_bundle,
        release_model_memory,
        precision_key,
        hf_token,
        torch,
        max_length,
        sink_threshold,
    ):
        _tokenizer = None
        _model = None
        _device = None
        _model_dtype = None
        _base_prompts = [base_prompt] if isinstance(base_prompt, str) else list(base_prompt)
        try:
            _tokenizer, _model, _device, _model_dtype, _model_error = (
                load_ephemeral_model_bundle(
                    model_id,
                    precision_key,
                    hf_token,
                )
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
                        "token0_position_rank": None,
                        "next_strongest_position": None,
                        "next_strongest_position_rate_percent": None,
                        "final_layer_drift": None,
                        "prompt_index": None,
                        "error": str(_model_error),
                    }
                ]

            _comparison_rows = []
            _prompt_progress = mo.status.progress_bar(
                _base_prompts,
                title=f"Benchmarking {model_id}",
                subtitle="Running paired anchor and plain-prompt probes.",
                completion_title=f"Finished {model_id}",
                show_rate=False,
            )
            for _prompt_index, _base_prompt in enumerate(_prompt_progress):
                for _condition, _anchor_name in [
                    ("with model first-token anchor", "Use model special token at first position"),
                    ("plain prompt", "Plain prompt only"),
                ]:
                    try:
                        _text, _anchor_note = anchored_prompt(_base_prompt, _anchor_name, _tokenizer)
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
                                "token0_position_rank": _sink_summary["token0_position_rank"],
                                "next_strongest_position": _sink_summary[
                                    "next_strongest_position"
                                ],
                                "next_strongest_position_rate_percent": _sink_summary[
                                    "next_strongest_position_rate_percent"
                                ],
                                "final_layer_drift": _drift_summary["final_layer_mean_drift"],
                                "prompt_index": _prompt_index,
                                "error": "",
                            }
                        )
                    except Exception as exc:  # noqa: BLE001 - keep partial benchmark rows.
                        _comparison_rows.append(
                            {
                                "model": model_id,
                                "dtype": _model_dtype,
                                "condition": _condition,
                                "tokens": None,
                                "sink_rate_percent": None,
                                "mean_sink_strength": None,
                                "last_token_attention_to_token_0": None,
                                "token0_position_rank": None,
                                "next_strongest_position": None,
                                "next_strongest_position_rate_percent": None,
                                "final_layer_drift": None,
                                "prompt_index": _prompt_index,
                                "error": str(exc),
                            }
                        )
            return _comparison_rows
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
                    "token0_position_rank": None,
                    "next_strongest_position": None,
                    "next_strongest_position_rate_percent": None,
                    "final_layer_drift": None,
                    "prompt_index": None,
                    "error": str(exc),
                }
            ]
        finally:
            if _model is not None:
                try:
                    _model.to("cpu")
                except Exception:
                    pass
            del _model
            del _tokenizer
            release_model_memory()

    def summarize_prompt_benchmark(rows, pd):
        if not rows:
            return []

        _table = pd.DataFrame(rows)
        if "error" not in _table.columns:
            _table["error"] = ""

        _summary_rows = []
        _group_columns = ["model", "dtype", "condition"]
        for _group_values, _group in _table.groupby(_group_columns, dropna=False):
            _row = dict(zip(_group_columns, _group_values))
            _errors = [
                str(_error)
                for _error in _group.get("error", [])
                if isinstance(_error, str) and _error.strip()
            ]
            _valid = _group[_group["error"].fillna("") == ""]
            _row["prompt_count"] = int(len(_group))
            _row["valid_prompt_count"] = int(len(_valid))
            if len(_valid) == 0:
                _row.update(
                    {
                        "tokens": None,
                        "sink_rate_percent": None,
                        "mean_sink_strength": None,
                        "last_token_attention_to_token_0": None,
                        "token0_position_rank": None,
                        "next_strongest_position": None,
                        "next_strongest_position_rate_percent": None,
                        "final_layer_drift": None,
                        "error": "; ".join(_errors),
                    }
                )
            else:
                _row.update(
                    {
                        "tokens": float(_valid["tokens"].mean()),
                        "sink_rate_percent": float(_valid["sink_rate_percent"].mean()),
                        "mean_sink_strength": float(_valid["mean_sink_strength"].mean()),
                        "last_token_attention_to_token_0": float(
                            _valid["last_token_attention_to_token_0"].mean()
                        ),
                        "token0_position_rank": float(_valid["token0_position_rank"].mean()),
                        "next_strongest_position": float(
                            _valid["next_strongest_position"].mean()
                        ),
                        "next_strongest_position_rate_percent": float(
                            _valid["next_strongest_position_rate_percent"].mean()
                        ),
                        "final_layer_drift": float(_valid["final_layer_drift"].mean()),
                        "error": "; ".join(_errors),
                    }
                )
            _summary_rows.append(_row)
        return _summary_rows

    def measure_context_sweep(
        model_id,
        base_prompt,
        budgets,
        load_ephemeral_model_bundle,
        release_model_memory,
        precision_key,
        hf_token,
        torch,
        sink_threshold,
    ):
        _tokenizer = None
        _model = None
        _device = None
        _model_dtype = None
        try:
            _tokenizer, _model, _device, _model_dtype, _model_error = (
                load_ephemeral_model_bundle(
                    model_id,
                    precision_key,
                    hf_token,
                )
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
                        "token0_position_rank": None,
                        "next_strongest_position": None,
                        "next_strongest_position_rate_percent": None,
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
            _budget_progress = mo.status.progress_bar(
                list(budgets),
                title=f"Context sweep · {model_id}",
                subtitle="Increasing the inference token budget.",
                completion_title="Context sweep complete",
                show_rate=False,
            )
            for _budget in _budget_progress:
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
                            "token0_position_rank": _sink_summary["token0_position_rank"],
                            "next_strongest_position": _sink_summary[
                                "next_strongest_position"
                            ],
                            "next_strongest_position_rate_percent": _sink_summary[
                                "next_strongest_position_rate_percent"
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
                            "token0_position_rank": None,
                            "next_strongest_position": None,
                            "next_strongest_position_rate_percent": None,
                            "error": str(exc),
                        }
                    )
            return _context_rows
        finally:
            if _model is not None:
                try:
                    _model.to("cpu")
                except Exception:
                    pass
            del _model
            del _tokenizer
            release_model_memory()

    def _normalize_attention_layer_kind(layer_kind):
        _text = str(layer_kind).lower()
        if any(_marker in _text for _marker in ["sliding", "local", "window"]):
            return "local sliding-window attention"
        if any(_marker in _text for _marker in ["global", "full"]):
            return "global attention"
        return "reported attention layer"

    def infer_attention_layer_kinds(model, layer_count):
        _configs = []
        _config = getattr(model, "config", None)
        if _config is not None:
            _configs.append(_config)
            for _attribute in ["text_config", "language_config", "decoder_config"]:
                _nested_config = getattr(_config, _attribute, None)
                if _nested_config is not None:
                    _configs.append(_nested_config)

        for _config_object in _configs:
            for _attribute in ["layer_types", "attention_types", "attn_types"]:
                _layer_types = getattr(_config_object, _attribute, None)
                if isinstance(_layer_types, (list, tuple)) and len(_layer_types) >= layer_count:
                    return [
                        _normalize_attention_layer_kind(_layer_types[_layer])
                        for _layer in range(layer_count)
                    ]

        # Some configs expose a cadence instead of an explicit layer-type list.
        for _config_object in _configs:
            _full_interval = (
                getattr(_config_object, "full_attention_interval", None)
                or getattr(_config_object, "global_attention_frequency", None)
                or getattr(_config_object, "attention_pattern_period", None)
            )
            _sliding_window = getattr(_config_object, "sliding_window", None)
            if isinstance(_full_interval, int) and _full_interval > 0 and _sliding_window:
                return [
                    "global attention"
                    if (_layer + 1) % _full_interval == 0 or _layer == layer_count - 1
                    else "local sliding-window attention"
                    for _layer in range(layer_count)
                ]

        return ["reported attention layer" for _ in range(layer_count)]

    def dense_moe_layer_breakdown(sink_summary, layer_kinds, torch, sink_threshold):
        def _dense_moe_finite_mean(tensor, fallback=0.0):
            _finite_values = tensor[torch.isfinite(tensor)]
            if _finite_values.numel() == 0:
                return float(fallback)
            return float(_finite_values.mean().item())

        _sink_scores = sink_summary["sink_scores"]
        _layer_count = int(_sink_scores.shape[0])
        if not layer_kinds or len(layer_kinds) != _layer_count:
            layer_kinds = ["reported attention layer" for _ in range(_layer_count)]

        def _layer_row(_label, _layer_indices, _order):
            if not _layer_indices:
                return None
            _subset = _sink_scores[_layer_indices, :]
            return {
                "layer_group": _label,
                "layer_group_order": _order,
                "layer_count": int(len(_layer_indices)),
                "sink_rate_percent": float(
                    (_subset > float(sink_threshold)).float().mean().item() * 100.0
                ),
                "mean_sink_strength": _dense_moe_finite_mean(_subset),
            }

        _rows = []
        _third = max(1, int((_layer_count + 2) // 3))
        _depth_groups = [
            ("early third", list(range(0, min(_third, _layer_count))), 0),
            ("middle third", list(range(min(_third, _layer_count), min(2 * _third, _layer_count))), 1),
            ("late third", list(range(min(2 * _third, _layer_count), _layer_count)), 2),
        ]
        for _label, _indices, _order in _depth_groups:
            _row = _layer_row(_label, _indices, _order)
            if _row is not None:
                _rows.append(_row)

        _unique_kinds = list(dict.fromkeys(layer_kinds))
        for _index, _kind in enumerate(_unique_kinds):
            _indices = [
                _layer
                for _layer, _layer_kind in enumerate(layer_kinds)
                if _layer_kind == _kind
            ]
            _row = _layer_row(_kind, _indices, 10 + _index)
            if _row is not None:
                _rows.append(_row)
        return _rows

    def summarize_dense_moe_rows(rows, pd):
        if not rows:
            return []
        _table = pd.DataFrame(rows)
        if "error" not in _table.columns:
            _table["error"] = ""

        _summary_rows = []
        _group_columns = ["model_label", "model", "architecture", "dtype", "condition"]
        for _group_values, _group in _table.groupby(_group_columns, dropna=False):
            _row = dict(zip(_group_columns, _group_values))
            _errors = [
                str(_error)
                for _error in _group.get("error", [])
                if isinstance(_error, str) and _error.strip()
            ]
            _valid = _group[_group["error"].fillna("") == ""]
            _row["prompt_count"] = int(len(_group))
            _row["valid_prompt_count"] = int(len(_valid))
            if len(_valid) == 0:
                _row.update(
                    {
                        "tokens": None,
                        "layer_count": None,
                        "head_count": None,
                        "global_layer_count": None,
                        "local_layer_count": None,
                        "sink_rate_percent": None,
                        "sink_rate_std": None,
                        "sink_rate_min": None,
                        "sink_rate_max": None,
                        "mean_sink_strength": None,
                        "last_token_attention_to_token_0": None,
                        "token0_position_rank": None,
                        "final_layer_drift": None,
                        "error": "; ".join(_errors),
                    }
                )
            else:
                _sink_rates = _valid["sink_rate_percent"].dropna()
                _row.update(
                    {
                        "tokens": float(_valid["tokens"].mean()),
                        "layer_count": float(_valid["layer_count"].mean()),
                        "head_count": float(_valid["head_count"].mean()),
                        "global_layer_count": float(_valid["global_layer_count"].mean()),
                        "local_layer_count": float(_valid["local_layer_count"].mean()),
                        "sink_rate_percent": float(_valid["sink_rate_percent"].mean()),
                        "sink_rate_std": float(_sink_rates.std(ddof=0))
                        if len(_sink_rates) > 1
                        else 0.0,
                        "sink_rate_min": float(_sink_rates.min()),
                        "sink_rate_max": float(_sink_rates.max()),
                        "mean_sink_strength": float(_valid["mean_sink_strength"].mean()),
                        "last_token_attention_to_token_0": float(
                            _valid["last_token_attention_to_token_0"].mean()
                        ),
                        "token0_position_rank": float(_valid["token0_position_rank"].mean()),
                        "final_layer_drift": float(_valid["final_layer_drift"].mean())
                        if "final_layer_drift" in _valid.columns
                        and _valid["final_layer_drift"].notna().any()
                        else None,
                        "error": "; ".join(_errors),
                    }
                )
            _summary_rows.append(_row)
        return _summary_rows

    def summarize_dense_moe_layer_rows(layer_rows, pd):
        if not layer_rows:
            return []
        _table = pd.DataFrame(layer_rows)
        if "error" not in _table.columns:
            _table["error"] = ""

        _summary_rows = []
        _group_columns = [
            "model_label",
            "architecture",
            "condition",
            "layer_group",
            "layer_group_order",
        ]
        for _group_values, _group in _table.groupby(_group_columns, dropna=False):
            _row = dict(zip(_group_columns, _group_values))
            _errors = [
                str(_error)
                for _error in _group.get("error", [])
                if isinstance(_error, str) and _error.strip()
            ]
            _valid = _group[_group["error"].fillna("") == ""]
            _row["prompt_count"] = int(len(_group))
            _row["valid_prompt_count"] = int(len(_valid))
            if len(_valid) == 0:
                _row.update(
                    {
                        "layer_count": None,
                        "sink_rate_percent": None,
                        "sink_rate_std": None,
                        "mean_sink_strength": None,
                        "error": "; ".join(_errors),
                    }
                )
            else:
                _sink_rates = _valid["sink_rate_percent"].dropna()
                _row.update(
                    {
                        "layer_count": float(_valid["layer_count"].mean()),
                        "sink_rate_percent": float(_valid["sink_rate_percent"].mean()),
                        "sink_rate_std": float(_sink_rates.std(ddof=0))
                        if len(_sink_rates) > 1
                        else 0.0,
                        "mean_sink_strength": float(_valid["mean_sink_strength"].mean()),
                        "error": "; ".join(_errors),
                    }
                )
            _summary_rows.append(_row)
        return sorted(_summary_rows, key=lambda _row: float(_row["layer_group_order"]))

    def measure_gemma4_dense_moe(
        model_specs,
        base_prompts,
        load_ephemeral_model_bundle,
        release_model_memory,
        precision_key,
        hf_token,
        torch,
        max_length,
        sink_threshold,
        measure_drift=False,
    ):
        _base_prompts = [base_prompts] if isinstance(base_prompts, str) else list(base_prompts)
        _metric_rows = []
        _layer_rows = []

        _model_progress = mo.status.progress_bar(
            list(model_specs),
            title="Dense-vs-MoE model sweep",
            subtitle="Models are loaded one at a time and released after measurement.",
            completion_title="Dense-vs-MoE model sweep complete",
            show_rate=False,
        )
        for _model_spec in _model_progress:
            _tokenizer = None
            _model = None
            _device = None
            _model_dtype = None
            try:
                _tokenizer, _model, _device, _model_dtype, _model_error = (
                    load_ephemeral_model_bundle(
                        _model_spec["model"],
                        precision_key,
                        hf_token,
                    )
                )
                if _model_error is not None or _model is None:
                    _metric_rows.append(
                        {
                            "model_label": _model_spec["label"],
                            "model": _model_spec["model"],
                            "architecture": _model_spec["architecture"],
                            "dtype": _model_dtype,
                            "condition": "load failed",
                            "tokens": None,
                            "layer_count": None,
                            "head_count": None,
                            "global_layer_count": None,
                            "local_layer_count": None,
                            "sink_rate_percent": None,
                            "mean_sink_strength": None,
                            "last_token_attention_to_token_0": None,
                            "token0_position_rank": None,
                            "final_layer_drift": None,
                            "prompt_index": None,
                            "error": str(_model_error),
                        }
                    )
                    continue

                _prompt_progress = mo.status.progress_bar(
                    _base_prompts,
                    title=f"Prompt sweep · {_model_spec['label']}",
                    subtitle="Evaluating plain and first-token-anchor conditions.",
                    completion_title=f"Finished {_model_spec['label']}",
                    show_rate=False,
                )
                for _prompt_index, _base_prompt in enumerate(_prompt_progress):
                    for _condition, _anchor_name in [
                        ("plain prompt", "Plain prompt only"),
                        ("with model first-token anchor", "Use model special token at first position"),
                    ]:
                        try:
                            _text, _anchor_note = anchored_prompt(
                                _base_prompt,
                                _anchor_name,
                                _tokenizer,
                            )
                            _base_probe = run_attention_probe(
                                _text,
                                _model,
                                _tokenizer,
                                _device,
                                torch,
                                max_length,
                                top_k=4,
                                collect_hidden=bool(measure_drift),
                            )
                            _sink_summary = summarize_attention_sink(
                                _base_probe,
                                torch,
                                sink_threshold,
                            )
                            _layer_count = int(_sink_summary["sink_scores"].shape[0])
                            _head_count = int(_sink_summary["sink_scores"].shape[1])
                            _layer_kinds = infer_attention_layer_kinds(_model, _layer_count)
                            _global_layer_count = sum(
                                1 for _kind in _layer_kinds if _kind == "global attention"
                            )
                            _local_layer_count = sum(
                                1
                                for _kind in _layer_kinds
                                if _kind == "local sliding-window attention"
                            )
                            if measure_drift:
                                _perturbed_text = perturb_prompt(_text)
                                _perturbed_probe = run_attention_probe(
                                    _perturbed_text,
                                    _model,
                                    _tokenizer,
                                    _device,
                                    torch,
                                    max_length,
                                    top_k=4,
                                    collect_hidden=True,
                                )
                                _drift_summary = hidden_drift_summary(
                                    _base_probe,
                                    _perturbed_probe,
                                    torch,
                                )
                                _final_layer_drift = _drift_summary["final_layer_mean_drift"]
                            else:
                                _final_layer_drift = None

                            _metric_rows.append(
                                {
                                    "model_label": _model_spec["label"],
                                    "model": _model_spec["model"],
                                    "architecture": _model_spec["architecture"],
                                    "dtype": _model_dtype,
                                    "condition": _condition,
                                    "tokens": _sink_summary["token_count"],
                                    "layer_count": _layer_count,
                                    "head_count": _head_count,
                                    "global_layer_count": _global_layer_count,
                                    "local_layer_count": _local_layer_count,
                                    "sink_rate_percent": _sink_summary["sink_rate_percent"],
                                    "mean_sink_strength": _sink_summary["mean_sink_strength"],
                                    "last_token_attention_to_token_0": _sink_summary[
                                        "last_token_attention_to_token_0"
                                    ],
                                    "token0_position_rank": _sink_summary[
                                        "token0_position_rank"
                                    ],
                                    "final_layer_drift": _final_layer_drift,
                                    "prompt_index": _prompt_index,
                                    "error": "",
                                }
                            )

                            for _layer_row in dense_moe_layer_breakdown(
                                _sink_summary,
                                _layer_kinds,
                                torch,
                                sink_threshold,
                            ):
                                _layer_row.update(
                                    {
                                        "model_label": _model_spec["label"],
                                        "model": _model_spec["model"],
                                        "architecture": _model_spec["architecture"],
                                        "dtype": _model_dtype,
                                        "condition": _condition,
                                        "prompt_index": _prompt_index,
                                        "error": "",
                                    }
                                )
                                _layer_rows.append(_layer_row)
                        except Exception as exc:  # noqa: BLE001 - preserve partial rows.
                            _metric_rows.append(
                                {
                                    "model_label": _model_spec["label"],
                                    "model": _model_spec["model"],
                                    "architecture": _model_spec["architecture"],
                                    "dtype": _model_dtype,
                                    "condition": _condition,
                                    "tokens": None,
                                    "layer_count": None,
                                    "head_count": None,
                                    "global_layer_count": None,
                                    "local_layer_count": None,
                                    "sink_rate_percent": None,
                                    "mean_sink_strength": None,
                                    "last_token_attention_to_token_0": None,
                                    "token0_position_rank": None,
                                    "final_layer_drift": None,
                                    "prompt_index": _prompt_index,
                                    "error": str(exc),
                                }
                            )
            finally:
                if _model is not None:
                    try:
                        _model.to("cpu")
                    except Exception:
                        pass
                del _model
                del _tokenizer
                release_model_memory()

        return _metric_rows, _layer_rows

    return (
        measure_anchor_effect,
        measure_context_sweep,
        measure_gemma4_dense_moe,
        summarize_dense_moe_layer_rows,
        summarize_dense_moe_rows,
        summarize_prompt_benchmark,
    )


@app.cell(hide_code=True)
def _(
    clear_cached_model_bundle,
    DEFAULT_SWEEP_MODELS,
    MODEL_OPTIONS,
    NEUTRAL_BENCHMARK_PROMPTS,
    TOKEN_BUDGET_OPTIONS,
    comparison_model_a,
    comparison_model_b,
    comparison_prompt_set,
    comparison_run_button,
    comparison_run_mode,
    comparison_token_budget,
    hf_token,
    load_ephemeral_model_bundle,
    measure_anchor_effect,
    mo,
    pd,
    probe_config,
    release_model_memory,
    selected_precision_key,
    selected_prompt,
    sink_threshold,
    summarize_prompt_benchmark,
    torch,
):
    if (
        comparison_run_mode.value == "Skip cloud sweep"
        or not comparison_run_button.value
        or pd is None
    ):
        comparison_table = None
    else:
        clear_cached_model_bundle()
        _comparison_rows = []
        _selected_prompt = probe_config.prompt if probe_config is not None else selected_prompt
        if comparison_prompt_set.value == "Neutral document mini-benchmark":
            _sweep_prompts = list(NEUTRAL_BENCHMARK_PROMPTS)
        else:
            _sweep_prompts = [_selected_prompt]
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

        _model_progress = mo.status.progress_bar(
            _comparison_model_ids,
            title="Model-family sweep",
            subtitle="Each model is loaded, measured, and released before the next one.",
            completion_title="Model-family sweep complete",
            show_rate=False,
        )
        for _model_id in _model_progress:
            _model_prompt_rows = measure_anchor_effect(
                _model_id,
                _sweep_prompts,
                load_ephemeral_model_bundle,
                release_model_memory,
                selected_precision_key,
                hf_token,
                torch,
                _comparison_token_budget,
                sink_threshold.value,
            )
            for _row in _model_prompt_rows:
                _row["prompt_set"] = comparison_prompt_set.value
            if comparison_prompt_set.value == "Neutral document mini-benchmark":
                _comparison_rows.extend(summarize_prompt_benchmark(_model_prompt_rows, pd))
            else:
                _comparison_rows.extend(_model_prompt_rows)
        comparison_table = pd.DataFrame(_comparison_rows)
        clear_cached_model_bundle()
    return (comparison_table,)


@app.cell(hide_code=True)
def _(comparison_table, format_result_table, mo):
    if comparison_table is None:
        _comparison_output = mo.md(
            "_Optional cloud benchmark not run. Start with a selected pair or the fixed RTX family sweep when GPU time is available._"
        )
    else:
        _comparison_view = format_result_table(
            comparison_table,
            columns=[
                "model",
                "condition",
                "prompt_count",
                "valid_prompt_count",
                "tokens",
                "sink_rate_percent",
                "mean_sink_strength",
                "last_token_attention_to_token_0",
                "token0_position_rank",
                "final_layer_drift",
                "error",
            ],
            labels={
                "model": "Model",
                "condition": "Condition",
                "prompt_count": "Prompts",
                "valid_prompt_count": "Valid",
                "tokens": "Mean tokens",
                "sink_rate_percent": "Sink rate (%)",
                "mean_sink_strength": "Mean sink strength",
                "last_token_attention_to_token_0": "Final-query → token 0",
                "token0_position_rank": "Token-0 rank",
                "final_layer_drift": "Final-layer drift",
                "error": "Errors",
            },
            decimals={
                "tokens": 1,
                "sink_rate_percent": 2,
                "mean_sink_strength": 3,
                "last_token_attention_to_token_0": 3,
                "token0_position_rank": 1,
                "final_layer_drift": 3,
            },
            wrapped_columns=["model", "error"],
            page_size=10,
            label="Cross-model evidence matrix",
        )
        _comparison_output = mo.vstack(
            [
                mo.md(
                    """
                    Read the rows as a controlled evidence matrix, not a
                    leaderboard. The paired conditions separate the model special
                    token from the first content position, while the model families
                    show where the pattern transfers. Each benchmark row averages
                    document-style prompt prefixes.
                    """
                ),
                _comparison_view,
            ],
            gap=1,
        )
    _comparison_output
    return


@app.cell(hide_code=True)
def _(
    clear_cached_model_bundle,
    CONTEXT_SWEEP_BUDGETS,
    MODEL_OPTIONS,
    context_sweep_button,
    context_sweep_model,
    hf_token,
    load_ephemeral_model_bundle,
    measure_context_sweep,
    pd,
    probe_config,
    release_model_memory,
    selected_precision_key,
    selected_prompt,
    sink_threshold,
    torch,
):
    if not context_sweep_button.value or pd is None:
        context_sweep_table = None
    else:
        clear_cached_model_bundle()
        _context_model_id = MODEL_OPTIONS[context_sweep_model.value]
        _context_prompt = probe_config.prompt if probe_config is not None else selected_prompt
        context_sweep_table = pd.DataFrame(
            measure_context_sweep(
                _context_model_id,
                _context_prompt,
                CONTEXT_SWEEP_BUDGETS,
                load_ephemeral_model_bundle,
                release_model_memory,
                selected_precision_key,
                hf_token,
                torch,
                sink_threshold.value,
            )
        )
        clear_cached_model_bundle()
    return (context_sweep_table,)


@app.cell(hide_code=True)
def _(context_sweep_table, format_result_table, mo):
    if context_sweep_table is None:
        _context_sweep_output = mo.md(
            "_Optional inference-context boundary test not run._"
        )
    else:
        _context_view = format_result_table(
            context_sweep_table,
            columns=[
                "model",
                "max_tokens",
                "actual_tokens",
                "sink_rate_percent",
                "mean_sink_strength",
                "last_token_attention_to_token_0",
                "token0_position_rank",
                "error",
            ],
            labels={
                "model": "Model",
                "max_tokens": "Token budget",
                "actual_tokens": "Actual tokens",
                "sink_rate_percent": "Sink rate (%)",
                "mean_sink_strength": "Mean sink strength",
                "last_token_attention_to_token_0": "Final-query → token 0",
                "token0_position_rank": "Token-0 rank",
                "error": "Error",
            },
            decimals={
                "sink_rate_percent": 2,
                "mean_sink_strength": 3,
                "last_token_attention_to_token_0": 3,
                "token0_position_rank": 1,
            },
            wrapped_columns=["model", "error"],
            page_size=10,
            label="Inference-context boundary test",
        )
        _context_sweep_output = mo.vstack(
            [
                _context_view,
                mo.md(
                    """
                    Read this as a distinction between training context and
                    inference context. A trend that differs from the paper's
                    training result is still useful evidence: it says the two
                    levers should not be conflated.
                    """
                ).callout(kind="success"),
            ],
            gap=0.75,
        )
    _context_sweep_output
    return


@app.cell(hide_code=True)
def _(TOKEN_BUDGET_OPTIONS, mo):
    dense_moe_prompt_set = mo.ui.dropdown(
        options=[
            "Current selected prompt",
            "Neutral mini-benchmark (4 prompts)",
            "Full neutral mini-benchmark (8 prompts)",
        ],
        value="Current selected prompt",
        label="Dense-vs-MoE prompt set",
        full_width=True,
    )
    dense_moe_token_budget = mo.ui.dropdown(
        options=list(TOKEN_BUDGET_OPTIONS.keys()),
        value="512 tokens",
        label="Dense-vs-MoE token budget",
        full_width=True,
    )
    dense_moe_measure_drift = mo.ui.checkbox(
        value=False,
        label="Also measure perturbation drift (slower; keeps hidden states)",
    )
    dense_moe_run_button = mo.ui.run_button(
        label="Run Gemma 4 dense-vs-MoE probe",
        kind="success",
        full_width=True,
    )
    return (
        dense_moe_measure_drift,
        dense_moe_prompt_set,
        dense_moe_run_button,
        dense_moe_token_budget,
    )


@app.cell(hide_code=True)
def _(
    dense_moe_measure_drift,
    dense_moe_prompt_set,
    dense_moe_run_button,
    dense_moe_token_budget,
    mo,
):
    mo.vstack(
        [
            mo.md(
                r"""
                ## 6. Research extension: Dense vs MoE

                This is the notebook's original research question. If two Gemma
                4 models share the same hybrid local/global attention design,
                but one routes tokens through sparse experts, does the
                first-token sink still behave the same way?

                We do not assume an answer. A similar profile suggests that the
                effect is primarily tied to attention and depth; a split profile
                suggests that sparse MLP routing changes the circuit.

                | Pre-registered interpretation | What we would observe |
                | --- | --- |
                | Attention/depth account | Dense and MoE models have similar sink rates and normalized-depth profiles. |
                | Routing-sensitive account | Their profiles diverge systematically, suggesting sparse MLP routing changes how the attention circuit is used. |

                | Model | Architecture | Parameters | Why this pair is clean |
                | --- | --- | ---: | --- |
                | `google/gemma-4-31B-it` | Dense | 30.7B active | Same Gemma 4 family and long-context hybrid attention design. |
                | `google/gemma-4-26B-A4B-it` | MoE | 25.2B total / 3.8B active | Sparse expert routing changes the MLP path while keeping the attention family comparable. |

                The comparison holds prompt set, precision, token budget, anchor
                condition, and sink threshold fixed. Because the models have
                different depths, layers are compared at normalized position

                $$
                \tau_{\ell}=\frac{\ell}{L-1}\in[0,1],
                $$

                and also grouped into early, middle, and late thirds. This is a
                controlled architecture comparison, not a causal intervention on
                expert routing.
                """
            ),
            mo.md(
                """
                The runner loads the dense model and MoE model one at a time,
                computes the same opportunity-normalized sink metric, and then
                reports both a headline rate and a normalized-depth profile.
                When the model config exposes layer types, local sliding-window
                and full global attention layers are also separated.
                """
            ).callout(kind="info"),
            mo.hstack(
                [dense_moe_prompt_set, dense_moe_token_budget],
                widths="equal",
                wrap=True,
                gap=1,
            ),
            dense_moe_measure_drift,
            dense_moe_run_button,
        ],
        gap=1,
    )
    return


@app.cell(hide_code=True)
def _(
    clear_cached_model_bundle,
    dense_moe_measure_drift,
    dense_moe_prompt_set,
    dense_moe_run_button,
    dense_moe_token_budget,
    GEMMA4_DENSE_MOE_MODELS,
    hf_token,
    load_ephemeral_model_bundle,
    measure_gemma4_dense_moe,
    NEUTRAL_BENCHMARK_PROMPTS,
    pd,
    probe_config,
    release_model_memory,
    selected_precision_key,
    selected_prompt,
    sink_threshold,
    summarize_dense_moe_layer_rows,
    summarize_dense_moe_rows,
    TOKEN_BUDGET_OPTIONS,
    torch,
):
    if not dense_moe_run_button.value or pd is None:
        gemma4_dense_moe_layer_table = None
        gemma4_dense_moe_raw_table = None
        gemma4_dense_moe_table = None
    else:
        clear_cached_model_bundle()
        if dense_moe_prompt_set.value == "Full neutral mini-benchmark (8 prompts)":
            _dense_moe_prompts = list(NEUTRAL_BENCHMARK_PROMPTS)
        elif dense_moe_prompt_set.value == "Neutral mini-benchmark (4 prompts)":
            _dense_moe_prompts = list(NEUTRAL_BENCHMARK_PROMPTS[:4])
        else:
            _dense_moe_selected_prompt = (
                probe_config.prompt if probe_config is not None else selected_prompt
            )
            _dense_moe_prompts = [_dense_moe_selected_prompt]

        _dense_moe_metric_rows, _dense_moe_layer_rows = measure_gemma4_dense_moe(
            GEMMA4_DENSE_MOE_MODELS,
            _dense_moe_prompts,
            load_ephemeral_model_bundle,
            release_model_memory,
            selected_precision_key,
            hf_token,
            torch,
            int(TOKEN_BUDGET_OPTIONS[dense_moe_token_budget.value]),
            sink_threshold.value,
            measure_drift=bool(dense_moe_measure_drift.value),
        )
        gemma4_dense_moe_raw_table = pd.DataFrame(_dense_moe_metric_rows)
        gemma4_dense_moe_table = pd.DataFrame(
            summarize_dense_moe_rows(_dense_moe_metric_rows, pd)
        )
        gemma4_dense_moe_layer_table = pd.DataFrame(
            summarize_dense_moe_layer_rows(_dense_moe_layer_rows, pd)
        )
        clear_cached_model_bundle()
    return (
        gemma4_dense_moe_layer_table,
        gemma4_dense_moe_raw_table,
        gemma4_dense_moe_table,
    )


@app.cell(hide_code=True)
def _(
    format_result_table,
    gemma4_dense_moe_layer_table,
    gemma4_dense_moe_raw_table,
    gemma4_dense_moe_table,
    mo,
    plot_dense_moe_attention_type,
    plot_dense_moe_depth_profile,
    plot_dense_moe_sink_bars,
):
    if gemma4_dense_moe_table is None:
        _dense_moe_output = mo.md(
            "_Optional Gemma 4 architecture extension not run. Begin with the one-prompt setting before expanding the benchmark._"
        )
    else:
        _dense_moe_sink_fig = plot_dense_moe_sink_bars(gemma4_dense_moe_table)
        _dense_moe_depth_fig = plot_dense_moe_depth_profile(gemma4_dense_moe_layer_table)
        _dense_moe_type_fig = plot_dense_moe_attention_type(gemma4_dense_moe_layer_table)
        _dense_moe_error_table = None
        if gemma4_dense_moe_raw_table is not None and "error" in gemma4_dense_moe_raw_table.columns:
            _dense_moe_errors = gemma4_dense_moe_raw_table[
                gemma4_dense_moe_raw_table["error"].fillna("") != ""
            ]
            if len(_dense_moe_errors) > 0:
                _dense_moe_error_view = format_result_table(
                    _dense_moe_errors,
                    columns=[
                        "model_label",
                        "architecture",
                        "condition",
                        "prompt_index",
                        "error",
                    ],
                    labels={
                        "model_label": "Model",
                        "architecture": "Architecture",
                        "condition": "Condition",
                        "prompt_index": "Prompt",
                        "error": "Error",
                    },
                    wrapped_columns=["model_label", "error"],
                    page_size=10,
                    label="Dense-vs-MoE error details",
                )
                _dense_moe_error_table = mo.vstack(
                    [
                        mo.md("Some prompt/model rows failed; successful rows are still summarized below.").callout(kind="warn"),
                        _dense_moe_error_view,
                    ],
                    gap=0.75,
                )

        _valid_summary = gemma4_dense_moe_table.copy()
        if "valid_prompt_count" in _valid_summary.columns:
            _valid_summary = _valid_summary[
                _valid_summary["valid_prompt_count"].fillna(0) > 0
            ]

        def _condition_value(_architecture, _condition):
            _match = _valid_summary[
                (_valid_summary["architecture"] == _architecture)
                & (_valid_summary["condition"] == _condition)
            ]
            if len(_match) == 0 or _match["sink_rate_percent"].isna().all():
                return None
            return float(_match.iloc[0]["sink_rate_percent"])

        _dense_plain = _condition_value("dense", "plain prompt")
        _dense_anchor = _condition_value("dense", "with model first-token anchor")
        _moe_plain = _condition_value("moe", "plain prompt")
        _moe_anchor = _condition_value("moe", "with model first-token anchor")
        if all(
            _value is not None
            for _value in [_dense_plain, _dense_anchor, _moe_plain, _moe_anchor]
        ):
            _result_summary = mo.md(
                f"""
                **Result at a glance.** Adding the first-token anchor changes the
                sink rate by **{_dense_anchor - _dense_plain:+.1f} percentage
                points** in the Dense model and **{_moe_anchor - _moe_plain:+.1f}
                points** in the MoE model. The Dense–MoE gap is
                **{abs(_dense_anchor - _moe_anchor):.1f} points** with the anchor
                and **{abs(_dense_plain - _moe_plain):.1f} points** without it.

                The headline rates answer whether the effect survives sparse
                routing; the depth and layer-type plots show where any remaining
                architectural difference lives.
                """
            ).callout(kind="info")
        else:
            _result_summary = mo.md(
                "The comparison is partial. Plots include every aggregate with at least one valid prompt; inspect the error details before drawing a conclusion."
            ).callout(kind="warn")

        _dense_moe_views = [_result_summary]
        if _dense_moe_sink_fig is not None:
            _dense_moe_views.append(_dense_moe_sink_fig)
        if _dense_moe_depth_fig is not None:
            _dense_moe_views.append(_dense_moe_depth_fig)
        if _dense_moe_type_fig is not None:
            _dense_moe_views.append(_dense_moe_type_fig)
        if _dense_moe_error_table is not None:
            _dense_moe_views.append(_dense_moe_error_table)

        _summary_table_view = format_result_table(
            gemma4_dense_moe_table,
            columns=[
                "model_label",
                "architecture",
                "condition",
                "prompt_count",
                "valid_prompt_count",
                "tokens",
                "layer_count",
                "head_count",
                "sink_rate_percent",
                "sink_rate_std",
                "mean_sink_strength",
                "last_token_attention_to_token_0",
                "token0_position_rank",
                "final_layer_drift",
                "error",
            ],
            labels={
                "model_label": "Model",
                "architecture": "Architecture",
                "condition": "Condition",
                "prompt_count": "Prompts",
                "valid_prompt_count": "Valid",
                "tokens": "Mean tokens",
                "layer_count": "Layers",
                "head_count": "Heads",
                "sink_rate_percent": "Sink rate (%)",
                "sink_rate_std": "Prompt SD (pp)",
                "mean_sink_strength": "Mean sink strength",
                "last_token_attention_to_token_0": "Final-query → token 0",
                "token0_position_rank": "Token-0 rank",
                "final_layer_drift": "Final-layer drift",
                "error": "Errors",
            },
            decimals={
                "tokens": 1,
                "layer_count": 0,
                "head_count": 0,
                "sink_rate_percent": 2,
                "sink_rate_std": 2,
                "mean_sink_strength": 3,
                "last_token_attention_to_token_0": 3,
                "token0_position_rank": 1,
                "final_layer_drift": 3,
            },
            wrapped_columns=["model_label", "error"],
            page_size=10,
            label="Dense-vs-MoE summary metrics",
        )
        _detail_sections = {"Summary metrics": _summary_table_view}
        if gemma4_dense_moe_layer_table is not None and len(gemma4_dense_moe_layer_table) > 0:
            _detail_sections["Layer and attention-type breakdown"] = format_result_table(
                gemma4_dense_moe_layer_table,
                columns=[
                    "model_label",
                    "architecture",
                    "condition",
                    "layer_group",
                    "layer_count",
                    "sink_rate_percent",
                    "sink_rate_std",
                    "mean_sink_strength",
                    "valid_prompt_count",
                    "error",
                ],
                labels={
                    "model_label": "Model",
                    "architecture": "Architecture",
                    "condition": "Condition",
                    "layer_group": "Layer group",
                    "layer_count": "Layers",
                    "sink_rate_percent": "Sink rate (%)",
                    "sink_rate_std": "Prompt SD (pp)",
                    "mean_sink_strength": "Mean sink strength",
                    "valid_prompt_count": "Valid prompts",
                    "error": "Errors",
                },
                decimals={
                    "layer_count": 0,
                    "sink_rate_percent": 2,
                    "sink_rate_std": 2,
                    "mean_sink_strength": 3,
                },
                wrapped_columns=["model_label", "error"],
                page_size=12,
                label="Layer and attention-type breakdown",
            )
        if gemma4_dense_moe_raw_table is not None and len(gemma4_dense_moe_raw_table) > 0:
            _detail_sections["Raw prompt-level rows"] = format_result_table(
                gemma4_dense_moe_raw_table,
                columns=[
                    "model_label",
                    "architecture",
                    "condition",
                    "prompt_index",
                    "tokens",
                    "sink_rate_percent",
                    "mean_sink_strength",
                    "last_token_attention_to_token_0",
                    "token0_position_rank",
                    "final_layer_drift",
                    "error",
                ],
                labels={
                    "model_label": "Model",
                    "architecture": "Architecture",
                    "condition": "Condition",
                    "prompt_index": "Prompt",
                    "tokens": "Tokens",
                    "sink_rate_percent": "Sink rate (%)",
                    "mean_sink_strength": "Mean sink strength",
                    "last_token_attention_to_token_0": "Final-query → token 0",
                    "token0_position_rank": "Token-0 rank",
                    "final_layer_drift": "Final-layer drift",
                    "error": "Error",
                },
                decimals={
                    "sink_rate_percent": 2,
                    "mean_sink_strength": 3,
                    "last_token_attention_to_token_0": 3,
                    "final_layer_drift": 3,
                },
                wrapped_columns=["model_label", "error"],
                page_size=12,
                label="Raw prompt-level rows",
            )
        _dense_moe_views.append(mo.accordion(_detail_sections))
        _dense_moe_output = mo.vstack(_dense_moe_views, gap=1)
    _dense_moe_output
    return


@app.cell
def _(mo):
    mo.vstack(
        [
            mo.md(
                """
                ## 7. Takeaway

                Treat attention maps as possible **control flow**, not only
                semantic lookup. A token with little surface meaning can still
                be infrastructure the model uses to regulate information flow.
                """
            ),
            mo.Html(
                """
                <style>
                  #sink-takeaway {
                    background: linear-gradient(140deg, #f8fbff 0%, #ffffff 52%, #f2fbf6 100%);
                    border: 1px solid #d8e2ee;
                    border-radius: 12px;
                    color: #172033;
                    overflow: hidden;
                  }
                  #sink-takeaway .takeaway-grid {
                    display: grid;
                    gap: 0;
                    grid-template-columns: repeat(3, minmax(0, 1fr));
                  }
                  #sink-takeaway article {
                    border-right: 1px solid #dfe7f0;
                    min-height: 190px;
                    padding: 20px;
                  }
                  #sink-takeaway article:last-child { border-right: 0; }
                  #sink-takeaway .takeaway-number {
                    align-items: center;
                    background: #e8f1ff;
                    border-radius: 50%;
                    color: #1d4ed8;
                    display: inline-flex;
                    font-size: 0.76rem;
                    font-weight: 800;
                    height: 28px;
                    justify-content: center;
                    margin-bottom: 11px;
                    width: 28px;
                  }
                  #sink-takeaway h3 {
                    color: #172033;
                    font-size: 1rem;
                    line-height: 1.3;
                    margin: 0 0 8px;
                  }
                  #sink-takeaway p {
                    color: #475569;
                    font-size: 0.9rem;
                    line-height: 1.52;
                    margin: 0;
                  }
                  #sink-takeaway .takeaway-limit {
                    background: #f8fafc;
                    border-top: 1px solid #dfe7f0;
                    color: #526174;
                    font-size: 0.82rem;
                    line-height: 1.5;
                    padding: 13px 20px;
                  }
                  @media (max-width: 700px) {
                    #sink-takeaway .takeaway-grid { grid-template-columns: 1fr; }
                    #sink-takeaway article {
                      border-bottom: 1px solid #dfe7f0;
                      border-right: 0;
                      min-height: 0;
                    }
                    #sink-takeaway article:last-child { border-bottom: 0; }
                  }
                </style>
                <section id="sink-takeaway" aria-label="Notebook conclusions">
                  <div class="takeaway-grid">
                    <article>
                      <span class="takeaway-number" aria-hidden="true">1</span>
                      <h3>Paper claim</h3>
                      <p>First-token sinks can give attention heads a low-information routing target, approximating a no-op and limiting destructive mixing through depth.</p>
                    </article>
                    <article>
                      <span class="takeaway-number" aria-hidden="true">2</span>
                      <h3>What we reproduce and replicate</h3>
                      <p>LLaMA supplies the direct paper-family probe. Gemma 2 applies the same anchor and perturbation protocol as a replication-style transfer test.</p>
                    </article>
                    <article>
                      <span class="takeaway-number" aria-hidden="true">3</span>
                      <h3>What this notebook adds</h3>
                      <p>The inference-context sweep separates a boundary condition from the paper's training result, while Gemma 4 asks whether sparse MoE routing changes the sink profile.</p>
                    </article>
                  </div>
                  <div class="takeaway-limit"><strong>Limits.</strong> The inference-context sweep does not reproduce training-context experiments, and the Sink Switch visualizes attention redistribution without patching a model forward pass.</div>
                </section>
                """
            ),
        ],
        gap=0.75,
    )
    return


if __name__ == "__main__":
    app.run()
