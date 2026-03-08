# from posts_class import PostData
# from ..posts_class import PostData
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from classes.posts_class import PostData
posts = PostData()


# linkedin_url = "https://www.linkedin.com/in/premkumar-jagadeesan-538a7658/"
# person_posts = posts.get_posts_by_person(linkedin_url)
# print(person_posts)

# urn_comments = "7358329017885773826"
# post_comments = posts.get_post_comments(urn_comments)
# print(post_comments)

# urn_rections = "7358329017885773826"
# post_reactions = posts.get_post_reactions(urn_rections)
# print(post_reactions)

# urn_details = "7358329017885773826"
# post_details = posts.get_post_details(urn_details)
# print(post_details)

# company_linkedin_url = "https://www.linkedin.com/company/kovaico/"
# company_posts = posts.get_posts_by_company(company_linkedin_url)
# print(company_posts)

search_posts = {
    "search_keywords": "AI",
    "sort_by": "Latest",
    "date_posted": "",
    "content_type": "",
    "from_member": [
    "ACoAAAxCmnwBRsVWmVIxeUBoSlo33iq-9s8PRdY"
    ],
    "from_company": [],
    "mentioning_member": [],
    "mentioning_company": [],
    "author_company": [],
    "author_industry": [],
    "author_keyword": "",
    "page": 1
}
searched_posts = posts.search_posts(search_posts)
print(searched_posts)