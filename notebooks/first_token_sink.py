import marimo

__generated_with = "0.23.13"
app = marimo.App(width="full")


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell
def _(mo):
    mo.md("""
    # The first token is a circuit breaker

    Large language models often pour attention into the first token. At first
    glance, that looks like wasted computation.

    The paper's sharper claim is more interesting:

    **the first token can act like a low-information circuit breaker that helps
    deep Transformers avoid over-mixing.**

    The notebook starts with the paper's evidence, then turns the claim into a
    live experiment: change the prompt, remove or add the first-position anchor,
    inspect attention heads, and compare whether the effect survives in another
    model family.
    """)
    return


@app.cell
def _():
    dependency_error = None
    np = None
    pd = None
    plt = None
    torch = None
    AutoModelForCausalLM = None
    AutoTokenizer = None

    try:
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
        np,
        pd,
        plt,
        torch,
    )


@app.cell
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


@app.cell
def _():
    PAPER_URL = "https://arxiv.org/abs/2504.02732"
    ALPHAXIV_URL = "https://www.alphaxiv.org/abs/2504.02732"

    MODEL_OPTIONS = {
        "tiny-gpt2 - fastest sanity check": "sshleifer/tiny-gpt2",
        "distilgpt2 - good interactive default": "distilgpt2",
        "gpt2 - stronger small model": "gpt2",
        "gpt2-medium - better GPU demo": "openai-community/gpt2-medium",
        "Qwen2.5 0.5B - open external generalization": "Qwen/Qwen2.5-0.5B",
        "Qwen2.5 1.5B - GPU external generalization": "Qwen/Qwen2.5-1.5B",
        "Gemma 2 2B - paper-family stretch": "google/gemma-2-2b",
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
    return ALPHAXIV_URL, ANCHOR_MODES, MODEL_OPTIONS, PAPER_URL, PROMPT_PRESETS


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

    This notebook reproduces the shape of the Gemma perturbation experiment on
    smaller accessible models, then asks a shareable question: **does the same
    sink-as-circuit-breaker story generalize outside the paper's model families?**

    Links: [alphaXiv]({ALPHAXIV_URL}) | [arXiv]({PAPER_URL})
    """)
    return


@app.cell
def _(ANCHOR_MODES, MODEL_OPTIONS, PROMPT_PRESETS, mo):
    model_choice = mo.ui.dropdown(
        options=list(MODEL_OPTIONS.keys()),
        value="distilgpt2 - good interactive default",
        label="Model",
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
        start=16,
        stop=128,
        step=16,
        value=64,
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
            mo.hstack([model_choice, anchor_mode], widths="equal", gap=1),
            mo.hstack([prompt_preset, max_tokens, sink_threshold], widths="equal", gap=1),
            custom_prompt,
        ],
        gap=1,
    )
    return (
        anchor_mode,
        custom_prompt,
        max_tokens,
        model_choice,
        prompt_preset,
        sink_threshold,
    )


@app.cell
def _(PROMPT_PRESETS, custom_prompt, prompt_preset):
    selected_preset_name = prompt_preset.value or "Paper-style greeting"
    selected_prompt = custom_prompt.value.strip() or PROMPT_PRESETS[selected_preset_name]
    return selected_preset_name, selected_prompt


@app.cell
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

    return anchored_prompt, clean_token, decode_token, perturb_prompt


@app.cell
def _(AutoModelForCausalLM, AutoTokenizer, dependency_error, torch):
    from functools import lru_cache

    @lru_cache(maxsize=8)
    def load_model_bundle(model_id):
        if dependency_error is not None:
            return None, None, None, dependency_error

        device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        try:
            tokenizer = AutoTokenizer.from_pretrained(model_id)
            if tokenizer.pad_token is None:
                tokenizer.pad_token = tokenizer.eos_token

            try:
                model = AutoModelForCausalLM.from_pretrained(
                    model_id,
                    attn_implementation="eager",
                )
            except TypeError:
                model = AutoModelForCausalLM.from_pretrained(model_id)

            model.to(device)
            model.eval()
            return tokenizer, model, device, None
        except Exception as exc:  # noqa: BLE001 - show model load failures in UI.
            return None, None, None, exc

    return (load_model_bundle,)


@app.cell
def _(MODEL_OPTIONS, load_model_bundle, model_choice):
    selected_model_id = MODEL_OPTIONS[model_choice.value]
    tokenizer, model, device, model_error = load_model_bundle(selected_model_id)
    return device, model, model_error, selected_model_id, tokenizer


@app.cell
def _(device, mo, model_error, selected_model_id, torch):
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

            {cuda_line}
            """
        ).callout(kind="info")
    return


