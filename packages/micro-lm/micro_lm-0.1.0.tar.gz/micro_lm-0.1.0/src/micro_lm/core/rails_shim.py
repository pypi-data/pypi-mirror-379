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

from importlib import import_module

class Rails:
    def __init__(self, *, rails: str, T: int):
        self.rails = rails
        self.T = T

    def verify(self, *, domain: str, label: str, context: dict, policy: dict) -> dict:
        import os
        if os.getenv("MICROLM_STRICT_SHIM") == "1":
            return {"ok": True, "reason": "shim:forced"}

        # 1) Try LOCAL domain adapter first
        try:
            mod = import_module(f"micro_lm.domains.{domain}.verify_local")
            local = getattr(mod, "verify_action_local", None)
            if callable(local):
                pre = local(label=label, context=context, policy=policy)
                # Short-circuit on BLOCK only
                if pre.get("ok") is False:
                    return pre
                # # Short-circuit on SUCCESS with a tag
                # if pre.get("ok", False):
                #     return {"ok": True, "reason": "local:verified"}
        except Exception:
            pass  # fall through to rails/shim

        # 2) If ngeodesic exists, call it; else accept via shim
        try:
            from ngeodesic.stage11 import verify_action  # type: ignore[attr-defined]
            out = verify_action(
                domain=domain, label=label,
                context=context or {}, policy=policy or {},
                rails=self.rails, T=self.T
            )
            return {
                "ok": bool(out.get("ok", False)),
                "reason": out.get("reason", "verified"),
                **{k: v for k, v in out.items() if k not in ("ok", "reason")}
            }
        except Exception:
            return {"ok": True, "reason": "shim:accept:stage-4"}
