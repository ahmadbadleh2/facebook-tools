from selenium import webdriver
from selenium.webdriver.common.by import By
import threading
import os
import time
def parse_cookies(cookies_str):
    cookies_dict = []
    cookies_pairs = cookies_str.split(';')
    for pair in cookies_pairs:
        if '=' in pair:
            key, value = pair.split('=', 1)
            cookies_dict.append({
                'name': key.strip(),
                'value': value.strip(),
                'domain': '.facebook.com'
            })
    return cookies_dict


def use_cookies(thread_id, cookies_str, post_url):
    driver = webdriver.Chrome()
    driver.get("https://mbasic.facebook.com")

    cookies = parse_cookies(cookies_str)
    for cookie in cookies:
        driver.add_cookie(cookie)

    driver.get('https://mbasic.facebook.com')
    driver.get(post_url)
    print(f"Thread {thread_id}: Logged in and accessed post URL")

    try:
        sharing = driver.find_element(By.XPATH, "//a[span/text()='مشاركة']")
        sharing.click()
        time.sleep(2)
        sharing2 = driver.find_element(By.XPATH, "//input[@type='submit' and @value='مشاركة']")
        sharing2.click()
        print("Clicked on the shar button.")
    except Exception as e:
        print("An error occurred:", e)

    driver.quit()

def distribute_cookies(num_threads, post_url):
    cookies_file_path = os.path.join(os.path.expanduser("~"), "Desktop",
                                     "mr", "facebook","sharing","text", "cookies.txt")

    with open(cookies_file_path, 'r') as file:
        all_cookies = file.readlines()

    threads = []

    for i in range(min(num_threads, len(all_cookies))):
        cookies = all_cookies[i].strip()
        thread = threading.Thread(target=use_cookies,
                                  args=(i, cookies, post_url))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()
if __name__ == "__main__":
    try:
        num_threads = int(input("Number of sharing: "))
        post_link_path = os.path.join(os.path.expanduser("~"), "Desktop",
                                      "mr","facebook","sharing","text","post_link_p.txt")

        with open(post_link_path, 'r') as file:
            post_url = file.read().strip()

        distribute_cookies(num_threads, post_url)
    except ValueError:
        print("Please enter a valid number.")
