# EasyApartmentBuilder

- 原文（韓文）：https://support.midasuser.com/hc/ko/articles/60728140059161-EasyApartmentBuilder
- 影片：[15_EasyApartmentBuilder.mp4](../videos/15_EasyApartmentBuilder.mp4)
- GEN NX API CHALLENGE 2026

---

這是一款以結構平面圖 .dxf 為基礎，透過 Wall Mark／ID 自動化，實現簡單、快速公寓分析建模
的外掛程式。

## 主要功能

**01. Wall Mark 自動產生**
自動產生 Wall Mark 為牆體命名，並可依使用者需求自由變更。

**02. Wall ID 自動指定**
依 Wall Mark 自動指定 Wall ID，以滿足 GEN NX 的牆體設計邏輯（依 Wall ID 設計）。

**03. 可考慮基準樓層**
可依使用者需求同時考慮多個樓層的 dxf，並可指定基準樓層，將 Wall Mark／ID 相同套用至
其他樓層。

**04. 使用者便利功能**
可在外掛程式中預先確認模型將如何呈現的 Material、Properties、Thickness，並可同時
考慮梁、柱單元，輕鬆實現複雜的建模。
