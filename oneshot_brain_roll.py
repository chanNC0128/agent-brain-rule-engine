"""One-shot IQ/trait brain roll.

Roll once from seed at birth / seed lock. Do NOT re-roll every tick.
Same seed -> same values. Weights and formula RHS stay blank.
Does not touch decide() location formula.
"""

from __future__ import annotations

import hashlib
import struct
from typing import Any

IQ_SEED_SLOT = "iq_seed_slot"
TRAIT_SLOT = "trait_slot"
TRAIT_BIG_EVENT_GATE = "trait_big_event_gate"
TRAIT_CHANGE_PROB = "trait_change_prob"
IQ_EVENT_SLOT = "iq_event_slot"
TRAIT_EVENT_SLOT = "trait_event_slot"
ONESHOT_SEED_ENTRY = "oneshot_seed_entry"

EXISTING = (
    "diligence", "curiosity", "sociability", "creativity", "intelligence",
    "eq", "satisfaction", "anger_at", "joy",
)
COG = (
    "邏輯推理", "圖像記憶", "聽覺記憶", "空間建構", "數字直覺", "模式識別",
    "語言天賦", "發散思維", "收斂思維", "認知彈性", "專注上限",
)
TEMP = (
    "內外向", "孤僻", "討好", "表演慾", "利他", "馬基雅維利", "無同理", "自戀",
    "正義", "完美", "強迫秩序", "破壞慾", "叛逆", "服從", "慕強", "救世主",
    "宿命", "冒險", "避險",
)
PHYS = (
    "高敏感", "痛覺閾", "多巴胺基準", "皮質醇反應", "晝夜節律", "體能恢復", "反應神經",
)
SIGNED = {"內外向", "多巴胺基準", "皮質醇反應", "晝夜節律"}
EMO_LEVELS = ("弱", "中", "強")
LOCK = "random_unlocked"


def _u01(seed: str, key: str) -> float:
    digest = hashlib.sha256(f"{seed}:{key}".encode("utf-8")).digest()
    return struct.unpack(">Q", digest[:8])[0] / 2**64


def _ri(seed: str, key: str, lo: int, hi: int) -> int:
    return int(round(lo + _u01(seed, key) * (hi - lo)))


def roll_once(seed: str) -> dict[str, Any]:
    """Roll all 47 vocab values once. Never call this per tick."""
    values: dict[str, Any] = {}
    for name in EXISTING + COG:
        values[name] = {"value": _ri(seed, name, 0, 100), "range": "0-100", "lock": LOCK}
    for name in TEMP + PHYS:
        if name in SIGNED:
            values[name] = {"value": _ri(seed, name, -100, 100), "range": "-100..100", "lock": LOCK}
        else:
            values[name] = {"value": _ri(seed, name, 0, 100), "range": "0-100", "lock": LOCK}
    emo = EMO_LEVELS[int(_u01(seed, "即時情緒") * 3) % 3]
    values["即時情緒"] = {"value": emo, "range": "強/中/弱", "lock": LOCK}
    return {
        "entry": ONESHOT_SEED_ENTRY,
        "seed_used": seed,
        "per_tick": False,
        "slots": {
            IQ_SEED_SLOT: {"rolled_once": True, "value": None},
            TRAIT_SLOT: {"count_locked": True},
            TRAIT_BIG_EVENT_GATE: {"armed": False},
            TRAIT_CHANGE_PROB: {"weight": None},
            IQ_EVENT_SLOT: {"rhs": None},
            TRAIT_EVENT_SLOT: {"rhs": None},
        },
        "values": values,
        "iq_proxy": values["intelligence"]["value"],
    }


def replay_same(seed: str) -> bool:
    return roll_once(seed)["values"] == roll_once(seed)["values"]


if __name__ == "__main__":
    demo = roll_once("AW-brain-example-check-2026-10-07")
    assert demo["per_tick"] is False
    assert replay_same(demo["seed_used"])
    print("seed", demo["seed_used"])
    print("iq_proxy", demo["iq_proxy"])
    print("即時情緒", demo["values"]["即時情緒"]["value"])
    print("replay_ok", True)
    print("vocab_count", len(demo["values"]))
