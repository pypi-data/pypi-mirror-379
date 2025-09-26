from __future__ import annotations

from dataclasses import asdict, field
from datetime import datetime
from typing import Dict, List, Optional

import os
import json

from ._compat import dataclass

DEFAULT_COUNT = 3
DEFAULT_PROVIDER = os.environ.get("IMAGEMCP_DEFAULT_PROVIDER", "openrouter")
_ENV_DEFAULT_MODEL = os.environ.get("IMAGEMCP_DEFAULT_MODEL")
_OPENROUTER_MODEL = os.environ.get(
    "IMAGEMCP_OPENROUTER_MODEL", "google/gemini-2.5-flash-image-preview"
)
_GOOGLE_MODEL = os.environ.get("IMAGEMCP_GOOGLE_MODEL", "gemini-2.5-flash-image-preview")


def _default_model_for_provider(provider: str) -> str:
    if _ENV_DEFAULT_MODEL:
        return _ENV_DEFAULT_MODEL
    if provider == "openrouter":
        return _OPENROUTER_MODEL
    if provider == "google":
        return _GOOGLE_MODEL
    return _OPENROUTER_MODEL


@dataclass()
class PlanConstraints:
    width: Optional[int] = None
    height: Optional[int] = None
    size: Optional[str] = None
    aspectRatio: Optional[str] = None
    seed: Optional[int] = None
    provider: Optional[str] = None
    model: Optional[str] = None
    providerOptions: Dict[str, object] = field(default_factory=dict)
    guidance: Optional[str] = None
    mood: Optional[str] = None
    palette: Optional[str] = None


@dataclass()
class PlanPayload:
    slot: str
    requestText: str
    constraints: PlanConstraints = field(default_factory=PlanConstraints)
    count: int = DEFAULT_COUNT
    provider: Optional[str] = None
    model: Optional[str] = None
    projectRoot: Optional[str] = None


@dataclass()
class KnownContext:
    slot: Optional[str] = None
    constraints: Optional[PlanConstraints] = None
    projectRoot: Optional[str] = None


@dataclass()
class CollectContextPayload:
    requestText: Optional[str] = ""
    known: KnownContext = field(default_factory=KnownContext)


@dataclass()
class PlanInput:
    slot: str
    request_text: str
    constraints: Dict[str, object]
    count: int = DEFAULT_COUNT
    project_root: Optional[str] = None

    @classmethod
    def from_payload(cls, payload: PlanPayload) -> "PlanInput":
        constraints = _constraints_to_dict(payload.constraints)
        if payload.provider and "provider" not in constraints:
            constraints["provider"] = payload.provider
        if payload.model and "model" not in constraints:
            constraints["model"] = payload.model
        return cls(
            slot=payload.slot,
            request_text=payload.requestText,
            constraints=constraints,
            count=payload.count or DEFAULT_COUNT,
            project_root=payload.projectRoot,
        )


def collect_context_questions(payload: CollectContextPayload) -> Dict[str, object]:
    known = payload.known or KnownContext()
    constraints = known.constraints
    missing = []
    if not known.slot:
        missing.append(
            {
                "field": "slot",
                "prompt": "Which slot should these variations update? (e.g. hero, testimonial-slot-1)",
                "type": "string",
            }
        )
    if constraints is None:
        missing.append(
            {
                "field": "constraints",
                "prompt": "Any size or aspect requirements? Provide width/height in px or aspect ratio (e.g. 16:9).",
                "type": "object",
            }
        )
    if not known.projectRoot:
        missing.append(
            {
                "field": "projectRoot",
                "prompt": "Absolute path to the project root (where .imagemcp/config.json lives).",
                "type": "string",
            }
        )
    defaults = {
        "count": DEFAULT_COUNT,
        "projectRoot": known.projectRoot or ".",
        "provider": DEFAULT_PROVIDER,
        "model": _default_model_for_provider(DEFAULT_PROVIDER),
    }
    notes = [
        "Gather either an explicit size (e.g. 1024x1024) or an aspect ratio (e.g. 16:9); the planner will reject requests without geometry so the CLI receives clear instructions.",
        "The CLI promotes variant #0 immediately so previews update right away; other picks are available via the gallery server.",
        "Seeds are optional and provider-specific. Include one for reproducibility when the provider supports it.",
    ]
    notes.extend(_geometry_hint_notes(constraints))
    return {"missing": missing, "defaults": defaults, "notes": notes}


