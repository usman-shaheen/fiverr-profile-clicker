from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.common.by import By

path="C:\\Program Files (x86)\chromedriver.exe"

url="https://www.fiverr.com/your-username"

driver=webdriver.Chrome(path)
driver.get(url)

#search in the search box
# search=driver.find_element_by_name('s')
# search.send_keys('code')
# search.send_keys(Keys.RETURN)

#select main section and perform action in it
try:
   main=WebDriverWait(driver,10).until(
       EC.presence_of_element_located((By.CLASS_NAME,'gigs-wrapper') )
   )
   articles=main.find_elements_by_class_name('gig-card-layout')
   for article in articles:
       title=article.find_element_by_class_name('text-display-7')
       sellername=article.find_element_by_class_name('seller-name')
       # href=title.find_element_by_xpath('//a[@href]')
       # print(href.get_attribute('href'))
       title.click()
       driver.switch_to.window(driver.window_handles[0])
       time.sleep(3)
       print('success')

except:
   # driver.quit()
   print('error')



