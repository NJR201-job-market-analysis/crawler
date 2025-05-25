# crawler

本專案為多網站職缺爬蟲程式集合，包含 Cake.me 與 Yourator 等平台的職缺資料擷取。

## 專案結構

- `cake/`  
  - `cake_crawler.py`：Cake.me 職缺爬蟲主程式  
  - `main.py`：Cake.me 爬蟲執行入口  
  - `cake_me_crawl_20250523.ipynb`：Cake.me 職缺資料分析與爬取範例 Notebook

- `yourator/`  
  - `yourator_crawler.py`：Yourator 職缺爬蟲主程式  
  - `main.py`：Yourator 爬蟲執行入口


## 使用方式

1. 進入對應資料夾（如 `cake/` 或 `yourator/`）。
2. 執行 `main.py` 以開始爬取職缺資料，結果將輸出為 CSV 檔案。
3. 亦可參考 `cake_me_crawl_20250523.ipynb` 進行進階資料分析。

## 依賴套件

- requests
- beautifulsoup4
- pandas
- tqdm（僅 Notebook 需要）

請先安裝相關 Python 套件。

## 版權

僅供學術與技術交流使用，請勿用於商業用途。# crawler
上傳爬蟲程式碼

## 測試：這是次標題