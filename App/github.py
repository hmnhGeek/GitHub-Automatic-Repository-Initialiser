from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from getpass import getpass as gp
import argparse as ap
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time, os

def start(user, passw, repo):
    
    chrome = os.path.dirname(__file__)+'/../drivers/chromedriver.exe'
    browser = webdriver.Chrome(chrome)

    browser.get('https://github.com/')
    browser.find_element_by_xpath("/html/body/div[1]/header/div/div[2]/div/span/div/a[1]").click()

    username = browser.find_element_by_xpath('//*[@id="login_field"]')
    password = browser.find_element_by_xpath('//*[@id="password"]')

    username.send_keys(user)
    password.send_keys(passw)

    
    browser.find_element_by_xpath('//*[@id="login"]/form/div[4]/input[3]').click()

    # make repo now
    browser.find_element_by_xpath('//*[@id="your_repos"]/div/div[1]/a').click()

    elem  = WebDriverWait(browser, 50).until(EC.visibility_of_element_located((By.ID, 'repository_name')))
    repo_name = browser.find_element_by_id('repository_name')
    repo_name.send_keys(repo)

    time.sleep(5)

    browser.find_element_by_xpath('//*[@id="repository_auto_init"]').click()
    browser.find_element_by_xpath('//*[@id="new_repository"]/div[4]/button').click()

    browser.find_element_by_xpath('//*[@id="user-links"]/li[3]/details/summary/img').click()
    browser.find_element_by_xpath('//*[@id="user-links"]/li[3]/details/ul/li[9]/form/button').click()
    

parser = ap.ArgumentParser()
parser.add_argument('--user', action = "store", type = str, dest = 'u', help = "Github username!!")
parser.add_argument('--repo', action = "store", type = str, dest = 'r', help = "Github repository!!")

args = parser.parse_args()

if args.u and args.r:
    passwo = gp("Password: ")
    start(args.u, passwo, args.r)
