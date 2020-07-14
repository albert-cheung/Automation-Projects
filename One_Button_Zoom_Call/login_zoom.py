from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time

chromeOptions = Options()

#Open Zoom Login Page in the Browser
driver = webdriver.Chrome(options=chromeOptions)
driver.get("https://company.zoom.us/signin")

#Look for username/password element.
username = driver.find_element_by_id("UsernameInput")
password = driver.find_element_by_id("PasswordInput")

#Put in username and login
username.send_keys("Username")
password.send_keys("Password")

#Enter submit button
password.send_keys(Keys.TAB);
password.send_keys(Keys.TAB);
password.send_keys(Keys.RETURN);

#Script will now navigate to Zoom landing page. Click on join meeting website.
join_button =  driver.find_element_by_id("btnJoinMeeting")
join_button.send_keys(Keys.RETURN);

time.sleep(2)

#Enter in Zoom room number. Hit Return.
join_meeting =  driver.find_element_by_id("join-confno")
join_meeting.send_keys("Zoom Room #");
join_meeting.send_keys(Keys.TAB);
join_meeting.send_keys(Keys.RETURN);


