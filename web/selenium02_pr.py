from selenium import webdriver
import time
options = webdriver.ChromeOptions()
# options.add_argument('headless')

options.add_argument("disable-gpu")   
options.add_argument("lang=ko_KR")    
options.add_argument('user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36')  # user-agent 

driver = webdriver.Chrome('./py_projects/web/chromedriver.exe', chrome_options = options)

driver.get("http://www.yes24.com/24/Category/BestSeller")

time.sleep(3)
tag = driver.find_element_by_id('bestList').find_elements_by_tag_name("ol").find_element_by_class_name("copy")

for tmp in tag:
    print(tmp.text.split("\n"))