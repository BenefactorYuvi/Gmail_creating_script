from selenium import webdriver
import time
import selenium
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--incognito")

s=Service("C:\\Users\\Yuvi\\Downloads\\chromedriver_win32\\chromedriver.exe")
driver = webdriver.Chrome(service=s)
driver.get("https://accounts.google.com/signin/v2/identifier?service=mail&passive=true&rm=false&continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&ss=1&scc=1&ltmpl=default&ltmplcache=2&emr=1&osid=1&flowName=GlifWebSignIn&flowEntry=ServiceLogin")

time.sleep(1)

create_account = driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[2]/div/div/div[1]/div/button/span').click()
myself = driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[2]/div/div/div[2]/div/ul/li[1]/span[2]').click()

first_name = input('Enter first name > ')
last_name = input('Enter last name > ')
username = input('Enter username > ')
password = input('Enter password > ')

time.sleep(6)

fname_textbox = driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[2]/div[1]/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div[1]/div[1]/div/div[1]/div/div[1]/input')
fname_textbox.send_keys(first_name)

lname_textbox = driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[2]/div[1]/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div[1]/div[2]/div/div[1]/div/div[1]/input')
lname_textbox.send_keys(last_name)

username_textbox = driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[2]/div[1]/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[2]/div[1]/div/div[1]/div/div[1]/input')
username_textbox.send_keys(username)

password_textbox = driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[2]/div[1]/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[3]/div[1]/div/div/div[1]/div/div[1]/div/div[1]/input')
password_textbox.send_keys(password)

confirm_textbox = driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[2]/div[1]/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[3]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
confirm_textbox.send_keys(password)

time.sleep(1)

text_warning = "That username is taken. Try another."

try:
    if text_warning == driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[2]/div[1]/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[2]/div[1]/div/div[2]/div[2]/div').text:
        print("That username is taken. Try another.")

except selenium.common.exceptions.NoSuchElementException:
    proceed = driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[2]/div[1]/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button').click()

time.sleep(2)

phone = input('Please Enter you phone number [Indian] > ')
time.sleep(4)
phn_number = driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[2]/div[1]/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[2]/div/div[2]/div[1]/label/input')
phn_number.send_keys(phone)

proceed1 = driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[2]/div[1]/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button').click()

time.sleep(1)

otp = input("Please enter the otp send to this number > ")
time.sleep(4)
otp_textbox = driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[2]/div[1]/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[2]/div/div[1]/div/div[1]/input')
otp_textbox.send_keys(otp)

verify = driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[2]/div[1]/div[2]/div/div/div[2]/div/div[2]/div[2]/div[1]/div/div/button').click()

time.sleep(1)

day = input('Enter DAY for DATE OF BIRTH > ')

time.sleep(2)

day_textbox = driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[2]/div[1]/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[3]/div[1]/div/div/div[1]/div/div[1]/input')
day_textbox.send_keys(day)

time.sleep(2)

print("Enter Month manually")

time.sleep(4)

year = input('Enter YEAR for DATE OF BIRTH > ')

time.sleep(2)

year_textbox = driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[2]/div[1]/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[3]/div[3]/div/div/div[1]/div/div[1]/input')
year_textbox.send_keys(year)

time.sleep(2)

print("Enter Gender Manually")

time.sleep(4)

proceed2 = driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[2]/div[1]/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button').click()
time.sleep(2)
yes_in = driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[2]/div[1]/div[2]/div/div/div[2]/div/div[2]/div[2]/div[1]/div/div/button').click()
time.sleep(2)
agree = driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[2]/div[1]/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button').click()
time.sleep(2)

print("Congratulations!! Your Gmail has been successfully created.")
print("Your gmail is : ", username, "@gmail.com")
print("Your password is : ", password)

time.sleep(1000)