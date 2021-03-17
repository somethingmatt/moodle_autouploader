from helium import *
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from datetime import date, timedelta
import time

# Path to file with password
# alternatively it can be "hard-set" as value in PASSWORD
f = open("./path_to/password.txt","r")
PASSWORD = f.read()
# PASSWORD = "password"
f.close()

# set username for moodle login
USERNAME = "user_name"

# Path to "Anwesenheits-Formblatt"
fPATH = "C:/path/to/file/Anwesenheit-Formblatt-20210317.pdf"

# set Selenium-Driver from Helium-instance
# open testbrowser on moodle login page
driver = start_chrome("https://moodle.oszimt.de/login/index.php")

# set current date and searchtext
today = date.today().strftime("%d.%m.%Y")
searchText = 'Anwesenheit ' + today

# insert USERNAME and PASSWORD into login form fields and login
write(USERNAME, into='Anmeldename')
write(PASSWORD, into='Kennwort')
click("Login")

# main function, gets Selenium driver
def main(driver):
    find_or_restart(driver, searchText)

# checks site if text is existent and opens page
# can be improved with driver.refresh() and loop
def find_or_restart(driver, text):
    # BP Seite
    go_to("https://moodle.oszimt.de/course/view.php?id=2326")
    wait = WebDriverWait(driver, 2)
    try:
        elem = driver.find_element_by_xpath(".//span[contains(@class, 'instancename') and text()='" + text + "']").click()
        click_or_restart(driver)

    except NoSuchElementException:
        print("no")
        # waits 90 s until "refresh"
        time.sleep(90)
        find_or_restart(driver, text)

# on submit page check for button
# if there already has been a submit it changes to "Abgabe bearbeiten"
# if no button, page is refreshed
# improvement with loop
def click_or_restart(driver):
    if Button("Abgabe hinzufügen").exists():
        click("Abgabe hinzufügen")
        time.sleep(3)
        drag_file(r""+ fPATH +"", to="Dateien zum Hochladen hier loslassen")
        time.sleep(2)
        driver.find_element_by_id("id_submitbutton").click()
    elif Button("Abgabe bearbeiten").exists():
        click("Abgabe bearbeiten")
        time.sleep(3)
        drag_file(r""+ fPATH +"", to="Dateien zum Hochladen hier loslassen")
        time.sleep(2)
        driver.find_element_by_id("id_submitbutton").click()
        time.sleep(1)
    else:
        print("refresh")
        driver.refresh()
        print("refresh done")
        time.sleep(2)
        click_or_restart(driver)

    end_prgm(driver)

# kill driver and helium instance
def end_prgm(driver):
    kill_browser()
    driver.quit()

# run program
main(driver)
