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

class PostData(LinkedinProvider):
    def get_posts_by_person(self,linkedin_url):
        params = {"linkedin_url": linkedin_url, "type" : "posts"}
        logging.info("Getting posts data")
        return self.get(path="/get-profile-posts", params=params)
    
    def get_post_comments(self,urn):
        params = {"urn" : urn}
        logging.info("Getting post comments")
        return self.get(path="/get-post-comments", params=params)
    
    def get_post_reactions(self,urn):
        params = {"urn" : urn}
        logging.info("Getting post reactions")
        return self.get(path="/get-post-reactions", params=params)
    
    def get_post_details(self,urn):
        params = {"urn" : urn}
        logging.info("Getting post details")
        return self.get(path="/get-post-details", params=params)
    
    def get_posts_by_company(self, linkedin_url):
        params = {"linkedin_url" : linkedin_url, "sort_by":"recent"} #sort_by : top or recent
        logging.info("Getting posts data from company")
        return self.get(path="/get-company-posts", params=params)
    
    def search_posts(self, body):
        logging.info("Search Posts")
        return self.post(path="/search-posts", body=body)
        