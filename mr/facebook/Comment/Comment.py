from selenium import webdriver
from selenium.webdriver.common.by import By
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
            cookies_dict.append(
                {
                    "name": key.strip(),
                    "value": value.strip(),
                    "domain": ".facebook.com",
                }
            )
    return cookies_dict

def use_cookies(thread_id, cookies_str, post_url):
    driver = webdriver.Chrome()
    driver.get("https://mbasic.facebook.com")

    try:
        cookies = parse_cookies(cookies_str)
        for cookie in cookies:
            driver.add_cookie(cookie)

        driver.get(post_url)
        print(f"Thread {thread_id}: Logged in and accessed post URL")

        with open(os.path.join(os.path.expanduser("~"), "Desktop", "mr", "facebook", "Comment", "text", "comment.txt"), 'r', encoding='utf-8') as file:
            lines = file.readlines()
            random_line = random.choice(lines)
        time.sleep(3)
        comment_textarea = driver.find_element(By.NAME, "comment_text")
        comment_textarea.send_keys(random_line)
        comment_button = driver.find_element(By.XPATH,"//input[@type='submit']")
        comment_button.click()
        time.sleep(10)
        print("Commented.")
    except Exception as e:
        print(f"An error occurred in thread {thread_id}: {e}")
    finally:
        driver.quit()

def distribute_cookies(num_threads, post_url):
    cookies_file_path = os.path.join(
        os.path.expanduser("~"),
        "Desktop",
        "mr",
        "facebook",
        "comment",
        "text",
        "cookies.txt",
    )

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
        num_threads = int(input("Number of comment: "))
        post_link_path = os.path.join(
            os.path.expanduser("~"),
            "Desktop",
            "mr",
            "facebook",
            "comment",
            "text",
            "post_link.txt",
        )

        with open(post_link_path, "r") as file:
            post_url = file.read().strip()

        distribute_cookies(num_threads, post_url)
    except ValueError:
        print("Please enter a valid number.")
