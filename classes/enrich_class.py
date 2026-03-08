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

class EnrichData(LinkedinProvider):

    def get_enrich_data(self,linkedin_url):
        params = {"linkedin_url" : linkedin_url}
        logging.info("Enrich Lead data")
        return self.get("/enrich-lead", params=params)
    
    def get_extra_profile_data(self,linkedin_url):
        params = {"linkedin_url" : linkedin_url}
        logging.info("Extra profile data")
        return self.get("/get-extra-profile-data", params=params)
    
    def get_years_of_experience(self,linkedin_url):
        params = {"linkedin_url" : linkedin_url}
        logging.info("Get total years of experience")
        return self.get("/get-year-of-experiences", params=params)
    
    def get_Profile_pdf_cv(self,linkedin_url):
        params = {"linkedin_url" : linkedin_url}
        logging.info("Getting user's Resume or CV")
        return self.get("/get-profile-pdf-cv", params=params)
