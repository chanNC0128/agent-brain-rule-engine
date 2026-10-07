# agent-brain-rule-engine

Agent World **大腦** rule engine 倉（與身體倉 `agent-body-engine`、主世界 `Agent-world` 分倉）。

## 範圍

- 詞彙表、事件公式讀寫（等號右邊未到則留空）
- 第二層規格：人格＋情緒 → 事件；工作＋技能 → 後果旗
- 一次性 IQ／人格擲骰（seed 一次，唔每 tick）

## 唔做

- 唔改 `decide()` 地點公式
- 唔改地圖／frontend
- 唔合體身體引擎
- 未完成一次性擲前唔接 LLM／Ollama／LM Studio

## 檔案

| 路徑 | 說明 |
| --- | --- |
| `vocab_rule_spec.md` | 詞彙、範圍、事件公式 1–15、結構規則 |
| `rule_engine_layer2.md` | 第二層打磨稿 |
| `value_roll_spec.md` | value-roll 程式規格 |
| `one_shot_roll_slots.md` | 一次性擲槽名 |
| `oneshot_seed_entry_spec.md` | 一次種子入口規格 |
| `oneshot_brain_roll.py` | 短 code：`roll_once(seed)` |
| `oneshot_brain_roll_README.md` | 擲骰說明 |

## 跑例子

```bash
python3 oneshot_brain_roll.py
```
