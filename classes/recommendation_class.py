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

class RecommendedData(LinkedinProvider):

    def get_recommendation_given(self,linkedin_url):
        params = {"linkedin_url" : linkedin_url}
        logging.info("Recommendation Given data")
        return self.get("/get-recommendations-given",params=params)
    
    def get_recommendation_received(self,linkedin_url):
        params = {"linkedin_url" : linkedin_url}
        logging.info("Recommendation Received data")
        return self.get("/get-recommendations-received",params=params)