# value-roll 程式規格

署名：rule engine 工程師。本輪只寫規格，不寫等號右邊公式，不改 `decide()`，不 merge／push，不改地圖／frontend。權重繼續留空。

## 前置狀態（已數）

| 項 | 計數 |
| --- | --- |
| 詞彙名 name-closed | **47／47** |
| 仍空白嘅事件公式名 | **0**（1–15 名已列完；等號右邊仍全部空，唔准發明） |

## 目的

一次 seed 為 47 個已鎖定詞彙名擲出數值（同可選一組性格組合）。**唔係每 tick 隨機**。同一 `seed` 重跑必須得到同一組數；`seed + tick` 只用於之後已定結構嘅浮動（見 `vocab_rule_spec.md`），唔用嚟每 tick 重擲人格。

## 輸入

| 名 | 說明 |
| --- | --- |
| `seed` | 字串或整數；一次鎖定，整場世界共用直至用戶改 seed |
| `vocab` | 固定 47 名（見下表）；唔准加新標籤 |
| `tick` | **本規格 value-roll 唔讀 tick 改詞彙數**；tick 只預留給日後浮動欄 |

## 輸出

| 名 | 說明 |
| --- | --- |
| `values[name]` | 每詞一個數或（即時情緒）強／中／弱 |
| `lock` | 一律標 `random_unlocked`（唔當正式常數，直至用戶鎖） |
| `persona` | 由已有特質高分組合出嘅一組性格名＋數（可選交付） |
| `seed_used` | 寫回用過嘅 seed |

## 決定性規則

1. 用 `hash(seed + ":" + name)`（或同等決定性 PRNG）映射到該詞範圍。
2. 範圍跟 `vocab_rule_spec.md`：多數 `0–100`；`內外向`、`多巴胺基準`、`皮質醇反應`、`晝夜節律` 用 `−100..100`；`即時情緒` 只得 `弱／中／強`。
3. 禁止語言「隨便」；禁止 `random` 模組無 seed。
4. **每 tick 唔重擲** value-roll。重播：同一 seed → 同一 `values`。
5. 已有九欄（diligence…joy）可擲數，但**唔覆寫欄定義／範圍**。
6. **唔填**事件公式 1–15 等號右邊；**唔填** `W_*` 權重。

## 47 詞彙名（固定，name-closed）

已有：diligence, curiosity, sociability, creativity, intelligence, eq, satisfaction, anger_at, joy

認知：邏輯推理、圖像記憶、聽覺記憶、空間建構、數字直覺、模式識別、語言天賦、發散思維、收斂思維、認知彈性、專注上限

性情：內外向、孤僻、討好、表演慾、利他、馬基雅維利、無同理、自戀、正義、完美、強迫秩序、破壞慾、叛逆、服從、慕強、救世主、宿命、冒險、避險

生理：高敏感、痛覺閾、多巴胺基準、皮質醇反應、晝夜節律、體能恢復、反應神經

情緒：即時情緒

## 同浮動嘅邊界

- value-roll：一次 seed → 47 值。
- 結構浮動（Trigger／Severity 等）：日後用 `seed + tick` 可重跑；**今片唔實作、唔填權重**。

## 禁

改 `decide()`、merge、push、地圖、frontend；發明公式等號右邊；發明新詞彙名。

## 下一刀（唔好自己做）

用戶確認後先寫實際 value-roll 程式；或鎖正式 seed／把 `random_unlocked` 改成 locked。
