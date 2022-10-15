from selenium import webdriver
import time

browser = webdriver.Chrome(executable_path='C:\Chromedriver\chromedriver')
browser.get('https://www.google.com/maps/@10.54063,76.1283185,7z')
time.sleep(2)


def searchplace():
    place = browser.find_element_by_class_name('tactile-searchbox-input')
    place.send_keys('kochi')
    Sumbit = browser.find_element_by_xpath('/html/body/div[3]/div[9]/div[3]/div[1]/div[1]/div[1]/div[2]/div[1]/button')
    Sumbit.click()
searchplace()    

def directions():
    time.sleep(5)
    direction = browser.find_element_by_xpath("/html/body/div[3]/div[9]/div[9]/div/div/div[1]/div[2]/div/div[1]/div/div/div[4]/div[1]/button")
    direction.click()
directions()    


def find():
    time.sleep(6)
    find = browser.find_element_by_xpath("/html/body/div[3]/div[9]/div[3]/div[1]/div[2]/div/div[3]/div[1]/div[1]/div[2]/div[1]/div/input")
    find.send_keys('wayanad')
    time.sleep(6)
    search = browser.find_element_by_xpath("/html/body/div[3]/div[9]/div[3]/div[1]/div[2]/div/div[3]/div[1]/div[1]/div[2]/button[1]")
    search.click()
find()    


