from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import TimeoutException
import threading
import os
import time
import random


def parse_cookies(cookies_str):
    cookies_dict = []
    cookies_pairs = cookies_str.split(';')
    for pair in cookies_pairs:
        if '=' in pair:
            key, value = pair.split('=', 1)
            cookies_dict.append({
                'name': key.strip(),
                'value': value.strip(),
                'domain': '.facebook.com',
            })
    return cookies_dict

chrome_options = Options()
# إضافة خيارات لمحاكاة تصفح الجوال
chrome_options.add_experimental_option("mobileEmulation", {
    "deviceMetrics": {"width": 360, "height": 640, "pixelRatio": 3.0},
    "userAgent": "Mozilla/5.0 (Linux; Android 8.0.0; Pixel 2 Build/OPD3.170816.012) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.84 Mobile Safari/537.36"
})


def use_cookies(thread_id, cookies_str, post_url):
    driver = webdriver.Chrome(options=chrome_options)
    driver.get('https://m.facebook.com')

    cookies = parse_cookies(cookies_str)
    for cookie in cookies:
        driver.add_cookie(cookie)

    driver.get(post_url)
    print(f"Thread {thread_id}: Logged in and accessed post URL")

    time.sleep(5)
    try:
        # استخدام WebDriverWait للانتظار حتى تحميل الصفحة بشكل كامل (ضبط الوقت حسب الحاجة)
        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.TAG_NAME, "body")))

        # تنفيذ الكود الخاص بالنقر على العنصر
        share_button_script = """
        document.querySelectorAll('*').forEach(function(node) {
            if (node.innerText.includes("󰍺")) {
                node.click();
            }
        });
        """
        driver.execute_script(share_button_script)

    except TimeoutException:
        print("تم تجاوز الوقت المحدد لانتظار تحميل الصفحة.")
    except Exception as e:
        print(f"Error: {e}")
    time.sleep(5)
    try:
        share_on_group = """
                document.querySelectorAll('*').forEach(function(node) {
            if (node.innerText.includes("󱙫")) {
                node.click();
            }
        });
        """
        driver.execute_script(share_on_group)

    except TimeoutException:
        print("تم تجاوز الوقت المحدد لانتظار تحميل الصفحة.")
    except Exception as e:
        print(f"Error: {e}")

    time.sleep(5)
    while True:
        try:
            time.sleep(2)
            if "#4a4a4a;" in driver.page_source:
                random_group = """
                let elements = document.querySelectorAll('[style="color:#4a4a4a;"]');
                let randomElement = elements[Math.floor(Math.random() * elements.length)];
                randomElement.click();
                """
                driver.execute_script(random_group)
                time.sleep(3)
                break
            else:
                pass
        except:
            print(e)
    submit ="""
    document.querySelectorAll('[class^="m bg"]').forEach(element => {
    element.click();
    });
    """
    driver.execute_script(submit)

    time.sleep(1000)

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
        post_link_path = os.path.join(os.path.expanduser("~"), "Desktop", "mr",
                                      "facebook", "sharing", "text",
                                      "post_link_s_m_g.txt")

        with open(post_link_path, 'r') as file:
            post_url = file.read().strip()

        distribute_cookies(num_threads, post_url)
    except ValueError:
        print("Please enter a valid number.")
