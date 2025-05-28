# 測試 工作日誌（2025/5/22 - 2025/5/28）
Agent : 整理這最近七天的工作日誌 (git log)(no pager)

### 6天前 (5/22)
- **falloutnicole**: 
  - 新增 cake 和 yourator 職缺爬蟲功能
  - 更新 yourator_crawler.py

### 4天前 (5/24)
- **judyazby**:
  - README 內容測試
- **soldierHuang**:
  - 實作 cake_me_crawl_20250523.ipynb 爬蟲程式（兩次更新）

### 3天前 (5/25)
- **soldierHuang**:
  - 新增專題製作的時程規劃與人員存活表
  - 刪除專題製作相關的甘特圖文件
  - 更新 README.md，新增專案結構與使用方式說明
  - 開發 104人力銀行_crawl.ipynb 爬蟲功能
- **falloutnicole**:
  - 開發 LinkedIn 爬蟲功能
  - 修正分頁設定：頁碼從 1 開始啟動
  - 修正頁面設定問題
- **Labor365**:
  - 新增 1111 人力銀行相關功能

### 2天前 (5/26)
- **Labor365 & falloutnicole**:
  - 多次更新 1111 人力銀行爬蟲程式 (新專案main2.py)
  - 進行代碼合併及衝突解決
- **falloutnicole**:
  - 刪除 .idea 目錄

### 昨天 (5/27)
- **soldierHuang**:
  - 新增 LinkedIn 爬蟲功能：
    - 實作登錄機制
    - 開發職缺網址生成功能
    - 實作數據提取功能
  - 更新 README.md：
    - 新增 LinkedIn 支援說明及使用方式
    - 新增 104 人力銀行及 1111 人力銀行的支援說明
    - 調整依賴套件描述
    - 調整使用方式步驟的說明

## 開發重點總結
1. 完成多個求職平台的爬蟲功能：
   - LinkedIn
   - 104人力銀行
   - 1111人力銀行
   - Yourator
   - CakeResume

2. 文件更新與維護：
   - 持續更新 README.md
   - 完善各平台使用說明
   - 新增功能支援說明

3. 程式優化：
   - 修正分頁機制問題
   - 改善爬蟲功能

4. 專案管理：
   - 規劃專案時程
   - 調整專案結構
   - 移除不必要的文件

## 專案結構
```
crawler/
├── 104/
│   └── 104人力銀行_crawl.ipynb
├── 1111/
│   ├── 新專案main2.py
│   └── 新專題main.py
├── cake/
│   ├── cake_crawler.py
│   ├── cake_me_crawl_20250523.ipynb
│   └── main.py
├── linkedin/
│   ├── Linkedin_crawl_20250527.ipynb
│   └── linkedin.py
└── yourator/
    ├── main.py
    └── yourator_crawler.py
```