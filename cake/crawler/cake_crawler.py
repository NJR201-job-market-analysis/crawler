import urllib.request as req
from typing import cast, List
from bs4 import BeautifulSoup, Tag
from crawler.cake_logger import logger

BASE_URL = "https://www.cake.me"
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36 Edg/135.0.0.0"
}

COMMON_SKILLS = [
    # 主流語言/框架
    "JavaScript",
    "Javascript",
    "Typescript",
    "TypeScript",
    "Node.js",
    "NodeJs",
    "Node",
    "Python",
    "Java",
    "Go",
    "Golang",
    "Flutter",
    "C#",
    "C++",
    "C",
    "PHP",
    "Ruby",
    "Swift",
    "Kotlin",
    "Scala",
    "Perl",
    "Rust",
    "Objective-C",
    ".NET",
    # 資料庫
    "SQL",
    "MySQL",
    "PostgreSQL",
    "MSSQL",
    "Oracle",
    "MongoDB",
    "Redis",
    "ElasticSearch",
    "SQLite",
    # 前端
    "HTML5",
    "CSS3",
    "HTML",
    "CSS",
    "Sass",
    "Less",
    "React",
    "React Native",
    "React.js" "ReactJs",
    "Redux",
    "Nextjs",
    "NextJs",
    "Vue",
    "Vue.js",
    "Angular",
    # DevOps/雲端
    "Shell Script",
    "Bash",
    "Linux",
    "Unix",
    "AWS",
    "GCP",
    "Azure",
    "Google Cloud",
    "Amazon Web Services",
    "Microsoft Azure",
    "Docker",
    "Kubernetes",
    "K8s",
    "Git",
    "GitHub",
    "GitLab",
    "CI/CD",
    "Jenkins",
    "GitHub Actions",
    "GitLab CI",
    # API/通訊
    "GraphQL",
    "Graphql",
    "RESTful",
    "Restful",
    "gRPC",
    "Pubsub",
    "Message Queue",
    "RabbitMQ",
    "Kafka",
    "Nginx",
    "Apache",
    # 其他
    "Agile",
    "Scrum",
    "Kanban",
    # ...可再擴充...
]


def cake_crawler(category, job_type):
    result = []
    page = 1

    logger.info(f"🐛 開始爬取 | {category} | {job_type}")

    while page <= 1:
        # if job_type is None then https://www.cake.me/campaigns/software-developer/jobs?page=1
        # if job_type is it_front-end-engineer then
        # https://www.cake.me/campaigns/software-developer/jobs?page=1&profession[0]=it_front-end-engineer

        base_url = f"{BASE_URL}/campaigns/{category}/jobs?page={page}"
        url = (
            base_url + "&profession[0]=" + job_type
            if job_type is not None
            else base_url
        )

        # print("頁面:", url)

        r = req.Request(url)
        r.add_header(
            "User-Agent",
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36 Edg/135.0.0.0",
        )

        try:
            res = req.urlopen(r)
        except Exception as e:
            logger.error(f"請求 {url} 失敗 | {e}")
            break

        soup = BeautifulSoup(res.read(), features="html.parser")

        # 型別很嚴格，要先轉型不然 IDE 會報錯
        jobs = cast(
            List[Tag],
            soup.find_all("div", {"class": "CampaignJobSearchItem_wrapper__HsxKW"}),
        )

        for job in jobs:
            job_title = cast(
                Tag, job.select_one("a.CampaignJobSearchItem_jobTitle__LQGW_")
            )

            company_name = safe_get_text(
                job, "a.CampaignJobSearchItem_companyName__i9OXl"
            )

            job_skill_list = job.find_all("div", {"class": "Tags_item__B6Bjo"})
            # ['Golang', 'Java'] > "Golang,Java,"
            # 1. job_skill = "Golang,"
            # 2. job_skill = "Golang,Java,"
            job_skill = ""
            for skill in job_skill_list:
                job_skill = job_skill + " / " + skill.text

            # job_features 的 index 順序：
            # 0. 全職
            # 1. 大安區, 台北市
            # 2. 100000-150000
            # 3. 1-3年
            job_features = job.select(
                "div.CampaignJobSearchItem_features__H3moX .InlineMessage_inlineMessage____Ulc"
            )

            # 工作類型 (全職、兼職、實習)
            job_work_type = safe_get_text(
                job_features[0],
                "div.InlineMessage_label__LJGjW div.CampaignJobSearchItem_featureSegments___NcD4 > div:first-child > button",
            )

            job_location = safe_get_text(
                job_features[1],
                "div.InlineMessage_label__LJGjW div.CampaignJobSearchItem_featureSegments___NcD4 > div:first-child > button",
            )

            # 如果沒有地點，薪水的 index 要從 2 變成 1
            job_salary = safe_get_text(
                job_features[1 if job_location is None else 2],
                "div.InlineMessage_label__LJGjW",
            )

            # 如果沒有地點，薪水的 index 要從 3 變成 2
            job_exp = safe_get_text(
                job_features[2 if job_location is None else 3],
                "div.InlineMessage_label__LJGjW",
            )

            job_url = f"{BASE_URL}{job_title.get('href')}"
            job_detail_html = fetch_job_detail(job_url)
            job_description = extract_job_description(job_detail_html)
            job_skill = extract_skills(job_detail_html)

            data = {
                "job_title": job_title.text,
                "company_name": company_name,
                "work_type": job_work_type,
                "required_skills": job_skill,
                "job_description": job_description,
                "location": job_location,
                "salary": job_salary,
                "experience": job_exp,
                "job_url": job_url,
                "job_type": job_type,
                "category": category,
            }
            result.append(data)

        page += 1

    return result

    # save to csv
    # df = pd.json_normalize(table)
    # df.to_csv(filename + ".csv", encoding="utf-8")


def extract_skills(job_detail_html):
    try:
        found_skills = set()
        soup = BeautifulSoup(job_detail_html, features="html.parser")
        job_description_list = soup.find_all(
            "div", {"class": "ContentSection_contentSection__ELRlG"}
        )
        for job_description in job_description_list:
            for line in job_description.stripped_strings:
                line_lower = line.lower()
                for skill in COMMON_SKILLS:
                    if skill.lower() in line_lower:
                        found_skills.add(skill)
        return ",".join(sorted(found_skills)) if found_skills else ""
    except Exception as e:
        logger.error(f"Failed to parse skills: {e}")
        return ""


def extract_job_description(job_detail_html):
    try:
        soup = BeautifulSoup(job_detail_html, features="html.parser")
        job_description_list = soup.find_all(
            "div", {"class": "ContentSection_contentSection__ELRlG"}
        )

        all_text = []

        for job_description in job_description_list:
            text_content = " ".join(job_description.stripped_strings)
            if text_content:
                all_text.append(text_content)

        return " ".join(all_text)
    except Exception as e:
        logger.error(f"Failed to parse job description: {e}")
        return ""


def fetch_job_detail(job_url):
    try:
        r = req.Request(job_url)
        r.add_header(
            "User-Agent",
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36 Edg/135.0.0.0",
        )
        res = req.urlopen(r)
        return res.read()
    except Exception as e:
        logger.error(f"請求 {job_url} 失敗 | {e}")
        return ""


def safe_get_text(soup, selector, default=""):
    try:
        return soup.select_one(selector).text
    except (IndexError, AttributeError):
        return default
