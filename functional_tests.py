from selenium import webdriver
import django

driver = webdriver.Firefox()

driver.get("http://localhost:8000")

assert 'Django' in driver.title
