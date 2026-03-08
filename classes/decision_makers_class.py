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

class DecisionMakerData(LinkedinProvider):
    def get_decision_makers(self,body):
        logging.info("Search Decision makers data")
        return self.post("/search-decision-makers",body)