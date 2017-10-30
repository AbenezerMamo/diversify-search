import requests
import json
import webbrowser
import sys
import re
from bs4 import BeautifulSoup

# 1. Query Google with a string and get back the top 10 results for the query
# 2. Generate 10 different variations of the query string - store it
# 3. Make batched queries to Google with the 10 variations of the query - store the top result in each
# 4. Return batched results of the diverse results that originated from the original and the variatied query

# Query
diverse_results = []
searches = ["pro", "con", "for", "against", "Support ", "Remove ", "How can we improve ", "How can we avoid ", "How can we avoid ", "What is wrong with ", "What is good about ", "What is bad about ", "What do republicans think about ", "What do democrats think about "]

def queryGoogle(query_string, term):
    r = requests.get("http://google.com/search?q=" + term + query_string)
    data = r.content
    soup = BeautifulSoup(data, 'html.parser')
    # for item in soup.children:
    #     print(item)
    results = soup.findAll(attrs={'class': 'g'})
    search_result = results[0].a.get("href")
    diverse_results.append(re.search("(?P<url>https?://[^\s]+)", str(search_result)).group("url"))
    # if (re.search("(?P<url>https?://[^\s]+)", str(results[0])).group("url")) != None:
    #     diverse_results.append(re.search("(?P<url>https?://[^\s]+)", str(results[0])).group("url"))


    return results[0]

def diverse_search(query_string):
    for term in searches:
        queryGoogle(query_string, term)



# Get the user's query
query = input('Search: ')
print("Searching...\n")
search = diverse_search(query)
diverse_results = set(diverse_results)
for diverse_result in diverse_results:
    print("Result: " + diverse_result + "\n")
    webbrowser.open(diverse_result)
