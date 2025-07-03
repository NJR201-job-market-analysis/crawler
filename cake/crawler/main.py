from crawler.cake_crawler import cake_crawler
from crawler.cake_database import CakeDatabase

# https://www.cake.me/campaigns?locationId=1&page=1

# 測試用
result = cake_crawler("top500-companies", "it")
# CakeDatabase().insert_jobs(result)
# cake_crawler("software-developer", None, "cakesoftwaredeveloperjobs")
# cake_crawler("digital-nomad", "it", "cakedigitalnomadjobs")

