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

class CompanyData(LinkedinProvider):
    def get_company_data_by_url(self, linkedin_url):
        params = {"linkedin_url": linkedin_url}
        logging.info("Getting company data")
        return self.get(path="/get-company-by-linkedinurl", params=params)
    
    def get_company_data_by_domain(self, domain):
        params = {"domain": domain}
        logging.info("Getting company data")
        return self.get(path="/get-company-by-domain", params=params)
    
    def get_company_data_by_id(self, company_id):
        params = {"company_id": company_id}
        logging.info("Getting company data")
        return self.get(path="/get-company-by-id", params=params)
    
    def filter_companies(self, body):
        logging.info("Filter companies")
        return self.post(path="/search-companies-instantly", body=body)