@app.cell
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


@app.cell
def _(anchor_mode, anchored_prompt, selected_prompt, tokenizer):
    analysis_prompt, anchor_note = anchored_prompt(
        selected_prompt,
        anchor_mode.value,
        tokenizer,
    )
    return analysis_prompt, anchor_note


@app.cell
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


@app.cell
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

        with torch.no_grad():
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


@app.cell
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


@app.cell
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


@app.cell
def _(pd, probe, sink_threshold, torch):
    if probe is None:
        sink_scores = None
        sink_rate = 0.0
        sink_table = pd.DataFrame() if pd is not None else None
    else:
        attention = probe["attention"]
        if attention.shape[-1] <= 1:
            sink_scores = torch.zeros(attention.shape[0], attention.shape[1])
        else:
            sink_scores = attention[:, :, 1:, 0].mean(dim=-1)

        strong_sink_mask = sink_scores > float(sink_threshold.value)
        sink_rate = float(strong_sink_mask.float().mean().item() * 100.0)

        _rows = []
        for _layer in range(sink_scores.shape[0]):
            for _head in range(sink_scores.shape[1]):
                _rows.append(
                    {
                        "layer": _layer,
                        "head": _head,
                        "mean_attention_to_first_token": float(sink_scores[_layer, _head]),
                        "strong_sink": bool(strong_sink_mask[_layer, _head]),
                    }
                )
        sink_table = pd.DataFrame(_rows).sort_values(
            "mean_attention_to_first_token",
            ascending=False,
        )
    return sink_rate, sink_scores, sink_table


@app.cell
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


@app.cell
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


@app.cell
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


@app.cell
def _(plot_sink_map, sink_scores, sink_threshold):
    if sink_scores is None:
        sink_map_fig = None
    else:
        sink_map_fig = plot_sink_map(sink_scores, float(sink_threshold.value))

    sink_map_fig
    return


@app.cell
def _(mo, sink_table):
    strongest_sink_heads = sink_table.head(12) if sink_table is not None else None
    mo.vstack([mo.md("## 5. Strongest sink heads"), strongest_sink_heads])
    return


@app.cell
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


