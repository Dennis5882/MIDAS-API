# AutoGenerationCmFactor

- 原文（韓文）：https://support.midasuser.com/hc/ko/articles/60729138404761-AutoGenerationCmFactor
- 影片：[04_AutoGenerationCmFactor.mp4](../videos/04_AutoGenerationCmFactor.mp4)
- GEN NX API CHALLENGE 2026

---

這是一款自動計算 MIDAS GEN NX 建立載重組合時，地震載重所需 Cm Factor（修正係數）的外掛程式。

## 主要功能

**01. 計算地震載重修正係數**
自動計算 MIDAS GEN NX 建立載重組合時，地震載重所需的 Cm Factor（修正係數）。

**02. 自動輸入**
可一次性讀取模型中已輸入、計算修正係數所需的各項數值。

**03. 套用 KDS 41 17 00 第 4.2.2 節規定**
自動判斷並套用以下兩項規定：(2) 當基岩深度超過 20m 且地盤平均剪力波速達 360m/s 以上時，
套用表 4.2-2 所規定 Fv 值的 80%；(3) 當地盤分類為 S5 且基岩深度不明時，套用表 4.2-1
與表 4.2-2 所規定 Fa、Fv 值的 110%。

**04. 輸出地震載重修正係數計算書**
提供修正係數計算依據計算書輸出功能，說明係基於何種資料計算而得。
