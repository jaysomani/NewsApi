# data_models.py
class Article:
    def __init__(self, title, link, description, pub_date):
        self.title = title
        self.link = link
        self.description = description
        self.pub_date = pub_date
