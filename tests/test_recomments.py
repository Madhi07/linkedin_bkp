import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from classes.recommendation_class import RecommendedData

recom = RecommendedData()

linkedin_url = "https://www.linkedin.com/in/premkumar-jagadeesan-538a7658/"
recom_given = recom.get_recommendation_given(linkedin_url)
print(recom_given)

recom_received = recom.get_recommendation_received(linkedin_url)
print(recom_received)