import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from classes.enrich_class import EnrichData

enrich = EnrichData()

linkedin_url = "https://www.linkedin.com/in/premkumar-jagadeesan-538a7658/"
# enriched_data = enrich.get_enrich_data(linkedin_url)
# print(enriched_data)

total_experience = enrich.get_years_of_experience(linkedin_url)
print(total_experience)

extra_data = enrich.get_extra_profile_data(linkedin_url)
print(extra_data)

resume_cv = enrich.get_Profile_pdf_cv(linkedin_url)
print(resume_cv)