import select

from selenium import webdriver

driver=webdriver.Chrome()
driver.get("https://jqueryui.com/")
driver.implicitly_wait(30)

driver.find_element_by_xpath("//a[@href='https://jqueryui.com/datepicker/']").click()

Framewar=driver.find_element_by_xpath("//iframe[@class='demo-frame']")
driver.switch_to_frame(Framewar)

month=driver.find_element_by_class_name("ui-datepicker-month")
s1=select(month)
s1.select_by_visible_text("March")

year=driver.find_element_by_class_name("ui-datepicker-year")
s2=select(year)
s2.select_by_value("2020")


driver.find_element_by_xpath("//a[text()='1']").click()
