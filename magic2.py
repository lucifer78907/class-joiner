from selenium import webdriver
from time import sleep
import selenium
from datetime import time, datetime, timedelta

gecko_location = r"geckodriver"

user_name = ""
password = ""

login_url = "https://cuchd.blackboard.com/"
driver = webdriver.Firefox(executable_path=gecko_location)

driver.get(url=login_url)

sleep(5.0)

biology = "https://cuchd.blackboard.com/ultra/courses/_10137_1/outline"
maths = "https://cuchd.blackboard.com/ultra/courses/_10134_1/outline"
comm = "https://cuchd.blackboard.com/ultra/courses/_10139_1/outline"
comm_lab = "https://cuchd.blackboard.com/ultra/courses/_10138_1/outline"
autocad = "https://cuchd.blackboard.com/ultra/courses/_10133_1/outline"
electronics = "https://cuchd.blackboard.com/ultra/courses/_10136_1/outline"
electronics_lab = "https://cuchd.blackboard.com/ultra/courses/_10135_1/outline"
ai = "https://cuchd.blackboard.com/ultra/courses/_10132_1/outline"
life_skills = "https://cuchd.blackboard.com/ultra/courses/_10140_1/outline"
c_programming = "https://cuchd.blackboard.com/ultra/courses/_10131_1/outline"
c_programming_lab = "https://cuchd.blackboard.com/ultra/courses/_10130_1/outline"

dictionary = {
    "Monday": [
        {
            "time": time(hour=9, minute=45, second=0, microsecond=0),
            "class": maths
        },
        {
            "time": time(hour=10, minute=45, second=0, microsecond=0),
            "class": c_programming
        },
        {
            "time": time(hour=11, minute=45, second=0, microsecond=0),
            "class": c_programming_lab
        },
        {
            "time": time(hour=13, minute=30, second=0, microsecond=0),
            "class": electronics_lab
        },
        {
            "time": time(hour=14, minute=30, second=0, microsecond=0),
            "class": electronics_lab
        }
    ],
    "Tuesday": [
        {
            "time": time(hour=9, minute=45, second=0, microsecond=0),
            "class": biology
        },
        {
            "time": time(hour=10, minute=45, second=0, microsecond=0),
            "class": c_programming
        },
        {
            "time": time(hour=11, minute=45, second=0, microsecond=0),
            "class": c_programming_lab
        },
        {
            "time": time(hour=13, minute=30, second=0, microsecond=0),
            "class": comm
        },
        {
            "time": time(hour=14, minute=30, second=0, microsecond=0),
            "class": electronics
        }
    ],
    "Wednesday": [
        {
            "time": time(hour=9, minute=45, second=0, microsecond=0),
            "class": life_skills
        },
        {
            "time": time(hour=10, minute=45, second=0, microsecond=0),
            "class": comm_lab
        },
        {
            "time": time(hour=11, minute=45, second=0, microsecond=0),
            "class": comm_lab
        },
        {
            "time": time(hour=13, minute=30, second=0, microsecond=0),
            "class": comm
        },
        {
            "time": time(hour=14, minute=30, second=0, microsecond=0),
            "class": biology
        }
    ],
    "Thursday": [
        {
            "time": time(hour=9, minute=45, second=0, microsecond=0),
            "class": autocad
        },
        {
            "time": time(hour=10, minute=45, second=0, microsecond=0),
            "class": autocad
        },
        {
            "time": time(hour=11, minute=45, second=0, microsecond=0),
            "class": electronics
        },
        {
            "time": time(hour=13, minute=30, second=0, microsecond=0),
            "class": maths
        }
    ],
    "Friday": [
        {
            "time": time(hour=9, minute=45, second=0, microsecond=0),
            "class": electronics
        },
        {
            "time": time(hour=10, minute=45, second=0, microsecond=0),
            "class": c_programming_lab
        },
        {
            "time": time(hour=11, minute=45, second=0, microsecond=0),
            "class": c_programming_lab
        },
        {
            "time": time(hour=13, minute=30, second=0, microsecond=0),
            "class": biology
        },
        {
            "time": time(hour=14, minute=30, second=0, microsecond=0),
            "class": maths
        }
    ],
    "Saturday": [
        {
            "time": time(hour=9, minute=45, second=0, microsecond=0),
            "class": autocad
        },
        {
            "time": time(hour=10, minute=45, second=0, microsecond=0),
            "class": ai
        },
        {
            "time": time(hour=11, minute=45, second=0, microsecond=0),
            "class": ai
        },
        {
            "time": time(hour=13, minute=30, second=0, microsecond=0),
            "class": maths
        }
    ]
}


agree_button = driver.find_element_by_id(id_="agree_button")
agree_button.click()
mobile_element = driver.find_element_by_id(id_="user_id")
password_element = driver.find_element_by_id(id_="password")
login_button = driver.find_element_by_id(id_="entry-login")

mobile_element.send_keys(user_name)
password_element.send_keys(password)
login_button.click()
current_date = datetime.now()
current_time = time(
    hour=current_date.hour,
    minute=current_date.minute,
    second=current_date.second,
    microsecond=current_date.microsecond
)

five_minute_earlier = time(hour=current_time.hour, minute=current_time.minute-5, second=current_time.second)
five_minute_after = time(hour=current_time.hour, minute=current_time.minute+5, second=current_time.second)

attending_link = ""
today_date = datetime.today().strftime("%A")
todays_schedule = dictionary[today_date]
for cls in todays_schedule:

    class_time = cls["time"]
    if five_minute_earlier <= class_time <= five_minute_after:
        attending_link = cls["class"]
        break

if not attending_link:
    print("No Class Found")
    exit(0)

driver.get(url=attending_link)
sleep(10.0)

driver.find_element_by_id("sessions-list-dropdown").click()
sleep(2.0)

driver.find_element_by_xpath("//ul[@id='sessions-list']/li[2]/a").click()
sleep(20.0)
print("DONEEEEEEEEEEEEEEEEEEEEEEEEE")
exit(0)
