from selenium import webdriver

browser=webdriver.Chrome(r"C:\Users\a\AppData\Local\Google\Chrome\Application\chromedriver.exe")
browser.get("http://www.taobao.com")
input_first=browser.find_element_by_id('q')
input_second=browser.find_element_by_id()
print(browser.page_source)
browser.close()