def plan_image_job(payload: PlanPayload) -> Dict[str, object]:
    plan_input = PlanInput.from_payload(payload)
    if not plan_input.slot:
        raise ValueError("'slot' is required")
    count = max(1, plan_input.count)
    size, aspect_ratio, warnings = _derive_geometry(plan_input.constraints)
    if size is None and aspect_ratio is None:
        raise ValueError("Provide either an explicit size or an aspect ratio before planning.")
    provider = str(plan_input.constraints.get("provider") or DEFAULT_PROVIDER)
    model = str(plan_input.constraints.get("model") or _default_model_for_provider(provider))
    seed = plan_input.constraints.get("seed")
    project_root = plan_input.project_root or "."
    init_note = (
        "If this is your first run, the CLI will auto-initialize the project at {project_root}."
    ).format(project_root=project_root)

    prompt = _build_prompt(plan_input.slot, plan_input.request_text, plan_input.constraints)
    stdin_payload = {
        "prompt": prompt,
        "requestText": plan_input.request_text,
        "providerOptions": plan_input.constraints.get("providerOptions", {}),
        "provider": provider,
        "model": model,
    }
    if seed is not None:
        stdin_payload["seed"] = seed
    if size:
        stdin_payload["size"] = size
    if aspect_ratio:
        stdin_payload["aspectRatio"] = aspect_ratio
    output = {
        "plan": {
            "prompt": prompt,
            "n": count,
            "size": size,
            "aspectRatio": aspect_ratio,
            "seed": seed,
            "provider": provider,
            "model": model,
            "providerOptions": plan_input.constraints.get("providerOptions", {}),
            "constraints": plan_input.constraints,
        },
        "cli": {
            "command": _build_cli_command(
                plan_input.slot,
                project_root,
                count,
                size,
                aspect_ratio,
                provider,
                model,
                prompt,
            ),
            "stdin": stdin_payload,
            "projectRoot": project_root,
        },
        "sessionHint": f"{plan_input.slot}-{datetime.utcnow().strftime('%Y%m%d')}",
        "costEstimate": {
            "unit": "image-variant",
            "quantity": count,
            "estimatedCredits": count * 1.0,
        },
        "project": {
            "projectRoot": project_root,
        },
        "notes": warnings + [init_note],
    }
    return output


def _derive_geometry(constraints: Dict[str, object]) -> tuple[Optional[str], Optional[str], List[str]]:
    size: Optional[str] = None
    aspect_ratio: Optional[str] = None
    warnings: List[str] = []
    explicit_size = constraints.get("size")
    width = constraints.get("width")
    height = constraints.get("height")
    aspect = constraints.get("aspectRatio")

    if explicit_size:
        size = str(explicit_size)
    elif width is not None or height is not None:
        if width is None or height is None:
            warnings.append("Both width and height are required to form an explicit size.")
        else:
            try:
                size = f"{int(width)}x{int(height)}"
            except (TypeError, ValueError):
                warnings.append("Width/height constraints must be integers; omit or correct them before planning.")
    if size is None and aspect:
        aspect_ratio = str(aspect)
    if size and aspect:
        warnings.append("Both explicit size and aspect provided; using explicit size per policy.")
    if size is None and aspect_ratio is None:
        warnings.append("No geometry provided; supply size or aspect ratio to control generation.")
    return size, aspect_ratio, warnings


def _constraints_to_dict(constraints: PlanConstraints) -> Dict[str, object]:
    data = asdict(constraints)
    return {k: v for k, v in data.items() if v not in (None, {}, [])}


