# 一次性擲槽規格（今晚三小任務）

署名：rule engine 工程師。不改既有程式、不改 `decide()`、不 push。不連 LLM／Ollama／LM Studio。權重未給留空，不發明等號右邊。`seed + tick` 重播同結果；智商唔跟 tick 重擲。

## 前置

- 詞彙名 47／47 已列完
- 事件公式名空白 0（等號右邊仍全部空）

## 1. 智商一次性 seed 槽

| 欄 | 狀態 |
| --- | --- |
| `iq_seed_slot` | 留名 |
| 擲時機 | 出生／鎖定 seed 時擲 **一次** |
| per-tick | **唔改**智商 |
| 數值 | **唔填**（本輪） |
| 重播 | 同一 seed → 同一智商 |

## 2. 性格槽

| 欄 | 狀態 |
| --- | --- |
| `trait_slot` | 留名；性格數量平時鎖定（唔加唔減） |
| `trait_big_event_gate` | 大事件旗先至有機會改數量／內容 |
| `trait_change_prob` | 概率欄 **只留名** |
| 權重 | **空白**（不發明） |

## 3. 事件可影響留位

| 欄 | 狀態 |
| --- | --- |
| `iq_event_slot` | 只留名；公式右邊 **空白** |
| `trait_event_slot` | 只留名；公式右邊 **空白** |

說明：大事件可經呢兩個槽「有機會」影響智商／性格；機率同權重未給，全部留空。

## 禁

改前面程式、`decide()`、push；發明權重；填智商／性格數值；接 LLM／Ollama／LM Studio。

## 空白欄一覽

`iq_seed_slot` 數值、`trait_change_prob` 權重、`iq_event_slot` 等號右邊、`trait_event_slot` 等號右邊、一切未給 W。
