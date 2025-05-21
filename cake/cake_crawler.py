import urllib.request as req
import bs4 as bs
import pandas as pd


def cake_crawler(category, job_type, filename):
    table = []
    page = 19

    #
    while True:
        # if job_type is None then https://www.cake.me/campaigns/software-developer/jobs?page=1
        # if job_type is it_front-end-engineer then
        # https://www.cake.me/campaigns/software-developer/jobs?page=1&profession[0]=it_front-end-engineer
        base_url = "https://www.cake.me/campaigns/" + category + "/jobs?" + "page=" + str(page)
        url = base_url + "&profession[0]=" + job_type if job_type is not None else base_url
        print("頁面:", url)
        r = req.Request(url)
        r.add_header("User-Agent",
                     "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36 Edg/135.0.0.0")
        resp = None
        try:
            resp = req.urlopen(r)
        except Exception as e:
            print("something went wrong!", e)
            break
        html = bs.BeautifulSoup(resp.read(), features="html.parser")

        jobs = html.find_all("div", {"class": "CampaignJobSearchItem_wrapper__HsxKW"})

        for job in jobs:
            job_title = job.find("a", {"class": "CampaignJobSearchItem_jobTitle__LQGW_"})

            company_name = job.find("a", {"class": "CampaignJobSearchItem_companyName__i9OXl"})
            job_desc = job.find("div", {"class": "CampaignJobSearchItem_description__aRR24"})
            job_skill_list = job.find_all("div", {"class": "Tags_item__B6Bjo"})
            # ['Golang', 'Java'] > "Golang,Java,"
            # 1. job_skill = "Golang,"
            # 2. job_skill = "Golang,Java,"
            job_skill = ""
            for skill in job_skill_list:
                job_skill = job_skill + " / " + skill.text

            job_detail = job.find("div", {"class": "CampaignJobSearchItem_features__H3moX"})
            job_infos = job_detail.find_all("div", {"class": "InlineMessage_inlineMessage____Ulc"})

            job_location = job_infos[1].find("div", {"class": "CampaignJobSearchItem_featureSegments___NcD4"}) if len(
                job_infos) >= 2 else None
            job_location = job_location.text if job_location is not None else ''

            # 如果沒有地點，下面的薪水和經驗的index要往前

            job_salary_index = 1 if job_location is None else 2
            job_salary = job_infos[job_salary_index].find("div", {"class": "InlineMessage_label__LJGjW"}).text if len(
                job_infos) >= job_salary_index + 1 else ''

            job_exp_index = 2 if job_location is None else 3
            job_exp = job_infos[job_exp_index].find("div", {"class": "InlineMessage_label__LJGjW"}).text if len(
                job_infos) >= job_exp_index + 1 else ''

            # print(job_title.text, company_name.text, job_location.text, job_salary.text, job_exp.text)

            data = {
                "職缺": job_title.text,
                "公司": company_name.text,
                "要求技能": job_skill,
                "公司簡述": job_desc.text,
                "地點": job_location,
                "薪資": job_salary,
                "經驗": job_exp,
            }
            table.append(data)

        page += 1

    df = pd.json_normalize(table)
    df.to_csv(filename + ".csv", encoding="utf-8")
    df
