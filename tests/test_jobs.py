import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from classes.jobs_class import JobsData

jobs = JobsData()


# job_url = "https://www.linkedin.com/jobs/view/4277707892"
# job_details = jobs.get_job_details(job_url)
# print(job_details)

# search_jobs = {
#     "keywords": "AI",
#     "geo_code": 92000000,
#     "date_posted": "Any time",
#     "experience_levels": [],
#     "company_ids": [
#     ],
#     "title_ids": [],
#     "onsite_remotes": [],
#     "functions": [],
#     "industries": [],
#     "job_types": [],
#     "sort_by": "Most relevant",
#     "easy_apply": "false",
#     "under_10_applicants": "false",
#     "start": 0
# }
# searched_jobs = jobs.search_jobs(search_jobs)
# print(searched_jobs)


# search_jobs_v2 = {
#   "location": "coimbatore",
#   "keywords": "startup",
#   "start": 0
# }
# searched_jobs_v2 = jobs.search_jobs_v2(search_jobs_v2)
# print(searched_jobs_v2)