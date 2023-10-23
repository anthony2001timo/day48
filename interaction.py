from selenium import webdriver

chrome_driver_path = "/Users/philippmuellauer/Development/chromedriver"
driver = webdriver.chrome(chrome_driver_path)

driver.get("https://en.wikipedia.org/wiki/Main_Page")
article_count = driver.find_element_by_css_selector("#articlecount a")
print(article_count.text)
