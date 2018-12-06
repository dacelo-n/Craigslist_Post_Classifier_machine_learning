## Craigslist_Post_Classifier_machine_learning
The main goal of this project is to take post titles, and or descriptions and run them through machine learning algorithms 
to determine if they are 'legit' or 'suspicious' or any criteria that you would like.
It is based off of my earlier web scraping Craigslist project 
[craiglist-job-scraper.py](https://github.com/dacelo-n/web-scraping-automation/blob/master/craigslist-job-scraper.py)
## Prereqs
You need to install 'selenium and 'sklearn' either via the command line
`pip install selenium`
`pip install sklearn`

Or if you're using Pycharm, via the **Project Interpreter** option in **Settings** under **File**.

You'll also need to install the Chrome webdriver, with instructions and file [here](http://chromedriver.chromium.org/downloads)

## Changing the url

The value of `self.url = ` should be changed to your local version of Craigslist and to the section you want to search in.
For example, you can run the search under **Jobs**, **Temp Jobs**, **Community**, **Housing**, etc etc.

```
  def __init__(self):
        # replace the url with your local version of Craiglist. Ive been using 'temp jobs' but
        # you can link to any part of the site you wish to search in.
        self.url = 'https://paris.craigslist.fr/d/temp-jobs/search/ggg?lang=en&cc=gb'
        self.driver = webdriver.Chrome()
        self.delay = 3

```
## Changing the training data in data.py
Next you should comment out the following block of code:
```
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from posts import *

# from the dictionary 'data', all the keys and values are 
# stored separately into lists
keys = []
values = []
for key, value in data.items():
    keys.append(key)
    values.append(value)

# an object of CountVectorizer is created then all the values 
# are transformed into a matrix of counts
vector = CountVectorizer()
counts = vector.fit_transform(values)
# we intialize our classifier, assigning keys as our targets
clf = MultinomialNB()
targets = keys
# we then train our data, the counts derived from the values
# with our keys
clf.fit(counts, targets)
# the titles of the Craigslist postings that we gathered are then
# also transformed into a matrix of counts in order to compare them
titles_counts = vector.transform(titles)
# it makes its prediction
pred = clf.predict(titles_counts)

# we can know see a large amount of Craiglists job (or any other type) postings
# and the corresponding predictions on them. 
# in our case, 'legit' vs 'suspicious' ads
result_dictionary = dict(zip(titles, pred))
for key, value in result_dictionary.items():
    print(key + " : " +  value + "\n")
```
And uncomment `print(titles)`. Run the program. You should now have on the display, a printed list `titles` with all the post 
titles of the given url link. 

You know need to do the painstaking task of copy/pasting it to `data.py` and giving whatever **labels** as the keys for each title.
What I mean by that is, its your turn to add what kind of classifications you want to assign to each title. Whether it be 'spam', 
'suspicious', 'legit;, 'good', 'bad', etc.
## Running the program
Now you can uncomment the above pieces of code and run the program. You should be left with a list of titles followed by their
classification.
