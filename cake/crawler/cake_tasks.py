from crawler.cake_worker import app

# from cake.cake_crawler import cake_crawler


@app.task
def crawl_cake_jobs(category, job_type, filename):
    """
    Celery task for crawling Cake jobs
    """
    try:
        # result = cake_crawler(category, job_type, filename)
        return {
            "status": "success",
            "filename": filename,
            "result": "test",
            "category": category,
            "jobtype": job_type,
        }
    except Exception as e:
        return {
            "status": "error",
            "filename": filename,
            "error": str(e),
            "category": category,
            "jobtype": job_type,
        }


@app.task
def test_task():
    """
    Simple test task
    """
    return "Hello from Cake worker!"
