from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
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

chrome_options = Options()
# إضافة خيارات لمحاكاة تصفح الجوال
chrome_options.add_experimental_option("mobileEmulation", {
    "deviceName": "iPhone X"
})

def use_cookies(cookies_str, post_url):
    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://m.facebook.com")

    cookies = parse_cookies(cookies_str)
    for cookie in cookies:
        driver.add_cookie(cookie)

    driver.get('https://m.facebook.com')
    driver.get(post_url)
    print("Logged in and accessed post URL")
    time.sleep(20)
    try:
        # Find the element with the specified class name
        element = driver.find_element(By.CLASS_NAME, "dd")

        # Click on the element
        element.click()
        time.sleep(15)
        print("Clicked on the share button.")
    except Exception as e:
        print("An error occurred:", e)

    driver.quit()

if __name__ == "__main__":
    try:
        cookies_file_path = os.path.join(os.path.expanduser("~"), "Desktop",
                                         "mr", "facebook", "Messages", "text", "cookies.txt")

        with open(cookies_file_path, 'r') as file:
            cookies = file.read().strip()

        post_link_path = os.path.join(os.path.expanduser("~"), "Desktop",
                                      "mr", "facebook", "Messages", "text", "post_link.txt")

        with open(post_link_path, 'r') as file:
            post_url = file.read().strip()

        use_cookies(cookies, post_url)
    except Exception as e:
        print("An error occurred:", e)