@app.cell
def _(mo, perturbed_prompt):
    mo.md(f"""
    ## 6. Perturbation probe

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


@app.cell
def _(perturb_error, perturbed_probe, plot_hidden_delta, probe, torch):
    if probe is None or perturbed_probe is None or perturb_error is not None:
        hidden_delta = None
        hidden_delta_fig = None
    else:
        _layers = min(probe["hidden"].shape[0], perturbed_probe["hidden"].shape[0])
        _token_count = min(probe["hidden"].shape[1], perturbed_probe["hidden"].shape[1])
        hidden_delta = torch.linalg.vector_norm(
            probe["hidden"][:_layers, :_token_count, :]
            - perturbed_probe["hidden"][:_layers, :_token_count, :],
            dim=-1,
        )
        hidden_delta_fig = plot_hidden_delta(hidden_delta, probe["tokens"][:_token_count])

    hidden_delta_fig
    return (hidden_delta,)


@app.cell
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


@app.cell
def _(MODEL_OPTIONS, mo):
    comparison_run_mode = mo.ui.dropdown(
        options=[
            "Skip expensive model comparison",
            "Run two-model comparison",
        ],
        value="Skip expensive model comparison",
        label="Generalization lab",
        full_width=True,
    )
    comparison_model_a = mo.ui.dropdown(
        options=list(MODEL_OPTIONS.keys()),
        value="distilgpt2 - good interactive default",
        label="Reference model",
        full_width=True,
    )
    comparison_model_b = mo.ui.dropdown(
        options=list(MODEL_OPTIONS.keys()),
        value="Qwen2.5 0.5B - open external generalization",
        label="Generalization model",
        full_width=True,
    )
    comparison_token_budget = mo.ui.slider(
        start=16,
        stop=96,
        step=16,
        value=48,
        show_value=True,
        label="Comparison token budget",
        full_width=True,
    )

    mo.vstack(
        [
            mo.md(
                """
                ## 7. Does the story generalize?

                The paper's headline empirical examples use Gemma 7B and the
                LLaMA 3.1 family. A stronger notebook should not stop there. This
                optional lab checks whether the same first-position effect appears
                in a second accessible model family.

                Qwen is included as an external generalization target, not as a
                model claimed by the paper.
                """
            ),
            mo.hstack([comparison_run_mode, comparison_token_budget], widths="equal", gap=1),
            mo.hstack([comparison_model_a, comparison_model_b], widths="equal", gap=1),
        ],
        gap=1,
    )
    return (
        comparison_model_a,
        comparison_model_b,
        comparison_run_mode,
        comparison_token_budget,
    )


@app.cell
def _(anchored_prompt, perturb_prompt, run_attention_probe):
    def measure_anchor_effect(
        model_id,
        base_prompt,
        load_model_bundle,
        torch,
        max_length,
        sink_threshold,
    ):
        _tokenizer, _model, _device, _model_error = load_model_bundle(model_id)
        if _model_error is not None or _model is None:
            return [
                {
                    "model": model_id,
                    "condition": "load failed",
                    "sink_rate_percent": None,
                    "mean_sink_strength": None,
                    "final_layer_drift": None,
                    "error": str(_model_error),
                }
            ]

        _comparison_rows = []
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

            _attention = _base_probe["attention"]
            if _attention.shape[-1] <= 1:
                _condition_sink_scores = torch.zeros(
                    _attention.shape[0],
                    _attention.shape[1],
                )
            else:
                _condition_sink_scores = _attention[:, :, 1:, 0].mean(dim=-1)

            _strong_sink_rate = float(
                (_condition_sink_scores > float(sink_threshold)).float().mean().item()
                * 100.0
            )
            _mean_sink_strength = float(_condition_sink_scores.mean().item())

            _layer_count = min(
                _base_probe["hidden"].shape[0],
                _perturbed_probe["hidden"].shape[0],
            )
            _token_count = min(
                _base_probe["hidden"].shape[1],
                _perturbed_probe["hidden"].shape[1],
            )
            _delta = torch.linalg.vector_norm(
                _base_probe["hidden"][:_layer_count, :_token_count, :]
                - _perturbed_probe["hidden"][:_layer_count, :_token_count, :],
                dim=-1,
            )
            _final_layer_drift = float(_delta[-1].mean().item())

            _comparison_rows.append(
                {
                    "model": model_id,
                    "condition": _condition,
                    "sink_rate_percent": _strong_sink_rate,
                    "mean_sink_strength": _mean_sink_strength,
                    "final_layer_drift": _final_layer_drift,
                    "error": "",
                }
            )

        return _comparison_rows

    return (measure_anchor_effect,)


@app.cell
def _(
    MODEL_OPTIONS,
    comparison_model_a,
    comparison_model_b,
    comparison_run_mode,
    comparison_token_budget,
    load_model_bundle,
    measure_anchor_effect,
    pd,
    selected_prompt,
    sink_threshold,
    torch,
):
    if comparison_run_mode.value == "Skip expensive model comparison" or pd is None:
        comparison_table = None
    else:
        _comparison_rows = []
        _comparison_model_ids = []
        for _model_label in [comparison_model_a.value, comparison_model_b.value]:
            _model_id = MODEL_OPTIONS[_model_label]
            if _model_id not in _comparison_model_ids:
                _comparison_model_ids.append(_model_id)

        for _model_id in _comparison_model_ids:
            _comparison_rows.extend(
                measure_anchor_effect(
                    _model_id,
                    selected_prompt,
                    load_model_bundle,
                    torch,
                    comparison_token_budget.value,
                    sink_threshold.value,
                )
            )
        comparison_table = pd.DataFrame(_comparison_rows)
    return (comparison_table,)


@app.cell
def _(comparison_table, mo):
    if comparison_table is None:
        _comparison_output = mo.md(
            """
            The comparison lab is skipped by default because it can load multiple
            models. Enable it for the final GPU demo or when recording the
            submission video.
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


@app.cell
def _(mo, probe):
    next_token_output = probe["next_tokens"] if probe is not None else None
    mo.vstack([mo.md("## 8. Next-token distribution"), next_token_output])
    return


@app.cell
def _(mo):
    mo.md("""
    ## Shareable notebook arc

    The final version should feel like a short investigation:

    1. A surprising visual: many heads attend to the first token.
    2. The paper's explanation: the sink can act as an approximate no-op.
    3. A reproduction: perturbation spreads more when the first-token anchor is absent.
    4. A generalization check: try a second model family such as Qwen.
    5. A practical takeaway: attention sinks matter for long context, streaming,
       quantization, and robustness.

    That arc is designed for the rubric's shareability clause: a viewer should
    leave with one memorable mechanism and a reason to open the original paper.
    """)
    return


if __name__ == "__main__":
    app.run()
