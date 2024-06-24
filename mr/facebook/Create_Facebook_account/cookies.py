from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import time
from threading import Thread
import threading
import random
# تحديد المسارات التلقائية لملفات الإدخال والإخراج
input_file_path = os.path.join(
    os.path.expanduser("~"),
    "Desktop",
    "mr",
    "facebook",
    "Create_Facebook_account",
    "Accounts",
    "accounts.txt",
)
output_file_path = os.path.join(
    os.path.expanduser("~"),
    "Desktop",
    "mr",
    "facebook",
    "Create_Facebook_account",
    "Accounts",
    "cookies.txt",
)

# عدد الثريدات
num_threads = int(input("Enter the number of threads: "))

# دالة لاستخراج الكوكيز
def extract_cookies(email, password):
    options = webdriver.ChromeOptions()

    driver = webdriver.Chrome(options=options)

    driver.get("https://mbasic.facebook.com/login")

    WebDriverWait(driver,
                    10).until(EC.element_to_be_clickable((By.NAME, "email"))).click()

    for letter in email:
        email_set = driver.find_element(By.NAME, "email")
        email_set.send_keys(letter)
        time_sleep = random.uniform(0.1, 0.01)
        time.sleep(time_sleep)
    driver.find_element(By.NAME, "pass").send_keys(password)
    driver.find_element(By.NAME, "login").click()

    cookies = driver.get_cookies()
    cookies_str = ";".join([f"{cookie['name']}={cookie['value']}" for cookie in cookies])

    with open(output_file_path, "a") as cookies_file:
        cookies_file.write(f"{cookies_str}\n")
    time.sleep(1)
    driver.quit()

# دالة لتشغيل عملية استخراج الكوكيز في ثريد
def thread_function(email, password):
    try:
        extract_cookies(email, password)
    except Exception as e:
        print(f"Error with {email}: {str(e)}")

if __name__ == "__main__":
    with open(input_file_path, "r") as accounts_file:
        lines = accounts_file.readlines()

    threads = []
    for i in range(min(num_threads, len(lines))):
        email, password = lines[i].strip().split(":")
        thread = threading.Thread(target=thread_function, args=(email, password))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()
