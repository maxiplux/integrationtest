import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("--no-sandbox")
options.add_argument("--headless")
print ("Ready and Goooooo!")
driver = webdriver.Chrome('chromedriver', chrome_options=options) 
driver.get('http://www.google.com/xhtml');
time.sleep(5) # Let the user actually see something!
search_box = driver.find_element_by_name('q')
search_box.send_keys('blog.juanfrancisco.net')
search_box.submit()

time.sleep(3) # Let the user actually see something!
assert  'blog.juanfrancisco.net' in driver.page_source
driver.quit()
print ("Done!")