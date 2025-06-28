from crawler.cake_tasks import crawl_cake_jobs

crawl_cake_jobs.delay(
    category="software-developer",
    job_type="it_front-end-engineer",
    filename="cake_jobs.csv",
)
