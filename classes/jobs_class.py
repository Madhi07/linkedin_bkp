import logging
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from LinkedinProvider import LinkedinProvider

logging.basicConfig(
    filename="user.log",
    encoding="utf-8",
    level=logging.DEBUG,
    format="%(asctime)s | %(levelname)s  | %(filename)s:%(lineno)d | %(message)s",
)

class JobsData(LinkedinProvider):
    def get_job_details(self,job_url):
        params = {"job_url":job_url,"include_skills": "false","include_hiring_team":"false"}
        logging.info("Getting job details of a particular job")
        return self.get("/get-job-details", params=params)
    
    def search_jobs(self,body):
        logging.info("Search jobs")
        return self.post("/search-jobs", body)
    
    def search_jobs_v2(self,body):
        logging.info("Search jobs")
        return self.post("/search-jobs-v2", body)