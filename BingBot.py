from splinter import Browser
from selenium import webdriver
import random
from time import sleep

searches = 30
mobilesearches = 30
maxdelay = 500
username = 'USERNAME@live.com/@outlook.com/@msn.com'
password = 'PASSWORD'

words = open('words.txt','r').read().split('\n')
print('\nPartial Wordlist: \n')
for i in range(0,20):
    print(words[i])
def queryGen(partial):
    struct=random.choice(range(0,4))
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
    return query


def sentence(wordlist):
    #words = list()
    # while len(words) < 3:
    #     word = random.choice(wordlist)
    #     if 'ing' in word:
    #         words.append(word)
    #     if 'logy' in word:
    #         words.append(word)
    #     if 'able' in word:
    #         words.append(word)
    #     if 'ee' in word:
    #         words.append(word)
    #     if 'ly' in word:
    #         words.append(word)
    #print(words)
    return wordlist[int(random.random()*len(wordlist))]

def login(b):
    b.visit('https://login.live.com')
    b.fill('loginfmt', username)
    sleep(1)
    login = b.find_by_id('idSIButton9')
    login.click()
    sleep(2)
    b.find_by_id('i0118').fill(password)
    login = b.find_by_id('idSIButton9')
    login.click()
    return b

b = Browser("chrome")
b = login(b)
sleep(1)
for j in range(0,searches):
     b.visit('https://www.bing.com')
     sleep((random.random() * 2)+1)
     b.fill('q',queryGen(sentence(words)))
     go = b.find_by_id('sb_form_go').first
     sleep(random.random() * 5)
     go.click()
     sleep(random.random() * 20)
b.quit()


mobile_emulation = {"deviceName": "Google Nexus 5"}
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("mobileEmulation",mobile_emulation)
b = Browser("chrome",options=chrome_options)
b = login(b)
for j in range(0,mobilesearches):
    b.visit('https://www.bing.com')
    sleep((random.random() * 2)+1)
    b.fill('q',queryGen(sentence(words)))
    go = b.find_by_id('sbBtn').first
    sleep(random.random() * 5)
    go.click()
    sleep(random.random() * 20)