def _geometry_hint_notes(constraints: Optional[PlanConstraints]) -> List[str]:
    if not constraints:
        return []
    notes: List[str] = []
    if constraints.width and constraints.height:
        notes.append(f"Known geometry: {constraints.width}x{constraints.height} pixels.")
    elif constraints.aspectRatio:
        notes.append(f"Known aspect ratio: {constraints.aspectRatio}.")
    return notes


def normalize_plan_payload(payload: PlanPayload | Dict[str, object] | str) -> PlanPayload:
    if isinstance(payload, PlanPayload):
        return payload
    if isinstance(payload, str):
        try:
            payload = json.loads(payload)
        except json.JSONDecodeError as exc:
            raise ValueError("Payload must be a JSON object.") from exc
    if not isinstance(payload, dict):
        raise ValueError("Payload must be a JSON object.")
    constraints_data = payload.get("constraints") or {}
    if isinstance(constraints_data, str):
        constraints_data = json.loads(constraints_data)
    constraints = PlanConstraints(**constraints_data)
    count_raw = payload.get("count", DEFAULT_COUNT)
    try:
        count_value = int(count_raw)
    except (TypeError, ValueError):
        count_value = DEFAULT_COUNT
    return PlanPayload(
        slot=str(payload.get("slot", "")),
        requestText=str(payload.get("requestText", "")),
        constraints=constraints,
        count=count_value,
        provider=payload.get("provider"),
        model=payload.get("model"),
    )


def normalize_collect_context_payload(
    payload: CollectContextPayload | Dict[str, object] | str,
) -> CollectContextPayload:
    if isinstance(payload, CollectContextPayload):
        return payload
    if isinstance(payload, str):
        try:
            payload = json.loads(payload)
        except json.JSONDecodeError as exc:
            raise ValueError("Payload must be a JSON object.") from exc
    if not isinstance(payload, dict):
        raise ValueError("Payload must be a JSON object.")
    known_data = payload.get("known") or {}
    if isinstance(known_data, str):
        known_data = json.loads(known_data)
    constraints_data = known_data.get("constraints") or {}
    if isinstance(constraints_data, str):
        constraints_data = json.loads(constraints_data)
    known = KnownContext(
        slot=known_data.get("slot"),
        constraints=PlanConstraints(**constraints_data) if constraints_data else None,
        projectRoot=known_data.get("projectRoot"),
    )
    return CollectContextPayload(
        requestText=payload.get("requestText"),
        known=known,
    )


__all__ = [
    "CollectContextPayload",
    "PlanConstraints",
    "PlanPayload",
    "collect_context_questions",
    "plan_image_job",
    "normalize_plan_payload",
    "normalize_collect_context_payload",
]


def _build_prompt(slot: str, request_text: str, constraints: Dict[str, object]) -> str:
    guidance = constraints.get("guidance")
    description = request_text or f"Generate {DEFAULT_COUNT} fresh variants"
    base = description.strip()
    pieces = [base, f"Slot: {slot}"]
    if guidance:
        pieces.append(f"Guidance: {guidance}")
    mood = constraints.get("mood")
    if mood:
        pieces.append(f"Mood: {mood}")
    palette = constraints.get("palette")
    if palette:
        pieces.append(f"Palette: {palette}")
    return " | ".join(pieces)


def _build_cli_command(
    slot: str,
    project_root: Optional[str],
    count: int,
    size: Optional[str],
    aspect_ratio: Optional[str],
    provider: str,
    model: str,
    prompt: str,
) -> List[str]:
    command: List[str] = ["imgen"]
    if project_root and project_root != ".":
        command.extend(["--project-root", str(project_root)])
    command.extend([
        "gen",
        "--slot",
        slot,
        "--n",
        str(count),
        "--provider",
        provider,
        "--model",
        model,
        "--prompt",
        prompt,
        "--json",
    ])
    if size:
        command.extend(["--size", size])
    elif aspect_ratio:
        command.extend(["--aspect-ratio", aspect_ratio])
    return command


__all__ = ["collect_context_questions", "plan_image_job"]
from ._compat import dataclass
