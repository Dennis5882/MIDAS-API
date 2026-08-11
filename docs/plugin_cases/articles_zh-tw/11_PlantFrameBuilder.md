# Plant Frame Builder

- 原文（韓文）：https://support.midasuser.com/hc/ko/articles/60728306572441-PlantFrameBuilder
- 影片：[11_PlantFrameBuilder.mp4](../videos/11_PlantFrameBuilder.mp4)
- GEN NX API CHALLENGE 2026

---

這是一款 GEN NX API 外掛程式，僅需輸入 Bay 間距、層高等數值，即可自動生成雙排多層管架
（Pipe Rack）供結構分析用的初始鋼構架模型（Node/Column/Beam/Brace/Support）。

## 主要功能

**01. 參數化超高速自動建模（省去重複輸入、提升實務彈性）**
無需繁瑣手動作業，僅輸入參數（Bay 間距、層高等）即可瞬間完成 Pipe Rack 構架。除可讀取
既有模型的材料（Material）與斷面（Section）外，亦可在介面內即時新增、指定，因此即使從空白
模型也能立即開始。從形狀到支承條件皆一次處理完成，有效縮短重複建模所需時間。

**02. 即時 3D 預覽與完整事前驗證（杜絕人為疏失）**
參數變更時即時更新 3D 預覽，可直覺確認形狀。在正式反映至 GEN NX 模型前，會驗證預期構件
數量、將指定的 ID 範圍，以及與既有模型是否發生衝突。僅在通過驗證的安全狀態下才會建立模型，
藉此杜絕人為疏失。
