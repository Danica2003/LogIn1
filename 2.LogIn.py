from selenium import webdriver
import Constants
import Locators
import time
import importJson

driver = webdriver.Chrome()    

def LogIn(email,password):
    driver = webdriver.Chrome()
    driver.get(Constants.BASE_URL)

    loginButton = driver.find_element_by_css_selector(Locators.log_dugme_prijavi_se_css_s)
    loginButton.click()

    emailField = driver.find_element_by_css_selector(Locators.log_polje_imejl_css_s)
    passwordField  = driver.find_element_by_css_selector(Locators.log_polje_sifra_css_s)

    emailField.send_keys(email)
    passwordField.send_keys(password)

    logInPotvrdiButton = driver.find_element_by_css_selector(Locators.log_dugme_uloguj_se_css_s)
    logInPotvrdiButton.click()


    if(driver.current_url==f"{Constants.BASE_URL}{Constants.LOGOVAN_URL}"):
        print(f"USPESAN LOG IN SA IMEJLOM: {email} I SIFROM: {password}")
    else:
        print(f"NEUSPESAN LOG IN SA IMEJLOM: {email} I SIFROM {password} REGISTRUJ SE!")
    time.sleep(3)


for podatak in importJson.DATA_T:
    LogIn(podatak["email"],podatak["password"])


