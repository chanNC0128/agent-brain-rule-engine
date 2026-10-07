# 一次種子入口規格（IQ／人格擲骰）

署名：rule engine 工程師。日期標記：2026-10-07。不接 Ollama／LM Studio／任何模型。不改 `decide()` 地點公式。不改地圖／frontend。不 push。不把擲骰寫進每 tick。權重同等號右邊全部留空，不發明數字。

## 前置

- 詞彙名 47／47 已列完；今日不加新詞
- 槽名沿用 `one_shot_roll_slots.md`（齊，見下）
- 空白公式名 0；公式等號右邊仍空

## 1. 槽名（齊，只沿用，缺則只補名）

| 槽 | 狀態 |
| --- | --- |
| `iq_seed_slot` | 齊 |
| `trait_slot` | 齊 |
| `trait_big_event_gate` | 齊 |
| `trait_change_prob` | 齊（只留名） |
| `iq_event_slot` | 齊（等號右邊空白） |
| `trait_event_slot` | 齊（等號右邊空白） |

本輪無需補名。

## 2. 一次種子入口

| 項 | 規則 |
| --- | --- |
| 入口名 | `oneshot_seed_entry` |
| 時機 | 出生／世界鎖定 seed 時呼叫 **一次** |
| 讀 | 世界 `seed`（字串或整數，用戶鎖定前可換；鎖定後固定） |
| 寫 | 經 `iq_seed_slot`、`trait_slot` 寫入一次結果容器（數值本輪 **唔填**） |
| per-tick | **禁止**重入入口；tick 循環唔准再擲 IQ／性格基線 |
| 重播 | 同一 `seed` → 同一 IQ／性格基線；`seed + tick` 只預留給日後已定結構浮動，**唔**用嚟每 tick 重擲入口 |
| 決定性 | `hash(seed + ":" + slot_name)` 或同等有 seed PRNG；禁止無 seed 嘅 `random` |

## 3. 權重／等號右邊（全部留空）

| 欄 | 本輪 |
| --- | --- |
| `iq_seed_slot` 數值 | 空 |
| `trait_change_prob` 權重 | 空 |
| `iq_event_slot` 等號右邊 | 空 |
| `trait_event_slot` 等號右邊 | 空 |
| 一切未給 W | 空 |

大事件經 `trait_big_event_gate` 先有機會改性格數量／內容；機率同權重未給，唔發明。

## 禁

接模型；push；地圖；frontend；把擲骰寫進每 tick；改 `decide()`；發明數字或等號右邊。

## 下一刀（唔好自己做）

用戶畀 seed 字串或允許填數後，先寫實際一次性擲程式；仍未完成前唔開 LLM。
