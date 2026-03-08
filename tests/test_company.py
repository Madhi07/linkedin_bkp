import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from classes.company_class import CompanyData

company = CompanyData()

# linkedin_url = "https://www.linkedin.com/company/episyche/"
# company_data_by_url = company.get_company_data_by_url(linkedin_url)
# print("Company data: ", company_data_by_url)

# domain = "zoho.com"
# company_data_by_domain = company.get_company_data_by_domain(domain)
# print("Company data: ", company_data_by_domain)

# company_id = "96966289"
# company_data_by_company_id = company.get_company_data_by_id(company_id)
# print("Company data", company_data_by_company_id)

# search_body = {
#     "company_name": "",
#     "industry": "Software Development",
#     "employee_range": "",
#     "city": "coimbatore",
#     "state": "tamil nadu",
#     "country": "",
#     "count": 100,
#     "sort_by": "follower_count",
#     "page": 1
# }
# filtered_companies = company.filter_companies(search_body)
# print("Search results :", filtered_companies)
