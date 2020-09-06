from splinter import Browser
from selenium import webdriver
import random
from time import sleep
from feedparser import parse as p

maxsearches = 50  # Most number of searches performed per run
minsearches = 30  # Minimum number of searches performed per run
maxdelay = 500  # Max delay between searches.
#username = 'USERNAME@live.com/@outlook.com/@msn.com'
#password = 'PASSWORD'
username = 'bob@live.com'
password = 'PASSWORD'

StackExchangeFeed = ""  # URL for a StackExchange question feed.  Ignored if empty.

# Load a list of English words
words = open('words.txt','r').read().split('\n')
print('\nPartial Wordlist: \n')
for i in range(0,10):
    print(random.choice(words))

def fQueryGen(partial):
    '''Scrapes a query from StackExchange if URL present.  Otherwise generates a fake query locally.'''
    global StackExchangeFeed
    if len(StackExchangeFeed) != 0:
        try:
            return random.choice([elem['title'][0:-20] for elem in p(StackExchangeFeed)['entries']])
        except:
            print("Stack Exchange failed!")
            return queryGen(partial)
    else:
        return queryGen(partial)

def queryGen(partial):
    '''Generates a fake search locally.'''
    struct=random.choice(range(0,5))
    print("Structure: " + str(struct))
    if struct == 0:
        query = "how to " + partial
    if struct == 1:
        query = "what is " + partial
    if struct == 2:
        query = "define " + partial
    if struct == 3:
        query = "buy " + partial
    if struct == 4:
        query = partial + "setup"
    if struct == 5:
        query = "how long until " + partial
    return query


def sentence(wordlist):
    '''Returns a random word.'''
    return wordlist[int(random.random()*len(wordlist))]

def login(b):
    '''Logs browser b into Windows Live.'''
    b.visit('https://login.live.com')
    b.fill('loginfmt', username)
    sleep(1)
    login = b.find_by_id('idSIButton9') # Username button
    login.click() # Submit username
    sleep(2)
    b.find_by_id('i0118').fill(password) # Password button
    login = b.find_by_id('idSIButton9')
    login.click() # Submit password
    return b

b = Browser("chrome", user_agent="Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4254.2 Safari/537.36")
b = login(b)
sleep(1)
# Perform random number of desktop searches.
for j in range(0,random.choice(range(minsearches,maxsearches))):
     b.visit('https://www.bing.com')
     sleep((random.random() * 2)+1)
     b.fill('q',fQueryGen(sentence(words))) # Type the search query
     go = b.find_by_id('sb_form_go').first
     sleep(random.random() * 5)
     go.click() # Search!
     sleep(random.random() * 20) # Random delay
b.quit()

# Perform random number of mobile searches.
mobile_emulation = {"deviceName": "Nexus 5"} # Set user agent to Nexus 5
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("mobileEmulation",mobile_emulation)
b = Browser("chrome",options=chrome_options)
b = login(b)
for j in range(0,random.choice(range(minsearches,maxsearches))):
    b.visit('https://www.bing.com')
    sleep((random.random() * 2)+1)
    b.fill('q',fQueryGen(sentence(words))) # Type the search query
    go = b.find_by_id('sbBtn').first
    sleep(random.random() * 5)
    go.click() # Search!
    sleep(random.random() * 20) # Random delay
b.quit()
