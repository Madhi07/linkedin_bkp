import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from classes.decision_makers_class import DecisionMakerData

decision = DecisionMakerData()

search_decision_makers =  {
    "company_ids": [
    "163640",
    "75637041",
    "162479",
    "19080118"
    ],
    "title_keywords": [
    "CEO",
    "Founder",
    "Owner"
    ],
    "geo_codes": [
    103644278,
    102299470
    ],
    "limit": "25"
}
searched_decision_makers = decision.get_decision_makers(search_decision_makers)
print(searched_decision_makers)