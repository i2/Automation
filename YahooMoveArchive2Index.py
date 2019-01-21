from selenium import webdriver
from selenium.webdriver.firefox.webdriver import FirefoxProfile
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time

profile = FirefoxProfile("/Users/me/Library/Application Support/Firefox/Profiles/ne66zwyu.default")
driver = webdriver.Firefox(profile)
driver.get('https://mail.yahoo.com/neo/launch?.src=ym&reason=myc')
driver.find_element_by_xpath('//div[3]/div/div/ul/li[5]/a/span').click()

while 1:
    driver.find_element_by_tag_name('body').send_keys(Keys.COMMAND + 'a')
    driver.find_element_by_tag_name('body').send_keys('d')
    driver.find_element_by_tag_name('body').send_keys('0')

#driver.quit()

