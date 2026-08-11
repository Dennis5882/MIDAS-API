# WallStiffnessAuto

- 原文（韓文）：https://support.midasuser.com/hc/ko/articles/60729084287897-WallStiffnessAuto
- 影片：[05_WallStiffnessAuto.mp4](../videos/05_WallStiffnessAuto.mp4)
- GEN NX API CHALLENGE 2026

---

WallStiffnessAuto 透過 GEN NX API 直接讀取 RC 牆體設計（KDS-41-20-2022）結果，
對超出規範的牆體，自動逐步調降其勁度增減係數（WSSF），直到所有 NG 全數解除為止。

## 主要功能

**01. 自動搜尋 NG 構件**
執行結構分析與牆體設計後，自動依樓層／Wall ID 擷取超出規範的牆體，並同時顯示主控應力比。

**02. 設定調降條件**
設定每次調降量、係數下限與最大反覆次數後，即在該範圍內自動反覆執行。

**03. 自動反覆調降**
每次反覆依「套用勁度 → 分析 → 重新確認設計」順序進行，當 NG 全數解除或係數達到下限時，
自動停止。

**04. 係數還原**
反覆過程中已調降的係數，隨時可透過一鍵按鈕還原至調降前的數值（1.0）。
