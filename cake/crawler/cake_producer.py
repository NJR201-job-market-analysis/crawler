from crawler.cake_tasks import crawl_cake_jobs

# 定義要爬取的分類和職位類型
categories = [
    ("software-developer", None),
    ("start-up", None),
    ("overseas-company", "it"),
    ("million-salary", "it"),
    ("top500-companies", "it"),
    ("digital-nomad", "it"),
    ("remote-work", "it"),
    ("bank", "it"),
    # 可以繼續添加更多分類
]

# 為每個分類創建一個任務
for category, job_type in categories:
    crawl_cake_jobs.delay(
        category=category, job_type=job_type, filename=f"cake_{category}_it_jobs.csv"
    )
