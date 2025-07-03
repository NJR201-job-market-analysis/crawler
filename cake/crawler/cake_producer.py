from crawler.cake_tasks import crawl_cake_jobs
from crawler.cake_logger import logger

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

tasks = []

# 為每個分類創建一個任務
for category, job_type in categories:
    logger.info(f"🚀 開始發送 {len(categories)} 個爬蟲任務")

    task = crawl_cake_jobs.delay(category=category, job_type=job_type)

    tasks.append(task)
    logger.info(f"📤 已發送任務: {category} | {job_type} | ID: {task.id}")

logger.info(f"✅ 所有任務已發送完成，共 {len(tasks)} 個任務")
