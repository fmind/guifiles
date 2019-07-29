#!/usr/bin/env python3

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("http://www.google.com")

form = driver.find_element_by_name("q")
form.send_keys("selenium documentation")
form.submit()
