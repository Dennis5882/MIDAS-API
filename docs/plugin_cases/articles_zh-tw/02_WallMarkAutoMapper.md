# WallMark Auto Mapper

- 原文（韓文）：https://support.midasuser.com/hc/ko/articles/60809496186521-WallMarkAutoMapper
- 影片：[02_WallMarkAutoMapper.mp4](../videos/02_WallMarkAutoMapper.mp4)
- GEN NX API CHALLENGE 2026

---

WallMark Auto Mapper 是一款從 DXF 結構平面圖擷取牆體名稱與位置資訊，自動與 MIDAS GEN NX
分析模型中既有各 Wall ID 的牆體位置進行比對匹配，並將圖面上的牆體名稱指定為對應 Wall ID 的
Wall Mark 加以管理的外掛程式。自動比對結果可在預覽畫面與結果表中檢視、修改後，再選擇性套用至模型。

## 主要功能

**01. 擷取 DXF 圖面的牆體名稱與位置資訊**
從所選 DXF 結構平面圖的指定圖層擷取牆體名稱與位置資訊，自動建立要與 GEN NX 模型比對的圖面端資料。

**02. 依 GEN NX Wall ID 計算牆體中心座標**
篩選所選樓層與 Wall Type（Membrane 或 Plate）對應的牆單元，並利用其 Node、Element 資訊，
計算既有各 Wall ID 的牆體中心座標。

**03. 圖面牆體資訊與 Wall ID 自動比對**
以容許距離為基準，比對從 DXF 結構平面圖擷取的牆體名稱、位置與 GEN NX 分析模型各 Wall ID
的牆體中心座標，連結最接近的候選項。比對結果依比對成功、需要檢視、比對失敗分類，並顯示於
預覽畫面與結果表。

**04. Wall Mark 檢視、套用與管理**
在預覽畫面與結果表中確認、修改圖面牆體名稱與 Wall ID 的比對結果後，將所選圖面牆體名稱指定為
一個以上對應 Wall ID 的 Wall Mark。支援既有 Wall Mark 的新增、修改、刪除，以及 Excel
匯入匯出、PDF 結果表輸出。
