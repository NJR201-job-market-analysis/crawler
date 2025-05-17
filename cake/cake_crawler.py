import urllib.request as req
import bs4 as bs
import pandas as pd
import urllib3.exceptions


def cake_crawler(job_type, filename):
    table = []
    page = 1

    while True:
        url = "https://www.cake.me/campaigns/software-developer/jobs?profession[0]=" + job_type + "&page=" + str(page)
        print("頁面:", url)
        r = req.Request(url)
        r.add_header("User-Agent", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36 Edg/135.0.0.0")
        resp = None
        try:
            resp = req.urlopen(r)
        except:
            print("something went wrong!")
            break
        html = bs.BeautifulSoup(resp.read(), features="html.parser")

        jobs = html.find_all("div", {"class":"CampaignJobSearchItem_wrapper__HsxKW"})

        for job in jobs:
            job_title = job.find("a", {"class":"CampaignJobSearchItem_jobTitle__LQGW_"})
            company_name = job.find("a", {"class":"CampaignJobSearchItem_companyName__i9OXl"})
            job_desc = job.find("div", {"class":"CampaignJobSearchItem_description__aRR24"})

            job_detail = job.find("div", {"class":"CampaignJobSearchItem_features__H3moX"})
            job_infos = job_detail.find_all("div", {"class":"InlineMessage_inlineMessage____Ulc"})

            job_location = job_infos[1].find("div", {"class":"CampaignJobSearchItem_featureSegments___NcD4"})
            job_salary = job_infos[2].find("div", {"class":"InlineMessage_label__LJGjW"})
            job_exp = job_infos[3].find("div", {"class":"InlineMessage_label__LJGjW"}).text if len(job_infos) >= 4 else ''

            # print(job_title.text, company_name.text, job_location.text, job_salary.text, job_exp.text)

            data = {
                "職缺": job_title.text,
                "公司": company_name.text,
                "公司簡述": job_desc.text,
                "地點": job_location.text,
                "薪資": job_salary.text,
                "經驗": job_exp,
            }
            table.append(data)

        page += 1

    df = pd.json_normalize(table)
    df.to_csv(filename + ".csv", encoding="utf-8")
    df