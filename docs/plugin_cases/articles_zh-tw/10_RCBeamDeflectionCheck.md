# RCBeamDeflectionCheck

- 原文（韓文）：https://support.midasuser.com/hc/ko/articles/60728330684697-RCBeamDeflectionCheck
- 影片：[10_RCBeamDeflectionCheck.mp4](../videos/10_RCBeamDeflectionCheck.mp4)
- GEN NX API CHALLENGE 2026

---

這是一款透過 API 讀取 MIDAS GEN NX 模型中 RC 梁的斷面、材料、配筋與各載重工況分析彎矩，
依 KDS 14 20 30 第 4.2 節規定，利用有效斷面勁度（Ie，Branson 法）自動計算短期、長期撓度，
並與容許撓度比較後，輸出 A4 結構計算書（撓度檢討書）的外掛程式。

## 主要功能

**01. 自動讀取模型資料**
透過 API 自動擷取 RC 梁的斷面、材料、配筋、分析彎矩。

**02. 自動計算撓度**
依 KDS 14 20 30 規定自動計算短期、長期撓度。

**03. 自動檢核容許基準**
將計算結果與容許撓度比較，判定是否符合規定。

**04. 自動輸出結構計算書**
產出包含計算過程與結果的 A4 撓度檢討書。
