from cake_crawler import cake_crawler

# https://www.cake.me/campaigns?locationId=1&page=1

# cake_crawler("it_front-end-engineer", "cakefrontendjobs")
# cake_crawler("it_back-end-engineer", "cakebackendjobs")
# cake_crawler("it_devops-system-admin", "cakedevopsjobs")
# cake_crawler("it_qa-test-engineer", "cakeqajobs")
# cake_crawler("it_database", "cakedatabasejobs")

cake_crawler("remote-work", "it", "cakeromoteworkjobs")
cake_crawler("software-developer", None, "cakesoftwaredeveloperjobs")
cake_crawler("digital-nomad", "it", "cakedigitalnomadjobs")

