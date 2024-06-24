from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import threading
import os
import time
import random

def parse_cookies(cookies_str):
    cookies_dict = []
    cookies_pairs = cookies_str.split(";")
    for pair in cookies_pairs:
        if "=" in pair:
            key, value = pair.split("=", 1)
            cookies_dict.append({
                "name": key.strip(),
                "value": value.strip(),
                "domain": ".facebook.com",
            })
    return cookies_dict

def read_comment_id():
    file_path = os.path.join(os.path.expanduser("~"), "Desktop", "mr", "facebook", "Reply_comment", "text", "comment_id.txt")
    with open(file_path, 'r') as file:
        comment_id = file.read().strip()
    return comment_id


def use_cookies(thread_id, cookies_str, post_url):
    driver = webdriver.Chrome()
    try:
        driver.get("https://mbasic.facebook.com")
        cookies = parse_cookies(cookies_str)
        for cookie in cookies:
            driver.add_cookie(cookie)

        driver.get(post_url)
        print(f"Thread {thread_id}: Logged in and accessed post URL")

        comment_id = read_comment_id()  # Dynamic reading of comment ID
        
        file_path = os.path.join(os.path.expanduser("~"), "Desktop", "mr",
                                 "facebook", "Reply_comment", "text",
                                 "comment.txt")
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            random_line = random.choice(lines)

        div_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, comment_id)))
        time.sleep(5)
           
        reply = div_element.find_element(By.XPATH, "//a[text()='رد']")
        reply.click()
        time.sleep(5)
        comment_ph = driver.find_element(By.XPATH,
                                             "//input[@value='إرفاق صورة']")
        comment_ph.click()
        folder_path = os.path.join(os.path.expanduser("~"), "Desktop", "mr",
                                   "facebook", "Comment", "photos")
        files = [
            f for f in os.listdir(folder_path)
            if os.path.isfile(os.path.join(folder_path, f))
        ]
        selected_file = random.choice(files)
        file_input = driver.find_element(By.NAME, "photo")
        file_input.send_keys(os.path.join(folder_path, selected_file))
        comment_textarea = driver.find_element(By.NAME, "comment_text")
        comment_textarea.send_keys(random_line)
        time.sleep(10)

        reply_button = driver.find_element(
            By.XPATH, "//input[@type='submit'][@value='تعليق']")
        reply_button.click()

        print("Reply Commented.")
    except Exception as e:
        print(f"An error occurred in thread {thread_id}: {e}")
    finally:
        driver.quit()

def distribute_cookies(num_threads, post_url):
    cookies_file_path = os.path.join(os.path.expanduser("~"), "Desktop", "mr", "facebook", "Reply_comment", "text", "cookies.txt")

    with open(cookies_file_path, "r") as file:
        all_cookies = file.readlines()

    threads = []

    for i in range(min(num_threads, len(all_cookies))):
        cookies = all_cookies[i].strip()
        thread = threading.Thread(target=use_cookies, args=(i, cookies, post_url))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

if __name__ == "__main__":
    try:
        num_threads = int(input("Number of Reply comment: "))
        post_link_path = os.path.join(os.path.expanduser("~"), "Desktop", "mr", "facebook", "Reply_comment", "text", "comment_link.txt")

        with open(post_link_path, "r") as file:
            post_url = file.read().strip()

        distribute_cookies(num_threads, post_url)
    except ValueError:
        print("Please enter a valid number.")
