from datetime import datetime
from crawler.cake_worker import app
from crawler.cake_crawler import cake_crawler
from crawler.cake_logger import logger
from crawler.cake_database import CakeDatabase


@app.task(bind=True)
def crawl_cake_jobs(self, category, job_type):

    task_id = self.request.id
    start_time = datetime.now()
    logger.info(f"🔍 開始爬取 | 📂 {category} | 🏷️ {job_type}")

    try:
        result = cake_crawler(category, job_type)
        logger.info(
            f"🗄️  寫入資料庫 | 📂 {category} | 🏷️  {job_type} | 📊 {len(result)} 筆"
        )
        CakeDatabase().insert_jobs(result)

        end_time = datetime.now()
        duration = (end_time - start_time).total_seconds()

        logger.info(f"✅ 任務完成 {task_id} | 耗時: {duration:.2f}秒")

        return {
            "status": "success",
            "task_id": task_id,
            "category": category,
            "job_type": job_type,
            "duration": duration,
            "result": result,
            "timestamp": end_time.isoformat(),
        }
    except Exception as e:
        logger.error(f"❌ 任務失敗 {task_id} | 錯誤: {str(e)}")

        return {
            "status": "error",
            "task_id": task_id,
            "error": str(e),
            "category": category,
            "job_type": job_type,
            "duration": duration,
            "timestamp": end_time.isoformat(),
        }


@app.task
def test_task():
    """
    Simple test task
    """
    return "Hello from Cake worker!"
