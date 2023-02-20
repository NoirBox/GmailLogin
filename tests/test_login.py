import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service

# Paste the path to the desired web driver on your device
service = Service("C:\\Users\\.......\\webdrivers\\chromedriver.exe")

# Select browser
driver = webdriver.Chrome(service=service)
# driver = webdriver.Firefox(service=service)

# Url of test start page
url_gmail_login = "https://www.google.com/intl/en/gmail/about/"

# Enet valid email and password
validEmail = ""
validPassword = ""


class TestGmailLogin:
    def setup_method(self, method):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.wait = WebDriverWait(self.driver, 20)

    def teardown_method(self, method):
        self.driver.quit()

    def test_empty_email(self):
        self.driver.get(url_gmail_login)
        login_button = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".button--mobile-before-hero-only")))
        login_button.click()
        email_field = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#identifierId")))
        email_field.send_keys("")
        email_field.send_keys(Keys.ENTER)
        error_message = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".RxsGPe")))
        assert error_message.text == "Enter an email or phone number"

    def test_invalid_email(self):
        self.driver.get(url_gmail_login)
        login_button = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".button--mobile-before-hero-only")))
        login_button.click()
        email_field = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#identifierId")))
        email_field.send_keys("invalid@email")
        email_field.send_keys(Keys.ENTER)
        error_message = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".RxsGPe")))
        assert error_message.text == "Enter a valid email or phone number"

    def test_valid_login_with_empty_password(self):
        self.driver.get(url_gmail_login)
        login_button = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".button--mobile-before-hero-only")))
        login_button.click()
        email_field = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#identifierId")))
        email_field.send_keys(validEmail)
        email_field.send_keys(Keys.ENTER)
        password_field = self.wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id=\"password\"]/div[1]/div/div[1]/input")))
        password_field.send_keys(Keys.ENTER)
        error_message = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".uSvLId")))
        assert error_message.text == "Enter a password"

    def test_valid_login_with_invalid_password(self):
        self.driver.get(url_gmail_login)
        login_button = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".button--mobile-before-hero-only")))
        login_button.click()
        email_field = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#identifierId")))
        email_field.send_keys(validEmail)
        email_field.send_keys(Keys.ENTER)
        password_field = self.wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id=\"password\"]/div[1]/div/div[1]/input")))
        password_field.send_keys("invalidPassword")
        password_field.send_keys(Keys.ENTER)
        error_message = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".uSvLId")))
        assert error_message.text == "Wrong password. Try again or click Forgot password to reset it."

    def test_valid_login_and_password(self):
        self.driver.get(url_gmail_login)
        login_button = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".button--mobile-before-hero-only")))
        login_button.click()
        email_field = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#identifierId")))
        email_field.send_keys(validEmail)
        email_field.send_keys(Keys.ENTER)
        password_field = self.wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id=\"password\"]/div[1]/div/div[1]/input")))
        password_field.send_keys(validPassword)
        password_field.send_keys(Keys.RETURN)
        user_icon = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".gbii")))
        assert user_icon.is_displayed()
