import 新專題main as main

#(一)查找資料條件, 已經有預設值, 請依需求自行修改

looking_for="desc&ks="+main.urllib.parse.quote("軟體+工程師") #查找中文關鍵字, 中間用+連接
#looking_for="software+python" #查找英文關鍵字, 中間用+連接 ex."software+engineer"
p_start=1      #從第幾頁開始找
p_limit=2      #找到第幾頁
w_place=[]     #預設不限縣市, 想找特定縣市請輸入縣市名稱, (一縣市以兩字為限), 並以逗號相隔 ex.["台北","桃園"]
wfh=False      #預設不限定遠端工作. 只想找遠端工作, 改成True
ex=False       #預設不限定工作經驗. 只想找工作經驗"不拘"的, 改成True

#(二)查找資料入口
main.find_all_pages(looking_for,p_start,p_limit,w_place,wfh,ex)
df = main.pd.json_normalize(main.table)

#(三)用class創資料夾並存檔案
f1=main.File(name="1111jobs.csv") # name="檔名"
f1.path("大肥貓咪資料夾")          # 創建資料夾名稱, 同時自動設好從資料夾到檔案的路徑(路徑名稱: f1.path_name)
df.to_csv(f1.path_name, encoding="utf-8")

#一步一步創資料夾存檔案
# dn="肥貓大資料夾" #創資料夾名稱
# fn="肥貓job4" #創檔名
# if not main.os.path.exists(dn):
#     main.os.makedirs(dn)
# fn=dn+"/"+fn+".csv"
# df.to_csv(fn, encoding="utf-8")


