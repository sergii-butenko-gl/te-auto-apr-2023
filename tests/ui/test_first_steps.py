
from selenium.webdriver.common.by import By


def test_signup_negative(wed_driver):
    wed_driver.get("https://github.com/login")

    login_fld = wed_driver.find_element(By.ID, "login_field")
    login_fld.send_keys("some_incoorect_email@gmail.com")
    
    pass_fld = wed_driver.find_element(By.ID, "password")
    pass_fld.send_keys("sldnfkbsdjfnkjsndfjk")
    
    signin_btn = wed_driver.find_element(By.NAME, "commit")
    signin_btn.click()

    login_alert = wed_driver.find_element(By.CLASS_NAME, "js-flash-alert")

    assert "Incorrect username or password" in login_alert.text



def test_signup_negative_pom(github_ui):
    github_ui.open_login_page()
    github_ui.enter_creds(username, password)
    github_ui.click_submit_btn()

    assert github_ui.check_allert_message()
