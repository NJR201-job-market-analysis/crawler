import urllib.request as req
import bs4 as bs
import pandas as pd
import json

def crawler(filename):
    table = []
    page = 1
    base_url = 'https://www.yourator.co'

    while True:
        search_url = f'{base_url}/api/v4/jobs?category[]=%E5%89%8D%E7%AB%AF%E5%B7%A5%E7%A8%8B&category[]=%E5%BE%8C%E7%AB%AF%E5%B7%A5%E7%A8%8B&category[]=%E5%85%A8%E7%AB%AF%E5%B7%A5%E7%A8%8B&category[]=%E6%B8%AC%E8%A9%A6%E5%B7%A5%E7%A8%8B&category[]=%E8%B3%87%E6%96%99%E5%BA%AB&category[]=DevOps%20%2F%20SRE&category[]=%E8%BB%9F%E9%AB%94%E5%B7%A5%E7%A8%8B%E5%B8%AB&category[]=%E9%9B%B2%E7%AB%AF%E5%B7%A5%E7%A8%8B%E5%B8%AB&category[]=%E7%B3%BB%E7%B5%B1%E6%9E%B6%E6%A7%8B%E5%B8%AB&category[]=%E6%95%B8%E6%93%9A%20%2F%20%E8%B3%87%E6%96%99%E5%88%86%E6%9E%90%E5%B8%AB&negotiable=false&page={page}&sort=recent_updated&task_based=false'
        print("頁面:", search_url)
        r = req.Request(search_url)
        r.add_header("User-Agent",
                     "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36 Edg/135.0.0.0")

        res = json.loads(req.urlopen(r).read())
        if res['payload']['hasMore'] is False:
            break
        for job_post in res['payload']['jobs']:
            detail_url = f'{base_url}{job_post['path']}'
            # TODO: request detail to get exp and company desc
            table.append({
                "職缺": job_post['name'],
                "公司": job_post['company']['brand'],
                "要求技能": ",".join(job_post['tags']),
                "公司簡述": "",
                "地點": job_post['location'],
                "薪資": job_post['salary'],
                "經驗": "",
            })
        page += 1

    df = pd.json_normalize(table)
    df.to_csv(filename + ".csv", encoding="utf-8")
