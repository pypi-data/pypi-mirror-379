"""
# ==============================================================================
# Apache 2.0 License (ngeodesic.ai)
# ==============================================================================
# Copyright 2025 Ian C. Moore (Provisional Patents #63/864,726, #63/865,437, #63/871,647 and #63/872,334)
# Email: ngeodesic@gmail.com
# Part of Noetic Geodesic Framework (NGF)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""

from __future__ import annotations
from typing import Dict, Any, List, Optional
import json, argparse, os
from micro_lm.core.runner import run_micro  # public in module map
from micro_lm.domains.defi.verify_local import verify_action_local  # package map shows it's exported
import hashlib


"""
python3 -m micro_lm.cli.defi_quickstart "deposit 10 ETH into aave" \
  --rails stage11 --use_wdd --pca_prior .artifacts/defi/pca_prior.npz --profile --verbose
"""

# Canonical runner (Tier-2 entrypoint)
from micro_lm.core.runner import run_micro  # exported public API in package map
# (Runner contract used across your milestones)  # see M11 usage
# - returns dict with at least: plan.sequence, flags, (maybe) verify
# - rails="stage11" is the canonical default for Tier-1/2 consolidation

DEFAULT_POLICY = {
    "ltv_max": 0.75,
    "hf_min": 1.0,
    "mapper": {
        "model_path": os.getenv("MICRO_LM_MAPPER_PATH", ".artifacts/defi_mapper_embed.joblib"),
        "confidence_threshold": float(os.getenv("MICRO_LM_MAPPER_THRESHOLD", "0.7")),
    },
}
DEFAULT_CONTEXT = {"oracle": {"age_sec": 5, "max_age_sec": 30}}
DEFAULT_RAILS = "stage11"
DEFAULT_T = 180

# --- canonicalization: keep this, just add transfer aliases if missing ---
def _canon_primitive(name: str) -> str:
    t = (name or "").strip().lower()
    table = {
        "swap_assets": "swap_asset",
        "swap": "swap_asset",
        "deposit_assets": "deposit_asset",
        "deposit": "deposit_asset",
        "withdraw_assets": "withdraw_asset",
        "withdraw": "withdraw_asset",
        "stake_assets": "stake_asset",
        "stake": "stake_asset",
        "unstake_assets": "unstake_asset",
        "unstake": "unstake_asset",
        "borrow_assets": "borrow_asset",
        "borrow": "borrow_asset",
        "repay_assets": "repay_asset",
        "repay": "repay_asset",
        "transfer_assets": "transfer_asset",
        "transfer": "transfer_asset",
        "send": "transfer_asset",
    }
    return table.get(t, t)

# --- NEW: lexical fallback that understands all 8 primitives and preserves order ---
_PRIM_LEX = {
    "swap_asset": [
        r"\bswap\b", r"\bconvert\b", r"\btrade\b", r"\bexchange\b",
        r"\broute\b .* \b(uniswap|sushi|curve|balancer)\b",
    ],
    "deposit_asset": [
        r"\bdeposit\b", r"\bsupply\b", r"\badd\s+liquidity\b", r"\bprovide\s+liquidity\b",
        r"\bput\b .* \binto\b .* \b(aave|compound|maker|yearn|lido)\b",
    ],
    "withdraw_asset": [
        r"\bwithdraw\b", r"\bredeem\b", r"\bremove\s+liquidity\b", r"\bunstake\s+lp\b",
    ],
    "borrow_asset": [
        r"\bborrow\b", r"\btake\s+out\s+a\s+loan\b",
    ],
    "repay_asset": [
        r"\brepay\b", r"\bpay\s*back\b", r"\bclose\s+loan\b",
    ],
    "stake_asset": [
        r"\bstake\b", r"\bdelegate\b", r"\bbond\b",
    ],
    "unstake_asset": [
        r"\bunstake\b", r"\bundelegate\b", r"\bunbond\b",
    ],
    "transfer_asset": [
        r"\btransfer\b", r"\bsend\b", r"\bmove\b .* \bto\b",
    ],
}

import re

def _lexical_match_primitive(chunk: str) -> Optional[str]:
    p = (chunk or "").lower()
    for prim, pats in _PRIM_LEX.items():
        for rgx in pats:
            if re.search(rgx, p):
                return prim
    return None

def _lexical_sequence(prompt: str) -> List[str]:
    """
    Parse a natural language prompt into an ordered list of primitives.
    Very conservative: returns [] if nothing obvious is found.
    """
    if not prompt:
        return []
    text = prompt.strip()
    # Split along soft sequencing cues while preserving order
    parts = re.split(r"\bthen\b|->|→|;|, and then | and then ", text, flags=re.IGNORECASE)
    seq: List[str] = []
    seen = set()
    for chunk in parts:
        prim = _lexical_match_primitive(chunk)
        if prim:
            canon = _canon_primitive(prim)
            if canon not in seen:
                seen.add(canon)
                seq.append(canon)
    return seq

def _lexical_primitive(prompt: str) -> Optional[str]:
    """
    Back-compat: first primitive only.
    """
    seq = _lexical_sequence(prompt)
    return seq[0] if seq else None


def _seq_hash(seq):
    s = "|".join(seq) if seq else "∅"
    return hashlib.sha256(s.encode()).hexdigest()[:12]

# helpers: abstain + WDD summarizer
def _is_abstain(minimal: dict, res: dict) -> bool:
    v = (minimal.get("verify") or {})
    reason = (v.get("reason") or "").lower()
    seq = (minimal.get("plan") or {}).get("sequence") or []
    flags = res.get("flags") or {}
    # Same spirit as the Stage-8 harness: treat non-exec + abstain tokens as abstain
    # plus explicit WDD decision if present. (See citations.)
    abstain_token = ("abstain" in reason) or ("low_conf" in reason)
    wdd_decision = (res.get("aux") or {}).get("wdd", {}).get("decision")
    stage11_decision = (res.get("aux") or {}).get("stage11", {}).get("wdd", {}).get("decision")
    return (not seq) or abstain_token or (str(wdd_decision).upper() == "ABSTAIN") or (str(stage11_decision).upper() == "ABSTAIN")

def _summarize_wdd(aux: dict) -> dict:
    # Try both aux.wdd and aux.stage11.wdd
    w = (aux.get("wdd") or (aux.get("stage11") or {}).get("wdd") or {})
    # Map to your table-like fields; if a field is missing, leave None
    decision    = w.get("decision")               # "PASS"/"ABSTAIN"
    keep        = w.get("keep")                   # components kept (PCA or shortlist)
    sigma       = w.get("sigma")                  # null σ or matched-filter σ
    proto_w     = w.get("proto_w")                # prototype index/weight
    which_prior = w.get("which_prior")            # e.g., "swap(L-4)"
    mf_peak     = w.get("mf_peak") or w.get("nxcorr_peak")  # matched-filter peak if present
    note = None
    if mf_peak is not None:
        note = f"fallback: MF_peak={mf_peak}"
    return {
        "decision": decision,
        "keep": keep,
        "sigma": sigma,
        "proto_w": proto_w,
        "which_prior": which_prior,
        "note": note,
    }


def _tokens_from_output(out: dict) -> str:
    v = out.get("verify") or {}
    reason = str(v.get("reason") or "").lower()
    tags = v.get("tags") or []
    if isinstance(tags, list):
        reason += " " + " ".join(str(t).lower() for t in tags)
    flags = out.get("flags") or {}
    try:
        reason += " " + " ".join(str(k).lower() for k in flags.keys())
    except Exception:
        pass
    return reason.strip()


# --- M11-compatible verify fallback (priority: ltv > hf > oracle > abstain) ---
def _fallback_verify_from_flags(result: Dict[str, Any]) -> Dict[str, Any]:
    plan = result.get("plan") or {}
    seq  = plan.get("sequence") or []
    flags = result.get("flags") or {}

    # Compact blob of flag tokens for quick checks (M11 logic)
    blob = " ".join([f"{str(k).lower()}:{str(v).lower()}" for k, v in flags.items()])

    if any(tok in blob for tok in ["ltv_breach:true", "ltv:true"]):
        return {"ok": False, "reason": "ltv_breach"}
    if any(tok in blob for tok in ["hf_breach:true", "health_breach:true", "hf:true"]):
        return {"ok": False, "reason": "hf_breach"}
    if any(tok in blob for tok in ["oracle_stale:true", "oracle:true", "stale:true"]):
        return {"ok": False, "reason": "oracle_stale"}

    if not seq:
        return {"ok": False, "reason": "abstain_non_exec"}
    return {"ok": True, "reason": ""}

# --- helper: reason from flags (Stage-11 priority) ---
def _reason_from_flags(flags: dict) -> str | None:
    blob = " ".join([f"{str(k).lower()}:{str(v).lower()}" for k, v in (flags or {}).items()])
    if any(tok in blob for tok in ("ltv_breach:true", "ltv:true")):
        return "ltv_breach"
    if any(tok in blob for tok in ("hf_breach:true", "health_breach:true", "hf:true")):
        return "hf_breach"
    if any(tok in blob for tok in ("oracle_stale:true", "oracle:true", "stale:true")):
        return "oracle_stale"
    return None

def run_defi(prompt: str,
               policy: Dict[str, Any] | None = None,
               context: Dict[str, Any] | None = None,
               rails: str = DEFAULT_RAILS,
               T: int = DEFAULT_T,
               *,
               use_wdd: bool = False,
               pca_prior: str | None = None,
               profile: bool = False,
               verbose: bool = False) -> Dict[str, Any]:

    pol = json.loads(json.dumps({**DEFAULT_POLICY, **(policy or {})}))
    ctx = json.loads(json.dumps({**DEFAULT_CONTEXT, **(context or {})}))

    # NEW: opt-in WDD audit backend (policy flag the runner can read)
    if use_wdd:
        pol["audit"] = {
            "backend": "wdd",          # drives audit selection
            "profile": bool(profile),  # write profile/topline like Stage 6
        }
        if pca_prior:
            pol["audit"]["pca_prior"] = pca_prior  # pass notebook prior

    # 1) canonical run (runner should consult pol["audit"])
    res = run_micro(domain="defi", prompt=prompt, context=ctx, policy=pol, rails=rails, T=T)

    # 2) Normalize plan to notebook contract
    seq: List[str] = (res.get("plan") or {}).get("sequence") or []
    
    # Fallback ONLY if mapper abstained or produced nothing
    if not seq:
        # Try ordered lexical parse with all 8 primitives
        seq = _lexical_sequence(prompt)
    
    # Canonicalize just in case (mapper/runner aliases)
    seq = [_canon_primitive(s) for s in seq if s]

    # --- 3) Verification: combine rails + local DeFi policy checks ---
    rails_v = res.get("verify") if isinstance(res.get("verify"), dict) else {"ok": True, "reason": "shim:accept:stage-4"}
    
    # Local verifier on the chosen action (first primitive)
    from micro_lm.domains.defi.verify_local import verify_action_local
    action = (seq[0] if seq else None)
    try:
        local_v = verify_action_local(action, pol, ctx, res.get("state"))
    except Exception:
        local_v = {"ok": True, "reason": ""}  # non-blocking fallback
    
    ok_rails = bool(rails_v.get("ok", False))
    ok_local = bool(local_v.get("ok", True))
    ok = (ok_rails and ok_local)
    
    # Prefer local reason when blocking (e.g., 'ltv'), keep rails reason on pass
    reason = rails_v.get("reason", "") if ok else (local_v.get("reason") or rails_v.get("reason") or "abstain_non_exec")
    
    # Tags: always include rails:<rails>; only add WDD tags if audit backend is wdd
    tags = list(rails_v.get("tags") or [])
    rtag = f"rails:{rails}"
    if rtag not in tags:
        tags.append(rtag)
    audit = pol.get("audit") or {}
    if str(audit.get("backend", "")).lower() == "wdd":
        if "wdd:on" not in tags: tags.append("wdd:on")
        if "audit:wdd" not in tags: tags.append("audit:wdd")
    
    v_block = {"ok": ok, "reason": reason, "tags": tags}
    
    # Gate the plan on verification (and explicitly on LTV reason)
    if not ok or "ltv" in str(reason).lower():
        seq = []


    # 4) Minimal (notebook-parity) payload
    minimal = {
        "plan":   {"sequence": list(seq)},
        "verify": {"ok": bool(v_block.get("ok")), "reason": str(v_block.get("reason") or "")},
    }

    if not verbose:
        return minimal

    # 5) Verbose: surface WDD status & rails details (benchmark-style)
    aux   = res.get("aux") or {}
    flags = res.get("flags") or {}
    top1  = (seq[0] if seq else None)

    stage11_on = bool((aux.get("stage11") or {})) or (rails.lower() == "stage11")
    audit_wdd  = str(((pol.get("audit") or {}).get("backend") or "")).lower() == "wdd"

    tags = []
    if stage11_on:
        tags += ["rails:stage11", "wdd:on"]
    if audit_wdd:
        tags += ["audit:wdd"]
    minimal_verify = dict(minimal["verify"])
    if tags:
        minimal_verify["tags"] = tags

    # NEW: WDD row summary (matches your table)
    wdd_summary = _summarize_wdd(aux)
    abstained = _is_abstain(minimal, res)
    
    return {
        "prompt": prompt,
        "domain": "defi",
        "rails": rails,
        "T": T,
        "top1": top1,
        "sequence": list(seq),
        "plan": minimal["plan"],
        "verify": minimal_verify,
        "flags": flags,
        "aux": aux,
        "det_hash": _seq_hash(seq),
        "wdd_summary": wdd_summary,     # <— table-like fields
        "abstained": bool(abstained),   # <— single truthy flag
    }

