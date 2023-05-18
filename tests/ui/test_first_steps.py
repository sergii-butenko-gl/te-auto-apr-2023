from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def test_login_negative():
    # created a driver
    driver = webdriver.Chrome()
    
    # open login page
    driver.get("https://github.com/login")

    # enter wrong/correct email
    login_fld = driver.find_element(By.ID, "login_field")
    login_fld.send_keys("some_incoorect_email@gmail.com")
    
    # enter wrong pass
    pass_fld = driver.find_element(By.ID, "password")
    pass_fld.send_keys("sldnfkbsdjfnkjsndfjk")
    
    # click sign+in button
    signin_btn = driver.find_element(By.NAME, "commit")
    signin_btn.click()

    # check error message

    driver.quit()