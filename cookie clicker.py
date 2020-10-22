from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager

URL_SECTION = "https://orteil.dashnet.org/cookieclicker"
TO_CLICK = "bigCookie"
FOR_CLICK_COUNT = "cookies"
TO_UPGRADE = "productPrice" 
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get(URL_SECTION)

driver.implicitly_wait(5)

click = driver.find_element_by_id(TO_CLICK)
click_count = driver.find_element_by_id(FOR_CLICK_COUNT)
items = [driver.find_element_by_id(TO_UPGRADE + str(i)) for i in range(1,-1,-1)]

actions = ActionChains(driver)
actions.click(click)

for i in range(5000000):
	actions.perform()
	count = int(click_count.text.split(" ")[0])
	for item in items:
		value = int(item.text)
		if value <= count:
			upgrade_actions = ActionChains(driver)
			upgrade_actions.move_to_element(item)
			upgrade_actions.click()
			upgrade_actions.perform() 