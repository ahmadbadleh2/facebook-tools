from selenium import webdriver
from selenium.webdriver.common.by import By
import threading
import os
import time
import datetime


import os
import datetime

def read_credentials(file_path):
    try:
        with open(file_path, 'r') as file:
            data = file.readline().strip().split(':')
            if len(data) == 3:
                return data[0], data[1], data[2]
    except FileNotFoundError:
        print("Credentials file not found.")
    return None, None, None

def parse_date(date_str):
    for date_format in ("%Y-%m-%d", "%d/%m/%Y", "%Y/%m/%d"):
        try:
            return datetime.datetime.strptime(date_str, date_format).date()
        except ValueError:
            continue
    raise ValueError(f"Time data '{date_str}' does not match any known formats")

def check_credentials(username, password, expiry_date):
    today = datetime.date.today()
    expiry = parse_date(expiry_date)
    if today > expiry:
        return False, "Expired"
    input_username = input("Enter username: ")
    input_password = input("Enter password: ")
    if input_username == username and input_password == password:
        return True, "Valid"
    return False, "Invalid"

def main():
    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop", "mr", "facebook", "interaction", "text")
    file_path = os.path.join(desktop_path, "user.txt")
    
    username, password, expiry_date = read_credentials(file_path)

    if not username or not password or not expiry_date:
        print("Error reading credentials.")
        return

    try:
        is_valid, status = check_credentials(username, password, expiry_date)
    except ValueError as e:
        print(e)
        return

    if is_valid:
        print("Access granted.")
        # Place the main code of your script here
    else:
        print(f"Access denied: {status} credentials or expired access.")

if __name__ == "__main__":
    main()







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

def use_cookies(thread_id, cookies_str, post_url, reaction_text):
    driver = webdriver.Chrome()
    driver.get("https://mbasic.facebook.com")

    cookies = parse_cookies(cookies_str)
    for cookie in cookies:
        driver.add_cookie(cookie)

    driver.get("https://mbasic.facebook.com")
    driver.get(post_url)
    print(f"Thread {thread_id}: Logged in and accessed post URL")

    try:
        react_button = driver.find_element(
            By.XPATH, f"//span[contains(text(), '{reaction_text}')]"
        )
        react_button.click()
        print(f"Clicked on the {reaction_text} button.")
    except Exception as e:
        print("An error occurred:", e)

    driver.quit()

def distribute_cookies(num_threads, post_url, reaction_text):
    cookies_file_path = os.path.join(
        os.path.expanduser("~"),
        "Desktop",
        "mr",
        "facebook",
        "interaction",
        "text",
        "cookies.txt",
    )

    with open(cookies_file_path, "r") as file:
        all_cookies = file.readlines()

    threads = []

    for i in range(min(num_threads, len(all_cookies))):
        cookies = all_cookies[i].strip()
        thread = threading.Thread(target=use_cookies, args=(i, cookies, post_url, reaction_text))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

if __name__ == "__main__":
    try:
        choice = input(
            "\n1-like\n2-love\n3-support\n4-laugh\n5-wow\n6-sad\n7-angry\nChoose program to run: "
        )
        num_threads = int(input("Number of interactions: "))
        post_link_path = os.path.join(
            os.path.expanduser("~"),
            "Desktop",
            "mr",
            "facebook",
            "interaction",
            "text",
            "post_link.txt",
        )

        with open(post_link_path, "r") as file:
            post_url = file.read().strip()

        if choice == "1":
            distribute_cookies(num_threads, post_url, "أعجبني")
        elif choice == "2":
            distribute_cookies(num_threads, post_url, "أحببته")
        elif choice == "3":
            distribute_cookies(num_threads, post_url, "أدعمه")
        elif choice == "4":
            distribute_cookies(num_threads, post_url, "هاهاها")
        elif choice == "5":
            distribute_cookies(num_threads, post_url, "واااو")
        elif choice == "6":
            distribute_cookies(num_threads, post_url, "أحزنني")
        elif choice == "7":
            distribute_cookies(num_threads, post_url, "أغضبني")
        else:
            print("Incorrect selection")
    except ValueError:
        print("Please enter a valid number.")
