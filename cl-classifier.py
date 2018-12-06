from selenium import  webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys


class CraiglistJobScraper(object):
    def __init__(self):
        # self.job_type = job_type
        self.url = 'https://paris.craigslist.fr/d/temp-jobs/search/ggg?lang=en&cc=gb'
        self.driver = webdriver.Chrome()
        self.delay = 3

    def run_driver(self):
        self.driver.get(self.url)
        try:
            wait = WebDriverWait(self.driver, self.delay)
            wait.until(EC.presence_of_element_located((By.ID, "searchform")))
        except TimeoutException:
            print("Page took too long to load")

    def close_driver(self):
        self.driver.close()

    def get_post_titles(self):
        all_posts = self.driver.find_elements_by_css_selector(".result-title.hdrlnk")
        post_title_list = [post.text for post in all_posts]
        return post_title_list

    def get_post_urls(self):
        all_posts = self.driver.find_elements_by_css_selector(".result-title.hdrlnk")
        post_url_list = [post.get_attribute('href') for post in all_posts]
        return post_url_list

    def get_post_desc(self, links):
        post_desc_list = []
        for link in links:
            self.driver.get(link)
            self.driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + 't')
            self.driver.get(link)
            post_desc_list.append(self.driver.find_elements_by_id('postingbody'))

        return post_desc_list


# scraper object created, functions called
scraper = CraiglistJobScraper()
scraper.run_driver()
titles = scraper.get_post_titles()
urls = scraper.get_post_urls()

print(str(len(titles)) + ' hits found from ' + str(len(titles)))
scraper.close_driver()

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from posts import *

keys = []
values = []
for key, value in data.items():
    keys.append(key)
    values.append(value)

vector = CountVectorizer()
counts = vector.fit_transform(values)

clf = MultinomialNB()
targets = keys
clf.fit(counts, targets)
titles_counts = vector.transform(titles)
pred = clf.predict(titles_counts)

result_dictionary = dict(zip(titles, pred))
for key, value in result_dictionary.items():
    print(key + " : " +  value + "\n")